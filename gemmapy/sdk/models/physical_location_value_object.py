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

class PhysicalLocationValueObject(object):
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
        'nucleotide': 'int',
        'nucleotide_length': 'int',
        'strand': 'str',
        'bin': 'int',
        'chromosome': 'str',
        'taxon': 'TaxonValueObject'
    }

    attribute_map = {
        'id': 'id',
        'nucleotide': 'nucleotide',
        'nucleotide_length': 'nucleotideLength',
        'strand': 'strand',
        'bin': 'bin',
        'chromosome': 'chromosome',
        'taxon': 'taxon'
    }

    def __init__(self, id=None, nucleotide=None, nucleotide_length=None, strand=None, bin=None, chromosome=None, taxon=None):  # noqa: E501
        """PhysicalLocationValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._nucleotide = None
        self._nucleotide_length = None
        self._strand = None
        self._bin = None
        self._chromosome = None
        self._taxon = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if nucleotide is not None:
            self.nucleotide = nucleotide
        if nucleotide_length is not None:
            self.nucleotide_length = nucleotide_length
        if strand is not None:
            self.strand = strand
        if bin is not None:
            self.bin = bin
        if chromosome is not None:
            self.chromosome = chromosome
        if taxon is not None:
            self.taxon = taxon

    @property
    def id(self):
        """Gets the id of this PhysicalLocationValueObject.  # noqa: E501


        :return: The id of this PhysicalLocationValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PhysicalLocationValueObject.


        :param id: The id of this PhysicalLocationValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def nucleotide(self):
        """Gets the nucleotide of this PhysicalLocationValueObject.  # noqa: E501


        :return: The nucleotide of this PhysicalLocationValueObject.  # noqa: E501
        :rtype: int
        """
        return self._nucleotide

    @nucleotide.setter
    def nucleotide(self, nucleotide):
        """Sets the nucleotide of this PhysicalLocationValueObject.


        :param nucleotide: The nucleotide of this PhysicalLocationValueObject.  # noqa: E501
        :type: int
        """

        self._nucleotide = nucleotide

    @property
    def nucleotide_length(self):
        """Gets the nucleotide_length of this PhysicalLocationValueObject.  # noqa: E501


        :return: The nucleotide_length of this PhysicalLocationValueObject.  # noqa: E501
        :rtype: int
        """
        return self._nucleotide_length

    @nucleotide_length.setter
    def nucleotide_length(self, nucleotide_length):
        """Sets the nucleotide_length of this PhysicalLocationValueObject.


        :param nucleotide_length: The nucleotide_length of this PhysicalLocationValueObject.  # noqa: E501
        :type: int
        """

        self._nucleotide_length = nucleotide_length

    @property
    def strand(self):
        """Gets the strand of this PhysicalLocationValueObject.  # noqa: E501


        :return: The strand of this PhysicalLocationValueObject.  # noqa: E501
        :rtype: str
        """
        return self._strand

    @strand.setter
    def strand(self, strand):
        """Sets the strand of this PhysicalLocationValueObject.


        :param strand: The strand of this PhysicalLocationValueObject.  # noqa: E501
        :type: str
        """

        self._strand = strand

    @property
    def bin(self):
        """Gets the bin of this PhysicalLocationValueObject.  # noqa: E501


        :return: The bin of this PhysicalLocationValueObject.  # noqa: E501
        :rtype: int
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """Sets the bin of this PhysicalLocationValueObject.


        :param bin: The bin of this PhysicalLocationValueObject.  # noqa: E501
        :type: int
        """

        self._bin = bin

    @property
    def chromosome(self):
        """Gets the chromosome of this PhysicalLocationValueObject.  # noqa: E501


        :return: The chromosome of this PhysicalLocationValueObject.  # noqa: E501
        :rtype: str
        """
        return self._chromosome

    @chromosome.setter
    def chromosome(self, chromosome):
        """Sets the chromosome of this PhysicalLocationValueObject.


        :param chromosome: The chromosome of this PhysicalLocationValueObject.  # noqa: E501
        :type: str
        """

        self._chromosome = chromosome

    @property
    def taxon(self):
        """Gets the taxon of this PhysicalLocationValueObject.  # noqa: E501


        :return: The taxon of this PhysicalLocationValueObject.  # noqa: E501
        :rtype: TaxonValueObject
        """
        return self._taxon

    @taxon.setter
    def taxon(self, taxon):
        """Sets the taxon of this PhysicalLocationValueObject.


        :param taxon: The taxon of this PhysicalLocationValueObject.  # noqa: E501
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
        if issubclass(PhysicalLocationValueObject, dict):
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
        if not isinstance(other, PhysicalLocationValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
