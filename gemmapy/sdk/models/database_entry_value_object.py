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

class DatabaseEntryValueObject(object):
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
        'accession': 'str',
        'external_database': 'ExternalDatabaseValueObject'
    }

    attribute_map = {
        'id': 'id',
        'accession': 'accession',
        'external_database': 'externalDatabase'
    }

    def __init__(self, id=None, accession=None, external_database=None):  # noqa: E501
        """DatabaseEntryValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._accession = None
        self._external_database = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if accession is not None:
            self.accession = accession
        if external_database is not None:
            self.external_database = external_database

    @property
    def id(self):
        """Gets the id of this DatabaseEntryValueObject.  # noqa: E501


        :return: The id of this DatabaseEntryValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatabaseEntryValueObject.


        :param id: The id of this DatabaseEntryValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def accession(self):
        """Gets the accession of this DatabaseEntryValueObject.  # noqa: E501


        :return: The accession of this DatabaseEntryValueObject.  # noqa: E501
        :rtype: str
        """
        return self._accession

    @accession.setter
    def accession(self, accession):
        """Sets the accession of this DatabaseEntryValueObject.


        :param accession: The accession of this DatabaseEntryValueObject.  # noqa: E501
        :type: str
        """

        self._accession = accession

    @property
    def external_database(self):
        """Gets the external_database of this DatabaseEntryValueObject.  # noqa: E501


        :return: The external_database of this DatabaseEntryValueObject.  # noqa: E501
        :rtype: ExternalDatabaseValueObject
        """
        return self._external_database

    @external_database.setter
    def external_database(self, external_database):
        """Sets the external_database of this DatabaseEntryValueObject.


        :param external_database: The external_database of this DatabaseEntryValueObject.  # noqa: E501
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
        if issubclass(DatabaseEntryValueObject, dict):
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
        if not isinstance(other, DatabaseEntryValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
