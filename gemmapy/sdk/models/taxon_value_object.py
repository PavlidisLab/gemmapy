# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.7.4
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TaxonValueObject(object):
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
        'scientific_name': 'str',
        'common_name': 'str',
        'ncbi_id': 'int',
        'external_database': 'ExternalDatabaseValueObject'
    }

    attribute_map = {
        'id': 'id',
        'scientific_name': 'scientificName',
        'common_name': 'commonName',
        'ncbi_id': 'ncbiId',
        'external_database': 'externalDatabase'
    }

    def __init__(self, id=None, scientific_name=None, common_name=None, ncbi_id=None, external_database=None):  # noqa: E501
        """TaxonValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._scientific_name = None
        self._common_name = None
        self._ncbi_id = None
        self._external_database = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if scientific_name is not None:
            self.scientific_name = scientific_name
        if common_name is not None:
            self.common_name = common_name
        if ncbi_id is not None:
            self.ncbi_id = ncbi_id
        if external_database is not None:
            self.external_database = external_database

    @property
    def id(self):
        """Gets the id of this TaxonValueObject.  # noqa: E501


        :return: The id of this TaxonValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaxonValueObject.


        :param id: The id of this TaxonValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def scientific_name(self):
        """Gets the scientific_name of this TaxonValueObject.  # noqa: E501


        :return: The scientific_name of this TaxonValueObject.  # noqa: E501
        :rtype: str
        """
        return self._scientific_name

    @scientific_name.setter
    def scientific_name(self, scientific_name):
        """Sets the scientific_name of this TaxonValueObject.


        :param scientific_name: The scientific_name of this TaxonValueObject.  # noqa: E501
        :type: str
        """

        self._scientific_name = scientific_name

    @property
    def common_name(self):
        """Gets the common_name of this TaxonValueObject.  # noqa: E501


        :return: The common_name of this TaxonValueObject.  # noqa: E501
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this TaxonValueObject.


        :param common_name: The common_name of this TaxonValueObject.  # noqa: E501
        :type: str
        """

        self._common_name = common_name

    @property
    def ncbi_id(self):
        """Gets the ncbi_id of this TaxonValueObject.  # noqa: E501


        :return: The ncbi_id of this TaxonValueObject.  # noqa: E501
        :rtype: int
        """
        return self._ncbi_id

    @ncbi_id.setter
    def ncbi_id(self, ncbi_id):
        """Sets the ncbi_id of this TaxonValueObject.


        :param ncbi_id: The ncbi_id of this TaxonValueObject.  # noqa: E501
        :type: int
        """

        self._ncbi_id = ncbi_id

    @property
    def external_database(self):
        """Gets the external_database of this TaxonValueObject.  # noqa: E501


        :return: The external_database of this TaxonValueObject.  # noqa: E501
        :rtype: ExternalDatabaseValueObject
        """
        return self._external_database

    @external_database.setter
    def external_database(self, external_database):
        """Sets the external_database of this TaxonValueObject.


        :param external_database: The external_database of this TaxonValueObject.  # noqa: E501
        :type: ExternalDatabaseValueObject
        """

        self._external_database = external_database

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
        if issubclass(TaxonValueObject, dict):
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
        if not isinstance(other, TaxonValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
