# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.7.2
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExperimentExpressionLevelsValueObject(object):
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
        'dataset_id': 'int',
        'gene_expression_levels': 'list[GeneElementExpressionsValueObject]'
    }

    attribute_map = {
        'dataset_id': 'datasetId',
        'gene_expression_levels': 'geneExpressionLevels'
    }

    def __init__(self, dataset_id=None, gene_expression_levels=None):  # noqa: E501
        """ExperimentExpressionLevelsValueObject - a model defined in Swagger"""  # noqa: E501
        self._dataset_id = None
        self._gene_expression_levels = None
        self.discriminator = None
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if gene_expression_levels is not None:
            self.gene_expression_levels = gene_expression_levels

    @property
    def dataset_id(self):
        """Gets the dataset_id of this ExperimentExpressionLevelsValueObject.  # noqa: E501


        :return: The dataset_id of this ExperimentExpressionLevelsValueObject.  # noqa: E501
        :rtype: int
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this ExperimentExpressionLevelsValueObject.


        :param dataset_id: The dataset_id of this ExperimentExpressionLevelsValueObject.  # noqa: E501
        :type: int
        """

        self._dataset_id = dataset_id

    @property
    def gene_expression_levels(self):
        """Gets the gene_expression_levels of this ExperimentExpressionLevelsValueObject.  # noqa: E501


        :return: The gene_expression_levels of this ExperimentExpressionLevelsValueObject.  # noqa: E501
        :rtype: list[GeneElementExpressionsValueObject]
        """
        return self._gene_expression_levels

    @gene_expression_levels.setter
    def gene_expression_levels(self, gene_expression_levels):
        """Sets the gene_expression_levels of this ExperimentExpressionLevelsValueObject.


        :param gene_expression_levels: The gene_expression_levels of this ExperimentExpressionLevelsValueObject.  # noqa: E501
        :type: list[GeneElementExpressionsValueObject]
        """

        self._gene_expression_levels = gene_expression_levels

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
        if issubclass(ExperimentExpressionLevelsValueObject, dict):
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
        if not isinstance(other, ExperimentExpressionLevelsValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
