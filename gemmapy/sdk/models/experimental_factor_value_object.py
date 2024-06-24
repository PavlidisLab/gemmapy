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

class ExperimentalFactorValueObject(object):
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
        'category': 'str',
        'category_uri': 'str',
        'description': 'str',
        'factor_values': 'str',
        'name': 'str',
        'type': 'str',
        'values': 'list[FactorValueValueObject]'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'category_uri': 'categoryUri',
        'description': 'description',
        'factor_values': 'factorValues',
        'name': 'name',
        'type': 'type',
        'values': 'values'
    }

    def __init__(self, id=None, category=None, category_uri=None, description=None, factor_values=None, name=None, type=None, values=None):  # noqa: E501
        """ExperimentalFactorValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._category = None
        self._category_uri = None
        self._description = None
        self._factor_values = None
        self._name = None
        self._type = None
        self._values = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if category_uri is not None:
            self.category_uri = category_uri
        if description is not None:
            self.description = description
        if factor_values is not None:
            self.factor_values = factor_values
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if values is not None:
            self.values = values

    @property
    def id(self):
        """Gets the id of this ExperimentalFactorValueObject.  # noqa: E501


        :return: The id of this ExperimentalFactorValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExperimentalFactorValueObject.


        :param id: The id of this ExperimentalFactorValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def category(self):
        """Gets the category of this ExperimentalFactorValueObject.  # noqa: E501


        :return: The category of this ExperimentalFactorValueObject.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ExperimentalFactorValueObject.


        :param category: The category of this ExperimentalFactorValueObject.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def category_uri(self):
        """Gets the category_uri of this ExperimentalFactorValueObject.  # noqa: E501


        :return: The category_uri of this ExperimentalFactorValueObject.  # noqa: E501
        :rtype: str
        """
        return self._category_uri

    @category_uri.setter
    def category_uri(self, category_uri):
        """Sets the category_uri of this ExperimentalFactorValueObject.


        :param category_uri: The category_uri of this ExperimentalFactorValueObject.  # noqa: E501
        :type: str
        """

        self._category_uri = category_uri

    @property
    def description(self):
        """Gets the description of this ExperimentalFactorValueObject.  # noqa: E501


        :return: The description of this ExperimentalFactorValueObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExperimentalFactorValueObject.


        :param description: The description of this ExperimentalFactorValueObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def factor_values(self):
        """Gets the factor_values of this ExperimentalFactorValueObject.  # noqa: E501

        This is deprecated, use `values` directly instead.  # noqa: E501

        :return: The factor_values of this ExperimentalFactorValueObject.  # noqa: E501
        :rtype: str
        """
        return self._factor_values

    @factor_values.setter
    def factor_values(self, factor_values):
        """Sets the factor_values of this ExperimentalFactorValueObject.

        This is deprecated, use `values` directly instead.  # noqa: E501

        :param factor_values: The factor_values of this ExperimentalFactorValueObject.  # noqa: E501
        :type: str
        """

        self._factor_values = factor_values

    @property
    def name(self):
        """Gets the name of this ExperimentalFactorValueObject.  # noqa: E501


        :return: The name of this ExperimentalFactorValueObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExperimentalFactorValueObject.


        :param name: The name of this ExperimentalFactorValueObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ExperimentalFactorValueObject.  # noqa: E501


        :return: The type of this ExperimentalFactorValueObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExperimentalFactorValueObject.


        :param type: The type of this ExperimentalFactorValueObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["categorical", "continuous"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def values(self):
        """Gets the values of this ExperimentalFactorValueObject.  # noqa: E501


        :return: The values of this ExperimentalFactorValueObject.  # noqa: E501
        :rtype: list[FactorValueValueObject]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ExperimentalFactorValueObject.


        :param values: The values of this ExperimentalFactorValueObject.  # noqa: E501
        :type: list[FactorValueValueObject]
        """

        self._values = values

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
        if issubclass(ExperimentalFactorValueObject, dict):
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
        if not isinstance(other, ExperimentalFactorValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
