#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:06:47 2024

@author: omancarci
"""
import os
import time

import anndata as ad
import pandas as pd
import pytest

import gemmapy
from gemmapy import _subprocessors as sub
from gemmapy.gemmapy_api import GemmaPath

api = gemmapy.GemmaPy()

@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(1)

def test_path():
    client = gemmapy.GemmaPy(path=GemmaPath.PROD)
    assert client.raw.api_client.configuration.host == 'https://gemma.msl.ubc.ca/rest/v2'
    client = gemmapy.GemmaPy(path=GemmaPath.DEV)
    assert client.raw.api_client.configuration.host == 'https://dev.gemma.msl.ubc.ca/rest/v2'
    client = gemmapy.GemmaPy(path=GemmaPath.STAGING)
    assert client.raw.api_client.configuration.host == 'https://staging-gemma.msl.ubc.ca/rest/v2'
    client = gemmapy.GemmaPy(path='dev')
    assert client.raw.api_client.configuration.host == 'https://dev.gemma.msl.ubc.ca/rest/v2'
    client = gemmapy.GemmaPy(path='https://example.com/rest/v2')
    assert client.raw.api_client.configuration.host == 'https://example.com/rest/v2'

def test_auth(monkeypatch):
    monkeypatch.setitem(os.environ, 'GEMMA_USERNAME', '')
    monkeypatch.setitem(os.environ, 'GEMMA_PASSWORD', '')
    monkeypatch.setitem(os.environ, 'GEMMA_PASSWORD_CMD', '')

    client = gemmapy.GemmaPy()
    assert client.raw.api_client.configuration.username == ''
    assert client.raw.api_client.configuration.password == ''

    client = gemmapy.GemmaPy(auth=['foo', 'bar'])
    assert client.raw.api_client.configuration.username == 'foo'
    assert client.raw.api_client.configuration.password == 'bar'

    with pytest.raises(OSError):
        gemmapy.GemmaPy(auth=('username',))

    monkeypatch.setitem(os.environ, 'GEMMA_USERNAME', 'foo')
    monkeypatch.setitem(os.environ, 'GEMMA_PASSWORD', 'bar')
    client = gemmapy.GemmaPy()
    assert client.raw.api_client.configuration.username == 'foo'
    assert client.raw.api_client.configuration.password == 'bar'

    monkeypatch.setitem(os.environ, 'GEMMA_USERNAME', 'foo')
    monkeypatch.setitem(os.environ, 'GEMMA_PASSWORD', '')
    monkeypatch.setitem(os.environ, 'GEMMA_PASSWORD_CMD', 'echo 1234')
    client = gemmapy.GemmaPy()
    assert client.raw.api_client.configuration.username == 'foo'
    assert client.raw.api_client.configuration.password == '1234'

    with pytest.raises(OSError):
        monkeypatch.setitem(os.environ, 'GEMMA_USERNAME', 'foo')
        monkeypatch.setitem(os.environ, 'GEMMA_PASSWORD', '')
        monkeypatch.setitem(os.environ, 'GEMMA_PASSWORD_CMD', '')
        gemmapy.GemmaPy()

def test_get_single_cell_data():
    # TODO: use a publicly available dataset
    client = gemmapy.GemmaPy()
    ad = client.get_single_cell_dataset_object('GSE227313', download_dir='.')
    print(ad)

def test_get_genes():
    assert len(api.get_genes('BRCA1')) > 0
    assert len(api.get_genes(['BRCA1'])) > 0
    assert len(api.get_genes(672)) > 0
    assert len(api.get_genes([672])) > 0
    assert len(api.get_genes([672, 'BRCA1'])) > 0

def test_get_result_sets():
    res = api.get_result_sets([200])
    
    assert type(res) is pd.core.frame.DataFrame
    
    res2 = api.get_result_sets(result_sets = [res.result_ID[0]])
    assert type(res2) is pd.core.frame.DataFrame
    
    assert res.shape[1] == 10
    assert res2.shape[1] == 10
    assert res.shape[0] > 0
    assert res2.shape[0] > 0

    assert len(set(res2.result_ID)) == 1
        
    assert res2.result_ID[0] in list(res.result_ID)
    

def test_search_annotations():
    res = api.search_annotations(query = ['traumatic'])
    assert type(res) is pd.core.frame.DataFrame
    assert res.shape[1] == 4
    
    assert res.shape[0] > 0
    res2 = api.search_annotations(query = ['gibberish'])
    assert type(res2) is pd.core.frame.DataFrame
    assert res2.shape[0] ==0
    assert res2.shape[1] == 4

def test_get_dataset_annotations():
    res = api.get_dataset_annotations(1)
    assert type(res) is pd.core.frame.DataFrame
    assert res.shape[1] == 5

def test_get_dataset_differential_expression_analyses():
    res = api.get_dataset_differential_expression_analyses(200)
    assert type(res) is pd.core.frame.DataFrame

def test_result_set_table_compatibility():
    res = api.get_dataset_differential_expression_analyses(200)
    res2 = api.get_result_sets(result_sets = [res.result_ID[0]])
    
    assert all(
        sub.list_in_list(res2.contrast_ID, res.contrast_ID)
        )
    
    dif_exp = api._GemmaPy__get_result_set(res.result_ID[0])
    expected_cols = ["contrast_" + str(x) +"_log2fc" for x in res2.contrast_ID]
    
    assert all(
        sub.list_in_list(expected_cols,list(dif_exp.columns))
        )

def test_get_dataset_expression_for_genes():
    res = api.get_dataset_expression_for_genes(datasets = [1,4], genes = [10225,2841])
     
    assert all(
         [type(value) is pd.core.frame.DataFrame for value in res.values()]
         )
    
    # assert res[2].shape == (0,0)
    assert res[1].shape[0]>1
    assert res[4].shape[0]>1
     
def test_get_processed_expression_samples_compatibility():
    exp = api.get_dataset_processed_expression(2)
    samples = api.get_dataset_samples(2)
    
    exp_cols = [x for x in exp.columns if x in list(samples.sample_name)]    
    
    assert all([exp_cols[i] == samples.sample_name[i] for i in range(len(exp_cols))])


def test_get_dataset_qt_types_raw_expression():
    qtypes = api.get_dataset_quantitation_types(2)
    qtype_id = list(qtypes[qtypes.type=='raw'].ID)[0]
    
    exp = api.get_dataset_raw_expression(2,qtype_id)
    assert type(exp) is pd.core.frame.DataFrame
    
    samples = api.get_dataset_samples(2)
    exp_cols = [x for x in exp.columns if x in list(samples.sample_name)]    
    assert all([exp_cols[i] == samples.sample_name[i] for i in range(len(exp_cols))])

def test_get_dataset_object():
    datasets = [549, 873, 1869]
    genes = [8913, 7840]
    obj = api.get_dataset_object(datasets,genes)
    
    assert len(obj) == 3
    assert type(obj) == dict
    assert type(obj[list(obj)[0]]) == ad.AnnData
    
    ds = 442
    dea = api.get_dataset_differential_expression_analyses(dataset = ds)
    
    obj =  api.get_dataset_object(datasets =sub.rep(ds,dea.shape[0]),
                           result_sets = dea.result_ID,
                           contrasts = dea.contrast_ID,output_type='dict')
    
    assert len(obj) == dea.shape[0]


# def test_measurements():
#    dataset = "GSE106"
#    samples = api.get_dataset_samples(dataset)
    
