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

class ContrastResultValueObject(object):
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
        'pvalue': 'float',
        'coefficient': 'float',
        'log_fold_change': 'float',
        'factor_value': 'FactorValueBasicValueObject',
        'second_factor_value': 'FactorValueBasicValueObject',
        'tstat': 'float'
    }

    attribute_map = {
        'id': 'id',
        'pvalue': 'pvalue',
        'coefficient': 'coefficient',
        'log_fold_change': 'logFoldChange',
        'factor_value': 'factorValue',
        'second_factor_value': 'secondFactorValue',
        'tstat': 'tstat'
    }

    def __init__(self, id=None, pvalue=None, coefficient=None, log_fold_change=None, factor_value=None, second_factor_value=None, tstat=None):  # noqa: E501
        """ContrastResultValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._pvalue = None
        self._coefficient = None
        self._log_fold_change = None
        self._factor_value = None
        self._second_factor_value = None
        self._tstat = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if pvalue is not None:
            self.pvalue = pvalue
        if coefficient is not None:
            self.coefficient = coefficient
        if log_fold_change is not None:
            self.log_fold_change = log_fold_change
        if factor_value is not None:
            self.factor_value = factor_value
        if second_factor_value is not None:
            self.second_factor_value = second_factor_value
        if tstat is not None:
            self.tstat = tstat

    @property
    def id(self):
        """Gets the id of this ContrastResultValueObject.  # noqa: E501


        :return: The id of this ContrastResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContrastResultValueObject.


        :param id: The id of this ContrastResultValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def pvalue(self):
        """Gets the pvalue of this ContrastResultValueObject.  # noqa: E501


        :return: The pvalue of this ContrastResultValueObject.  # noqa: E501
        :rtype: float
        """
        return self._pvalue

    @pvalue.setter
    def pvalue(self, pvalue):
        """Sets the pvalue of this ContrastResultValueObject.


        :param pvalue: The pvalue of this ContrastResultValueObject.  # noqa: E501
        :type: float
        """

        self._pvalue = pvalue

    @property
    def coefficient(self):
        """Gets the coefficient of this ContrastResultValueObject.  # noqa: E501


        :return: The coefficient of this ContrastResultValueObject.  # noqa: E501
        :rtype: float
        """
        return self._coefficient

    @coefficient.setter
    def coefficient(self, coefficient):
        """Sets the coefficient of this ContrastResultValueObject.


        :param coefficient: The coefficient of this ContrastResultValueObject.  # noqa: E501
        :type: float
        """

        self._coefficient = coefficient

    @property
    def log_fold_change(self):
        """Gets the log_fold_change of this ContrastResultValueObject.  # noqa: E501


        :return: The log_fold_change of this ContrastResultValueObject.  # noqa: E501
        :rtype: float
        """
        return self._log_fold_change

    @log_fold_change.setter
    def log_fold_change(self, log_fold_change):
        """Sets the log_fold_change of this ContrastResultValueObject.


        :param log_fold_change: The log_fold_change of this ContrastResultValueObject.  # noqa: E501
        :type: float
        """

        self._log_fold_change = log_fold_change

    @property
    def factor_value(self):
        """Gets the factor_value of this ContrastResultValueObject.  # noqa: E501


        :return: The factor_value of this ContrastResultValueObject.  # noqa: E501
        :rtype: FactorValueBasicValueObject
        """
        return self._factor_value

    @factor_value.setter
    def factor_value(self, factor_value):
        """Sets the factor_value of this ContrastResultValueObject.


        :param factor_value: The factor_value of this ContrastResultValueObject.  # noqa: E501
        :type: FactorValueBasicValueObject
        """

        self._factor_value = factor_value

    @property
    def second_factor_value(self):
        """Gets the second_factor_value of this ContrastResultValueObject.  # noqa: E501


        :return: The second_factor_value of this ContrastResultValueObject.  # noqa: E501
        :rtype: FactorValueBasicValueObject
        """
        return self._second_factor_value

    @second_factor_value.setter
    def second_factor_value(self, second_factor_value):
        """Sets the second_factor_value of this ContrastResultValueObject.


        :param second_factor_value: The second_factor_value of this ContrastResultValueObject.  # noqa: E501
        :type: FactorValueBasicValueObject
        """

        self._second_factor_value = second_factor_value

    @property
    def tstat(self):
        """Gets the tstat of this ContrastResultValueObject.  # noqa: E501


        :return: The tstat of this ContrastResultValueObject.  # noqa: E501
        :rtype: float
        """
        return self._tstat

    @tstat.setter
    def tstat(self, tstat):
        """Sets the tstat of this ContrastResultValueObject.


        :param tstat: The tstat of this ContrastResultValueObject.  # noqa: E501
        :type: float
        """

        self._tstat = tstat

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
        if issubclass(ContrastResultValueObject, dict):
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
        if not isinstance(other, ContrastResultValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
