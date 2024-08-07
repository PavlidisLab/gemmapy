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

class BibliographicPhenotypesValueObject(object):
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
        'gene_ncbi': 'int',
        'gene_name': 'str',
        'evidence_id': 'int',
        'phenotypes_values': 'list[CharacteristicValueObject]',
        'all_id_of_phenotype': 'list[int]'
    }

    attribute_map = {
        'gene_ncbi': 'geneNCBI',
        'gene_name': 'geneName',
        'evidence_id': 'evidenceId',
        'phenotypes_values': 'phenotypesValues',
        'all_id_of_phenotype': 'allIdOfPhenotype'
    }

    def __init__(self, gene_ncbi=None, gene_name=None, evidence_id=None, phenotypes_values=None, all_id_of_phenotype=None):  # noqa: E501
        """BibliographicPhenotypesValueObject - a model defined in Swagger"""  # noqa: E501
        self._gene_ncbi = None
        self._gene_name = None
        self._evidence_id = None
        self._phenotypes_values = None
        self._all_id_of_phenotype = None
        self.discriminator = None
        if gene_ncbi is not None:
            self.gene_ncbi = gene_ncbi
        if gene_name is not None:
            self.gene_name = gene_name
        if evidence_id is not None:
            self.evidence_id = evidence_id
        if phenotypes_values is not None:
            self.phenotypes_values = phenotypes_values
        if all_id_of_phenotype is not None:
            self.all_id_of_phenotype = all_id_of_phenotype

    @property
    def gene_ncbi(self):
        """Gets the gene_ncbi of this BibliographicPhenotypesValueObject.  # noqa: E501


        :return: The gene_ncbi of this BibliographicPhenotypesValueObject.  # noqa: E501
        :rtype: int
        """
        return self._gene_ncbi

    @gene_ncbi.setter
    def gene_ncbi(self, gene_ncbi):
        """Sets the gene_ncbi of this BibliographicPhenotypesValueObject.


        :param gene_ncbi: The gene_ncbi of this BibliographicPhenotypesValueObject.  # noqa: E501
        :type: int
        """

        self._gene_ncbi = gene_ncbi

    @property
    def gene_name(self):
        """Gets the gene_name of this BibliographicPhenotypesValueObject.  # noqa: E501


        :return: The gene_name of this BibliographicPhenotypesValueObject.  # noqa: E501
        :rtype: str
        """
        return self._gene_name

    @gene_name.setter
    def gene_name(self, gene_name):
        """Sets the gene_name of this BibliographicPhenotypesValueObject.


        :param gene_name: The gene_name of this BibliographicPhenotypesValueObject.  # noqa: E501
        :type: str
        """

        self._gene_name = gene_name

    @property
    def evidence_id(self):
        """Gets the evidence_id of this BibliographicPhenotypesValueObject.  # noqa: E501


        :return: The evidence_id of this BibliographicPhenotypesValueObject.  # noqa: E501
        :rtype: int
        """
        return self._evidence_id

    @evidence_id.setter
    def evidence_id(self, evidence_id):
        """Sets the evidence_id of this BibliographicPhenotypesValueObject.


        :param evidence_id: The evidence_id of this BibliographicPhenotypesValueObject.  # noqa: E501
        :type: int
        """

        self._evidence_id = evidence_id

    @property
    def phenotypes_values(self):
        """Gets the phenotypes_values of this BibliographicPhenotypesValueObject.  # noqa: E501


        :return: The phenotypes_values of this BibliographicPhenotypesValueObject.  # noqa: E501
        :rtype: list[CharacteristicValueObject]
        """
        return self._phenotypes_values

    @phenotypes_values.setter
    def phenotypes_values(self, phenotypes_values):
        """Sets the phenotypes_values of this BibliographicPhenotypesValueObject.


        :param phenotypes_values: The phenotypes_values of this BibliographicPhenotypesValueObject.  # noqa: E501
        :type: list[CharacteristicValueObject]
        """

        self._phenotypes_values = phenotypes_values

    @property
    def all_id_of_phenotype(self):
        """Gets the all_id_of_phenotype of this BibliographicPhenotypesValueObject.  # noqa: E501


        :return: The all_id_of_phenotype of this BibliographicPhenotypesValueObject.  # noqa: E501
        :rtype: list[int]
        """
        return self._all_id_of_phenotype

    @all_id_of_phenotype.setter
    def all_id_of_phenotype(self, all_id_of_phenotype):
        """Sets the all_id_of_phenotype of this BibliographicPhenotypesValueObject.


        :param all_id_of_phenotype: The all_id_of_phenotype of this BibliographicPhenotypesValueObject.  # noqa: E501
        :type: list[int]
        """

        self._all_id_of_phenotype = all_id_of_phenotype

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
        if issubclass(BibliographicPhenotypesValueObject, dict):
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
        if not isinstance(other, BibliographicPhenotypesValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
