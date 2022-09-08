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

class QuantitationType(object):
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
        'name': 'str',
        'description': 'str',
        'id': 'int',
        'is_background': 'bool',
        'is_background_subtracted': 'bool',
        'is_batch_corrected': 'bool',
        'is_masked_preferred': 'bool',
        'is_normalized': 'bool',
        'is_preferred': 'bool',
        'is_recomputed_from_raw_data': 'bool',
        'is_ratio': 'bool',
        'general_type': 'GeneralType',
        'representation': 'PrimitiveType',
        'scale': 'ScaleType',
        'type': 'StandardQuantitationType'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'is_background': 'isBackground',
        'is_background_subtracted': 'isBackgroundSubtracted',
        'is_batch_corrected': 'isBatchCorrected',
        'is_masked_preferred': 'isMaskedPreferred',
        'is_normalized': 'isNormalized',
        'is_preferred': 'isPreferred',
        'is_recomputed_from_raw_data': 'isRecomputedFromRawData',
        'is_ratio': 'isRatio',
        'general_type': 'generalType',
        'representation': 'representation',
        'scale': 'scale',
        'type': 'type'
    }

    def __init__(self, name=None, description=None, id=None, is_background=None, is_background_subtracted=None, is_batch_corrected=None, is_masked_preferred=None, is_normalized=None, is_preferred=None, is_recomputed_from_raw_data=None, is_ratio=None, general_type=None, representation=None, scale=None, type=None):  # noqa: E501
        """QuantitationType - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._id = None
        self._is_background = None
        self._is_background_subtracted = None
        self._is_batch_corrected = None
        self._is_masked_preferred = None
        self._is_normalized = None
        self._is_preferred = None
        self._is_recomputed_from_raw_data = None
        self._is_ratio = None
        self._general_type = None
        self._representation = None
        self._scale = None
        self._type = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_background is not None:
            self.is_background = is_background
        if is_background_subtracted is not None:
            self.is_background_subtracted = is_background_subtracted
        if is_batch_corrected is not None:
            self.is_batch_corrected = is_batch_corrected
        if is_masked_preferred is not None:
            self.is_masked_preferred = is_masked_preferred
        if is_normalized is not None:
            self.is_normalized = is_normalized
        if is_preferred is not None:
            self.is_preferred = is_preferred
        if is_recomputed_from_raw_data is not None:
            self.is_recomputed_from_raw_data = is_recomputed_from_raw_data
        if is_ratio is not None:
            self.is_ratio = is_ratio
        if general_type is not None:
            self.general_type = general_type
        if representation is not None:
            self.representation = representation
        if scale is not None:
            self.scale = scale
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this QuantitationType.  # noqa: E501


        :return: The name of this QuantitationType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QuantitationType.


        :param name: The name of this QuantitationType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this QuantitationType.  # noqa: E501


        :return: The description of this QuantitationType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QuantitationType.


        :param description: The description of this QuantitationType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this QuantitationType.  # noqa: E501


        :return: The id of this QuantitationType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuantitationType.


        :param id: The id of this QuantitationType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_background(self):
        """Gets the is_background of this QuantitationType.  # noqa: E501


        :return: The is_background of this QuantitationType.  # noqa: E501
        :rtype: bool
        """
        return self._is_background

    @is_background.setter
    def is_background(self, is_background):
        """Sets the is_background of this QuantitationType.


        :param is_background: The is_background of this QuantitationType.  # noqa: E501
        :type: bool
        """

        self._is_background = is_background

    @property
    def is_background_subtracted(self):
        """Gets the is_background_subtracted of this QuantitationType.  # noqa: E501


        :return: The is_background_subtracted of this QuantitationType.  # noqa: E501
        :rtype: bool
        """
        return self._is_background_subtracted

    @is_background_subtracted.setter
    def is_background_subtracted(self, is_background_subtracted):
        """Sets the is_background_subtracted of this QuantitationType.


        :param is_background_subtracted: The is_background_subtracted of this QuantitationType.  # noqa: E501
        :type: bool
        """

        self._is_background_subtracted = is_background_subtracted

    @property
    def is_batch_corrected(self):
        """Gets the is_batch_corrected of this QuantitationType.  # noqa: E501


        :return: The is_batch_corrected of this QuantitationType.  # noqa: E501
        :rtype: bool
        """
        return self._is_batch_corrected

    @is_batch_corrected.setter
    def is_batch_corrected(self, is_batch_corrected):
        """Sets the is_batch_corrected of this QuantitationType.


        :param is_batch_corrected: The is_batch_corrected of this QuantitationType.  # noqa: E501
        :type: bool
        """

        self._is_batch_corrected = is_batch_corrected

    @property
    def is_masked_preferred(self):
        """Gets the is_masked_preferred of this QuantitationType.  # noqa: E501


        :return: The is_masked_preferred of this QuantitationType.  # noqa: E501
        :rtype: bool
        """
        return self._is_masked_preferred

    @is_masked_preferred.setter
    def is_masked_preferred(self, is_masked_preferred):
        """Sets the is_masked_preferred of this QuantitationType.


        :param is_masked_preferred: The is_masked_preferred of this QuantitationType.  # noqa: E501
        :type: bool
        """

        self._is_masked_preferred = is_masked_preferred

    @property
    def is_normalized(self):
        """Gets the is_normalized of this QuantitationType.  # noqa: E501


        :return: The is_normalized of this QuantitationType.  # noqa: E501
        :rtype: bool
        """
        return self._is_normalized

    @is_normalized.setter
    def is_normalized(self, is_normalized):
        """Sets the is_normalized of this QuantitationType.


        :param is_normalized: The is_normalized of this QuantitationType.  # noqa: E501
        :type: bool
        """

        self._is_normalized = is_normalized

    @property
    def is_preferred(self):
        """Gets the is_preferred of this QuantitationType.  # noqa: E501


        :return: The is_preferred of this QuantitationType.  # noqa: E501
        :rtype: bool
        """
        return self._is_preferred

    @is_preferred.setter
    def is_preferred(self, is_preferred):
        """Sets the is_preferred of this QuantitationType.


        :param is_preferred: The is_preferred of this QuantitationType.  # noqa: E501
        :type: bool
        """

        self._is_preferred = is_preferred

    @property
    def is_recomputed_from_raw_data(self):
        """Gets the is_recomputed_from_raw_data of this QuantitationType.  # noqa: E501


        :return: The is_recomputed_from_raw_data of this QuantitationType.  # noqa: E501
        :rtype: bool
        """
        return self._is_recomputed_from_raw_data

    @is_recomputed_from_raw_data.setter
    def is_recomputed_from_raw_data(self, is_recomputed_from_raw_data):
        """Sets the is_recomputed_from_raw_data of this QuantitationType.


        :param is_recomputed_from_raw_data: The is_recomputed_from_raw_data of this QuantitationType.  # noqa: E501
        :type: bool
        """

        self._is_recomputed_from_raw_data = is_recomputed_from_raw_data

    @property
    def is_ratio(self):
        """Gets the is_ratio of this QuantitationType.  # noqa: E501


        :return: The is_ratio of this QuantitationType.  # noqa: E501
        :rtype: bool
        """
        return self._is_ratio

    @is_ratio.setter
    def is_ratio(self, is_ratio):
        """Sets the is_ratio of this QuantitationType.


        :param is_ratio: The is_ratio of this QuantitationType.  # noqa: E501
        :type: bool
        """

        self._is_ratio = is_ratio

    @property
    def general_type(self):
        """Gets the general_type of this QuantitationType.  # noqa: E501


        :return: The general_type of this QuantitationType.  # noqa: E501
        :rtype: GeneralType
        """
        return self._general_type

    @general_type.setter
    def general_type(self, general_type):
        """Sets the general_type of this QuantitationType.


        :param general_type: The general_type of this QuantitationType.  # noqa: E501
        :type: GeneralType
        """

        self._general_type = general_type

    @property
    def representation(self):
        """Gets the representation of this QuantitationType.  # noqa: E501


        :return: The representation of this QuantitationType.  # noqa: E501
        :rtype: PrimitiveType
        """
        return self._representation

    @representation.setter
    def representation(self, representation):
        """Sets the representation of this QuantitationType.


        :param representation: The representation of this QuantitationType.  # noqa: E501
        :type: PrimitiveType
        """

        self._representation = representation

    @property
    def scale(self):
        """Gets the scale of this QuantitationType.  # noqa: E501


        :return: The scale of this QuantitationType.  # noqa: E501
        :rtype: ScaleType
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this QuantitationType.


        :param scale: The scale of this QuantitationType.  # noqa: E501
        :type: ScaleType
        """

        self._scale = scale

    @property
    def type(self):
        """Gets the type of this QuantitationType.  # noqa: E501


        :return: The type of this QuantitationType.  # noqa: E501
        :rtype: StandardQuantitationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuantitationType.


        :param type: The type of this QuantitationType.  # noqa: E501
        :type: StandardQuantitationType
        """

        self._type = type

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
        if issubclass(QuantitationType, dict):
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
        if not isinstance(other, QuantitationType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
