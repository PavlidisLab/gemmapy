# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  ## Updates  ### Update 2.7.0  New endpoints for counting the number of results: `getNumberOfDatasets`, `getNumberOfPlatforms`, `getNumberOfResultSets`. These endpoints are faster than looking up `totalElements` as no data is retrieved or converted.  Datasets can now be filtered by annotations at the sample, factor value and all levels using the three newly exposed `experimentalDesign.experimentalFactors.factorValues.characteristics`, `bioAssays.sampleUsed.characteristics` and `allCharacteristics` collections. The two useful available properties for filtering are `value` and `valueUri`.  New `getDatasetsAnnotationsUsageStatistics`, `getDatasetsPlatformsUsageStatistics` and `getDatasetsTaxaUsageStatistics` endpoints for retrieving annotations, platforms and taxa used by the matched datasets. The endpoint accepts the same `filter` argument of `getDatasets`, allowing one to easily navigate terms, platforms and taxa available for filtering furthermore.  Properties available for filtering and sorting are enumerated in the description of the corresponding parameter. There's been a number of fixes and additional tests performed to ensure that all advertised properties are working as expected.  The `FilterArg` and `SortArg`-based parameters now have OpenAPI extensions to enumerate available properties in a structured format under the `x-gemma-filterable-properties`key. Possible values are exposed for enumerated types.  ```yaml x-gemma-filterable-properties: - name: technologyType   type: string   allowedValues:   - value: ONECOLOR     label: One Color   - value: SEQUENCING     label: Sequencing   security:     basicAuth: [GROUP_ADMIN]     cookieAuth: [GROUP_ADMIN] ```  Some of the exposed properties such as `geeq.publicSuitabilityScore` require specific authorities to use. This is documented in `x-filterable-properties` by specifying a [Security Requirement Object](https://spec.openapis.org/oas/latest.html#security-requirement-object).  Types that use the `[]` suffix are using sub-queries under the hood. It implies that the entity will be matched if at least one related entity matches the supplied filter. For example, the `characteristics.valueUri = http://purl.obolibrary.org/obo/UBERON_0002107` filter will match datasets with at least one `UBERON:0002107` tag attached.  Filtered endpoints (including paginated and limited ones) now expose a `groupBy` array that enumerates all the properties used to group results. This helps clear confusion about what constitute a business key in the returned response.  ### Update 2.6.1  Add support for filtering platforms by taxon ID, common name, scientific name, etc. for the `/platforms` endpoint.  ### Update 2.6.0  Add a new `externalDatabases` attribute to the main endpoint that displays version of some of the main external databases that we are using. This exposes versions and last updates for genomes, gene annotations, GO terms, and much more!  The `ExternalDatabaseValueObject` now exposes a `description` which provides additional details.  ### Update 2.5.2  Restore `factors` in `BioMaterialValueObject` as it is being still used by our RNA-Seq pipeline. The attribute is deprecated and should not be used and will be removed when we find a suitable alternative.  Introduce a new endpoint to retrieve quantitation types for a given dataset and parameters to retrieve expression data by quantitation type to `getDatasetProcessedExpression` and `getDatasetRawExpression`. As it was too difficult to extends `getDatasetExpression` to also support quantitation type while retaining the filter feature, we decided to deprecate it and reintroduce filtering for both raw and processed expression in the future.  Fix return type for `getResultSets` which was incorrectly referring to a renamed VO.  Annotate all possible types for `SearchResult.resultObject`. This incidentally includes the `GeneSetValueObject` in the specification which is not exposed elsewhere in the API.  ### Update 2.5.1  Restore `objectClass` visibility in `AnnotationValueObject`.  Fix incorrect response types for annotations search endpoints returning datasets.  ### Update 2.5.0  Major cleanups were performed in this release in order to stabilize the specification. Numerous properties from Gemma Web that were never intended to be exposed in Gemma REST have been hidden. It's a bit too much to describe in here, but you can navigate to the schemas section below to get a good glance at the models.  Favour `numberOfSomething` instead of `somethingCount` which is clearer. The older names are kept for backward-compatibility, but should be considered deprecated.  Gene aliases and multifunctionality rank are now filled in `GeneValueObject`.  Uniformly use `TaxonValueObject` to represent taxon. This is breaking change for the `ExpressionExperimentValueObject` and `ArrayDesignValueObject` as their `taxon` property will be an `object` instead of a `string`. Properties such as `taxonId` are now deprecated and `taxon.id` should be used instead.  Entities that have IDs now all inherit from `IdentifiableValueObject`. This implies that you can assume the presence of an `id` in a search result `resultObject` attribute for example.  New `/search` endpoint! for an unified search experience. Annotation-based search endpoints under `/annotations` are now deprecated.  New API docs! While not as nice looking, the previous theme will be gradually ported to Swagger UI as we focused on functionality over prettiness for this release.  ### Update 2.4.0 through 2.4.1  Release notes for the 2.4 series were not written down, so I'll try to do my best to recall features that were introduced at that time.  An [OpenAPI](https://www.openapis.org/) specification was introduced and available under `/rest/v2/openapi.json`, although not fully stabilized.  Add a `/resultSets` endpoint to navigate result sets directly, by ID or by dataset.  Add a `/resultSets/{resultSetId}` endpoint to retrieve a specific result set by its ID. This endpoint can be negotiated with an `Accept: text/tab-separated-values` header to obtain a TSV representation.  Add a `/datasets/{dataset}/analyses/differential/resultSets` endpoint that essentially redirect to a specific `/resultSet` endpoint by dataset ID.  Add an endpoint to retrieve preferred raw expression vectors.  ### Update 2.3.4  November 6th, 2018  November 6th [2.3.4] Bug fixes in the dataset search endpoint.  November 5th [2.3.3] Added filtering parameters to dataset search.  October 25th [2.3.2] Changed behavior of the dataset search endpoint to more closely match the Gemma web interface.  October 2nd [2.3.1] Added group information to the User value object.  September 27th [2.3.0] Breaking change in Taxa: Abbreviation property has been removed and is therefore no longer an accepted identifier.  ### Update 2.2.6  June 7th, 2018  Code maintenance, bug fixes. Geeq scores stable and made public.  June 7th [2.2.6] Added: User authentication endpoint.  May 2nd [2.2.5] Fixed: Cleaned up and optimized platforms/elements endpoint, removed redundant information (recursive properties nesting).  April 12th [2.2.3] Fixed: Array arguments not handling non-string properties properly, e.g. `ncbiIds` of genes.  April 9th [2.2.1] Fixed: Filter argument not working when the filtered field was a primitive type. This most significantly allows filtering by geeq boolean and double properties.  ### Update 2.2.0  February 8th, 2018  Breaking change in the 'Dataset differential analysis' endpoint: - No longer using `qValueThreshold` parameter. - Response format changed, now using `DifferentialExpressionAnalysisValueObject` instead of `DifferentialExpressionValueObject` - [Experimental] Added Geeq (Gene Expression Experiment Quality) scores to the dataset value objects   # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ArrayDesignWithUsageStatisticsValueObject(object):
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
        'last_updated': 'datetime',
        'troubled': 'bool',
        'last_troubled_event': 'AuditEventValueObject',
        'needs_attention': 'bool',
        'last_needs_attention_event': 'AuditEventValueObject',
        'curation_note': 'str',
        'last_note_update_event': 'AuditEventValueObject',
        'color': 'str',
        'description': 'str',
        'is_merged': 'bool',
        'is_mergee': 'bool',
        'name': 'str',
        'short_name': 'str',
        'technology_type': 'str',
        'release_version': 'str',
        'release_url': 'str',
        'external_references': 'list[DatabaseEntryValueObject]',
        'number_of_expression_experiments': 'int',
        'taxon_id': 'int',
        'trouble_details': 'str',
        'taxon': 'TaxonValueObject'
    }

    attribute_map = {
        'id': 'id',
        'last_updated': 'lastUpdated',
        'troubled': 'troubled',
        'last_troubled_event': 'lastTroubledEvent',
        'needs_attention': 'needsAttention',
        'last_needs_attention_event': 'lastNeedsAttentionEvent',
        'curation_note': 'curationNote',
        'last_note_update_event': 'lastNoteUpdateEvent',
        'color': 'color',
        'description': 'description',
        'is_merged': 'isMerged',
        'is_mergee': 'isMergee',
        'name': 'name',
        'short_name': 'shortName',
        'technology_type': 'technologyType',
        'release_version': 'releaseVersion',
        'release_url': 'releaseUrl',
        'external_references': 'externalReferences',
        'number_of_expression_experiments': 'numberOfExpressionExperiments',
        'taxon_id': 'taxonID',
        'trouble_details': 'troubleDetails',
        'taxon': 'taxon'
    }

    def __init__(self, id=None, last_updated=None, troubled=None, last_troubled_event=None, needs_attention=None, last_needs_attention_event=None, curation_note=None, last_note_update_event=None, color=None, description=None, is_merged=None, is_mergee=None, name=None, short_name=None, technology_type=None, release_version=None, release_url=None, external_references=None, number_of_expression_experiments=None, taxon_id=None, trouble_details=None, taxon=None):  # noqa: E501
        """ArrayDesignWithUsageStatisticsValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._last_updated = None
        self._troubled = None
        self._last_troubled_event = None
        self._needs_attention = None
        self._last_needs_attention_event = None
        self._curation_note = None
        self._last_note_update_event = None
        self._color = None
        self._description = None
        self._is_merged = None
        self._is_mergee = None
        self._name = None
        self._short_name = None
        self._technology_type = None
        self._release_version = None
        self._release_url = None
        self._external_references = None
        self._number_of_expression_experiments = None
        self._taxon_id = None
        self._trouble_details = None
        self._taxon = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if last_updated is not None:
            self.last_updated = last_updated
        if troubled is not None:
            self.troubled = troubled
        if last_troubled_event is not None:
            self.last_troubled_event = last_troubled_event
        if needs_attention is not None:
            self.needs_attention = needs_attention
        if last_needs_attention_event is not None:
            self.last_needs_attention_event = last_needs_attention_event
        if curation_note is not None:
            self.curation_note = curation_note
        if last_note_update_event is not None:
            self.last_note_update_event = last_note_update_event
        if color is not None:
            self.color = color
        if description is not None:
            self.description = description
        if is_merged is not None:
            self.is_merged = is_merged
        if is_mergee is not None:
            self.is_mergee = is_mergee
        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if technology_type is not None:
            self.technology_type = technology_type
        if release_version is not None:
            self.release_version = release_version
        if release_url is not None:
            self.release_url = release_url
        if external_references is not None:
            self.external_references = external_references
        if number_of_expression_experiments is not None:
            self.number_of_expression_experiments = number_of_expression_experiments
        if taxon_id is not None:
            self.taxon_id = taxon_id
        if trouble_details is not None:
            self.trouble_details = trouble_details
        if taxon is not None:
            self.taxon = taxon

    @property
    def id(self):
        """Gets the id of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The id of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArrayDesignWithUsageStatisticsValueObject.


        :param id: The id of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The last_updated of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ArrayDesignWithUsageStatisticsValueObject.


        :param last_updated: The last_updated of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def troubled(self):
        """Gets the troubled of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The troubled of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._troubled

    @troubled.setter
    def troubled(self, troubled):
        """Sets the troubled of this ArrayDesignWithUsageStatisticsValueObject.


        :param troubled: The troubled of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: bool
        """

        self._troubled = troubled

    @property
    def last_troubled_event(self):
        """Gets the last_troubled_event of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The last_troubled_event of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: AuditEventValueObject
        """
        return self._last_troubled_event

    @last_troubled_event.setter
    def last_troubled_event(self, last_troubled_event):
        """Sets the last_troubled_event of this ArrayDesignWithUsageStatisticsValueObject.


        :param last_troubled_event: The last_troubled_event of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: AuditEventValueObject
        """

        self._last_troubled_event = last_troubled_event

    @property
    def needs_attention(self):
        """Gets the needs_attention of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The needs_attention of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._needs_attention

    @needs_attention.setter
    def needs_attention(self, needs_attention):
        """Sets the needs_attention of this ArrayDesignWithUsageStatisticsValueObject.


        :param needs_attention: The needs_attention of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: bool
        """

        self._needs_attention = needs_attention

    @property
    def last_needs_attention_event(self):
        """Gets the last_needs_attention_event of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The last_needs_attention_event of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: AuditEventValueObject
        """
        return self._last_needs_attention_event

    @last_needs_attention_event.setter
    def last_needs_attention_event(self, last_needs_attention_event):
        """Sets the last_needs_attention_event of this ArrayDesignWithUsageStatisticsValueObject.


        :param last_needs_attention_event: The last_needs_attention_event of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: AuditEventValueObject
        """

        self._last_needs_attention_event = last_needs_attention_event

    @property
    def curation_note(self):
        """Gets the curation_note of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The curation_note of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._curation_note

    @curation_note.setter
    def curation_note(self, curation_note):
        """Sets the curation_note of this ArrayDesignWithUsageStatisticsValueObject.


        :param curation_note: The curation_note of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._curation_note = curation_note

    @property
    def last_note_update_event(self):
        """Gets the last_note_update_event of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The last_note_update_event of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: AuditEventValueObject
        """
        return self._last_note_update_event

    @last_note_update_event.setter
    def last_note_update_event(self, last_note_update_event):
        """Sets the last_note_update_event of this ArrayDesignWithUsageStatisticsValueObject.


        :param last_note_update_event: The last_note_update_event of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: AuditEventValueObject
        """

        self._last_note_update_event = last_note_update_event

    @property
    def color(self):
        """Gets the color of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The color of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ArrayDesignWithUsageStatisticsValueObject.


        :param color: The color of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def description(self):
        """Gets the description of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The description of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ArrayDesignWithUsageStatisticsValueObject.


        :param description: The description of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_merged(self):
        """Gets the is_merged of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The is_merged of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_merged

    @is_merged.setter
    def is_merged(self, is_merged):
        """Sets the is_merged of this ArrayDesignWithUsageStatisticsValueObject.


        :param is_merged: The is_merged of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: bool
        """

        self._is_merged = is_merged

    @property
    def is_mergee(self):
        """Gets the is_mergee of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The is_mergee of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_mergee

    @is_mergee.setter
    def is_mergee(self, is_mergee):
        """Sets the is_mergee of this ArrayDesignWithUsageStatisticsValueObject.


        :param is_mergee: The is_mergee of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: bool
        """

        self._is_mergee = is_mergee

    @property
    def name(self):
        """Gets the name of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The name of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArrayDesignWithUsageStatisticsValueObject.


        :param name: The name of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The short_name of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this ArrayDesignWithUsageStatisticsValueObject.


        :param short_name: The short_name of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def technology_type(self):
        """Gets the technology_type of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The technology_type of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """Sets the technology_type of this ArrayDesignWithUsageStatisticsValueObject.


        :param technology_type: The technology_type of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._technology_type = technology_type

    @property
    def release_version(self):
        """Gets the release_version of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The release_version of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        """Sets the release_version of this ArrayDesignWithUsageStatisticsValueObject.


        :param release_version: The release_version of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._release_version = release_version

    @property
    def release_url(self):
        """Gets the release_url of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The release_url of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._release_url

    @release_url.setter
    def release_url(self, release_url):
        """Sets the release_url of this ArrayDesignWithUsageStatisticsValueObject.


        :param release_url: The release_url of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._release_url = release_url

    @property
    def external_references(self):
        """Gets the external_references of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The external_references of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: list[DatabaseEntryValueObject]
        """
        return self._external_references

    @external_references.setter
    def external_references(self, external_references):
        """Sets the external_references of this ArrayDesignWithUsageStatisticsValueObject.


        :param external_references: The external_references of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: list[DatabaseEntryValueObject]
        """

        self._external_references = external_references

    @property
    def number_of_expression_experiments(self):
        """Gets the number_of_expression_experiments of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The number_of_expression_experiments of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: int
        """
        return self._number_of_expression_experiments

    @number_of_expression_experiments.setter
    def number_of_expression_experiments(self, number_of_expression_experiments):
        """Sets the number_of_expression_experiments of this ArrayDesignWithUsageStatisticsValueObject.


        :param number_of_expression_experiments: The number_of_expression_experiments of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: int
        """

        self._number_of_expression_experiments = number_of_expression_experiments

    @property
    def taxon_id(self):
        """Gets the taxon_id of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The taxon_id of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: int
        """
        return self._taxon_id

    @taxon_id.setter
    def taxon_id(self, taxon_id):
        """Sets the taxon_id of this ArrayDesignWithUsageStatisticsValueObject.


        :param taxon_id: The taxon_id of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: int
        """

        self._taxon_id = taxon_id

    @property
    def trouble_details(self):
        """Gets the trouble_details of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The trouble_details of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._trouble_details

    @trouble_details.setter
    def trouble_details(self, trouble_details):
        """Sets the trouble_details of this ArrayDesignWithUsageStatisticsValueObject.


        :param trouble_details: The trouble_details of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._trouble_details = trouble_details

    @property
    def taxon(self):
        """Gets the taxon of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501


        :return: The taxon of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: TaxonValueObject
        """
        return self._taxon

    @taxon.setter
    def taxon(self, taxon):
        """Sets the taxon of this ArrayDesignWithUsageStatisticsValueObject.


        :param taxon: The taxon of this ArrayDesignWithUsageStatisticsValueObject.  # noqa: E501
        :type: TaxonValueObject
        """

        self._taxon = taxon

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
        if issubclass(ArrayDesignWithUsageStatisticsValueObject, dict):
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
        if not isinstance(other, ArrayDesignWithUsageStatisticsValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
