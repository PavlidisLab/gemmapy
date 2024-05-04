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

class MeasurementValueObject(object):
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
        'value': 'str',
        'unit': 'str',
        'type': 'str',
        'representation': 'str'
    }

    attribute_map = {
        'id': 'id',
        'value': 'value',
        'unit': 'unit',
        'type': 'type',
        'representation': 'representation'
    }

    def __init__(self, id=None, value=None, unit=None, type=None, representation=None):  # noqa: E501
        """MeasurementValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._value = None
        self._unit = None
        self._type = None
        self._representation = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if value is not None:
            self.value = value
        if unit is not None:
            self.unit = unit
        if type is not None:
            self.type = type
        if representation is not None:
            self.representation = representation

    @property
    def id(self):
        """Gets the id of this MeasurementValueObject.  # noqa: E501


        :return: The id of this MeasurementValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MeasurementValueObject.


        :param id: The id of this MeasurementValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def value(self):
        """Gets the value of this MeasurementValueObject.  # noqa: E501


        :return: The value of this MeasurementValueObject.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MeasurementValueObject.


        :param value: The value of this MeasurementValueObject.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this MeasurementValueObject.  # noqa: E501


        :return: The unit of this MeasurementValueObject.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this MeasurementValueObject.


        :param unit: The unit of this MeasurementValueObject.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def type(self):
        """Gets the type of this MeasurementValueObject.  # noqa: E501


        :return: The type of this MeasurementValueObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MeasurementValueObject.


        :param type: The type of this MeasurementValueObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["ABSOLUTE", "CHANGE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def representation(self):
        """Gets the representation of this MeasurementValueObject.  # noqa: E501


        :return: The representation of this MeasurementValueObject.  # noqa: E501
        :rtype: str
        """
        return self._representation

    @representation.setter
    def representation(self, representation):
        """Sets the representation of this MeasurementValueObject.


        :param representation: The representation of this MeasurementValueObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOUBLE", "INT", "LONG", "CHAR", "BOOLEAN", "STRING", "INTARRAY", "DOUBLEARRAY", "CHARARRAY", "BOOLEANARRAY", "STRINGARRAY"]  # noqa: E501
        if representation not in allowed_values:
            raise ValueError(
                "Invalid value for `representation` ({0}), must be one of {1}"  # noqa: E501
                .format(representation, allowed_values)
            )

        self._representation = representation

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
        if issubclass(MeasurementValueObject, dict):
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
        if not isinstance(other, MeasurementValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
