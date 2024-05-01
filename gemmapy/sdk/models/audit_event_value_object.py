# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.7.4
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AuditEventValueObject(object):
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
        'id': 'int',
        'performer': 'str',
        '_date': 'datetime',
        'action': 'str',
        'note': 'str',
        'detail': 'str',
        'action_name': 'str',
        'event_type_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'performer': 'performer',
        '_date': 'date',
        'action': 'action',
        'note': 'note',
        'detail': 'detail',
        'action_name': 'actionName',
        'event_type_name': 'eventTypeName'
    }

    def __init__(self, id=None, performer=None, _date=None, action=None, note=None, detail=None, action_name=None, event_type_name=None):  # noqa: E501
        """AuditEventValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._performer = None
        self.__date = None
        self._action = None
        self._note = None
        self._detail = None
        self._action_name = None
        self._event_type_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if performer is not None:
            self.performer = performer
        if _date is not None:
            self._date = _date
        if action is not None:
            self.action = action
        if note is not None:
            self.note = note
        if detail is not None:
            self.detail = detail
        if action_name is not None:
            self.action_name = action_name
        if event_type_name is not None:
            self.event_type_name = event_type_name

    @property
    def id(self):
        """Gets the id of this AuditEventValueObject.  # noqa: E501


        :return: The id of this AuditEventValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditEventValueObject.


        :param id: The id of this AuditEventValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def performer(self):
        """Gets the performer of this AuditEventValueObject.  # noqa: E501


        :return: The performer of this AuditEventValueObject.  # noqa: E501
        :rtype: str
        """
        return self._performer

    @performer.setter
    def performer(self, performer):
        """Sets the performer of this AuditEventValueObject.


        :param performer: The performer of this AuditEventValueObject.  # noqa: E501
        :type: str
        """

        self._performer = performer

    @property
    def _date(self):
        """Gets the _date of this AuditEventValueObject.  # noqa: E501


        :return: The _date of this AuditEventValueObject.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this AuditEventValueObject.


        :param _date: The _date of this AuditEventValueObject.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def action(self):
        """Gets the action of this AuditEventValueObject.  # noqa: E501


        :return: The action of this AuditEventValueObject.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AuditEventValueObject.


        :param action: The action of this AuditEventValueObject.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def note(self):
        """Gets the note of this AuditEventValueObject.  # noqa: E501


        :return: The note of this AuditEventValueObject.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this AuditEventValueObject.


        :param note: The note of this AuditEventValueObject.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def detail(self):
        """Gets the detail of this AuditEventValueObject.  # noqa: E501


        :return: The detail of this AuditEventValueObject.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this AuditEventValueObject.


        :param detail: The detail of this AuditEventValueObject.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def action_name(self):
        """Gets the action_name of this AuditEventValueObject.  # noqa: E501


        :return: The action_name of this AuditEventValueObject.  # noqa: E501
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this AuditEventValueObject.


        :param action_name: The action_name of this AuditEventValueObject.  # noqa: E501
        :type: str
        """

        self._action_name = action_name

    @property
    def event_type_name(self):
        """Gets the event_type_name of this AuditEventValueObject.  # noqa: E501


        :return: The event_type_name of this AuditEventValueObject.  # noqa: E501
        :rtype: str
        """
        return self._event_type_name

    @event_type_name.setter
    def event_type_name(self, event_type_name):
        """Sets the event_type_name of this AuditEventValueObject.


        :param event_type_name: The event_type_name of this AuditEventValueObject.  # noqa: E501
        :type: str
        """

        self._event_type_name = event_type_name

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
        if issubclass(AuditEventValueObject, dict):
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
        if not isinstance(other, AuditEventValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
