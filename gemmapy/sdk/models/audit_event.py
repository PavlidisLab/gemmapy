# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma REST API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  The documentation of the underlying java code can be found [here](https://gemma.msl.ubc.ca/resources/apidocs/ubic/gemma/web/services/rest/package-summary.html). See the [links section](https://gemma.msl.ubc.ca/resources/restapidocs/#footer) in the footer of this page for other relevant links.  Use of this webpage and Gemma web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.   # noqa: E501

    OpenAPI spec version: 2.4.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AuditEvent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action': 'AuditAction',
        '_date': 'datetime',
        'detail': 'str',
        'event_type': 'AuditEventType',
        'id': 'int',
        'note': 'str',
        'performer': 'User'
    }

    attribute_map = {
        'action': 'action',
        '_date': 'date',
        'detail': 'detail',
        'event_type': 'eventType',
        'id': 'id',
        'note': 'note',
        'performer': 'performer'
    }

    def __init__(self, action=None, _date=None, detail=None, event_type=None, id=None, note=None, performer=None):  # noqa: E501
        """AuditEvent - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self.__date = None
        self._detail = None
        self._event_type = None
        self._id = None
        self._note = None
        self._performer = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if _date is not None:
            self._date = _date
        if detail is not None:
            self.detail = detail
        if event_type is not None:
            self.event_type = event_type
        if id is not None:
            self.id = id
        if note is not None:
            self.note = note
        if performer is not None:
            self.performer = performer

    @property
    def action(self):
        """Gets the action of this AuditEvent.  # noqa: E501


        :return: The action of this AuditEvent.  # noqa: E501
        :rtype: AuditAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AuditEvent.


        :param action: The action of this AuditEvent.  # noqa: E501
        :type: AuditAction
        """

        self._action = action

    @property
    def _date(self):
        """Gets the _date of this AuditEvent.  # noqa: E501


        :return: The _date of this AuditEvent.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this AuditEvent.


        :param _date: The _date of this AuditEvent.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def detail(self):
        """Gets the detail of this AuditEvent.  # noqa: E501


        :return: The detail of this AuditEvent.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this AuditEvent.


        :param detail: The detail of this AuditEvent.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def event_type(self):
        """Gets the event_type of this AuditEvent.  # noqa: E501


        :return: The event_type of this AuditEvent.  # noqa: E501
        :rtype: AuditEventType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this AuditEvent.


        :param event_type: The event_type of this AuditEvent.  # noqa: E501
        :type: AuditEventType
        """

        self._event_type = event_type

    @property
    def id(self):
        """Gets the id of this AuditEvent.  # noqa: E501


        :return: The id of this AuditEvent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditEvent.


        :param id: The id of this AuditEvent.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def note(self):
        """Gets the note of this AuditEvent.  # noqa: E501


        :return: The note of this AuditEvent.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this AuditEvent.


        :param note: The note of this AuditEvent.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def performer(self):
        """Gets the performer of this AuditEvent.  # noqa: E501


        :return: The performer of this AuditEvent.  # noqa: E501
        :rtype: User
        """
        return self._performer

    @performer.setter
    def performer(self, performer):
        """Sets the performer of this AuditEvent.


        :param performer: The performer of this AuditEvent.  # noqa: E501
        :type: User
        """

        self._performer = performer

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AuditEvent, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuditEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
