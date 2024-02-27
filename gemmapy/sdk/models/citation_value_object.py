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

class CitationValueObject(object):
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
        'citation': 'str',
        'id': 'int',
        'pubmed_accession': 'str',
        'pubmed_url': 'str',
        'retracted': 'bool'
    }

    attribute_map = {
        'citation': 'citation',
        'id': 'id',
        'pubmed_accession': 'pubmedAccession',
        'pubmed_url': 'pubmedURL',
        'retracted': 'retracted'
    }

    def __init__(self, citation=None, id=None, pubmed_accession=None, pubmed_url=None, retracted=None):  # noqa: E501
        """CitationValueObject - a model defined in Swagger"""  # noqa: E501
        self._citation = None
        self._id = None
        self._pubmed_accession = None
        self._pubmed_url = None
        self._retracted = None
        self.discriminator = None
        if citation is not None:
            self.citation = citation
        if id is not None:
            self.id = id
        if pubmed_accession is not None:
            self.pubmed_accession = pubmed_accession
        if pubmed_url is not None:
            self.pubmed_url = pubmed_url
        if retracted is not None:
            self.retracted = retracted

    @property
    def citation(self):
        """Gets the citation of this CitationValueObject.  # noqa: E501


        :return: The citation of this CitationValueObject.  # noqa: E501
        :rtype: str
        """
        return self._citation

    @citation.setter
    def citation(self, citation):
        """Sets the citation of this CitationValueObject.


        :param citation: The citation of this CitationValueObject.  # noqa: E501
        :type: str
        """

        self._citation = citation

    @property
    def id(self):
        """Gets the id of this CitationValueObject.  # noqa: E501


        :return: The id of this CitationValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CitationValueObject.


        :param id: The id of this CitationValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def pubmed_accession(self):
        """Gets the pubmed_accession of this CitationValueObject.  # noqa: E501


        :return: The pubmed_accession of this CitationValueObject.  # noqa: E501
        :rtype: str
        """
        return self._pubmed_accession

    @pubmed_accession.setter
    def pubmed_accession(self, pubmed_accession):
        """Sets the pubmed_accession of this CitationValueObject.


        :param pubmed_accession: The pubmed_accession of this CitationValueObject.  # noqa: E501
        :type: str
        """

        self._pubmed_accession = pubmed_accession

    @property
    def pubmed_url(self):
        """Gets the pubmed_url of this CitationValueObject.  # noqa: E501


        :return: The pubmed_url of this CitationValueObject.  # noqa: E501
        :rtype: str
        """
        return self._pubmed_url

    @pubmed_url.setter
    def pubmed_url(self, pubmed_url):
        """Sets the pubmed_url of this CitationValueObject.


        :param pubmed_url: The pubmed_url of this CitationValueObject.  # noqa: E501
        :type: str
        """

        self._pubmed_url = pubmed_url

    @property
    def retracted(self):
        """Gets the retracted of this CitationValueObject.  # noqa: E501


        :return: The retracted of this CitationValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._retracted

    @retracted.setter
    def retracted(self, retracted):
        """Sets the retracted of this CitationValueObject.


        :param retracted: The retracted of this CitationValueObject.  # noqa: E501
        :type: bool
        """

        self._retracted = retracted

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
        if issubclass(CitationValueObject, dict):
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
        if not isinstance(other, CitationValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
