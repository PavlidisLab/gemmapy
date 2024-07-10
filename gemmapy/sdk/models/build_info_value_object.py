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

class BuildInfoValueObject(object):
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
        'version': 'str',
        'timestamp': 'datetime',
        'git_hash': 'str'
    }

    attribute_map = {
        'version': 'version',
        'timestamp': 'timestamp',
        'git_hash': 'gitHash'
    }

    def __init__(self, version=None, timestamp=None, git_hash=None):  # noqa: E501
        """BuildInfoValueObject - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._timestamp = None
        self._git_hash = None
        self.discriminator = None
        if version is not None:
            self.version = version
        if timestamp is not None:
            self.timestamp = timestamp
        if git_hash is not None:
            self.git_hash = git_hash

    @property
    def version(self):
        """Gets the version of this BuildInfoValueObject.  # noqa: E501


        :return: The version of this BuildInfoValueObject.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BuildInfoValueObject.


        :param version: The version of this BuildInfoValueObject.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def timestamp(self):
        """Gets the timestamp of this BuildInfoValueObject.  # noqa: E501


        :return: The timestamp of this BuildInfoValueObject.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BuildInfoValueObject.


        :param timestamp: The timestamp of this BuildInfoValueObject.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def git_hash(self):
        """Gets the git_hash of this BuildInfoValueObject.  # noqa: E501


        :return: The git_hash of this BuildInfoValueObject.  # noqa: E501
        :rtype: str
        """
        return self._git_hash

    @git_hash.setter
    def git_hash(self, git_hash):
        """Sets the git_hash of this BuildInfoValueObject.


        :param git_hash: The git_hash of this BuildInfoValueObject.  # noqa: E501
        :type: str
        """

        self._git_hash = git_hash

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
        if issubclass(BuildInfoValueObject, dict):
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
        if not isinstance(other, BuildInfoValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
