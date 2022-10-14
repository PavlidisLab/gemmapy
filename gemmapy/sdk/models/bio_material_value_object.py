# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  Fix return type for `getResultSets` which was incorrectly referring to a renamed VO.  Remove the `security` requirements by default from the specification, which forced the Python package to supply empty credentials. There is currently no privileged endpoints, although some can return additional results.  ## Updates  ### Update 2.5.1  Restore `objectClass` visibility in `AnnotationValueObject`.  Fix incorrect response types for annotations search endpoints returning datasets.  ### Update 2.5.0  Major cleanups were performed in this release in order to stabilize the specification. Numerous properties from Gemma Web that were never intended to be exposed in Gemma REST have been hidden. It's a bit too much to describe in here, but you can navigate to the schemas section below to get a good glance at the models.  Favour `numberOfSomething` instead of `somethingCount` which is clearer. The older names are kept for backward-compatibility, but should be considered deprecated.  Gene aliases and multifunctionality rank are now filled in `GeneValueObject`.  Uniformly use `TaxonValueObject` to represent taxon. This is breaking change for the `ExpressionExperimentValueObject` and `ArrayDesignValueObject` as their `taxon` property will be an `object` instead of a `string`. Properties such as `taxonId` are now deprecated and `taxon.id` should be used instead.  Entities that have IDs now all inherit from `IdentifiableValueObject`. This implies that you can assume the presence of an `id` in a search result `resultObject` attribute for example.  New `/search` endpoint! for an unified search experience. Annotation-based search endpoints under `/annotations` are now deprecated.  New API docs! While not as nice looking, the previous theme will be gradually ported to Swagger UI as we focused on functionality over prettiness for this release.  ### Update 2.4.0 through 2.4.1  Release notes for the 2.4 series were not written down, so I'll try to do my best to recall features that were introduced at that time.  An [OpenAPI](https://www.openapis.org/) specification was introduced and available under `/rest/v2/openapi.json`, although not fully stabilized.  Add a `/resultSets` endpoint to navigate result sets directly, by ID or by dataset.  Add a `/resultSets/{resultSetId}` endpoint to retrieve a specific result set by its ID. This endpoint can be negotiated with an `Accept: text/tab-separated-values` header to obtain a TSV representation.  Add a `/datasets/{dataset}/analyses/differential/resultSets` endpoint that essentially redirect to a specific `/resultSet` endpoint by dataset ID.  Add an endpoint to retrieve preferred raw expression vectors.  ### Update 2.3.4  November 6th, 2018  November 6th [2.3.4] Bug fixes in the dataset search endpoint.  November 5th [2.3.3] Added filtering parameters to dataset search.  October 25th [2.3.2] Changed behavior of the dataset search endpoint to more closely match the Gemma web interface.  October 2nd [2.3.1] Added group information to the User value object.  September 27th [2.3.0] Breaking change in Taxa: Abbreviation property has been removed and is therefore no longer an accepted identifier.  ### Update 2.2.6  June 7th, 2018  Code maintenance, bug fixes. Geeq scores stable and made public.  June 7th [2.2.6] Added: User authentication endpoint.  May 2nd [2.2.5] Fixed: Cleaned up and optimized platforms/elements endpoint, removed redundant information (recursive properties nesting).  April 12th [2.2.3] Fixed: Array arguments not handling non-string properties properly, e.g. `ncbiIds` of genes.  April 9th [2.2.1] Fixed: Filter argument not working when the filtered field was a primitive type. This most significantly allows filtering by geeq boolean and double properties.  ### Update 2.2.0  February 8th, 2018  Breaking change in the 'Dataset differential analysis' endpoint: - No longer using `qValueThreshold` parameter. - Response format changed, now using `DifferentialExpressionAnalysisValueObject` instead of `DifferentialExpressionValueObject` - [Experimental] Added Geeq (Gene Expression Experiment Quality) scores to the dataset value objects   # noqa: E501

    OpenAPI spec version: 2.5.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BioMaterialValueObject(object):
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
        'name': 'str',
        'description': 'str',
        'bio_assay_ids': 'list[int]',
        'characteristics': 'list[CharacteristicValueObject]',
        'factor_value_objects': 'list[IdentifiableValueObject]',
        'factor_values': 'list[IdentifiableValueObject]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'bio_assay_ids': 'bioAssayIds',
        'characteristics': 'characteristics',
        'factor_value_objects': 'factorValueObjects',
        'factor_values': 'factorValues'
    }

    def __init__(self, id=None, name=None, description=None, bio_assay_ids=None, characteristics=None, factor_value_objects=None, factor_values=None):  # noqa: E501
        """BioMaterialValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._bio_assay_ids = None
        self._characteristics = None
        self._factor_value_objects = None
        self._factor_values = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if bio_assay_ids is not None:
            self.bio_assay_ids = bio_assay_ids
        if characteristics is not None:
            self.characteristics = characteristics
        if factor_value_objects is not None:
            self.factor_value_objects = factor_value_objects
        if factor_values is not None:
            self.factor_values = factor_values

    @property
    def id(self):
        """Gets the id of this BioMaterialValueObject.  # noqa: E501


        :return: The id of this BioMaterialValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BioMaterialValueObject.


        :param id: The id of this BioMaterialValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BioMaterialValueObject.  # noqa: E501


        :return: The name of this BioMaterialValueObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BioMaterialValueObject.


        :param name: The name of this BioMaterialValueObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this BioMaterialValueObject.  # noqa: E501


        :return: The description of this BioMaterialValueObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BioMaterialValueObject.


        :param description: The description of this BioMaterialValueObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def bio_assay_ids(self):
        """Gets the bio_assay_ids of this BioMaterialValueObject.  # noqa: E501


        :return: The bio_assay_ids of this BioMaterialValueObject.  # noqa: E501
        :rtype: list[int]
        """
        return self._bio_assay_ids

    @bio_assay_ids.setter
    def bio_assay_ids(self, bio_assay_ids):
        """Sets the bio_assay_ids of this BioMaterialValueObject.


        :param bio_assay_ids: The bio_assay_ids of this BioMaterialValueObject.  # noqa: E501
        :type: list[int]
        """

        self._bio_assay_ids = bio_assay_ids

    @property
    def characteristics(self):
        """Gets the characteristics of this BioMaterialValueObject.  # noqa: E501


        :return: The characteristics of this BioMaterialValueObject.  # noqa: E501
        :rtype: list[CharacteristicValueObject]
        """
        return self._characteristics

    @characteristics.setter
    def characteristics(self, characteristics):
        """Sets the characteristics of this BioMaterialValueObject.


        :param characteristics: The characteristics of this BioMaterialValueObject.  # noqa: E501
        :type: list[CharacteristicValueObject]
        """

        self._characteristics = characteristics

    @property
    def factor_value_objects(self):
        """Gets the factor_value_objects of this BioMaterialValueObject.  # noqa: E501


        :return: The factor_value_objects of this BioMaterialValueObject.  # noqa: E501
        :rtype: list[IdentifiableValueObject]
        """
        return self._factor_value_objects

    @factor_value_objects.setter
    def factor_value_objects(self, factor_value_objects):
        """Sets the factor_value_objects of this BioMaterialValueObject.


        :param factor_value_objects: The factor_value_objects of this BioMaterialValueObject.  # noqa: E501
        :type: list[IdentifiableValueObject]
        """

        self._factor_value_objects = factor_value_objects

    @property
    def factor_values(self):
        """Gets the factor_values of this BioMaterialValueObject.  # noqa: E501


        :return: The factor_values of this BioMaterialValueObject.  # noqa: E501
        :rtype: list[IdentifiableValueObject]
        """
        return self._factor_values

    @factor_values.setter
    def factor_values(self, factor_values):
        """Sets the factor_values of this BioMaterialValueObject.


        :param factor_values: The factor_values of this BioMaterialValueObject.  # noqa: E501
        :type: list[IdentifiableValueObject]
        """

        self._factor_values = factor_values

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
        if issubclass(BioMaterialValueObject, dict):
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
        if not isinstance(other, BioMaterialValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
