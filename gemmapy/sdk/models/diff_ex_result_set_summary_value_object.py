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

class DiffExResultSetSummaryValueObject(object):
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
        'analysis_id': 'int',
        'array_designs_used': 'list[int]',
        'baseline_group': 'FactorValueValueObject',
        'downregulated_count': 'int',
        'experimental_factors': 'list[ExperimentalFactorValueObject]',
        'factor_ids': 'list[int]',
        'number_of_diff_expressed_probes': 'int',
        'number_of_genes_analyzed': 'int',
        'number_of_probes_analyzed': 'int',
        'threshold': 'float',
        'upregulated_count': 'int',
        'bio_assay_set_analyzed_id': 'int',
        'qvalue': 'float',
        'experimental_factors_by_value_object': 'list[ExperimentalFactorValueObject]',
        'result_set_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'analysis_id': 'analysisId',
        'array_designs_used': 'arrayDesignsUsed',
        'baseline_group': 'baselineGroup',
        'downregulated_count': 'downregulatedCount',
        'experimental_factors': 'experimentalFactors',
        'factor_ids': 'factorIds',
        'number_of_diff_expressed_probes': 'numberOfDiffExpressedProbes',
        'number_of_genes_analyzed': 'numberOfGenesAnalyzed',
        'number_of_probes_analyzed': 'numberOfProbesAnalyzed',
        'threshold': 'threshold',
        'upregulated_count': 'upregulatedCount',
        'bio_assay_set_analyzed_id': 'bioAssaySetAnalyzedId',
        'qvalue': 'qvalue',
        'experimental_factors_by_value_object': 'experimentalFactorsByValueObject',
        'result_set_id': 'resultSetId'
    }

    def __init__(self, id=None, analysis_id=None, array_designs_used=None, baseline_group=None, downregulated_count=None, experimental_factors=None, factor_ids=None, number_of_diff_expressed_probes=None, number_of_genes_analyzed=None, number_of_probes_analyzed=None, threshold=None, upregulated_count=None, bio_assay_set_analyzed_id=None, qvalue=None, experimental_factors_by_value_object=None, result_set_id=None):  # noqa: E501
        """DiffExResultSetSummaryValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._analysis_id = None
        self._array_designs_used = None
        self._baseline_group = None
        self._downregulated_count = None
        self._experimental_factors = None
        self._factor_ids = None
        self._number_of_diff_expressed_probes = None
        self._number_of_genes_analyzed = None
        self._number_of_probes_analyzed = None
        self._threshold = None
        self._upregulated_count = None
        self._bio_assay_set_analyzed_id = None
        self._qvalue = None
        self._experimental_factors_by_value_object = None
        self._result_set_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if analysis_id is not None:
            self.analysis_id = analysis_id
        if array_designs_used is not None:
            self.array_designs_used = array_designs_used
        if baseline_group is not None:
            self.baseline_group = baseline_group
        if downregulated_count is not None:
            self.downregulated_count = downregulated_count
        if experimental_factors is not None:
            self.experimental_factors = experimental_factors
        if factor_ids is not None:
            self.factor_ids = factor_ids
        if number_of_diff_expressed_probes is not None:
            self.number_of_diff_expressed_probes = number_of_diff_expressed_probes
        if number_of_genes_analyzed is not None:
            self.number_of_genes_analyzed = number_of_genes_analyzed
        if number_of_probes_analyzed is not None:
            self.number_of_probes_analyzed = number_of_probes_analyzed
        if threshold is not None:
            self.threshold = threshold
        if upregulated_count is not None:
            self.upregulated_count = upregulated_count
        if bio_assay_set_analyzed_id is not None:
            self.bio_assay_set_analyzed_id = bio_assay_set_analyzed_id
        if qvalue is not None:
            self.qvalue = qvalue
        if experimental_factors_by_value_object is not None:
            self.experimental_factors_by_value_object = experimental_factors_by_value_object
        if result_set_id is not None:
            self.result_set_id = result_set_id

    @property
    def id(self):
        """Gets the id of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The id of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DiffExResultSetSummaryValueObject.


        :param id: The id of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def analysis_id(self):
        """Gets the analysis_id of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The analysis_id of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: int
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id):
        """Sets the analysis_id of this DiffExResultSetSummaryValueObject.


        :param analysis_id: The analysis_id of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: int
        """

        self._analysis_id = analysis_id

    @property
    def array_designs_used(self):
        """Gets the array_designs_used of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The array_designs_used of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: list[int]
        """
        return self._array_designs_used

    @array_designs_used.setter
    def array_designs_used(self, array_designs_used):
        """Sets the array_designs_used of this DiffExResultSetSummaryValueObject.


        :param array_designs_used: The array_designs_used of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: list[int]
        """

        self._array_designs_used = array_designs_used

    @property
    def baseline_group(self):
        """Gets the baseline_group of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The baseline_group of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: FactorValueValueObject
        """
        return self._baseline_group

    @baseline_group.setter
    def baseline_group(self, baseline_group):
        """Sets the baseline_group of this DiffExResultSetSummaryValueObject.


        :param baseline_group: The baseline_group of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: FactorValueValueObject
        """

        self._baseline_group = baseline_group

    @property
    def downregulated_count(self):
        """Gets the downregulated_count of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The downregulated_count of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: int
        """
        return self._downregulated_count

    @downregulated_count.setter
    def downregulated_count(self, downregulated_count):
        """Sets the downregulated_count of this DiffExResultSetSummaryValueObject.


        :param downregulated_count: The downregulated_count of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: int
        """

        self._downregulated_count = downregulated_count

    @property
    def experimental_factors(self):
        """Gets the experimental_factors of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The experimental_factors of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: list[ExperimentalFactorValueObject]
        """
        return self._experimental_factors

    @experimental_factors.setter
    def experimental_factors(self, experimental_factors):
        """Sets the experimental_factors of this DiffExResultSetSummaryValueObject.


        :param experimental_factors: The experimental_factors of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: list[ExperimentalFactorValueObject]
        """

        self._experimental_factors = experimental_factors

    @property
    def factor_ids(self):
        """Gets the factor_ids of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The factor_ids of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: list[int]
        """
        return self._factor_ids

    @factor_ids.setter
    def factor_ids(self, factor_ids):
        """Sets the factor_ids of this DiffExResultSetSummaryValueObject.


        :param factor_ids: The factor_ids of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: list[int]
        """

        self._factor_ids = factor_ids

    @property
    def number_of_diff_expressed_probes(self):
        """Gets the number_of_diff_expressed_probes of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The number_of_diff_expressed_probes of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: int
        """
        return self._number_of_diff_expressed_probes

    @number_of_diff_expressed_probes.setter
    def number_of_diff_expressed_probes(self, number_of_diff_expressed_probes):
        """Sets the number_of_diff_expressed_probes of this DiffExResultSetSummaryValueObject.


        :param number_of_diff_expressed_probes: The number_of_diff_expressed_probes of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: int
        """

        self._number_of_diff_expressed_probes = number_of_diff_expressed_probes

    @property
    def number_of_genes_analyzed(self):
        """Gets the number_of_genes_analyzed of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The number_of_genes_analyzed of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: int
        """
        return self._number_of_genes_analyzed

    @number_of_genes_analyzed.setter
    def number_of_genes_analyzed(self, number_of_genes_analyzed):
        """Sets the number_of_genes_analyzed of this DiffExResultSetSummaryValueObject.


        :param number_of_genes_analyzed: The number_of_genes_analyzed of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: int
        """

        self._number_of_genes_analyzed = number_of_genes_analyzed

    @property
    def number_of_probes_analyzed(self):
        """Gets the number_of_probes_analyzed of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The number_of_probes_analyzed of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: int
        """
        return self._number_of_probes_analyzed

    @number_of_probes_analyzed.setter
    def number_of_probes_analyzed(self, number_of_probes_analyzed):
        """Sets the number_of_probes_analyzed of this DiffExResultSetSummaryValueObject.


        :param number_of_probes_analyzed: The number_of_probes_analyzed of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: int
        """

        self._number_of_probes_analyzed = number_of_probes_analyzed

    @property
    def threshold(self):
        """Gets the threshold of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The threshold of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this DiffExResultSetSummaryValueObject.


        :param threshold: The threshold of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

    @property
    def upregulated_count(self):
        """Gets the upregulated_count of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The upregulated_count of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: int
        """
        return self._upregulated_count

    @upregulated_count.setter
    def upregulated_count(self, upregulated_count):
        """Sets the upregulated_count of this DiffExResultSetSummaryValueObject.


        :param upregulated_count: The upregulated_count of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: int
        """

        self._upregulated_count = upregulated_count

    @property
    def bio_assay_set_analyzed_id(self):
        """Gets the bio_assay_set_analyzed_id of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The bio_assay_set_analyzed_id of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: int
        """
        return self._bio_assay_set_analyzed_id

    @bio_assay_set_analyzed_id.setter
    def bio_assay_set_analyzed_id(self, bio_assay_set_analyzed_id):
        """Sets the bio_assay_set_analyzed_id of this DiffExResultSetSummaryValueObject.


        :param bio_assay_set_analyzed_id: The bio_assay_set_analyzed_id of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: int
        """

        self._bio_assay_set_analyzed_id = bio_assay_set_analyzed_id

    @property
    def qvalue(self):
        """Gets the qvalue of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The qvalue of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: float
        """
        return self._qvalue

    @qvalue.setter
    def qvalue(self, qvalue):
        """Sets the qvalue of this DiffExResultSetSummaryValueObject.


        :param qvalue: The qvalue of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: float
        """

        self._qvalue = qvalue

    @property
    def experimental_factors_by_value_object(self):
        """Gets the experimental_factors_by_value_object of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The experimental_factors_by_value_object of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: list[ExperimentalFactorValueObject]
        """
        return self._experimental_factors_by_value_object

    @experimental_factors_by_value_object.setter
    def experimental_factors_by_value_object(self, experimental_factors_by_value_object):
        """Sets the experimental_factors_by_value_object of this DiffExResultSetSummaryValueObject.


        :param experimental_factors_by_value_object: The experimental_factors_by_value_object of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: list[ExperimentalFactorValueObject]
        """

        self._experimental_factors_by_value_object = experimental_factors_by_value_object

    @property
    def result_set_id(self):
        """Gets the result_set_id of this DiffExResultSetSummaryValueObject.  # noqa: E501


        :return: The result_set_id of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :rtype: int
        """
        return self._result_set_id

    @result_set_id.setter
    def result_set_id(self, result_set_id):
        """Sets the result_set_id of this DiffExResultSetSummaryValueObject.


        :param result_set_id: The result_set_id of this DiffExResultSetSummaryValueObject.  # noqa: E501
        :type: int
        """

        self._result_set_id = result_set_id

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
        if issubclass(DiffExResultSetSummaryValueObject, dict):
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
        if not isinstance(other, DiffExResultSetSummaryValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other