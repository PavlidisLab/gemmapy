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

class ExpressionExperimentValueObject(object):
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
        'number_of_bio_assays': 'int',
        'description': 'str',
        'name': 'str',
        'accession': 'str',
        'batch_confound': 'str',
        'batch_effect': 'str',
        'external_database': 'str',
        'external_uri': 'str',
        'geeq': 'GeeqValueObject',
        'metadata': 'str',
        'short_name': 'str',
        'source': 'str',
        'technology_type': 'str',
        'bio_assay_count': 'int',
        'taxon_id': 'int',
        'trouble_details': 'str',
        'number_of_array_designs': 'int',
        'number_of_processed_expression_vectors': 'int',
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
        'number_of_bio_assays': 'numberOfBioAssays',
        'description': 'description',
        'name': 'name',
        'accession': 'accession',
        'batch_confound': 'batchConfound',
        'batch_effect': 'batchEffect',
        'external_database': 'externalDatabase',
        'external_uri': 'externalUri',
        'geeq': 'geeq',
        'metadata': 'metadata',
        'short_name': 'shortName',
        'source': 'source',
        'technology_type': 'technologyType',
        'bio_assay_count': 'bioAssayCount',
        'taxon_id': 'taxonId',
        'trouble_details': 'troubleDetails',
        'number_of_array_designs': 'numberOfArrayDesigns',
        'number_of_processed_expression_vectors': 'numberOfProcessedExpressionVectors',
        'taxon': 'taxon'
    }

    def __init__(self, id=None, last_updated=None, troubled=None, last_troubled_event=None, needs_attention=None, last_needs_attention_event=None, curation_note=None, last_note_update_event=None, number_of_bio_assays=None, description=None, name=None, accession=None, batch_confound=None, batch_effect=None, external_database=None, external_uri=None, geeq=None, metadata=None, short_name=None, source=None, technology_type=None, bio_assay_count=None, taxon_id=None, trouble_details=None, number_of_array_designs=None, number_of_processed_expression_vectors=None, taxon=None):  # noqa: E501
        """ExpressionExperimentValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._last_updated = None
        self._troubled = None
        self._last_troubled_event = None
        self._needs_attention = None
        self._last_needs_attention_event = None
        self._curation_note = None
        self._last_note_update_event = None
        self._number_of_bio_assays = None
        self._description = None
        self._name = None
        self._accession = None
        self._batch_confound = None
        self._batch_effect = None
        self._external_database = None
        self._external_uri = None
        self._geeq = None
        self._metadata = None
        self._short_name = None
        self._source = None
        self._technology_type = None
        self._bio_assay_count = None
        self._taxon_id = None
        self._trouble_details = None
        self._number_of_array_designs = None
        self._number_of_processed_expression_vectors = None
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
        if number_of_bio_assays is not None:
            self.number_of_bio_assays = number_of_bio_assays
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if accession is not None:
            self.accession = accession
        if batch_confound is not None:
            self.batch_confound = batch_confound
        if batch_effect is not None:
            self.batch_effect = batch_effect
        if external_database is not None:
            self.external_database = external_database
        if external_uri is not None:
            self.external_uri = external_uri
        if geeq is not None:
            self.geeq = geeq
        if metadata is not None:
            self.metadata = metadata
        if short_name is not None:
            self.short_name = short_name
        if source is not None:
            self.source = source
        if technology_type is not None:
            self.technology_type = technology_type
        if bio_assay_count is not None:
            self.bio_assay_count = bio_assay_count
        if taxon_id is not None:
            self.taxon_id = taxon_id
        if trouble_details is not None:
            self.trouble_details = trouble_details
        if number_of_array_designs is not None:
            self.number_of_array_designs = number_of_array_designs
        if number_of_processed_expression_vectors is not None:
            self.number_of_processed_expression_vectors = number_of_processed_expression_vectors
        if taxon is not None:
            self.taxon = taxon

    @property
    def id(self):
        """Gets the id of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The id of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExpressionExperimentValueObject.


        :param id: The id of this ExpressionExperimentValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The last_updated of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ExpressionExperimentValueObject.


        :param last_updated: The last_updated of this ExpressionExperimentValueObject.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def troubled(self):
        """Gets the troubled of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The troubled of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._troubled

    @troubled.setter
    def troubled(self, troubled):
        """Sets the troubled of this ExpressionExperimentValueObject.


        :param troubled: The troubled of this ExpressionExperimentValueObject.  # noqa: E501
        :type: bool
        """

        self._troubled = troubled

    @property
    def last_troubled_event(self):
        """Gets the last_troubled_event of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The last_troubled_event of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: AuditEventValueObject
        """
        return self._last_troubled_event

    @last_troubled_event.setter
    def last_troubled_event(self, last_troubled_event):
        """Sets the last_troubled_event of this ExpressionExperimentValueObject.


        :param last_troubled_event: The last_troubled_event of this ExpressionExperimentValueObject.  # noqa: E501
        :type: AuditEventValueObject
        """

        self._last_troubled_event = last_troubled_event

    @property
    def needs_attention(self):
        """Gets the needs_attention of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The needs_attention of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._needs_attention

    @needs_attention.setter
    def needs_attention(self, needs_attention):
        """Sets the needs_attention of this ExpressionExperimentValueObject.


        :param needs_attention: The needs_attention of this ExpressionExperimentValueObject.  # noqa: E501
        :type: bool
        """

        self._needs_attention = needs_attention

    @property
    def last_needs_attention_event(self):
        """Gets the last_needs_attention_event of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The last_needs_attention_event of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: AuditEventValueObject
        """
        return self._last_needs_attention_event

    @last_needs_attention_event.setter
    def last_needs_attention_event(self, last_needs_attention_event):
        """Sets the last_needs_attention_event of this ExpressionExperimentValueObject.


        :param last_needs_attention_event: The last_needs_attention_event of this ExpressionExperimentValueObject.  # noqa: E501
        :type: AuditEventValueObject
        """

        self._last_needs_attention_event = last_needs_attention_event

    @property
    def curation_note(self):
        """Gets the curation_note of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The curation_note of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._curation_note

    @curation_note.setter
    def curation_note(self, curation_note):
        """Sets the curation_note of this ExpressionExperimentValueObject.


        :param curation_note: The curation_note of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._curation_note = curation_note

    @property
    def last_note_update_event(self):
        """Gets the last_note_update_event of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The last_note_update_event of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: AuditEventValueObject
        """
        return self._last_note_update_event

    @last_note_update_event.setter
    def last_note_update_event(self, last_note_update_event):
        """Sets the last_note_update_event of this ExpressionExperimentValueObject.


        :param last_note_update_event: The last_note_update_event of this ExpressionExperimentValueObject.  # noqa: E501
        :type: AuditEventValueObject
        """

        self._last_note_update_event = last_note_update_event

    @property
    def number_of_bio_assays(self):
        """Gets the number_of_bio_assays of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The number_of_bio_assays of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: int
        """
        return self._number_of_bio_assays

    @number_of_bio_assays.setter
    def number_of_bio_assays(self, number_of_bio_assays):
        """Sets the number_of_bio_assays of this ExpressionExperimentValueObject.


        :param number_of_bio_assays: The number_of_bio_assays of this ExpressionExperimentValueObject.  # noqa: E501
        :type: int
        """

        self._number_of_bio_assays = number_of_bio_assays

    @property
    def description(self):
        """Gets the description of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The description of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExpressionExperimentValueObject.


        :param description: The description of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The name of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExpressionExperimentValueObject.


        :param name: The name of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def accession(self):
        """Gets the accession of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The accession of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._accession

    @accession.setter
    def accession(self, accession):
        """Sets the accession of this ExpressionExperimentValueObject.


        :param accession: The accession of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._accession = accession

    @property
    def batch_confound(self):
        """Gets the batch_confound of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The batch_confound of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._batch_confound

    @batch_confound.setter
    def batch_confound(self, batch_confound):
        """Sets the batch_confound of this ExpressionExperimentValueObject.


        :param batch_confound: The batch_confound of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._batch_confound = batch_confound

    @property
    def batch_effect(self):
        """Gets the batch_effect of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The batch_effect of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._batch_effect

    @batch_effect.setter
    def batch_effect(self, batch_effect):
        """Sets the batch_effect of this ExpressionExperimentValueObject.


        :param batch_effect: The batch_effect of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._batch_effect = batch_effect

    @property
    def external_database(self):
        """Gets the external_database of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The external_database of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._external_database

    @external_database.setter
    def external_database(self, external_database):
        """Sets the external_database of this ExpressionExperimentValueObject.


        :param external_database: The external_database of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._external_database = external_database

    @property
    def external_uri(self):
        """Gets the external_uri of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The external_uri of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._external_uri

    @external_uri.setter
    def external_uri(self, external_uri):
        """Sets the external_uri of this ExpressionExperimentValueObject.


        :param external_uri: The external_uri of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._external_uri = external_uri

    @property
    def geeq(self):
        """Gets the geeq of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The geeq of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: GeeqValueObject
        """
        return self._geeq

    @geeq.setter
    def geeq(self, geeq):
        """Sets the geeq of this ExpressionExperimentValueObject.


        :param geeq: The geeq of this ExpressionExperimentValueObject.  # noqa: E501
        :type: GeeqValueObject
        """

        self._geeq = geeq

    @property
    def metadata(self):
        """Gets the metadata of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The metadata of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ExpressionExperimentValueObject.


        :param metadata: The metadata of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def short_name(self):
        """Gets the short_name of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The short_name of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this ExpressionExperimentValueObject.


        :param short_name: The short_name of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def source(self):
        """Gets the source of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The source of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ExpressionExperimentValueObject.


        :param source: The source of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def technology_type(self):
        """Gets the technology_type of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The technology_type of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """Sets the technology_type of this ExpressionExperimentValueObject.


        :param technology_type: The technology_type of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._technology_type = technology_type

    @property
    def bio_assay_count(self):
        """Gets the bio_assay_count of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The bio_assay_count of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: int
        """
        return self._bio_assay_count

    @bio_assay_count.setter
    def bio_assay_count(self, bio_assay_count):
        """Sets the bio_assay_count of this ExpressionExperimentValueObject.


        :param bio_assay_count: The bio_assay_count of this ExpressionExperimentValueObject.  # noqa: E501
        :type: int
        """

        self._bio_assay_count = bio_assay_count

    @property
    def taxon_id(self):
        """Gets the taxon_id of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The taxon_id of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: int
        """
        return self._taxon_id

    @taxon_id.setter
    def taxon_id(self, taxon_id):
        """Sets the taxon_id of this ExpressionExperimentValueObject.


        :param taxon_id: The taxon_id of this ExpressionExperimentValueObject.  # noqa: E501
        :type: int
        """

        self._taxon_id = taxon_id

    @property
    def trouble_details(self):
        """Gets the trouble_details of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The trouble_details of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: str
        """
        return self._trouble_details

    @trouble_details.setter
    def trouble_details(self, trouble_details):
        """Sets the trouble_details of this ExpressionExperimentValueObject.


        :param trouble_details: The trouble_details of this ExpressionExperimentValueObject.  # noqa: E501
        :type: str
        """

        self._trouble_details = trouble_details

    @property
    def number_of_array_designs(self):
        """Gets the number_of_array_designs of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The number_of_array_designs of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: int
        """
        return self._number_of_array_designs

    @number_of_array_designs.setter
    def number_of_array_designs(self, number_of_array_designs):
        """Sets the number_of_array_designs of this ExpressionExperimentValueObject.


        :param number_of_array_designs: The number_of_array_designs of this ExpressionExperimentValueObject.  # noqa: E501
        :type: int
        """

        self._number_of_array_designs = number_of_array_designs

    @property
    def number_of_processed_expression_vectors(self):
        """Gets the number_of_processed_expression_vectors of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The number_of_processed_expression_vectors of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: int
        """
        return self._number_of_processed_expression_vectors

    @number_of_processed_expression_vectors.setter
    def number_of_processed_expression_vectors(self, number_of_processed_expression_vectors):
        """Sets the number_of_processed_expression_vectors of this ExpressionExperimentValueObject.


        :param number_of_processed_expression_vectors: The number_of_processed_expression_vectors of this ExpressionExperimentValueObject.  # noqa: E501
        :type: int
        """

        self._number_of_processed_expression_vectors = number_of_processed_expression_vectors

    @property
    def taxon(self):
        """Gets the taxon of this ExpressionExperimentValueObject.  # noqa: E501


        :return: The taxon of this ExpressionExperimentValueObject.  # noqa: E501
        :rtype: TaxonValueObject
        """
        return self._taxon

    @taxon.setter
    def taxon(self, taxon):
        """Sets the taxon of this ExpressionExperimentValueObject.


        :param taxon: The taxon of this ExpressionExperimentValueObject.  # noqa: E501
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
        if issubclass(ExpressionExperimentValueObject, dict):
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
        if not isinstance(other, ExpressionExperimentValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
