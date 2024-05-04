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

class WellComposedErrorBody(object):
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
        'code': 'int',
        'message': 'str',
        'errors': 'dict(str, str)'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'errors': 'errors'
    }

    def __init__(self, code=None, message=None, errors=None):  # noqa: E501
        """WellComposedErrorBody - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self._errors = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if errors is not None:
            self.errors = errors

    @property
    def code(self):
        """Gets the code of this WellComposedErrorBody.  # noqa: E501


        :return: The code of this WellComposedErrorBody.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this WellComposedErrorBody.


        :param code: The code of this WellComposedErrorBody.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this WellComposedErrorBody.  # noqa: E501


        :return: The message of this WellComposedErrorBody.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this WellComposedErrorBody.


        :param message: The message of this WellComposedErrorBody.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def errors(self):
        """Gets the errors of this WellComposedErrorBody.  # noqa: E501


        :return: The errors of this WellComposedErrorBody.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this WellComposedErrorBody.


        :param errors: The errors of this WellComposedErrorBody.  # noqa: E501
        :type: dict(str, str)
        """

        self._errors = errors

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
        if issubclass(WellComposedErrorBody, dict):
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
        if not isinstance(other, WellComposedErrorBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
