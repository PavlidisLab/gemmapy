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

class GeneElementExpressionsValueObject(object):
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
        'gene_official_symbol': 'str',
        'gene_ncbi_id': 'int',
        'vectors': 'list[VectorElementValueObject]'
    }

    attribute_map = {
        'gene_official_symbol': 'geneOfficialSymbol',
        'gene_ncbi_id': 'geneNcbiId',
        'vectors': 'vectors'
    }

    def __init__(self, gene_official_symbol=None, gene_ncbi_id=None, vectors=None):  # noqa: E501
        """GeneElementExpressionsValueObject - a model defined in Swagger"""  # noqa: E501
        self._gene_official_symbol = None
        self._gene_ncbi_id = None
        self._vectors = None
        self.discriminator = None
        if gene_official_symbol is not None:
            self.gene_official_symbol = gene_official_symbol
        if gene_ncbi_id is not None:
            self.gene_ncbi_id = gene_ncbi_id
        if vectors is not None:
            self.vectors = vectors

    @property
    def gene_official_symbol(self):
        """Gets the gene_official_symbol of this GeneElementExpressionsValueObject.  # noqa: E501


        :return: The gene_official_symbol of this GeneElementExpressionsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._gene_official_symbol

    @gene_official_symbol.setter
    def gene_official_symbol(self, gene_official_symbol):
        """Sets the gene_official_symbol of this GeneElementExpressionsValueObject.


        :param gene_official_symbol: The gene_official_symbol of this GeneElementExpressionsValueObject.  # noqa: E501
        :type: str
        """

        self._gene_official_symbol = gene_official_symbol

    @property
    def gene_ncbi_id(self):
        """Gets the gene_ncbi_id of this GeneElementExpressionsValueObject.  # noqa: E501


        :return: The gene_ncbi_id of this GeneElementExpressionsValueObject.  # noqa: E501
        :rtype: int
        """
        return self._gene_ncbi_id

    @gene_ncbi_id.setter
    def gene_ncbi_id(self, gene_ncbi_id):
        """Sets the gene_ncbi_id of this GeneElementExpressionsValueObject.


        :param gene_ncbi_id: The gene_ncbi_id of this GeneElementExpressionsValueObject.  # noqa: E501
        :type: int
        """

        self._gene_ncbi_id = gene_ncbi_id

    @property
    def vectors(self):
        """Gets the vectors of this GeneElementExpressionsValueObject.  # noqa: E501


        :return: The vectors of this GeneElementExpressionsValueObject.  # noqa: E501
        :rtype: list[VectorElementValueObject]
        """
        return self._vectors

    @vectors.setter
    def vectors(self, vectors):
        """Sets the vectors of this GeneElementExpressionsValueObject.


        :param vectors: The vectors of this GeneElementExpressionsValueObject.  # noqa: E501
        :type: list[VectorElementValueObject]
        """

        self._vectors = vectors

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
        if issubclass(GeneElementExpressionsValueObject, dict):
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
        if not isinstance(other, GeneElementExpressionsValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
