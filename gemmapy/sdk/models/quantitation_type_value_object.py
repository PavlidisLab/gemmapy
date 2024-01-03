# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  ## Updates  ### Update 2.7.1  - improved highlights of search results - fix the limit for getDatasetsAnnotations() endpoint to 5000 in the specification - fix missing initialization of datasets retrieved from the cache  Highlights now use Markdown syntax for formatting. Fields for highlighted ontology terms now use complete object path instead of just `term`. Last but not least, highlights from multiple results are merged.  ### Update 2.7.0  New endpoints for counting the number of results: `getNumberOfDatasets`, `getNumberOfPlatforms`, `getNumberOfResultSets`. These endpoints are faster than looking up `totalElements` as no data is retrieved or converted.  Datasets can now be filtered by annotations at the sample, factor value and all levels using the three newly exposed `experimentalDesign.experimentalFactors.factorValues.characteristics`, `bioAssays.sampleUsed.characteristics` and `allCharacteristics` collections. The two useful available properties for filtering are `value` and `valueUri`.  New `getDatasetsAnnotationsUsageStatistics`, `getDatasetsPlatformsUsageStatistics` and `getDatasetsTaxaUsageStatistics` endpoints for retrieving annotations, platforms and taxa used by the matched datasets. The endpoint accepts the same `filter` argument of `getDatasets`, allowing one to easily navigate terms, platforms and taxa available for filtering furthermore.  Properties available for filtering and sorting are enumerated in the description of the corresponding parameter. There's been a number of fixes and additional tests performed to ensure that all advertised properties are working as expected.  The `FilterArg` and `SortArg`-based parameters now have OpenAPI extensions to enumerate available properties in a structured format under the `x-gemma-filterable-properties`key. Possible values are exposed for enumerated types.  ```yaml x-gemma-filterable-properties: - name: technologyType   type: string   allowedValues:   - value: ONECOLOR     label: One Color   - value: SEQUENCING     label: Sequencing   security:     basicAuth: [GROUP_ADMIN]     cookieAuth: [GROUP_ADMIN] ```  Some of the exposed properties such as `geeq.publicSuitabilityScore` require specific authorities to use. This is documented in `x-filterable-properties` by specifying a [Security Requirement Object](https://spec.openapis.org/oas/latest.html#security-requirement-object).  Types that use the `[]` suffix are using sub-queries under the hood. It implies that the entity will be matched if at least one related entity matches the supplied filter. For example, the `characteristics.valueUri = http://purl.obolibrary.org/obo/UBERON_0002107` filter will match datasets with at least one `UBERON:0002107` tag attached.  Filtered endpoints (including paginated and limited ones) now expose a `groupBy` array that enumerates all the properties used to group results. This helps clear confusion about what constitute a business key in the returned response.  ### Update 2.6.1  Add support for filtering platforms by taxon ID, common name, scientific name, etc. for the `/platforms` endpoint.  ### Update 2.6.0  Add a new `externalDatabases` attribute to the main endpoint that displays version of some of the main external databases that we are using. This exposes versions and last updates for genomes, gene annotations, GO terms, and much more!  The `ExternalDatabaseValueObject` now exposes a `description` which provides additional details.  ### Update 2.5.2  Restore `factors` in `BioMaterialValueObject` as it is being still used by our RNA-Seq pipeline. The attribute is deprecated and should not be used and will be removed when we find a suitable alternative.  Introduce a new endpoint to retrieve quantitation types for a given dataset and parameters to retrieve expression data by quantitation type to `getDatasetProcessedExpression` and `getDatasetRawExpression`. As it was too difficult to extends `getDatasetExpression` to also support quantitation type while retaining the filter feature, we decided to deprecate it and reintroduce filtering for both raw and processed expression in the future.  Fix return type for `getResultSets` which was incorrectly referring to a renamed VO.  Annotate all possible types for `SearchResult.resultObject`. This incidentally includes the `GeneSetValueObject` in the specification which is not exposed elsewhere in the API.  ### Update 2.5.1  Restore `objectClass` visibility in `AnnotationValueObject`.  Fix incorrect response types for annotations search endpoints returning datasets.  ### Update 2.5.0  Major cleanups were performed in this release in order to stabilize the specification. Numerous properties from Gemma Web that were never intended to be exposed in Gemma REST have been hidden. It's a bit too much to describe in here, but you can navigate to the schemas section below to get a good glance at the models.  Favour `numberOfSomething` instead of `somethingCount` which is clearer. The older names are kept for backward-compatibility, but should be considered deprecated.  Gene aliases and multifunctionality rank are now filled in `GeneValueObject`.  Uniformly use `TaxonValueObject` to represent taxon. This is breaking change for the `ExpressionExperimentValueObject` and `ArrayDesignValueObject` as their `taxon` property will be an `object` instead of a `string`. Properties such as `taxonId` are now deprecated and `taxon.id` should be used instead.  Entities that have IDs now all inherit from `IdentifiableValueObject`. This implies that you can assume the presence of an `id` in a search result `resultObject` attribute for example.  New `/search` endpoint! for an unified search experience. Annotation-based search endpoints under `/annotations` are now deprecated.  New API docs! While not as nice looking, the previous theme will be gradually ported to Swagger UI as we focused on functionality over prettiness for this release.  ### Update 2.4.0 through 2.4.1  Release notes for the 2.4 series were not written down, so I'll try to do my best to recall features that were introduced at that time.  An [OpenAPI](https://www.openapis.org/) specification was introduced and available under `/rest/v2/openapi.json`, although not fully stabilized.  Add a `/resultSets` endpoint to navigate result sets directly, by ID or by dataset.  Add a `/resultSets/{resultSetId}` endpoint to retrieve a specific result set by its ID. This endpoint can be negotiated with an `Accept: text/tab-separated-values` header to obtain a TSV representation.  Add a `/datasets/{dataset}/analyses/differential/resultSets` endpoint that essentially redirect to a specific `/resultSet` endpoint by dataset ID.  Add an endpoint to retrieve preferred raw expression vectors.  ### Update 2.3.4  November 6th, 2018  November 6th [2.3.4] Bug fixes in the dataset search endpoint.  November 5th [2.3.3] Added filtering parameters to dataset search.  October 25th [2.3.2] Changed behavior of the dataset search endpoint to more closely match the Gemma web interface.  October 2nd [2.3.1] Added group information to the User value object.  September 27th [2.3.0] Breaking change in Taxa: Abbreviation property has been removed and is therefore no longer an accepted identifier.  ### Update 2.2.6  June 7th, 2018  Code maintenance, bug fixes. Geeq scores stable and made public.  June 7th [2.2.6] Added: User authentication endpoint.  May 2nd [2.2.5] Fixed: Cleaned up and optimized platforms/elements endpoint, removed redundant information (recursive properties nesting).  April 12th [2.2.3] Fixed: Array arguments not handling non-string properties properly, e.g. `ncbiIds` of genes.  April 9th [2.2.1] Fixed: Filter argument not working when the filtered field was a primitive type. This most significantly allows filtering by geeq boolean and double properties.  ### Update 2.2.0  February 8th, 2018  Breaking change in the 'Dataset differential analysis' endpoint: - No longer using `qValueThreshold` parameter. - Response format changed, now using `DifferentialExpressionAnalysisValueObject` instead of `DifferentialExpressionValueObject` - [Experimental] Added Geeq (Gene Expression Experiment Quality) scores to the dataset value objects   # noqa: E501

    OpenAPI spec version: 2.7.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class QuantitationTypeValueObject(object):
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
        'description': 'str',
        'general_type': 'str',
        'is_background': 'bool',
        'is_background_subtracted': 'bool',
        'is_batch_corrected': 'bool',
        'is_masked_preferred': 'bool',
        'is_normalized': 'bool',
        'is_preferred': 'bool',
        'is_ratio': 'bool',
        'is_recomputed_from_raw_data': 'bool',
        'name': 'str',
        'representation': 'str',
        'scale': 'str',
        'type': 'str',
        'vector_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'general_type': 'generalType',
        'is_background': 'isBackground',
        'is_background_subtracted': 'isBackgroundSubtracted',
        'is_batch_corrected': 'isBatchCorrected',
        'is_masked_preferred': 'isMaskedPreferred',
        'is_normalized': 'isNormalized',
        'is_preferred': 'isPreferred',
        'is_ratio': 'isRatio',
        'is_recomputed_from_raw_data': 'isRecomputedFromRawData',
        'name': 'name',
        'representation': 'representation',
        'scale': 'scale',
        'type': 'type',
        'vector_type': 'vectorType'
    }

    def __init__(self, id=None, description=None, general_type=None, is_background=None, is_background_subtracted=None, is_batch_corrected=None, is_masked_preferred=None, is_normalized=None, is_preferred=None, is_ratio=None, is_recomputed_from_raw_data=None, name=None, representation=None, scale=None, type=None, vector_type=None):  # noqa: E501
        """QuantitationTypeValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._description = None
        self._general_type = None
        self._is_background = None
        self._is_background_subtracted = None
        self._is_batch_corrected = None
        self._is_masked_preferred = None
        self._is_normalized = None
        self._is_preferred = None
        self._is_ratio = None
        self._is_recomputed_from_raw_data = None
        self._name = None
        self._representation = None
        self._scale = None
        self._type = None
        self._vector_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if general_type is not None:
            self.general_type = general_type
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
        if is_ratio is not None:
            self.is_ratio = is_ratio
        if is_recomputed_from_raw_data is not None:
            self.is_recomputed_from_raw_data = is_recomputed_from_raw_data
        if name is not None:
            self.name = name
        if representation is not None:
            self.representation = representation
        if scale is not None:
            self.scale = scale
        if type is not None:
            self.type = type
        if vector_type is not None:
            self.vector_type = vector_type

    @property
    def id(self):
        """Gets the id of this QuantitationTypeValueObject.  # noqa: E501


        :return: The id of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuantitationTypeValueObject.


        :param id: The id of this QuantitationTypeValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this QuantitationTypeValueObject.  # noqa: E501


        :return: The description of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QuantitationTypeValueObject.


        :param description: The description of this QuantitationTypeValueObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def general_type(self):
        """Gets the general_type of this QuantitationTypeValueObject.  # noqa: E501


        :return: The general_type of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: str
        """
        return self._general_type

    @general_type.setter
    def general_type(self, general_type):
        """Sets the general_type of this QuantitationTypeValueObject.


        :param general_type: The general_type of this QuantitationTypeValueObject.  # noqa: E501
        :type: str
        """

        self._general_type = general_type

    @property
    def is_background(self):
        """Gets the is_background of this QuantitationTypeValueObject.  # noqa: E501


        :return: The is_background of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_background

    @is_background.setter
    def is_background(self, is_background):
        """Sets the is_background of this QuantitationTypeValueObject.


        :param is_background: The is_background of this QuantitationTypeValueObject.  # noqa: E501
        :type: bool
        """

        self._is_background = is_background

    @property
    def is_background_subtracted(self):
        """Gets the is_background_subtracted of this QuantitationTypeValueObject.  # noqa: E501


        :return: The is_background_subtracted of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_background_subtracted

    @is_background_subtracted.setter
    def is_background_subtracted(self, is_background_subtracted):
        """Sets the is_background_subtracted of this QuantitationTypeValueObject.


        :param is_background_subtracted: The is_background_subtracted of this QuantitationTypeValueObject.  # noqa: E501
        :type: bool
        """

        self._is_background_subtracted = is_background_subtracted

    @property
    def is_batch_corrected(self):
        """Gets the is_batch_corrected of this QuantitationTypeValueObject.  # noqa: E501


        :return: The is_batch_corrected of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_batch_corrected

    @is_batch_corrected.setter
    def is_batch_corrected(self, is_batch_corrected):
        """Sets the is_batch_corrected of this QuantitationTypeValueObject.


        :param is_batch_corrected: The is_batch_corrected of this QuantitationTypeValueObject.  # noqa: E501
        :type: bool
        """

        self._is_batch_corrected = is_batch_corrected

    @property
    def is_masked_preferred(self):
        """Gets the is_masked_preferred of this QuantitationTypeValueObject.  # noqa: E501


        :return: The is_masked_preferred of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_masked_preferred

    @is_masked_preferred.setter
    def is_masked_preferred(self, is_masked_preferred):
        """Sets the is_masked_preferred of this QuantitationTypeValueObject.


        :param is_masked_preferred: The is_masked_preferred of this QuantitationTypeValueObject.  # noqa: E501
        :type: bool
        """

        self._is_masked_preferred = is_masked_preferred

    @property
    def is_normalized(self):
        """Gets the is_normalized of this QuantitationTypeValueObject.  # noqa: E501


        :return: The is_normalized of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_normalized

    @is_normalized.setter
    def is_normalized(self, is_normalized):
        """Sets the is_normalized of this QuantitationTypeValueObject.


        :param is_normalized: The is_normalized of this QuantitationTypeValueObject.  # noqa: E501
        :type: bool
        """

        self._is_normalized = is_normalized

    @property
    def is_preferred(self):
        """Gets the is_preferred of this QuantitationTypeValueObject.  # noqa: E501


        :return: The is_preferred of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_preferred

    @is_preferred.setter
    def is_preferred(self, is_preferred):
        """Sets the is_preferred of this QuantitationTypeValueObject.


        :param is_preferred: The is_preferred of this QuantitationTypeValueObject.  # noqa: E501
        :type: bool
        """

        self._is_preferred = is_preferred

    @property
    def is_ratio(self):
        """Gets the is_ratio of this QuantitationTypeValueObject.  # noqa: E501


        :return: The is_ratio of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_ratio

    @is_ratio.setter
    def is_ratio(self, is_ratio):
        """Sets the is_ratio of this QuantitationTypeValueObject.


        :param is_ratio: The is_ratio of this QuantitationTypeValueObject.  # noqa: E501
        :type: bool
        """

        self._is_ratio = is_ratio

    @property
    def is_recomputed_from_raw_data(self):
        """Gets the is_recomputed_from_raw_data of this QuantitationTypeValueObject.  # noqa: E501


        :return: The is_recomputed_from_raw_data of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_recomputed_from_raw_data

    @is_recomputed_from_raw_data.setter
    def is_recomputed_from_raw_data(self, is_recomputed_from_raw_data):
        """Sets the is_recomputed_from_raw_data of this QuantitationTypeValueObject.


        :param is_recomputed_from_raw_data: The is_recomputed_from_raw_data of this QuantitationTypeValueObject.  # noqa: E501
        :type: bool
        """

        self._is_recomputed_from_raw_data = is_recomputed_from_raw_data

    @property
    def name(self):
        """Gets the name of this QuantitationTypeValueObject.  # noqa: E501


        :return: The name of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QuantitationTypeValueObject.


        :param name: The name of this QuantitationTypeValueObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def representation(self):
        """Gets the representation of this QuantitationTypeValueObject.  # noqa: E501


        :return: The representation of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: str
        """
        return self._representation

    @representation.setter
    def representation(self, representation):
        """Sets the representation of this QuantitationTypeValueObject.


        :param representation: The representation of this QuantitationTypeValueObject.  # noqa: E501
        :type: str
        """

        self._representation = representation

    @property
    def scale(self):
        """Gets the scale of this QuantitationTypeValueObject.  # noqa: E501


        :return: The scale of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: str
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this QuantitationTypeValueObject.


        :param scale: The scale of this QuantitationTypeValueObject.  # noqa: E501
        :type: str
        """

        self._scale = scale

    @property
    def type(self):
        """Gets the type of this QuantitationTypeValueObject.  # noqa: E501


        :return: The type of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuantitationTypeValueObject.


        :param type: The type of this QuantitationTypeValueObject.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def vector_type(self):
        """Gets the vector_type of this QuantitationTypeValueObject.  # noqa: E501


        :return: The vector_type of this QuantitationTypeValueObject.  # noqa: E501
        :rtype: str
        """
        return self._vector_type

    @vector_type.setter
    def vector_type(self, vector_type):
        """Sets the vector_type of this QuantitationTypeValueObject.


        :param vector_type: The vector_type of this QuantitationTypeValueObject.  # noqa: E501
        :type: str
        """

        self._vector_type = vector_type

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
        if issubclass(QuantitationTypeValueObject, dict):
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
        if not isinstance(other, QuantitationTypeValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
