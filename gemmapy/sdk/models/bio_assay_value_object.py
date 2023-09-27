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

class BioAssayValueObject(object):
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
        'accession': 'DatabaseEntryValueObject',
        'array_design': 'ArrayDesignValueObject',
        'description': 'str',
        'metadata': 'str',
        'name': 'str',
        'original_platform': 'ArrayDesignValueObject',
        'outlier': 'bool',
        'predicted_outlier': 'bool',
        'processing_date': 'datetime',
        'sample': 'BioMaterialValueObject',
        'sequence_paired_reads': 'bool',
        'sequence_read_count': 'int',
        'sequence_read_length': 'int',
        'user_flagged_outlier': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'accession': 'accession',
        'array_design': 'arrayDesign',
        'description': 'description',
        'metadata': 'metadata',
        'name': 'name',
        'original_platform': 'originalPlatform',
        'outlier': 'outlier',
        'predicted_outlier': 'predictedOutlier',
        'processing_date': 'processingDate',
        'sample': 'sample',
        'sequence_paired_reads': 'sequencePairedReads',
        'sequence_read_count': 'sequenceReadCount',
        'sequence_read_length': 'sequenceReadLength',
        'user_flagged_outlier': 'userFlaggedOutlier'
    }

    def __init__(self, id=None, accession=None, array_design=None, description=None, metadata=None, name=None, original_platform=None, outlier=None, predicted_outlier=None, processing_date=None, sample=None, sequence_paired_reads=None, sequence_read_count=None, sequence_read_length=None, user_flagged_outlier=None):  # noqa: E501
        """BioAssayValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._accession = None
        self._array_design = None
        self._description = None
        self._metadata = None
        self._name = None
        self._original_platform = None
        self._outlier = None
        self._predicted_outlier = None
        self._processing_date = None
        self._sample = None
        self._sequence_paired_reads = None
        self._sequence_read_count = None
        self._sequence_read_length = None
        self._user_flagged_outlier = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if accession is not None:
            self.accession = accession
        if array_design is not None:
            self.array_design = array_design
        if description is not None:
            self.description = description
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if original_platform is not None:
            self.original_platform = original_platform
        if outlier is not None:
            self.outlier = outlier
        if predicted_outlier is not None:
            self.predicted_outlier = predicted_outlier
        if processing_date is not None:
            self.processing_date = processing_date
        if sample is not None:
            self.sample = sample
        if sequence_paired_reads is not None:
            self.sequence_paired_reads = sequence_paired_reads
        if sequence_read_count is not None:
            self.sequence_read_count = sequence_read_count
        if sequence_read_length is not None:
            self.sequence_read_length = sequence_read_length
        if user_flagged_outlier is not None:
            self.user_flagged_outlier = user_flagged_outlier

    @property
    def id(self):
        """Gets the id of this BioAssayValueObject.  # noqa: E501


        :return: The id of this BioAssayValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BioAssayValueObject.


        :param id: The id of this BioAssayValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def accession(self):
        """Gets the accession of this BioAssayValueObject.  # noqa: E501


        :return: The accession of this BioAssayValueObject.  # noqa: E501
        :rtype: DatabaseEntryValueObject
        """
        return self._accession

    @accession.setter
    def accession(self, accession):
        """Sets the accession of this BioAssayValueObject.


        :param accession: The accession of this BioAssayValueObject.  # noqa: E501
        :type: DatabaseEntryValueObject
        """

        self._accession = accession

    @property
    def array_design(self):
        """Gets the array_design of this BioAssayValueObject.  # noqa: E501


        :return: The array_design of this BioAssayValueObject.  # noqa: E501
        :rtype: ArrayDesignValueObject
        """
        return self._array_design

    @array_design.setter
    def array_design(self, array_design):
        """Sets the array_design of this BioAssayValueObject.


        :param array_design: The array_design of this BioAssayValueObject.  # noqa: E501
        :type: ArrayDesignValueObject
        """

        self._array_design = array_design

    @property
    def description(self):
        """Gets the description of this BioAssayValueObject.  # noqa: E501


        :return: The description of this BioAssayValueObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BioAssayValueObject.


        :param description: The description of this BioAssayValueObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def metadata(self):
        """Gets the metadata of this BioAssayValueObject.  # noqa: E501


        :return: The metadata of this BioAssayValueObject.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this BioAssayValueObject.


        :param metadata: The metadata of this BioAssayValueObject.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this BioAssayValueObject.  # noqa: E501


        :return: The name of this BioAssayValueObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BioAssayValueObject.


        :param name: The name of this BioAssayValueObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def original_platform(self):
        """Gets the original_platform of this BioAssayValueObject.  # noqa: E501


        :return: The original_platform of this BioAssayValueObject.  # noqa: E501
        :rtype: ArrayDesignValueObject
        """
        return self._original_platform

    @original_platform.setter
    def original_platform(self, original_platform):
        """Sets the original_platform of this BioAssayValueObject.


        :param original_platform: The original_platform of this BioAssayValueObject.  # noqa: E501
        :type: ArrayDesignValueObject
        """

        self._original_platform = original_platform

    @property
    def outlier(self):
        """Gets the outlier of this BioAssayValueObject.  # noqa: E501


        :return: The outlier of this BioAssayValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._outlier

    @outlier.setter
    def outlier(self, outlier):
        """Sets the outlier of this BioAssayValueObject.


        :param outlier: The outlier of this BioAssayValueObject.  # noqa: E501
        :type: bool
        """

        self._outlier = outlier

    @property
    def predicted_outlier(self):
        """Gets the predicted_outlier of this BioAssayValueObject.  # noqa: E501


        :return: The predicted_outlier of this BioAssayValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._predicted_outlier

    @predicted_outlier.setter
    def predicted_outlier(self, predicted_outlier):
        """Sets the predicted_outlier of this BioAssayValueObject.


        :param predicted_outlier: The predicted_outlier of this BioAssayValueObject.  # noqa: E501
        :type: bool
        """

        self._predicted_outlier = predicted_outlier

    @property
    def processing_date(self):
        """Gets the processing_date of this BioAssayValueObject.  # noqa: E501


        :return: The processing_date of this BioAssayValueObject.  # noqa: E501
        :rtype: datetime
        """
        return self._processing_date

    @processing_date.setter
    def processing_date(self, processing_date):
        """Sets the processing_date of this BioAssayValueObject.


        :param processing_date: The processing_date of this BioAssayValueObject.  # noqa: E501
        :type: datetime
        """

        self._processing_date = processing_date

    @property
    def sample(self):
        """Gets the sample of this BioAssayValueObject.  # noqa: E501


        :return: The sample of this BioAssayValueObject.  # noqa: E501
        :rtype: BioMaterialValueObject
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this BioAssayValueObject.


        :param sample: The sample of this BioAssayValueObject.  # noqa: E501
        :type: BioMaterialValueObject
        """

        self._sample = sample

    @property
    def sequence_paired_reads(self):
        """Gets the sequence_paired_reads of this BioAssayValueObject.  # noqa: E501


        :return: The sequence_paired_reads of this BioAssayValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._sequence_paired_reads

    @sequence_paired_reads.setter
    def sequence_paired_reads(self, sequence_paired_reads):
        """Sets the sequence_paired_reads of this BioAssayValueObject.


        :param sequence_paired_reads: The sequence_paired_reads of this BioAssayValueObject.  # noqa: E501
        :type: bool
        """

        self._sequence_paired_reads = sequence_paired_reads

    @property
    def sequence_read_count(self):
        """Gets the sequence_read_count of this BioAssayValueObject.  # noqa: E501


        :return: The sequence_read_count of this BioAssayValueObject.  # noqa: E501
        :rtype: int
        """
        return self._sequence_read_count

    @sequence_read_count.setter
    def sequence_read_count(self, sequence_read_count):
        """Sets the sequence_read_count of this BioAssayValueObject.


        :param sequence_read_count: The sequence_read_count of this BioAssayValueObject.  # noqa: E501
        :type: int
        """

        self._sequence_read_count = sequence_read_count

    @property
    def sequence_read_length(self):
        """Gets the sequence_read_length of this BioAssayValueObject.  # noqa: E501


        :return: The sequence_read_length of this BioAssayValueObject.  # noqa: E501
        :rtype: int
        """
        return self._sequence_read_length

    @sequence_read_length.setter
    def sequence_read_length(self, sequence_read_length):
        """Sets the sequence_read_length of this BioAssayValueObject.


        :param sequence_read_length: The sequence_read_length of this BioAssayValueObject.  # noqa: E501
        :type: int
        """

        self._sequence_read_length = sequence_read_length

    @property
    def user_flagged_outlier(self):
        """Gets the user_flagged_outlier of this BioAssayValueObject.  # noqa: E501


        :return: The user_flagged_outlier of this BioAssayValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._user_flagged_outlier

    @user_flagged_outlier.setter
    def user_flagged_outlier(self, user_flagged_outlier):
        """Sets the user_flagged_outlier of this BioAssayValueObject.


        :param user_flagged_outlier: The user_flagged_outlier of this BioAssayValueObject.  # noqa: E501
        :type: bool
        """

        self._user_flagged_outlier = user_flagged_outlier

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
        if issubclass(BioAssayValueObject, dict):
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
        if not isinstance(other, BioAssayValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
