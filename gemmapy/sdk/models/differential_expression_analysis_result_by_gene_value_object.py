# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.8.0
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DifferentialExpressionAnalysisResultByGeneValueObject(object):
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
        'probe_id': 'int',
        'probe_name': 'str',
        'genes': 'list[GeneValueObject]',
        'corrected_pvalue': 'float',
        'rank': 'float',
        'contrasts': 'list[ContrastResultValueObject]',
        'source_experiment_id': 'int',
        'experiment_analyzed_id': 'int',
        'result_set_id': 'int',
        'pvalue': 'float'
    }

    attribute_map = {
        'id': 'id',
        'probe_id': 'probeId',
        'probe_name': 'probeName',
        'genes': 'genes',
        'corrected_pvalue': 'correctedPvalue',
        'rank': 'rank',
        'contrasts': 'contrasts',
        'source_experiment_id': 'sourceExperimentId',
        'experiment_analyzed_id': 'experimentAnalyzedId',
        'result_set_id': 'resultSetId',
        'pvalue': 'pvalue'
    }

    def __init__(self, id=None, probe_id=None, probe_name=None, genes=None, corrected_pvalue=None, rank=None, contrasts=None, source_experiment_id=None, experiment_analyzed_id=None, result_set_id=None, pvalue=None):  # noqa: E501
        """DifferentialExpressionAnalysisResultByGeneValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._probe_id = None
        self._probe_name = None
        self._genes = None
        self._corrected_pvalue = None
        self._rank = None
        self._contrasts = None
        self._source_experiment_id = None
        self._experiment_analyzed_id = None
        self._result_set_id = None
        self._pvalue = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if probe_id is not None:
            self.probe_id = probe_id
        if probe_name is not None:
            self.probe_name = probe_name
        if genes is not None:
            self.genes = genes
        if corrected_pvalue is not None:
            self.corrected_pvalue = corrected_pvalue
        if rank is not None:
            self.rank = rank
        if contrasts is not None:
            self.contrasts = contrasts
        if source_experiment_id is not None:
            self.source_experiment_id = source_experiment_id
        if experiment_analyzed_id is not None:
            self.experiment_analyzed_id = experiment_analyzed_id
        if result_set_id is not None:
            self.result_set_id = result_set_id
        if pvalue is not None:
            self.pvalue = pvalue

    @property
    def id(self):
        """Gets the id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501


        :return: The id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DifferentialExpressionAnalysisResultByGeneValueObject.


        :param id: The id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def probe_id(self):
        """Gets the probe_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501


        :return: The probe_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._probe_id

    @probe_id.setter
    def probe_id(self, probe_id):
        """Sets the probe_id of this DifferentialExpressionAnalysisResultByGeneValueObject.


        :param probe_id: The probe_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :type: int
        """

        self._probe_id = probe_id

    @property
    def probe_name(self):
        """Gets the probe_name of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501


        :return: The probe_name of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :rtype: str
        """
        return self._probe_name

    @probe_name.setter
    def probe_name(self, probe_name):
        """Sets the probe_name of this DifferentialExpressionAnalysisResultByGeneValueObject.


        :param probe_name: The probe_name of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :type: str
        """

        self._probe_name = probe_name

    @property
    def genes(self):
        """Gets the genes of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501


        :return: The genes of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :rtype: list[GeneValueObject]
        """
        return self._genes

    @genes.setter
    def genes(self, genes):
        """Sets the genes of this DifferentialExpressionAnalysisResultByGeneValueObject.


        :param genes: The genes of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :type: list[GeneValueObject]
        """

        self._genes = genes

    @property
    def corrected_pvalue(self):
        """Gets the corrected_pvalue of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501


        :return: The corrected_pvalue of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :rtype: float
        """
        return self._corrected_pvalue

    @corrected_pvalue.setter
    def corrected_pvalue(self, corrected_pvalue):
        """Sets the corrected_pvalue of this DifferentialExpressionAnalysisResultByGeneValueObject.


        :param corrected_pvalue: The corrected_pvalue of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :type: float
        """

        self._corrected_pvalue = corrected_pvalue

    @property
    def rank(self):
        """Gets the rank of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501


        :return: The rank of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :rtype: float
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this DifferentialExpressionAnalysisResultByGeneValueObject.


        :param rank: The rank of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :type: float
        """

        self._rank = rank

    @property
    def contrasts(self):
        """Gets the contrasts of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501


        :return: The contrasts of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :rtype: list[ContrastResultValueObject]
        """
        return self._contrasts

    @contrasts.setter
    def contrasts(self, contrasts):
        """Sets the contrasts of this DifferentialExpressionAnalysisResultByGeneValueObject.


        :param contrasts: The contrasts of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :type: list[ContrastResultValueObject]
        """

        self._contrasts = contrasts

    @property
    def source_experiment_id(self):
        """Gets the source_experiment_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501


        :return: The source_experiment_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._source_experiment_id

    @source_experiment_id.setter
    def source_experiment_id(self, source_experiment_id):
        """Sets the source_experiment_id of this DifferentialExpressionAnalysisResultByGeneValueObject.


        :param source_experiment_id: The source_experiment_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :type: int
        """

        self._source_experiment_id = source_experiment_id

    @property
    def experiment_analyzed_id(self):
        """Gets the experiment_analyzed_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501


        :return: The experiment_analyzed_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._experiment_analyzed_id

    @experiment_analyzed_id.setter
    def experiment_analyzed_id(self, experiment_analyzed_id):
        """Sets the experiment_analyzed_id of this DifferentialExpressionAnalysisResultByGeneValueObject.


        :param experiment_analyzed_id: The experiment_analyzed_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :type: int
        """

        self._experiment_analyzed_id = experiment_analyzed_id

    @property
    def result_set_id(self):
        """Gets the result_set_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501


        :return: The result_set_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._result_set_id

    @result_set_id.setter
    def result_set_id(self, result_set_id):
        """Sets the result_set_id of this DifferentialExpressionAnalysisResultByGeneValueObject.


        :param result_set_id: The result_set_id of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :type: int
        """

        self._result_set_id = result_set_id

    @property
    def pvalue(self):
        """Gets the pvalue of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501


        :return: The pvalue of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :rtype: float
        """
        return self._pvalue

    @pvalue.setter
    def pvalue(self, pvalue):
        """Sets the pvalue of this DifferentialExpressionAnalysisResultByGeneValueObject.


        :param pvalue: The pvalue of this DifferentialExpressionAnalysisResultByGeneValueObject.  # noqa: E501
        :type: float
        """

        self._pvalue = pvalue

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
        if issubclass(DifferentialExpressionAnalysisResultByGeneValueObject, dict):
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
        if not isinstance(other, DifferentialExpressionAnalysisResultByGeneValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
