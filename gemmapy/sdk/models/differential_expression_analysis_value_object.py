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

class DifferentialExpressionAnalysisValueObject(object):
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
        'factor_values_used': 'dict(str, list[FactorValueValueObject])',
        'result_sets': 'list[DiffExResultSetSummaryValueObject]',
        'array_designs_used': 'list[int]',
        'bio_assay_set_id': 'int',
        'source_experiment': 'int',
        'subset_factor': 'ExperimentalFactorValueObject',
        'subset_factor_value': 'FactorValueValueObject',
        'factor_values_used_by_experimental_factor_id': 'dict(str, list[FactorValueValueObject])',
        'is_subset': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'factor_values_used': 'factorValuesUsed',
        'result_sets': 'resultSets',
        'array_designs_used': 'arrayDesignsUsed',
        'bio_assay_set_id': 'bioAssaySetId',
        'source_experiment': 'sourceExperiment',
        'subset_factor': 'subsetFactor',
        'subset_factor_value': 'subsetFactorValue',
        'factor_values_used_by_experimental_factor_id': 'factorValuesUsedByExperimentalFactorId',
        'is_subset': 'isSubset'
    }

    def __init__(self, id=None, factor_values_used=None, result_sets=None, array_designs_used=None, bio_assay_set_id=None, source_experiment=None, subset_factor=None, subset_factor_value=None, factor_values_used_by_experimental_factor_id=None, is_subset=None):  # noqa: E501
        """DifferentialExpressionAnalysisValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._factor_values_used = None
        self._result_sets = None
        self._array_designs_used = None
        self._bio_assay_set_id = None
        self._source_experiment = None
        self._subset_factor = None
        self._subset_factor_value = None
        self._factor_values_used_by_experimental_factor_id = None
        self._is_subset = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if factor_values_used is not None:
            self.factor_values_used = factor_values_used
        if result_sets is not None:
            self.result_sets = result_sets
        if array_designs_used is not None:
            self.array_designs_used = array_designs_used
        if bio_assay_set_id is not None:
            self.bio_assay_set_id = bio_assay_set_id
        if source_experiment is not None:
            self.source_experiment = source_experiment
        if subset_factor is not None:
            self.subset_factor = subset_factor
        if subset_factor_value is not None:
            self.subset_factor_value = subset_factor_value
        if factor_values_used_by_experimental_factor_id is not None:
            self.factor_values_used_by_experimental_factor_id = factor_values_used_by_experimental_factor_id
        if is_subset is not None:
            self.is_subset = is_subset

    @property
    def id(self):
        """Gets the id of this DifferentialExpressionAnalysisValueObject.  # noqa: E501


        :return: The id of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DifferentialExpressionAnalysisValueObject.


        :param id: The id of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def factor_values_used(self):
        """Gets the factor_values_used of this DifferentialExpressionAnalysisValueObject.  # noqa: E501


        :return: The factor_values_used of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :rtype: dict(str, list[FactorValueValueObject])
        """
        return self._factor_values_used

    @factor_values_used.setter
    def factor_values_used(self, factor_values_used):
        """Sets the factor_values_used of this DifferentialExpressionAnalysisValueObject.


        :param factor_values_used: The factor_values_used of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :type: dict(str, list[FactorValueValueObject])
        """

        self._factor_values_used = factor_values_used

    @property
    def result_sets(self):
        """Gets the result_sets of this DifferentialExpressionAnalysisValueObject.  # noqa: E501


        :return: The result_sets of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :rtype: list[DiffExResultSetSummaryValueObject]
        """
        return self._result_sets

    @result_sets.setter
    def result_sets(self, result_sets):
        """Sets the result_sets of this DifferentialExpressionAnalysisValueObject.


        :param result_sets: The result_sets of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :type: list[DiffExResultSetSummaryValueObject]
        """

        self._result_sets = result_sets

    @property
    def array_designs_used(self):
        """Gets the array_designs_used of this DifferentialExpressionAnalysisValueObject.  # noqa: E501


        :return: The array_designs_used of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :rtype: list[int]
        """
        return self._array_designs_used

    @array_designs_used.setter
    def array_designs_used(self, array_designs_used):
        """Sets the array_designs_used of this DifferentialExpressionAnalysisValueObject.


        :param array_designs_used: The array_designs_used of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :type: list[int]
        """

        self._array_designs_used = array_designs_used

    @property
    def bio_assay_set_id(self):
        """Gets the bio_assay_set_id of this DifferentialExpressionAnalysisValueObject.  # noqa: E501


        :return: The bio_assay_set_id of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :rtype: int
        """
        return self._bio_assay_set_id

    @bio_assay_set_id.setter
    def bio_assay_set_id(self, bio_assay_set_id):
        """Sets the bio_assay_set_id of this DifferentialExpressionAnalysisValueObject.


        :param bio_assay_set_id: The bio_assay_set_id of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :type: int
        """

        self._bio_assay_set_id = bio_assay_set_id

    @property
    def source_experiment(self):
        """Gets the source_experiment of this DifferentialExpressionAnalysisValueObject.  # noqa: E501


        :return: The source_experiment of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :rtype: int
        """
        return self._source_experiment

    @source_experiment.setter
    def source_experiment(self, source_experiment):
        """Sets the source_experiment of this DifferentialExpressionAnalysisValueObject.


        :param source_experiment: The source_experiment of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :type: int
        """

        self._source_experiment = source_experiment

    @property
    def subset_factor(self):
        """Gets the subset_factor of this DifferentialExpressionAnalysisValueObject.  # noqa: E501


        :return: The subset_factor of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :rtype: ExperimentalFactorValueObject
        """
        return self._subset_factor

    @subset_factor.setter
    def subset_factor(self, subset_factor):
        """Sets the subset_factor of this DifferentialExpressionAnalysisValueObject.


        :param subset_factor: The subset_factor of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :type: ExperimentalFactorValueObject
        """

        self._subset_factor = subset_factor

    @property
    def subset_factor_value(self):
        """Gets the subset_factor_value of this DifferentialExpressionAnalysisValueObject.  # noqa: E501


        :return: The subset_factor_value of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :rtype: FactorValueValueObject
        """
        return self._subset_factor_value

    @subset_factor_value.setter
    def subset_factor_value(self, subset_factor_value):
        """Sets the subset_factor_value of this DifferentialExpressionAnalysisValueObject.


        :param subset_factor_value: The subset_factor_value of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :type: FactorValueValueObject
        """

        self._subset_factor_value = subset_factor_value

    @property
    def factor_values_used_by_experimental_factor_id(self):
        """Gets the factor_values_used_by_experimental_factor_id of this DifferentialExpressionAnalysisValueObject.  # noqa: E501


        :return: The factor_values_used_by_experimental_factor_id of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :rtype: dict(str, list[FactorValueValueObject])
        """
        return self._factor_values_used_by_experimental_factor_id

    @factor_values_used_by_experimental_factor_id.setter
    def factor_values_used_by_experimental_factor_id(self, factor_values_used_by_experimental_factor_id):
        """Sets the factor_values_used_by_experimental_factor_id of this DifferentialExpressionAnalysisValueObject.


        :param factor_values_used_by_experimental_factor_id: The factor_values_used_by_experimental_factor_id of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :type: dict(str, list[FactorValueValueObject])
        """

        self._factor_values_used_by_experimental_factor_id = factor_values_used_by_experimental_factor_id

    @property
    def is_subset(self):
        """Gets the is_subset of this DifferentialExpressionAnalysisValueObject.  # noqa: E501


        :return: The is_subset of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_subset

    @is_subset.setter
    def is_subset(self, is_subset):
        """Sets the is_subset of this DifferentialExpressionAnalysisValueObject.


        :param is_subset: The is_subset of this DifferentialExpressionAnalysisValueObject.  # noqa: E501
        :type: bool
        """

        self._is_subset = is_subset

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
        if issubclass(DifferentialExpressionAnalysisValueObject, dict):
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
        if not isinstance(other, DifferentialExpressionAnalysisValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
