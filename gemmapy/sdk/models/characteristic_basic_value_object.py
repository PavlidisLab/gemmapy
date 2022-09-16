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

class CharacteristicBasicValueObject(object):
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
        'value_uri': 'str',
        'category': 'str',
        'category_uri': 'str'
    }

    attribute_map = {
        'id': 'id',
        'value': 'value',
        'value_uri': 'valueUri',
        'category': 'category',
        'category_uri': 'categoryUri'
    }

    def __init__(self, id=None, value=None, value_uri=None, category=None, category_uri=None):  # noqa: E501
        """CharacteristicBasicValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._value = None
        self._value_uri = None
        self._category = None
        self._category_uri = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if value is not None:
            self.value = value
        if value_uri is not None:
            self.value_uri = value_uri
        if category is not None:
            self.category = category
        if category_uri is not None:
            self.category_uri = category_uri

    @property
    def id(self):
        """Gets the id of this CharacteristicBasicValueObject.  # noqa: E501


        :return: The id of this CharacteristicBasicValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CharacteristicBasicValueObject.


        :param id: The id of this CharacteristicBasicValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def value(self):
        """Gets the value of this CharacteristicBasicValueObject.  # noqa: E501


        :return: The value of this CharacteristicBasicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CharacteristicBasicValueObject.


        :param value: The value of this CharacteristicBasicValueObject.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_uri(self):
        """Gets the value_uri of this CharacteristicBasicValueObject.  # noqa: E501


        :return: The value_uri of this CharacteristicBasicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._value_uri

    @value_uri.setter
    def value_uri(self, value_uri):
        """Sets the value_uri of this CharacteristicBasicValueObject.


        :param value_uri: The value_uri of this CharacteristicBasicValueObject.  # noqa: E501
        :type: str
        """

        self._value_uri = value_uri

    @property
    def category(self):
        """Gets the category of this CharacteristicBasicValueObject.  # noqa: E501


        :return: The category of this CharacteristicBasicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CharacteristicBasicValueObject.


        :param category: The category of this CharacteristicBasicValueObject.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def category_uri(self):
        """Gets the category_uri of this CharacteristicBasicValueObject.  # noqa: E501


        :return: The category_uri of this CharacteristicBasicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._category_uri

    @category_uri.setter
    def category_uri(self, category_uri):
        """Sets the category_uri of this CharacteristicBasicValueObject.


        :param category_uri: The category_uri of this CharacteristicBasicValueObject.  # noqa: E501
        :type: str
        """

        self._category_uri = category_uri

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
        if issubclass(CharacteristicBasicValueObject, dict):
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
        if not isinstance(other, CharacteristicBasicValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other