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

class AnnotationValueObject(object):
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
        'class_uri': 'str',
        'class_name': 'str',
        'term_uri': 'str',
        'term_name': 'str',
        'evidence_code': 'str',
        'object_class': 'str'
    }

    attribute_map = {
        'id': 'id',
        'class_uri': 'classUri',
        'class_name': 'className',
        'term_uri': 'termUri',
        'term_name': 'termName',
        'evidence_code': 'evidenceCode',
        'object_class': 'objectClass'
    }

    def __init__(self, id=None, class_uri=None, class_name=None, term_uri=None, term_name=None, evidence_code=None, object_class=None):  # noqa: E501
        """AnnotationValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._class_uri = None
        self._class_name = None
        self._term_uri = None
        self._term_name = None
        self._evidence_code = None
        self._object_class = None
        self.discriminator = None
        if id is not None:
            self.id = id
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
        if object_class is not None:
            self.object_class = object_class

    @property
    def id(self):
        """Gets the id of this AnnotationValueObject.  # noqa: E501


        :return: The id of this AnnotationValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnnotationValueObject.


        :param id: The id of this AnnotationValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def class_uri(self):
        """Gets the class_uri of this AnnotationValueObject.  # noqa: E501


        :return: The class_uri of this AnnotationValueObject.  # noqa: E501
        :rtype: str
        """
        return self._class_uri

    @class_uri.setter
    def class_uri(self, class_uri):
        """Sets the class_uri of this AnnotationValueObject.


        :param class_uri: The class_uri of this AnnotationValueObject.  # noqa: E501
        :type: str
        """

        self._class_uri = class_uri

    @property
    def class_name(self):
        """Gets the class_name of this AnnotationValueObject.  # noqa: E501


        :return: The class_name of this AnnotationValueObject.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this AnnotationValueObject.


        :param class_name: The class_name of this AnnotationValueObject.  # noqa: E501
        :type: str
        """

        self._class_name = class_name

    @property
    def term_uri(self):
        """Gets the term_uri of this AnnotationValueObject.  # noqa: E501


        :return: The term_uri of this AnnotationValueObject.  # noqa: E501
        :rtype: str
        """
        return self._term_uri

    @term_uri.setter
    def term_uri(self, term_uri):
        """Sets the term_uri of this AnnotationValueObject.


        :param term_uri: The term_uri of this AnnotationValueObject.  # noqa: E501
        :type: str
        """

        self._term_uri = term_uri

    @property
    def term_name(self):
        """Gets the term_name of this AnnotationValueObject.  # noqa: E501


        :return: The term_name of this AnnotationValueObject.  # noqa: E501
        :rtype: str
        """
        return self._term_name

    @term_name.setter
    def term_name(self, term_name):
        """Sets the term_name of this AnnotationValueObject.


        :param term_name: The term_name of this AnnotationValueObject.  # noqa: E501
        :type: str
        """

        self._term_name = term_name

    @property
    def evidence_code(self):
        """Gets the evidence_code of this AnnotationValueObject.  # noqa: E501


        :return: The evidence_code of this AnnotationValueObject.  # noqa: E501
        :rtype: str
        """
        return self._evidence_code

    @evidence_code.setter
    def evidence_code(self, evidence_code):
        """Sets the evidence_code of this AnnotationValueObject.


        :param evidence_code: The evidence_code of this AnnotationValueObject.  # noqa: E501
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
    def object_class(self):
        """Gets the object_class of this AnnotationValueObject.  # noqa: E501


        :return: The object_class of this AnnotationValueObject.  # noqa: E501
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this AnnotationValueObject.


        :param object_class: The object_class of this AnnotationValueObject.  # noqa: E501
        :type: str
        """

        self._object_class = object_class

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
        if issubclass(AnnotationValueObject, dict):
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
        if not isinstance(other, AnnotationValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
