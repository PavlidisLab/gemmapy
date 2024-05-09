# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.7.5
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnnotationSearchResultValueObject(object):
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
        'value': 'str',
        'value_uri': 'str',
        'category': 'str',
        'category_uri': 'str'
    }

    attribute_map = {
        'value': 'value',
        'value_uri': 'valueUri',
        'category': 'category',
        'category_uri': 'categoryUri'
    }

    def __init__(self, value=None, value_uri=None, category=None, category_uri=None):  # noqa: E501
        """AnnotationSearchResultValueObject - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._value_uri = None
        self._category = None
        self._category_uri = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if value_uri is not None:
            self.value_uri = value_uri
        if category is not None:
            self.category = category
        if category_uri is not None:
            self.category_uri = category_uri

    @property
    def value(self):
        """Gets the value of this AnnotationSearchResultValueObject.  # noqa: E501


        :return: The value of this AnnotationSearchResultValueObject.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AnnotationSearchResultValueObject.


        :param value: The value of this AnnotationSearchResultValueObject.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_uri(self):
        """Gets the value_uri of this AnnotationSearchResultValueObject.  # noqa: E501


        :return: The value_uri of this AnnotationSearchResultValueObject.  # noqa: E501
        :rtype: str
        """
        return self._value_uri

    @value_uri.setter
    def value_uri(self, value_uri):
        """Sets the value_uri of this AnnotationSearchResultValueObject.


        :param value_uri: The value_uri of this AnnotationSearchResultValueObject.  # noqa: E501
        :type: str
        """

        self._value_uri = value_uri

    @property
    def category(self):
        """Gets the category of this AnnotationSearchResultValueObject.  # noqa: E501


        :return: The category of this AnnotationSearchResultValueObject.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AnnotationSearchResultValueObject.


        :param category: The category of this AnnotationSearchResultValueObject.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def category_uri(self):
        """Gets the category_uri of this AnnotationSearchResultValueObject.  # noqa: E501


        :return: The category_uri of this AnnotationSearchResultValueObject.  # noqa: E501
        :rtype: str
        """
        return self._category_uri

    @category_uri.setter
    def category_uri(self, category_uri):
        """Sets the category_uri of this AnnotationSearchResultValueObject.


        :param category_uri: The category_uri of this AnnotationSearchResultValueObject.  # noqa: E501
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
        if issubclass(AnnotationSearchResultValueObject, dict):
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
        if not isinstance(other, AnnotationSearchResultValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
