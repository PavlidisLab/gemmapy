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

class CategoryWithUsageStatisticsValueObject(object):
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
        'class_uri': 'str',
        'class_name': 'str',
        'number_of_expression_experiments': 'int'
    }

    attribute_map = {
        'class_uri': 'classUri',
        'class_name': 'className',
        'number_of_expression_experiments': 'numberOfExpressionExperiments'
    }

    def __init__(self, class_uri=None, class_name=None, number_of_expression_experiments=None):  # noqa: E501
        """CategoryWithUsageStatisticsValueObject - a model defined in Swagger"""  # noqa: E501
        self._class_uri = None
        self._class_name = None
        self._number_of_expression_experiments = None
        self.discriminator = None
        if class_uri is not None:
            self.class_uri = class_uri
        if class_name is not None:
            self.class_name = class_name
        if number_of_expression_experiments is not None:
            self.number_of_expression_experiments = number_of_expression_experiments

    @property
    def class_uri(self):
        """Gets the class_uri of this CategoryWithUsageStatisticsValueObject.  # noqa: E501


        :return: The class_uri of this CategoryWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._class_uri

    @class_uri.setter
    def class_uri(self, class_uri):
        """Sets the class_uri of this CategoryWithUsageStatisticsValueObject.


        :param class_uri: The class_uri of this CategoryWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._class_uri = class_uri

    @property
    def class_name(self):
        """Gets the class_name of this CategoryWithUsageStatisticsValueObject.  # noqa: E501


        :return: The class_name of this CategoryWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this CategoryWithUsageStatisticsValueObject.


        :param class_name: The class_name of this CategoryWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._class_name = class_name

    @property
    def number_of_expression_experiments(self):
        """Gets the number_of_expression_experiments of this CategoryWithUsageStatisticsValueObject.  # noqa: E501


        :return: The number_of_expression_experiments of this CategoryWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: int
        """
        return self._number_of_expression_experiments

    @number_of_expression_experiments.setter
    def number_of_expression_experiments(self, number_of_expression_experiments):
        """Sets the number_of_expression_experiments of this CategoryWithUsageStatisticsValueObject.


        :param number_of_expression_experiments: The number_of_expression_experiments of this CategoryWithUsageStatisticsValueObject.  # noqa: E501
        :type: int
        """

        self._number_of_expression_experiments = number_of_expression_experiments

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
        if issubclass(CategoryWithUsageStatisticsValueObject, dict):
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
        if not isinstance(other, CategoryWithUsageStatisticsValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
