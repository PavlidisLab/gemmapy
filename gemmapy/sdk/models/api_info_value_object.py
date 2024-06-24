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

class ApiInfoValueObject(object):
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
        'welcome': 'str',
        'version': 'str',
        'documentation_url': 'str',
        'specification_url': 'str',
        'external_databases': 'list[ExternalDatabaseValueObject]',
        'build_info': 'BuildInfoValueObject',
        'docs': 'str'
    }

    attribute_map = {
        'welcome': 'welcome',
        'version': 'version',
        'documentation_url': 'documentationUrl',
        'specification_url': 'specificationUrl',
        'external_databases': 'externalDatabases',
        'build_info': 'buildInfo',
        'docs': 'docs'
    }

    def __init__(self, welcome=None, version=None, documentation_url=None, specification_url=None, external_databases=None, build_info=None, docs=None):  # noqa: E501
        """ApiInfoValueObject - a model defined in Swagger"""  # noqa: E501
        self._welcome = None
        self._version = None
        self._documentation_url = None
        self._specification_url = None
        self._external_databases = None
        self._build_info = None
        self._docs = None
        self.discriminator = None
        if welcome is not None:
            self.welcome = welcome
        if version is not None:
            self.version = version
        if documentation_url is not None:
            self.documentation_url = documentation_url
        if specification_url is not None:
            self.specification_url = specification_url
        if external_databases is not None:
            self.external_databases = external_databases
        if build_info is not None:
            self.build_info = build_info
        if docs is not None:
            self.docs = docs

    @property
    def welcome(self):
        """Gets the welcome of this ApiInfoValueObject.  # noqa: E501


        :return: The welcome of this ApiInfoValueObject.  # noqa: E501
        :rtype: str
        """
        return self._welcome

    @welcome.setter
    def welcome(self, welcome):
        """Sets the welcome of this ApiInfoValueObject.


        :param welcome: The welcome of this ApiInfoValueObject.  # noqa: E501
        :type: str
        """

        self._welcome = welcome

    @property
    def version(self):
        """Gets the version of this ApiInfoValueObject.  # noqa: E501


        :return: The version of this ApiInfoValueObject.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiInfoValueObject.


        :param version: The version of this ApiInfoValueObject.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def documentation_url(self):
        """Gets the documentation_url of this ApiInfoValueObject.  # noqa: E501


        :return: The documentation_url of this ApiInfoValueObject.  # noqa: E501
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this ApiInfoValueObject.


        :param documentation_url: The documentation_url of this ApiInfoValueObject.  # noqa: E501
        :type: str
        """

        self._documentation_url = documentation_url

    @property
    def specification_url(self):
        """Gets the specification_url of this ApiInfoValueObject.  # noqa: E501


        :return: The specification_url of this ApiInfoValueObject.  # noqa: E501
        :rtype: str
        """
        return self._specification_url

    @specification_url.setter
    def specification_url(self, specification_url):
        """Sets the specification_url of this ApiInfoValueObject.


        :param specification_url: The specification_url of this ApiInfoValueObject.  # noqa: E501
        :type: str
        """

        self._specification_url = specification_url

    @property
    def external_databases(self):
        """Gets the external_databases of this ApiInfoValueObject.  # noqa: E501


        :return: The external_databases of this ApiInfoValueObject.  # noqa: E501
        :rtype: list[ExternalDatabaseValueObject]
        """
        return self._external_databases

    @external_databases.setter
    def external_databases(self, external_databases):
        """Sets the external_databases of this ApiInfoValueObject.


        :param external_databases: The external_databases of this ApiInfoValueObject.  # noqa: E501
        :type: list[ExternalDatabaseValueObject]
        """

        self._external_databases = external_databases

    @property
    def build_info(self):
        """Gets the build_info of this ApiInfoValueObject.  # noqa: E501


        :return: The build_info of this ApiInfoValueObject.  # noqa: E501
        :rtype: BuildInfoValueObject
        """
        return self._build_info

    @build_info.setter
    def build_info(self, build_info):
        """Sets the build_info of this ApiInfoValueObject.


        :param build_info: The build_info of this ApiInfoValueObject.  # noqa: E501
        :type: BuildInfoValueObject
        """

        self._build_info = build_info

    @property
    def docs(self):
        """Gets the docs of this ApiInfoValueObject.  # noqa: E501


        :return: The docs of this ApiInfoValueObject.  # noqa: E501
        :rtype: str
        """
        return self._docs

    @docs.setter
    def docs(self, docs):
        """Sets the docs of this ApiInfoValueObject.


        :param docs: The docs of this ApiInfoValueObject.  # noqa: E501
        :type: str
        """

        self._docs = docs

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
        if issubclass(ApiInfoValueObject, dict):
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
        if not isinstance(other, ApiInfoValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
