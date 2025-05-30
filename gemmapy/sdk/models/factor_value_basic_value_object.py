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

class FactorValueBasicValueObject(object):
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
        'ontology_id': 'str',
        'experimental_factor_id': 'int',
        'experimental_factor_type': 'str',
        'experimental_factor_category': 'CharacteristicValueObject',
        'characteristics': 'list[CharacteristicValueObject]',
        'statements': 'list[StatementValueObject]',
        'summary': 'str',
        'value': 'str',
        'measurement': 'MeasurementValueObject',
        'is_measurement': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'ontology_id': 'ontologyId',
        'experimental_factor_id': 'experimentalFactorId',
        'experimental_factor_type': 'experimentalFactorType',
        'experimental_factor_category': 'experimentalFactorCategory',
        'characteristics': 'characteristics',
        'statements': 'statements',
        'summary': 'summary',
        'value': 'value',
        'measurement': 'measurement',
        'is_measurement': 'isMeasurement'
    }

    def __init__(self, id=None, ontology_id=None, experimental_factor_id=None, experimental_factor_type=None, experimental_factor_category=None, characteristics=None, statements=None, summary=None, value=None, measurement=None, is_measurement=None):  # noqa: E501
        """FactorValueBasicValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._ontology_id = None
        self._experimental_factor_id = None
        self._experimental_factor_type = None
        self._experimental_factor_category = None
        self._characteristics = None
        self._statements = None
        self._summary = None
        self._value = None
        self._measurement = None
        self._is_measurement = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if ontology_id is not None:
            self.ontology_id = ontology_id
        if experimental_factor_id is not None:
            self.experimental_factor_id = experimental_factor_id
        if experimental_factor_type is not None:
            self.experimental_factor_type = experimental_factor_type
        if experimental_factor_category is not None:
            self.experimental_factor_category = experimental_factor_category
        if characteristics is not None:
            self.characteristics = characteristics
        if statements is not None:
            self.statements = statements
        if summary is not None:
            self.summary = summary
        if value is not None:
            self.value = value
        if measurement is not None:
            self.measurement = measurement
        if is_measurement is not None:
            self.is_measurement = is_measurement

    @property
    def id(self):
        """Gets the id of this FactorValueBasicValueObject.  # noqa: E501


        :return: The id of this FactorValueBasicValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FactorValueBasicValueObject.


        :param id: The id of this FactorValueBasicValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ontology_id(self):
        """Gets the ontology_id of this FactorValueBasicValueObject.  # noqa: E501


        :return: The ontology_id of this FactorValueBasicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._ontology_id

    @ontology_id.setter
    def ontology_id(self, ontology_id):
        """Sets the ontology_id of this FactorValueBasicValueObject.


        :param ontology_id: The ontology_id of this FactorValueBasicValueObject.  # noqa: E501
        :type: str
        """

        self._ontology_id = ontology_id

    @property
    def experimental_factor_id(self):
        """Gets the experimental_factor_id of this FactorValueBasicValueObject.  # noqa: E501

        This property is not filled if rendered within an ExperimentalFactorValueObject.  # noqa: E501

        :return: The experimental_factor_id of this FactorValueBasicValueObject.  # noqa: E501
        :rtype: int
        """
        return self._experimental_factor_id

    @experimental_factor_id.setter
    def experimental_factor_id(self, experimental_factor_id):
        """Sets the experimental_factor_id of this FactorValueBasicValueObject.

        This property is not filled if rendered within an ExperimentalFactorValueObject.  # noqa: E501

        :param experimental_factor_id: The experimental_factor_id of this FactorValueBasicValueObject.  # noqa: E501
        :type: int
        """

        self._experimental_factor_id = experimental_factor_id

    @property
    def experimental_factor_type(self):
        """Gets the experimental_factor_type of this FactorValueBasicValueObject.  # noqa: E501

        This property is not filled if rendered within an ExperimentalFactorValueObject.  # noqa: E501

        :return: The experimental_factor_type of this FactorValueBasicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._experimental_factor_type

    @experimental_factor_type.setter
    def experimental_factor_type(self, experimental_factor_type):
        """Sets the experimental_factor_type of this FactorValueBasicValueObject.

        This property is not filled if rendered within an ExperimentalFactorValueObject.  # noqa: E501

        :param experimental_factor_type: The experimental_factor_type of this FactorValueBasicValueObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["categorical", "continuous"]  # noqa: E501
        if experimental_factor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `experimental_factor_type` ({0}), must be one of {1}"  # noqa: E501
                .format(experimental_factor_type, allowed_values)
            )

        self._experimental_factor_type = experimental_factor_type

    @property
    def experimental_factor_category(self):
        """Gets the experimental_factor_category of this FactorValueBasicValueObject.  # noqa: E501


        :return: The experimental_factor_category of this FactorValueBasicValueObject.  # noqa: E501
        :rtype: CharacteristicValueObject
        """
        return self._experimental_factor_category

    @experimental_factor_category.setter
    def experimental_factor_category(self, experimental_factor_category):
        """Sets the experimental_factor_category of this FactorValueBasicValueObject.


        :param experimental_factor_category: The experimental_factor_category of this FactorValueBasicValueObject.  # noqa: E501
        :type: CharacteristicValueObject
        """

        self._experimental_factor_category = experimental_factor_category

    @property
    def characteristics(self):
        """Gets the characteristics of this FactorValueBasicValueObject.  # noqa: E501


        :return: The characteristics of this FactorValueBasicValueObject.  # noqa: E501
        :rtype: list[CharacteristicValueObject]
        """
        return self._characteristics

    @characteristics.setter
    def characteristics(self, characteristics):
        """Sets the characteristics of this FactorValueBasicValueObject.


        :param characteristics: The characteristics of this FactorValueBasicValueObject.  # noqa: E501
        :type: list[CharacteristicValueObject]
        """

        self._characteristics = characteristics

    @property
    def statements(self):
        """Gets the statements of this FactorValueBasicValueObject.  # noqa: E501


        :return: The statements of this FactorValueBasicValueObject.  # noqa: E501
        :rtype: list[StatementValueObject]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """Sets the statements of this FactorValueBasicValueObject.


        :param statements: The statements of this FactorValueBasicValueObject.  # noqa: E501
        :type: list[StatementValueObject]
        """

        self._statements = statements

    @property
    def summary(self):
        """Gets the summary of this FactorValueBasicValueObject.  # noqa: E501


        :return: The summary of this FactorValueBasicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this FactorValueBasicValueObject.


        :param summary: The summary of this FactorValueBasicValueObject.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def value(self):
        """Gets the value of this FactorValueBasicValueObject.  # noqa: E501

        Use `summary` if you need a human-readable representation of this factor value or lookup the `characteristics` bag.  # noqa: E501

        :return: The value of this FactorValueBasicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FactorValueBasicValueObject.

        Use `summary` if you need a human-readable representation of this factor value or lookup the `characteristics` bag.  # noqa: E501

        :param value: The value of this FactorValueBasicValueObject.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def measurement(self):
        """Gets the measurement of this FactorValueBasicValueObject.  # noqa: E501


        :return: The measurement of this FactorValueBasicValueObject.  # noqa: E501
        :rtype: MeasurementValueObject
        """
        return self._measurement

    @measurement.setter
    def measurement(self, measurement):
        """Sets the measurement of this FactorValueBasicValueObject.


        :param measurement: The measurement of this FactorValueBasicValueObject.  # noqa: E501
        :type: MeasurementValueObject
        """

        self._measurement = measurement

    @property
    def is_measurement(self):
        """Gets the is_measurement of this FactorValueBasicValueObject.  # noqa: E501

        Indicate if this factor value represents a measurement. When this is true, the `measurement` field will be populated.  # noqa: E501

        :return: The is_measurement of this FactorValueBasicValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_measurement

    @is_measurement.setter
    def is_measurement(self, is_measurement):
        """Sets the is_measurement of this FactorValueBasicValueObject.

        Indicate if this factor value represents a measurement. When this is true, the `measurement` field will be populated.  # noqa: E501

        :param is_measurement: The is_measurement of this FactorValueBasicValueObject.  # noqa: E501
        :type: bool
        """

        self._is_measurement = is_measurement

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
        if issubclass(FactorValueBasicValueObject, dict):
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
        if not isinstance(other, FactorValueBasicValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
