# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.8.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DifferentialExpressionAnalysisResultSetValueObject(object):
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
        'analysis': 'DifferentialExpressionAnalysisValueObject',
        'experimental_factors': 'list[ExperimentalFactorValueObject]',
        'baseline_group': 'FactorValueBasicValueObject',
        'second_baseline_group': 'FactorValueBasicValueObject',
        'taxa': 'list[TaxonValueObject]',
        'results': 'list[DifferentialExpressionAnalysisResultValueObject]'
    }

    attribute_map = {
        'id': 'id',
        'analysis': 'analysis',
        'experimental_factors': 'experimentalFactors',
        'baseline_group': 'baselineGroup',
        'second_baseline_group': 'secondBaselineGroup',
        'taxa': 'taxa',
        'results': 'results'
    }

    def __init__(self, id=None, analysis=None, experimental_factors=None, baseline_group=None, second_baseline_group=None, taxa=None, results=None):  # noqa: E501
        """DifferentialExpressionAnalysisResultSetValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._analysis = None
        self._experimental_factors = None
        self._baseline_group = None
        self._second_baseline_group = None
        self._taxa = None
        self._results = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if analysis is not None:
            self.analysis = analysis
        if experimental_factors is not None:
            self.experimental_factors = experimental_factors
        if baseline_group is not None:
            self.baseline_group = baseline_group
        if second_baseline_group is not None:
            self.second_baseline_group = second_baseline_group
        if taxa is not None:
            self.taxa = taxa
        if results is not None:
            self.results = results

    @property
    def id(self):
        """Gets the id of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501


        :return: The id of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DifferentialExpressionAnalysisResultSetValueObject.


        :param id: The id of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def analysis(self):
        """Gets the analysis of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501


        :return: The analysis of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :rtype: DifferentialExpressionAnalysisValueObject
        """
        return self._analysis

    @analysis.setter
    def analysis(self, analysis):
        """Sets the analysis of this DifferentialExpressionAnalysisResultSetValueObject.


        :param analysis: The analysis of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :type: DifferentialExpressionAnalysisValueObject
        """

        self._analysis = analysis

    @property
    def experimental_factors(self):
        """Gets the experimental_factors of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501


        :return: The experimental_factors of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :rtype: list[ExperimentalFactorValueObject]
        """
        return self._experimental_factors

    @experimental_factors.setter
    def experimental_factors(self, experimental_factors):
        """Sets the experimental_factors of this DifferentialExpressionAnalysisResultSetValueObject.


        :param experimental_factors: The experimental_factors of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :type: list[ExperimentalFactorValueObject]
        """

        self._experimental_factors = experimental_factors

    @property
    def baseline_group(self):
        """Gets the baseline_group of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501


        :return: The baseline_group of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :rtype: FactorValueBasicValueObject
        """
        return self._baseline_group

    @baseline_group.setter
    def baseline_group(self, baseline_group):
        """Sets the baseline_group of this DifferentialExpressionAnalysisResultSetValueObject.


        :param baseline_group: The baseline_group of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :type: FactorValueBasicValueObject
        """

        self._baseline_group = baseline_group

    @property
    def second_baseline_group(self):
        """Gets the second_baseline_group of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501


        :return: The second_baseline_group of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :rtype: FactorValueBasicValueObject
        """
        return self._second_baseline_group

    @second_baseline_group.setter
    def second_baseline_group(self, second_baseline_group):
        """Sets the second_baseline_group of this DifferentialExpressionAnalysisResultSetValueObject.


        :param second_baseline_group: The second_baseline_group of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :type: FactorValueBasicValueObject
        """

        self._second_baseline_group = second_baseline_group

    @property
    def taxa(self):
        """Gets the taxa of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501


        :return: The taxa of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :rtype: list[TaxonValueObject]
        """
        return self._taxa

    @taxa.setter
    def taxa(self, taxa):
        """Sets the taxa of this DifferentialExpressionAnalysisResultSetValueObject.


        :param taxa: The taxa of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :type: list[TaxonValueObject]
        """

        self._taxa = taxa

    @property
    def results(self):
        """Gets the results of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501


        :return: The results of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :rtype: list[DifferentialExpressionAnalysisResultValueObject]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this DifferentialExpressionAnalysisResultSetValueObject.


        :param results: The results of this DifferentialExpressionAnalysisResultSetValueObject.  # noqa: E501
        :type: list[DifferentialExpressionAnalysisResultValueObject]
        """

        self._results = results

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
        if issubclass(DifferentialExpressionAnalysisResultSetValueObject, dict):
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
        if not isinstance(other, DifferentialExpressionAnalysisResultSetValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
