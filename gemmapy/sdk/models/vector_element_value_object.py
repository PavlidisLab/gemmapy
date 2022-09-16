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

class VectorElementValueObject(object):
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
        'design_element_name': 'str',
        'bio_assay_expression_levels': 'dict(str, float)'
    }

    attribute_map = {
        'design_element_name': 'designElementName',
        'bio_assay_expression_levels': 'bioAssayExpressionLevels'
    }

    def __init__(self, design_element_name=None, bio_assay_expression_levels=None):  # noqa: E501
        """VectorElementValueObject - a model defined in Swagger"""  # noqa: E501
        self._design_element_name = None
        self._bio_assay_expression_levels = None
        self.discriminator = None
        if design_element_name is not None:
            self.design_element_name = design_element_name
        if bio_assay_expression_levels is not None:
            self.bio_assay_expression_levels = bio_assay_expression_levels

    @property
    def design_element_name(self):
        """Gets the design_element_name of this VectorElementValueObject.  # noqa: E501


        :return: The design_element_name of this VectorElementValueObject.  # noqa: E501
        :rtype: str
        """
        return self._design_element_name

    @design_element_name.setter
    def design_element_name(self, design_element_name):
        """Sets the design_element_name of this VectorElementValueObject.


        :param design_element_name: The design_element_name of this VectorElementValueObject.  # noqa: E501
        :type: str
        """

        self._design_element_name = design_element_name

    @property
    def bio_assay_expression_levels(self):
        """Gets the bio_assay_expression_levels of this VectorElementValueObject.  # noqa: E501


        :return: The bio_assay_expression_levels of this VectorElementValueObject.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._bio_assay_expression_levels

    @bio_assay_expression_levels.setter
    def bio_assay_expression_levels(self, bio_assay_expression_levels):
        """Sets the bio_assay_expression_levels of this VectorElementValueObject.


        :param bio_assay_expression_levels: The bio_assay_expression_levels of this VectorElementValueObject.  # noqa: E501
        :type: dict(str, float)
        """

        self._bio_assay_expression_levels = bio_assay_expression_levels

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
        if issubclass(VectorElementValueObject, dict):
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
        if not isinstance(other, VectorElementValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other