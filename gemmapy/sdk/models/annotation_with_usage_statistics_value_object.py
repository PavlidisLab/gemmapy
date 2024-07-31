# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.8.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnnotationWithUsageStatisticsValueObject(object):
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
        'term_uri': 'str',
        'term_name': 'str',
        'evidence_code': 'str',
        'number_of_expression_experiments': 'int',
        'parent_terms': 'list[OntologyTermValueObject]'
    }

    attribute_map = {
        'class_uri': 'classUri',
        'class_name': 'className',
        'term_uri': 'termUri',
        'term_name': 'termName',
        'evidence_code': 'evidenceCode',
        'number_of_expression_experiments': 'numberOfExpressionExperiments',
        'parent_terms': 'parentTerms'
    }

    def __init__(self, class_uri=None, class_name=None, term_uri=None, term_name=None, evidence_code=None, number_of_expression_experiments=None, parent_terms=None):  # noqa: E501
        """AnnotationWithUsageStatisticsValueObject - a model defined in Swagger"""  # noqa: E501
        self._class_uri = None
        self._class_name = None
        self._term_uri = None
        self._term_name = None
        self._evidence_code = None
        self._number_of_expression_experiments = None
        self._parent_terms = None
        self.discriminator = None
        if class_uri is not None:
            self.class_uri = class_uri
        if class_name is not None:
            self.class_name = class_name
        if term_uri is not None:
            self.term_uri = term_uri
        if term_name is not None:
            self.term_name = term_name
        if evidence_code is not None:
            self.evidence_code = evidence_code
        if number_of_expression_experiments is not None:
            self.number_of_expression_experiments = number_of_expression_experiments
        if parent_terms is not None:
            self.parent_terms = parent_terms

    @property
    def class_uri(self):
        """Gets the class_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The class_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._class_uri

    @class_uri.setter
    def class_uri(self, class_uri):
        """Sets the class_uri of this AnnotationWithUsageStatisticsValueObject.


        :param class_uri: The class_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._class_uri = class_uri

    @property
    def class_name(self):
        """Gets the class_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The class_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this AnnotationWithUsageStatisticsValueObject.


        :param class_name: The class_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._class_name = class_name

    @property
    def term_uri(self):
        """Gets the term_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The term_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._term_uri

    @term_uri.setter
    def term_uri(self, term_uri):
        """Sets the term_uri of this AnnotationWithUsageStatisticsValueObject.


        :param term_uri: The term_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._term_uri = term_uri

    @property
    def term_name(self):
        """Gets the term_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The term_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._term_name

    @term_name.setter
    def term_name(self, term_name):
        """Sets the term_name of this AnnotationWithUsageStatisticsValueObject.


        :param term_name: The term_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._term_name = term_name

    @property
    def evidence_code(self):
        """Gets the evidence_code of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The evidence_code of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._evidence_code

    @evidence_code.setter
    def evidence_code(self, evidence_code):
        """Sets the evidence_code of this AnnotationWithUsageStatisticsValueObject.


        :param evidence_code: The evidence_code of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["IC", "IDA", "IEA", "IEP", "IGI", "IMP", "IPI", "ISS", "NAS", "ND", "RCA", "TAS", "NR", "EXP", "ISA", "ISM", "IGC", "ISO", "IIA", "IBA", "IBD", "IKR", "IRD", "IMR", "IED", "IAGP", "IPM", "QTM", "HDA", "HEP", "HGI", "HMP", "HTP", "OTHER"]  # noqa: E501
        if evidence_code not in allowed_values:
            raise ValueError(
                "Invalid value for `evidence_code` ({0}), must be one of {1}"  # noqa: E501
                .format(evidence_code, allowed_values)
            )

        self._evidence_code = evidence_code

    @property
    def number_of_expression_experiments(self):
        """Gets the number_of_expression_experiments of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The number_of_expression_experiments of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: int
        """
        return self._number_of_expression_experiments

    @number_of_expression_experiments.setter
    def number_of_expression_experiments(self, number_of_expression_experiments):
        """Sets the number_of_expression_experiments of this AnnotationWithUsageStatisticsValueObject.


        :param number_of_expression_experiments: The number_of_expression_experiments of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: int
        """

        self._number_of_expression_experiments = number_of_expression_experiments

    @property
    def parent_terms(self):
        """Gets the parent_terms of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The parent_terms of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: list[OntologyTermValueObject]
        """
        return self._parent_terms

    @parent_terms.setter
    def parent_terms(self, parent_terms):
        """Sets the parent_terms of this AnnotationWithUsageStatisticsValueObject.


        :param parent_terms: The parent_terms of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: list[OntologyTermValueObject]
        """

        self._parent_terms = parent_terms

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
        if issubclass(AnnotationWithUsageStatisticsValueObject, dict):
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
        if not isinstance(other, AnnotationWithUsageStatisticsValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
