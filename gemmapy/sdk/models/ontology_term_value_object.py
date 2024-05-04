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

class OntologyTermValueObject(object):
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
        'uri': 'str',
        'name': 'str',
        'parent_terms': 'list[OntologyTermValueObject]'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'parent_terms': 'parentTerms'
    }

    def __init__(self, uri=None, name=None, parent_terms=None):  # noqa: E501
        """OntologyTermValueObject - a model defined in Swagger"""  # noqa: E501
        self._uri = None
        self._name = None
        self._parent_terms = None
        self.discriminator = None
        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if parent_terms is not None:
            self.parent_terms = parent_terms

    @property
    def uri(self):
        """Gets the uri of this OntologyTermValueObject.  # noqa: E501


        :return: The uri of this OntologyTermValueObject.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this OntologyTermValueObject.


        :param uri: The uri of this OntologyTermValueObject.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this OntologyTermValueObject.  # noqa: E501


        :return: The name of this OntologyTermValueObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OntologyTermValueObject.


        :param name: The name of this OntologyTermValueObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_terms(self):
        """Gets the parent_terms of this OntologyTermValueObject.  # noqa: E501


        :return: The parent_terms of this OntologyTermValueObject.  # noqa: E501
        :rtype: list[OntologyTermValueObject]
        """
        return self._parent_terms

    @parent_terms.setter
    def parent_terms(self, parent_terms):
        """Sets the parent_terms of this OntologyTermValueObject.


        :param parent_terms: The parent_terms of this OntologyTermValueObject.  # noqa: E501
        :type: list[OntologyTermValueObject]
        """

        self._parent_terms = parent_terms

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
        if issubclass(OntologyTermValueObject, dict):
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
        if not isinstance(other, OntologyTermValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
