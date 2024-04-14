# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.7.3
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GeneSetValueObject(object):
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
        'name': 'str',
        'description': 'str',
        'gene_ids': 'list[int]',
        'size': 'int',
        'taxon': 'TaxonValueObject'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'gene_ids': 'geneIds',
        'size': 'size',
        'taxon': 'taxon'
    }

    def __init__(self, id=None, name=None, description=None, gene_ids=None, size=None, taxon=None):  # noqa: E501
        """GeneSetValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._gene_ids = None
        self._size = None
        self._taxon = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if gene_ids is not None:
            self.gene_ids = gene_ids
        if size is not None:
            self.size = size
        if taxon is not None:
            self.taxon = taxon

    @property
    def id(self):
        """Gets the id of this GeneSetValueObject.  # noqa: E501


        :return: The id of this GeneSetValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GeneSetValueObject.


        :param id: The id of this GeneSetValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GeneSetValueObject.  # noqa: E501


        :return: The name of this GeneSetValueObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GeneSetValueObject.


        :param name: The name of this GeneSetValueObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this GeneSetValueObject.  # noqa: E501


        :return: The description of this GeneSetValueObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GeneSetValueObject.


        :param description: The description of this GeneSetValueObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gene_ids(self):
        """Gets the gene_ids of this GeneSetValueObject.  # noqa: E501


        :return: The gene_ids of this GeneSetValueObject.  # noqa: E501
        :rtype: list[int]
        """
        return self._gene_ids

    @gene_ids.setter
    def gene_ids(self, gene_ids):
        """Sets the gene_ids of this GeneSetValueObject.


        :param gene_ids: The gene_ids of this GeneSetValueObject.  # noqa: E501
        :type: list[int]
        """

        self._gene_ids = gene_ids

    @property
    def size(self):
        """Gets the size of this GeneSetValueObject.  # noqa: E501


        :return: The size of this GeneSetValueObject.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this GeneSetValueObject.


        :param size: The size of this GeneSetValueObject.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def taxon(self):
        """Gets the taxon of this GeneSetValueObject.  # noqa: E501


        :return: The taxon of this GeneSetValueObject.  # noqa: E501
        :rtype: TaxonValueObject
        """
        return self._taxon

    @taxon.setter
    def taxon(self, taxon):
        """Sets the taxon of this GeneSetValueObject.


        :param taxon: The taxon of this GeneSetValueObject.  # noqa: E501
        :type: TaxonValueObject
        """

        self._taxon = taxon

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
        if issubclass(GeneSetValueObject, dict):
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
        if not isinstance(other, GeneSetValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
