# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.7.6
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SearchSettingsValueObject(object):
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
        'query': 'str',
        'result_types': 'list[SearchResultType]',
        'taxon': 'TaxonValueObject',
        'platform': 'ArrayDesignValueObject',
        'max_results': 'int'
    }

    attribute_map = {
        'query': 'query',
        'result_types': 'resultTypes',
        'taxon': 'taxon',
        'platform': 'platform',
        'max_results': 'maxResults'
    }

    def __init__(self, query=None, result_types=None, taxon=None, platform=None, max_results=None):  # noqa: E501
        """SearchSettingsValueObject - a model defined in Swagger"""  # noqa: E501
        self._query = None
        self._result_types = None
        self._taxon = None
        self._platform = None
        self._max_results = None
        self.discriminator = None
        if query is not None:
            self.query = query
        if result_types is not None:
            self.result_types = result_types
        if taxon is not None:
            self.taxon = taxon
        if platform is not None:
            self.platform = platform
        if max_results is not None:
            self.max_results = max_results

    @property
    def query(self):
        """Gets the query of this SearchSettingsValueObject.  # noqa: E501


        :return: The query of this SearchSettingsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchSettingsValueObject.


        :param query: The query of this SearchSettingsValueObject.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def result_types(self):
        """Gets the result_types of this SearchSettingsValueObject.  # noqa: E501


        :return: The result_types of this SearchSettingsValueObject.  # noqa: E501
        :rtype: list[SearchResultType]
        """
        return self._result_types

    @result_types.setter
    def result_types(self, result_types):
        """Sets the result_types of this SearchSettingsValueObject.


        :param result_types: The result_types of this SearchSettingsValueObject.  # noqa: E501
        :type: list[SearchResultType]
        """

        self._result_types = result_types

    @property
    def taxon(self):
        """Gets the taxon of this SearchSettingsValueObject.  # noqa: E501


        :return: The taxon of this SearchSettingsValueObject.  # noqa: E501
        :rtype: TaxonValueObject
        """
        return self._taxon

    @taxon.setter
    def taxon(self, taxon):
        """Sets the taxon of this SearchSettingsValueObject.


        :param taxon: The taxon of this SearchSettingsValueObject.  # noqa: E501
        :type: TaxonValueObject
        """

        self._taxon = taxon

    @property
    def platform(self):
        """Gets the platform of this SearchSettingsValueObject.  # noqa: E501


        :return: The platform of this SearchSettingsValueObject.  # noqa: E501
        :rtype: ArrayDesignValueObject
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this SearchSettingsValueObject.


        :param platform: The platform of this SearchSettingsValueObject.  # noqa: E501
        :type: ArrayDesignValueObject
        """

        self._platform = platform

    @property
    def max_results(self):
        """Gets the max_results of this SearchSettingsValueObject.  # noqa: E501


        :return: The max_results of this SearchSettingsValueObject.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this SearchSettingsValueObject.


        :param max_results: The max_results of this SearchSettingsValueObject.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

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
        if issubclass(SearchSettingsValueObject, dict):
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
        if not isinstance(other, SearchSettingsValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
