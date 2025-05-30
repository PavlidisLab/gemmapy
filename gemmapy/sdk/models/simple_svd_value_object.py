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

class SimpleSVDValueObject(object):
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
        'bio_assay_ids': 'list[int]',
        'bio_material_ids': 'list[int]',
        'variances': 'list[float]',
        'vmatrix': 'list[list[float]]'
    }

    attribute_map = {
        'bio_assay_ids': 'bioAssayIds',
        'bio_material_ids': 'bioMaterialIds',
        'variances': 'variances',
        'vmatrix': 'vmatrix'
    }

    def __init__(self, bio_assay_ids=None, bio_material_ids=None, variances=None, vmatrix=None):  # noqa: E501
        """SimpleSVDValueObject - a model defined in Swagger"""  # noqa: E501
        self._bio_assay_ids = None
        self._bio_material_ids = None
        self._variances = None
        self._vmatrix = None
        self.discriminator = None
        if bio_assay_ids is not None:
            self.bio_assay_ids = bio_assay_ids
        if bio_material_ids is not None:
            self.bio_material_ids = bio_material_ids
        if variances is not None:
            self.variances = variances
        if vmatrix is not None:
            self.vmatrix = vmatrix

    @property
    def bio_assay_ids(self):
        """Gets the bio_assay_ids of this SimpleSVDValueObject.  # noqa: E501


        :return: The bio_assay_ids of this SimpleSVDValueObject.  # noqa: E501
        :rtype: list[int]
        """
        return self._bio_assay_ids

    @bio_assay_ids.setter
    def bio_assay_ids(self, bio_assay_ids):
        """Sets the bio_assay_ids of this SimpleSVDValueObject.


        :param bio_assay_ids: The bio_assay_ids of this SimpleSVDValueObject.  # noqa: E501
        :type: list[int]
        """

        self._bio_assay_ids = bio_assay_ids

    @property
    def bio_material_ids(self):
        """Gets the bio_material_ids of this SimpleSVDValueObject.  # noqa: E501


        :return: The bio_material_ids of this SimpleSVDValueObject.  # noqa: E501
        :rtype: list[int]
        """
        return self._bio_material_ids

    @bio_material_ids.setter
    def bio_material_ids(self, bio_material_ids):
        """Sets the bio_material_ids of this SimpleSVDValueObject.


        :param bio_material_ids: The bio_material_ids of this SimpleSVDValueObject.  # noqa: E501
        :type: list[int]
        """

        self._bio_material_ids = bio_material_ids

    @property
    def variances(self):
        """Gets the variances of this SimpleSVDValueObject.  # noqa: E501


        :return: The variances of this SimpleSVDValueObject.  # noqa: E501
        :rtype: list[float]
        """
        return self._variances

    @variances.setter
    def variances(self, variances):
        """Sets the variances of this SimpleSVDValueObject.


        :param variances: The variances of this SimpleSVDValueObject.  # noqa: E501
        :type: list[float]
        """

        self._variances = variances

    @property
    def vmatrix(self):
        """Gets the vmatrix of this SimpleSVDValueObject.  # noqa: E501


        :return: The vmatrix of this SimpleSVDValueObject.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._vmatrix

    @vmatrix.setter
    def vmatrix(self, vmatrix):
        """Sets the vmatrix of this SimpleSVDValueObject.


        :param vmatrix: The vmatrix of this SimpleSVDValueObject.  # noqa: E501
        :type: list[list[float]]
        """

        self._vmatrix = vmatrix

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
        if issubclass(SimpleSVDValueObject, dict):
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
        if not isinstance(other, SimpleSVDValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
