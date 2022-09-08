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

class DifferentialExpressionAnalysisResultValueObject(object):
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
        'probe_id': 'int',
        'probe_name': 'str',
        'genes': 'list[GeneValueObject]',
        'corrected_pvalue': 'float',
        'rank': 'float',
        'contrasts': 'list[ContrastResultValueObject]',
        'pvalue': 'float'
    }

    attribute_map = {
        'probe_id': 'probeId',
        'probe_name': 'probeName',
        'genes': 'genes',
        'corrected_pvalue': 'correctedPvalue',
        'rank': 'rank',
        'contrasts': 'contrasts',
        'pvalue': 'pvalue'
    }

    def __init__(self, probe_id=None, probe_name=None, genes=None, corrected_pvalue=None, rank=None, contrasts=None, pvalue=None):  # noqa: E501
        """DifferentialExpressionAnalysisResultValueObject - a model defined in Swagger"""  # noqa: E501
        self._probe_id = None
        self._probe_name = None
        self._genes = None
        self._corrected_pvalue = None
        self._rank = None
        self._contrasts = None
        self._pvalue = None
        self.discriminator = None
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
        if pvalue is not None:
            self.pvalue = pvalue

    @property
    def probe_id(self):
        """Gets the probe_id of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501


        :return: The probe_id of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._probe_id

    @probe_id.setter
    def probe_id(self, probe_id):
        """Sets the probe_id of this DifferentialExpressionAnalysisResultValueObject.


        :param probe_id: The probe_id of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :type: int
        """

        self._probe_id = probe_id

    @property
    def probe_name(self):
        """Gets the probe_name of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501


        :return: The probe_name of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :rtype: str
        """
        return self._probe_name

    @probe_name.setter
    def probe_name(self, probe_name):
        """Sets the probe_name of this DifferentialExpressionAnalysisResultValueObject.


        :param probe_name: The probe_name of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :type: str
        """

        self._probe_name = probe_name

    @property
    def genes(self):
        """Gets the genes of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501


        :return: The genes of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :rtype: list[GeneValueObject]
        """
        return self._genes

    @genes.setter
    def genes(self, genes):
        """Sets the genes of this DifferentialExpressionAnalysisResultValueObject.


        :param genes: The genes of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :type: list[GeneValueObject]
        """

        self._genes = genes

    @property
    def corrected_pvalue(self):
        """Gets the corrected_pvalue of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501


        :return: The corrected_pvalue of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :rtype: float
        """
        return self._corrected_pvalue

    @corrected_pvalue.setter
    def corrected_pvalue(self, corrected_pvalue):
        """Sets the corrected_pvalue of this DifferentialExpressionAnalysisResultValueObject.


        :param corrected_pvalue: The corrected_pvalue of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :type: float
        """

        self._corrected_pvalue = corrected_pvalue

    @property
    def rank(self):
        """Gets the rank of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501


        :return: The rank of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :rtype: float
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this DifferentialExpressionAnalysisResultValueObject.


        :param rank: The rank of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :type: float
        """

        self._rank = rank

    @property
    def contrasts(self):
        """Gets the contrasts of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501


        :return: The contrasts of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :rtype: list[ContrastResultValueObject]
        """
        return self._contrasts

    @contrasts.setter
    def contrasts(self, contrasts):
        """Sets the contrasts of this DifferentialExpressionAnalysisResultValueObject.


        :param contrasts: The contrasts of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :type: list[ContrastResultValueObject]
        """

        self._contrasts = contrasts

    @property
    def pvalue(self):
        """Gets the pvalue of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501


        :return: The pvalue of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
        :rtype: float
        """
        return self._pvalue

    @pvalue.setter
    def pvalue(self, pvalue):
        """Sets the pvalue of this DifferentialExpressionAnalysisResultValueObject.


        :param pvalue: The pvalue of this DifferentialExpressionAnalysisResultValueObject.  # noqa: E501
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
        if issubclass(DifferentialExpressionAnalysisResultValueObject, dict):
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
        if not isinstance(other, DifferentialExpressionAnalysisResultValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
