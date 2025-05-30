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

class BioSequenceValueObject(object):
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
        'description': 'str',
        'fraction_repeats': 'float',
        'length': 'int',
        'name': 'str',
        'sequence': 'str',
        'sequence_database_entry': 'DatabaseEntryValueObject',
        'taxon': 'TaxonValueObject',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'fraction_repeats': 'fractionRepeats',
        'length': 'length',
        'name': 'name',
        'sequence': 'sequence',
        'sequence_database_entry': 'sequenceDatabaseEntry',
        'taxon': 'taxon',
        'type': 'type'
    }

    def __init__(self, id=None, description=None, fraction_repeats=None, length=None, name=None, sequence=None, sequence_database_entry=None, taxon=None, type=None):  # noqa: E501
        """BioSequenceValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._description = None
        self._fraction_repeats = None
        self._length = None
        self._name = None
        self._sequence = None
        self._sequence_database_entry = None
        self._taxon = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if fraction_repeats is not None:
            self.fraction_repeats = fraction_repeats
        if length is not None:
            self.length = length
        if name is not None:
            self.name = name
        if sequence is not None:
            self.sequence = sequence
        if sequence_database_entry is not None:
            self.sequence_database_entry = sequence_database_entry
        if taxon is not None:
            self.taxon = taxon
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this BioSequenceValueObject.  # noqa: E501


        :return: The id of this BioSequenceValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BioSequenceValueObject.


        :param id: The id of this BioSequenceValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this BioSequenceValueObject.  # noqa: E501


        :return: The description of this BioSequenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BioSequenceValueObject.


        :param description: The description of this BioSequenceValueObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fraction_repeats(self):
        """Gets the fraction_repeats of this BioSequenceValueObject.  # noqa: E501


        :return: The fraction_repeats of this BioSequenceValueObject.  # noqa: E501
        :rtype: float
        """
        return self._fraction_repeats

    @fraction_repeats.setter
    def fraction_repeats(self, fraction_repeats):
        """Sets the fraction_repeats of this BioSequenceValueObject.


        :param fraction_repeats: The fraction_repeats of this BioSequenceValueObject.  # noqa: E501
        :type: float
        """

        self._fraction_repeats = fraction_repeats

    @property
    def length(self):
        """Gets the length of this BioSequenceValueObject.  # noqa: E501


        :return: The length of this BioSequenceValueObject.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this BioSequenceValueObject.


        :param length: The length of this BioSequenceValueObject.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def name(self):
        """Gets the name of this BioSequenceValueObject.  # noqa: E501


        :return: The name of this BioSequenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BioSequenceValueObject.


        :param name: The name of this BioSequenceValueObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sequence(self):
        """Gets the sequence of this BioSequenceValueObject.  # noqa: E501


        :return: The sequence of this BioSequenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this BioSequenceValueObject.


        :param sequence: The sequence of this BioSequenceValueObject.  # noqa: E501
        :type: str
        """

        self._sequence = sequence

    @property
    def sequence_database_entry(self):
        """Gets the sequence_database_entry of this BioSequenceValueObject.  # noqa: E501


        :return: The sequence_database_entry of this BioSequenceValueObject.  # noqa: E501
        :rtype: DatabaseEntryValueObject
        """
        return self._sequence_database_entry

    @sequence_database_entry.setter
    def sequence_database_entry(self, sequence_database_entry):
        """Sets the sequence_database_entry of this BioSequenceValueObject.


        :param sequence_database_entry: The sequence_database_entry of this BioSequenceValueObject.  # noqa: E501
        :type: DatabaseEntryValueObject
        """

        self._sequence_database_entry = sequence_database_entry

    @property
    def taxon(self):
        """Gets the taxon of this BioSequenceValueObject.  # noqa: E501


        :return: The taxon of this BioSequenceValueObject.  # noqa: E501
        :rtype: TaxonValueObject
        """
        return self._taxon

    @taxon.setter
    def taxon(self, taxon):
        """Sets the taxon of this BioSequenceValueObject.


        :param taxon: The taxon of this BioSequenceValueObject.  # noqa: E501
        :type: TaxonValueObject
        """

        self._taxon = taxon

    @property
    def type(self):
        """Gets the type of this BioSequenceValueObject.  # noqa: E501


        :return: The type of this BioSequenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BioSequenceValueObject.


        :param type: The type of this BioSequenceValueObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["AFFY_TARGET", "AFFY_PROBE", "EST", "mRNA", "REFSEQ", "BAC", "WHOLE_GENOME", "WHOLE_CHROMOSOME", "DNA", "OTHER", "ORF", "AFFY_COLLAPSED", "OLIGO", "DUMMY"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(BioSequenceValueObject, dict):
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
        if not isinstance(other, BioSequenceValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
