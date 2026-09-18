#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for gemmapy._retry.

These are offline: RetryingRESTClient is driven against a stubbed
RESTClientObject.request so the retry policy can be exercised without waiting on
a real 503, and time.sleep is patched out so the suite does not actually wait.
"""
import email.utils
import time
from datetime import datetime, timedelta, timezone

import pytest
import urllib3

from gemmapy import sdk
from gemmapy._retry import (MAX_UNDIRECTED_RETRIES, RetryingRESTClient,
                            UNDIRECTED_WAIT, retry_after)
from gemmapy.sdk.rest import ApiException


@pytest.fixture
def no_sleep(monkeypatch):
    """Record what we would have waited instead of waiting."""
    waits = []
    monkeypatch.setattr(time, "sleep", waits.append)
    return waits


def make_client(responses, monkeypatch):
    """A RetryingRESTClient whose underlying request yields `responses` in turn.

    Each entry is either an ApiException to raise or a value to return.
    """
    client = RetryingRESTClient(sdk.Configuration())
    calls = []

    def fake_request(self, method, url, **kwargs):
        calls.append((method, url))
        item = responses[len(calls) - 1]
        if isinstance(item, Exception):
            raise item
        return item

    monkeypatch.setattr(sdk.rest.RESTClientObject, "request", fake_request)
    return client, calls


def api_error(status, headers=None):
    e = ApiException(status=status, reason="stub")
    e.headers = headers
    return e


# --- retry_after ------------------------------------------------------------

def test_retry_after_reads_delay_seconds():
    assert retry_after({"Retry-After": "30"}) == 30


def test_retry_after_is_case_insensitive_on_a_plain_dict():
    assert retry_after({"retry-after": "7"}) == 7


def test_retry_after_reads_urllib3_header_dict():
    headers = urllib3.response.HTTPHeaderDict()
    headers.add("Retry-After", "12")
    assert retry_after(headers) == 12


def test_retry_after_reads_http_date():
    when = datetime.now(timezone.utc) + timedelta(seconds=45)
    header = email.utils.format_datetime(when, usegmt=True)
    seconds = retry_after({"Retry-After": header})
    # whole seconds, and a little slack for the clock between the two calls
    assert 40 <= seconds <= 46


def test_retry_after_floors_at_one_second():
    past = email.utils.format_datetime(
        datetime.now(timezone.utc) - timedelta(seconds=60), usegmt=True)
    assert retry_after({"Retry-After": past}) == 1
    assert retry_after({"Retry-After": "0"}) == 1


@pytest.mark.parametrize("headers", [None, {}, {"Retry-After": "soon"}])
def test_retry_after_returns_none_when_unusable(headers):
    assert retry_after(headers) is None


# --- retry policy -----------------------------------------------------------

def test_success_passes_straight_through(monkeypatch, no_sleep):
    client, calls = make_client(["ok"], monkeypatch)
    assert client.request("GET", "/datasets") == "ok"
    assert len(calls) == 1
    assert no_sleep == []


def test_directed_503_waits_the_requested_time(monkeypatch, no_sleep):
    client, calls = make_client(
        [api_error(503, {"Retry-After": "2"}), "ok"], monkeypatch)
    assert client.request("GET", "/datasets") == "ok"
    assert no_sleep == [2]


def test_directed_503_is_not_capped_by_the_retry_limit(monkeypatch, no_sleep):
    """The server scheduling us does not count against the attempt limit, so
    this survives more 503s than an undirected response would allow."""
    attempts = MAX_UNDIRECTED_RETRIES + 5
    client, calls = make_client(
        [api_error(503, {"Retry-After": "1"})] * attempts + ["ok"], monkeypatch)
    assert client.request("GET", "/datasets") == "ok"
    assert len(calls) == attempts + 1


def test_503_without_retry_after_is_capped(monkeypatch, no_sleep):
    client, calls = make_client([api_error(503)] * 10, monkeypatch)
    with pytest.raises(ApiException):
        client.request("GET", "/datasets")
    assert len(calls) == MAX_UNDIRECTED_RETRIES + 1
    assert no_sleep == [UNDIRECTED_WAIT] * MAX_UNDIRECTED_RETRIES


@pytest.mark.parametrize("status", [0, 429, 500])
def test_other_transient_statuses_retry_then_give_up(status, monkeypatch, no_sleep):
    client, calls = make_client([api_error(status)] * 10, monkeypatch)
    with pytest.raises(ApiException):
        client.request("GET", "/datasets")
    assert len(calls) == MAX_UNDIRECTED_RETRIES + 1


def test_transient_status_recovers(monkeypatch, no_sleep):
    client, calls = make_client([api_error(500), api_error(429), "ok"], monkeypatch)
    assert client.request("GET", "/datasets") == "ok"
    assert len(calls) == 3


@pytest.mark.parametrize("status", [400, 401, 404, 422])
def test_non_transient_status_raises_immediately(status, monkeypatch, no_sleep):
    client, calls = make_client([api_error(status), "ok"], monkeypatch)
    with pytest.raises(ApiException):
        client.request("GET", "/datasets")
    assert len(calls) == 1
    assert no_sleep == []


@pytest.mark.parametrize("method", ["POST", "PUT", "DELETE", "PATCH"])
def test_non_idempotent_methods_are_never_retried(method, monkeypatch, no_sleep):
    """Re-sending a write that failed with a 500 could apply it twice, so only
    GET/HEAD/OPTIONS are repeated even when the server directs us to come back."""
    client, calls = make_client(
        [api_error(503, {"Retry-After": "1"}), "ok"], monkeypatch)
    with pytest.raises(ApiException):
        client.request(method, "/datasets")
    assert len(calls) == 1
    assert no_sleep == []


def test_client_is_installed_on_the_api_client():
    """A bare GemmaPy routes its calls through the retrying client."""
    import gemmapy
    api = gemmapy.GemmaPy()
    assert isinstance(api.raw.api_client.rest_client, RetryingRESTClient)


def test_real_503_and_retry_after_end_to_end():
    """The stubs above set ApiException.headers directly. This one serves an
    actual 503 over the loopback so the Retry-After really travels through
    urllib3 and RESTResponse.getheaders()."""
    import threading
    from http.server import BaseHTTPRequestHandler, HTTPServer

    hits = []

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            hits.append(self.path)
            if len(hits) == 1:
                self.send_response(503)
                self.send_header("Retry-After", "1")
                self.end_headers()
                self.wfile.write(b"busy")
            else:
                body = b'{"data":[]}'
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

        def log_message(self, *args):
            pass

    server = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        client = RetryingRESTClient(sdk.Configuration())
        started = time.time()
        response = client.GET(
            "http://127.0.0.1:%d/datasets" % server.server_address[1])
        elapsed = time.time() - started
    finally:
        server.shutdown()

    assert response.status == 200
    assert len(hits) == 2
    assert elapsed >= 1  # it waited the second the server asked for
