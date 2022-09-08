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

class User(object):
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
        'email': 'str',
        'last_name': 'str',
        'user_name': 'str',
        'password': 'str',
        'password_hint': 'str',
        'enabled': 'bool',
        'signup_token': 'str',
        'signup_token_datestamp': 'datetime',
        'jobs': 'list[JobInfo]',
        'full_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'email': 'email',
        'last_name': 'lastName',
        'user_name': 'userName',
        'password': 'password',
        'password_hint': 'passwordHint',
        'enabled': 'enabled',
        'signup_token': 'signupToken',
        'signup_token_datestamp': 'signupTokenDatestamp',
        'jobs': 'jobs',
        'full_name': 'fullName'
    }

    def __init__(self, name=None, description=None, id=None, email=None, last_name=None, user_name=None, password=None, password_hint=None, enabled=None, signup_token=None, signup_token_datestamp=None, jobs=None, full_name=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._id = None
        self._email = None
        self._last_name = None
        self._user_name = None
        self._password = None
        self._password_hint = None
        self._enabled = None
        self._signup_token = None
        self._signup_token_datestamp = None
        self._jobs = None
        self._full_name = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if email is not None:
            self.email = email
        if last_name is not None:
            self.last_name = last_name
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
        if password_hint is not None:
            self.password_hint = password_hint
        if enabled is not None:
            self.enabled = enabled
        if signup_token is not None:
            self.signup_token = signup_token
        if signup_token_datestamp is not None:
            self.signup_token_datestamp = signup_token_datestamp
        if jobs is not None:
            self.jobs = jobs
        if full_name is not None:
            self.full_name = full_name

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501


        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this User.  # noqa: E501


        :return: The description of this User.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this User.


        :param description: The description of this User.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501


        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def user_name(self):
        """Gets the user_name of this User.  # noqa: E501


        :return: The user_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this User.


        :param user_name: The user_name of this User.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this User.  # noqa: E501


        :return: The password of this User.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.


        :param password: The password of this User.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def password_hint(self):
        """Gets the password_hint of this User.  # noqa: E501


        :return: The password_hint of this User.  # noqa: E501
        :rtype: str
        """
        return self._password_hint

    @password_hint.setter
    def password_hint(self, password_hint):
        """Sets the password_hint of this User.


        :param password_hint: The password_hint of this User.  # noqa: E501
        :type: str
        """

        self._password_hint = password_hint

    @property
    def enabled(self):
        """Gets the enabled of this User.  # noqa: E501


        :return: The enabled of this User.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this User.


        :param enabled: The enabled of this User.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def signup_token(self):
        """Gets the signup_token of this User.  # noqa: E501


        :return: The signup_token of this User.  # noqa: E501
        :rtype: str
        """
        return self._signup_token

    @signup_token.setter
    def signup_token(self, signup_token):
        """Sets the signup_token of this User.


        :param signup_token: The signup_token of this User.  # noqa: E501
        :type: str
        """

        self._signup_token = signup_token

    @property
    def signup_token_datestamp(self):
        """Gets the signup_token_datestamp of this User.  # noqa: E501


        :return: The signup_token_datestamp of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._signup_token_datestamp

    @signup_token_datestamp.setter
    def signup_token_datestamp(self, signup_token_datestamp):
        """Sets the signup_token_datestamp of this User.


        :param signup_token_datestamp: The signup_token_datestamp of this User.  # noqa: E501
        :type: datetime
        """

        self._signup_token_datestamp = signup_token_datestamp

    @property
    def jobs(self):
        """Gets the jobs of this User.  # noqa: E501


        :return: The jobs of this User.  # noqa: E501
        :rtype: list[JobInfo]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this User.


        :param jobs: The jobs of this User.  # noqa: E501
        :type: list[JobInfo]
        """

        self._jobs = jobs

    @property
    def full_name(self):
        """Gets the full_name of this User.  # noqa: E501


        :return: The full_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this User.


        :param full_name: The full_name of this User.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
