# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.9.0
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject(object):
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
        'data': 'list[TaxonWithUsageStatisticsValueObject]',
        'warnings': 'list[WellComposedWarning]',
        'filter': 'str',
        'group_by': 'list[str]',
        'sort': 'SortValueObject',
        'query': 'str',
        'inferred_terms': 'list[CharacteristicValueObject]'
    }

    attribute_map = {
        'data': 'data',
        'warnings': 'warnings',
        'filter': 'filter',
        'group_by': 'groupBy',
        'sort': 'sort',
        'query': 'query',
        'inferred_terms': 'inferredTerms'
    }

    def __init__(self, data=None, warnings=None, filter=None, group_by=None, sort=None, query=None, inferred_terms=None):  # noqa: E501
        """QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._warnings = None
        self._filter = None
        self._group_by = None
        self._sort = None
        self._query = None
        self._inferred_terms = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if warnings is not None:
            self.warnings = warnings
        if filter is not None:
            self.filter = filter
        if group_by is not None:
            self.group_by = group_by
        if sort is not None:
            self.sort = sort
        if query is not None:
            self.query = query
        if inferred_terms is not None:
            self.inferred_terms = inferred_terms

    @property
    def data(self):
        """Gets the data of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501


        :return: The data of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: list[TaxonWithUsageStatisticsValueObject]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.


        :param data: The data of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :type: list[TaxonWithUsageStatisticsValueObject]
        """

        self._data = data

    @property
    def warnings(self):
        """Gets the warnings of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501


        :return: The warnings of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: list[WellComposedWarning]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.


        :param warnings: The warnings of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :type: list[WellComposedWarning]
        """

        self._warnings = warnings

    @property
    def filter(self):
        """Gets the filter of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501


        :return: The filter of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.


        :param filter: The filter of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def group_by(self):
        """Gets the group_by of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501


        :return: The group_by of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.


        :param group_by: The group_by of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :type: list[str]
        """

        self._group_by = group_by

    @property
    def sort(self):
        """Gets the sort of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501


        :return: The sort of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: SortValueObject
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.


        :param sort: The sort of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :type: SortValueObject
        """

        self._sort = sort

    @property
    def query(self):
        """Gets the query of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501


        :return: The query of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.


        :param query: The query of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def inferred_terms(self):
        """Gets the inferred_terms of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501


        :return: The inferred_terms of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: list[CharacteristicValueObject]
        """
        return self._inferred_terms

    @inferred_terms.setter
    def inferred_terms(self, inferred_terms):
        """Sets the inferred_terms of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.


        :param inferred_terms: The inferred_terms of this QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject.  # noqa: E501
        :type: list[CharacteristicValueObject]
        """

        self._inferred_terms = inferred_terms

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
        if issubclass(QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject, dict):
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
        if not isinstance(other, QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
