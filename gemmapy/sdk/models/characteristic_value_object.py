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

class CharacteristicValueObject(object):
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
        'url_id': 'str',
        'already_present_in_database': 'bool',
        'already_present_on_gene': 'bool',
        'category': 'str',
        'category_uri': 'str',
        'child': 'bool',
        'num_times_used': 'int',
        'ontology_used': 'str',
        'private_gene_count': 'int',
        'public_gene_count': 'int',
        'root': 'bool',
        'taxon': 'str',
        'value': 'str',
        'value_uri': 'str'
    }

    attribute_map = {
        'id': 'id',
        'url_id': 'urlId',
        'already_present_in_database': 'alreadyPresentInDatabase',
        'already_present_on_gene': 'alreadyPresentOnGene',
        'category': 'category',
        'category_uri': 'categoryUri',
        'child': 'child',
        'num_times_used': 'numTimesUsed',
        'ontology_used': 'ontologyUsed',
        'private_gene_count': 'privateGeneCount',
        'public_gene_count': 'publicGeneCount',
        'root': 'root',
        'taxon': 'taxon',
        'value': 'value',
        'value_uri': 'valueUri'
    }

    def __init__(self, id=None, url_id=None, already_present_in_database=None, already_present_on_gene=None, category=None, category_uri=None, child=None, num_times_used=None, ontology_used=None, private_gene_count=None, public_gene_count=None, root=None, taxon=None, value=None, value_uri=None):  # noqa: E501
        """CharacteristicValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._url_id = None
        self._already_present_in_database = None
        self._already_present_on_gene = None
        self._category = None
        self._category_uri = None
        self._child = None
        self._num_times_used = None
        self._ontology_used = None
        self._private_gene_count = None
        self._public_gene_count = None
        self._root = None
        self._taxon = None
        self._value = None
        self._value_uri = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if url_id is not None:
            self.url_id = url_id
        if already_present_in_database is not None:
            self.already_present_in_database = already_present_in_database
        if already_present_on_gene is not None:
            self.already_present_on_gene = already_present_on_gene
        if category is not None:
            self.category = category
        if category_uri is not None:
            self.category_uri = category_uri
        if child is not None:
            self.child = child
        if num_times_used is not None:
            self.num_times_used = num_times_used
        if ontology_used is not None:
            self.ontology_used = ontology_used
        if private_gene_count is not None:
            self.private_gene_count = private_gene_count
        if public_gene_count is not None:
            self.public_gene_count = public_gene_count
        if root is not None:
            self.root = root
        if taxon is not None:
            self.taxon = taxon
        if value is not None:
            self.value = value
        if value_uri is not None:
            self.value_uri = value_uri

    @property
    def id(self):
        """Gets the id of this CharacteristicValueObject.  # noqa: E501


        :return: The id of this CharacteristicValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CharacteristicValueObject.


        :param id: The id of this CharacteristicValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url_id(self):
        """Gets the url_id of this CharacteristicValueObject.  # noqa: E501


        :return: The url_id of this CharacteristicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._url_id

    @url_id.setter
    def url_id(self, url_id):
        """Sets the url_id of this CharacteristicValueObject.


        :param url_id: The url_id of this CharacteristicValueObject.  # noqa: E501
        :type: str
        """

        self._url_id = url_id

    @property
    def already_present_in_database(self):
        """Gets the already_present_in_database of this CharacteristicValueObject.  # noqa: E501


        :return: The already_present_in_database of this CharacteristicValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._already_present_in_database

    @already_present_in_database.setter
    def already_present_in_database(self, already_present_in_database):
        """Sets the already_present_in_database of this CharacteristicValueObject.


        :param already_present_in_database: The already_present_in_database of this CharacteristicValueObject.  # noqa: E501
        :type: bool
        """

        self._already_present_in_database = already_present_in_database

    @property
    def already_present_on_gene(self):
        """Gets the already_present_on_gene of this CharacteristicValueObject.  # noqa: E501


        :return: The already_present_on_gene of this CharacteristicValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._already_present_on_gene

    @already_present_on_gene.setter
    def already_present_on_gene(self, already_present_on_gene):
        """Sets the already_present_on_gene of this CharacteristicValueObject.


        :param already_present_on_gene: The already_present_on_gene of this CharacteristicValueObject.  # noqa: E501
        :type: bool
        """

        self._already_present_on_gene = already_present_on_gene

    @property
    def category(self):
        """Gets the category of this CharacteristicValueObject.  # noqa: E501


        :return: The category of this CharacteristicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CharacteristicValueObject.


        :param category: The category of this CharacteristicValueObject.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def category_uri(self):
        """Gets the category_uri of this CharacteristicValueObject.  # noqa: E501


        :return: The category_uri of this CharacteristicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._category_uri

    @category_uri.setter
    def category_uri(self, category_uri):
        """Sets the category_uri of this CharacteristicValueObject.


        :param category_uri: The category_uri of this CharacteristicValueObject.  # noqa: E501
        :type: str
        """

        self._category_uri = category_uri

    @property
    def child(self):
        """Gets the child of this CharacteristicValueObject.  # noqa: E501


        :return: The child of this CharacteristicValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._child

    @child.setter
    def child(self, child):
        """Sets the child of this CharacteristicValueObject.


        :param child: The child of this CharacteristicValueObject.  # noqa: E501
        :type: bool
        """

        self._child = child

    @property
    def num_times_used(self):
        """Gets the num_times_used of this CharacteristicValueObject.  # noqa: E501


        :return: The num_times_used of this CharacteristicValueObject.  # noqa: E501
        :rtype: int
        """
        return self._num_times_used

    @num_times_used.setter
    def num_times_used(self, num_times_used):
        """Sets the num_times_used of this CharacteristicValueObject.


        :param num_times_used: The num_times_used of this CharacteristicValueObject.  # noqa: E501
        :type: int
        """

        self._num_times_used = num_times_used

    @property
    def ontology_used(self):
        """Gets the ontology_used of this CharacteristicValueObject.  # noqa: E501


        :return: The ontology_used of this CharacteristicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._ontology_used

    @ontology_used.setter
    def ontology_used(self, ontology_used):
        """Sets the ontology_used of this CharacteristicValueObject.


        :param ontology_used: The ontology_used of this CharacteristicValueObject.  # noqa: E501
        :type: str
        """

        self._ontology_used = ontology_used

    @property
    def private_gene_count(self):
        """Gets the private_gene_count of this CharacteristicValueObject.  # noqa: E501


        :return: The private_gene_count of this CharacteristicValueObject.  # noqa: E501
        :rtype: int
        """
        return self._private_gene_count

    @private_gene_count.setter
    def private_gene_count(self, private_gene_count):
        """Sets the private_gene_count of this CharacteristicValueObject.


        :param private_gene_count: The private_gene_count of this CharacteristicValueObject.  # noqa: E501
        :type: int
        """

        self._private_gene_count = private_gene_count

    @property
    def public_gene_count(self):
        """Gets the public_gene_count of this CharacteristicValueObject.  # noqa: E501


        :return: The public_gene_count of this CharacteristicValueObject.  # noqa: E501
        :rtype: int
        """
        return self._public_gene_count

    @public_gene_count.setter
    def public_gene_count(self, public_gene_count):
        """Sets the public_gene_count of this CharacteristicValueObject.


        :param public_gene_count: The public_gene_count of this CharacteristicValueObject.  # noqa: E501
        :type: int
        """

        self._public_gene_count = public_gene_count

    @property
    def root(self):
        """Gets the root of this CharacteristicValueObject.  # noqa: E501


        :return: The root of this CharacteristicValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this CharacteristicValueObject.


        :param root: The root of this CharacteristicValueObject.  # noqa: E501
        :type: bool
        """

        self._root = root

    @property
    def taxon(self):
        """Gets the taxon of this CharacteristicValueObject.  # noqa: E501


        :return: The taxon of this CharacteristicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._taxon

    @taxon.setter
    def taxon(self, taxon):
        """Sets the taxon of this CharacteristicValueObject.


        :param taxon: The taxon of this CharacteristicValueObject.  # noqa: E501
        :type: str
        """

        self._taxon = taxon

    @property
    def value(self):
        """Gets the value of this CharacteristicValueObject.  # noqa: E501


        :return: The value of this CharacteristicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CharacteristicValueObject.


        :param value: The value of this CharacteristicValueObject.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_uri(self):
        """Gets the value_uri of this CharacteristicValueObject.  # noqa: E501


        :return: The value_uri of this CharacteristicValueObject.  # noqa: E501
        :rtype: str
        """
        return self._value_uri

    @value_uri.setter
    def value_uri(self, value_uri):
        """Sets the value_uri of this CharacteristicValueObject.


        :param value_uri: The value_uri of this CharacteristicValueObject.  # noqa: E501
        :type: str
        """

        self._value_uri = value_uri

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
        if issubclass(CharacteristicValueObject, dict):
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
        if not isinstance(other, CharacteristicValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other