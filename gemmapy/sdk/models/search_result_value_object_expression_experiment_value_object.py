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

class SearchResultValueObjectExpressionExperimentValueObject(object):
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
        'result_id': 'int',
        'result_type': 'SearchResultType',
        'score': 'float',
        'highlights': 'dict(str, str)',
        'result_object': 'ExpressionExperimentValueObject'
    }

    attribute_map = {
        'result_id': 'resultId',
        'result_type': 'resultType',
        'score': 'score',
        'highlights': 'highlights',
        'result_object': 'resultObject'
    }

    def __init__(self, result_id=None, result_type=None, score=None, highlights=None, result_object=None):  # noqa: E501
        """SearchResultValueObjectExpressionExperimentValueObject - a model defined in Swagger"""  # noqa: E501
        self._result_id = None
        self._result_type = None
        self._score = None
        self._highlights = None
        self._result_object = None
        self.discriminator = None
        if result_id is not None:
            self.result_id = result_id
        if result_type is not None:
            self.result_type = result_type
        if score is not None:
            self.score = score
        if highlights is not None:
            self.highlights = highlights
        if result_object is not None:
            self.result_object = result_object

    @property
    def result_id(self):
        """Gets the result_id of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501


        :return: The result_id of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501
        :rtype: int
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        """Sets the result_id of this SearchResultValueObjectExpressionExperimentValueObject.


        :param result_id: The result_id of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501
        :type: int
        """

        self._result_id = result_id

    @property
    def result_type(self):
        """Gets the result_type of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501


        :return: The result_type of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501
        :rtype: SearchResultType
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this SearchResultValueObjectExpressionExperimentValueObject.


        :param result_type: The result_type of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501
        :type: SearchResultType
        """

        self._result_type = result_type

    @property
    def score(self):
        """Gets the score of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501


        :return: The score of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this SearchResultValueObjectExpressionExperimentValueObject.


        :param score: The score of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def highlights(self):
        """Gets the highlights of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501


        :return: The highlights of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """Sets the highlights of this SearchResultValueObjectExpressionExperimentValueObject.


        :param highlights: The highlights of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501
        :type: dict(str, str)
        """

        self._highlights = highlights

    @property
    def result_object(self):
        """Gets the result_object of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501


        :return: The result_object of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501
        :rtype: ExpressionExperimentValueObject
        """
        return self._result_object

    @result_object.setter
    def result_object(self, result_object):
        """Sets the result_object of this SearchResultValueObjectExpressionExperimentValueObject.


        :param result_object: The result_object of this SearchResultValueObjectExpressionExperimentValueObject.  # noqa: E501
        :type: ExpressionExperimentValueObject
        """

        self._result_object = result_object

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
        if issubclass(SearchResultValueObjectExpressionExperimentValueObject, dict):
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
        if not isinstance(other, SearchResultValueObjectExpressionExperimentValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
