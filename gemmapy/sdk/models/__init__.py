# coding: utf-8

# flake8: noqa
"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  ## Updates  ### Update 2.7.1  - improved highlights of search results - fix the limit for getDatasetsAnnotations() endpoint to 5000 in the specification - fix missing initialization of datasets retrieved from the cache  Highlights now use Markdown syntax for formatting. Fields for highlighted ontology terms now use complete object path instead of just `term`. Last but not least, highlights from multiple results are merged.  ### Update 2.7.0  New endpoints for counting the number of results: `getNumberOfDatasets`, `getNumberOfPlatforms`, `getNumberOfResultSets`. These endpoints are faster than looking up `totalElements` as no data is retrieved or converted.  Datasets can now be filtered by annotations at the sample, factor value and all levels using the three newly exposed `experimentalDesign.experimentalFactors.factorValues.characteristics`, `bioAssays.sampleUsed.characteristics` and `allCharacteristics` collections. The two useful available properties for filtering are `value` and `valueUri`.  New `getDatasetsAnnotationsUsageStatistics`, `getDatasetsPlatformsUsageStatistics` and `getDatasetsTaxaUsageStatistics` endpoints for retrieving annotations, platforms and taxa used by the matched datasets. The endpoint accepts the same `filter` argument of `getDatasets`, allowing one to easily navigate terms, platforms and taxa available for filtering furthermore.  Properties available for filtering and sorting are enumerated in the description of the corresponding parameter. There's been a number of fixes and additional tests performed to ensure that all advertised properties are working as expected.  The `FilterArg` and `SortArg`-based parameters now have OpenAPI extensions to enumerate available properties in a structured format under the `x-gemma-filterable-properties`key. Possible values are exposed for enumerated types.  ```yaml x-gemma-filterable-properties: - name: technologyType   type: string   allowedValues:   - value: ONECOLOR     label: One Color   - value: SEQUENCING     label: Sequencing   security:     basicAuth: [GROUP_ADMIN]     cookieAuth: [GROUP_ADMIN] ```  Some of the exposed properties such as `geeq.publicSuitabilityScore` require specific authorities to use. This is documented in `x-filterable-properties` by specifying a [Security Requirement Object](https://spec.openapis.org/oas/latest.html#security-requirement-object).  Types that use the `[]` suffix are using sub-queries under the hood. It implies that the entity will be matched if at least one related entity matches the supplied filter. For example, the `characteristics.valueUri = http://purl.obolibrary.org/obo/UBERON_0002107` filter will match datasets with at least one `UBERON:0002107` tag attached.  Filtered endpoints (including paginated and limited ones) now expose a `groupBy` array that enumerates all the properties used to group results. This helps clear confusion about what constitute a business key in the returned response.  ### Update 2.6.1  Add support for filtering platforms by taxon ID, common name, scientific name, etc. for the `/platforms` endpoint.  ### Update 2.6.0  Add a new `externalDatabases` attribute to the main endpoint that displays version of some of the main external databases that we are using. This exposes versions and last updates for genomes, gene annotations, GO terms, and much more!  The `ExternalDatabaseValueObject` now exposes a `description` which provides additional details.  ### Update 2.5.2  Restore `factors` in `BioMaterialValueObject` as it is being still used by our RNA-Seq pipeline. The attribute is deprecated and should not be used and will be removed when we find a suitable alternative.  Introduce a new endpoint to retrieve quantitation types for a given dataset and parameters to retrieve expression data by quantitation type to `getDatasetProcessedExpression` and `getDatasetRawExpression`. As it was too difficult to extends `getDatasetExpression` to also support quantitation type while retaining the filter feature, we decided to deprecate it and reintroduce filtering for both raw and processed expression in the future.  Fix return type for `getResultSets` which was incorrectly referring to a renamed VO.  Annotate all possible types for `SearchResult.resultObject`. This incidentally includes the `GeneSetValueObject` in the specification which is not exposed elsewhere in the API.  ### Update 2.5.1  Restore `objectClass` visibility in `AnnotationValueObject`.  Fix incorrect response types for annotations search endpoints returning datasets.  ### Update 2.5.0  Major cleanups were performed in this release in order to stabilize the specification. Numerous properties from Gemma Web that were never intended to be exposed in Gemma REST have been hidden. It's a bit too much to describe in here, but you can navigate to the schemas section below to get a good glance at the models.  Favour `numberOfSomething` instead of `somethingCount` which is clearer. The older names are kept for backward-compatibility, but should be considered deprecated.  Gene aliases and multifunctionality rank are now filled in `GeneValueObject`.  Uniformly use `TaxonValueObject` to represent taxon. This is breaking change for the `ExpressionExperimentValueObject` and `ArrayDesignValueObject` as their `taxon` property will be an `object` instead of a `string`. Properties such as `taxonId` are now deprecated and `taxon.id` should be used instead.  Entities that have IDs now all inherit from `IdentifiableValueObject`. This implies that you can assume the presence of an `id` in a search result `resultObject` attribute for example.  New `/search` endpoint! for an unified search experience. Annotation-based search endpoints under `/annotations` are now deprecated.  New API docs! While not as nice looking, the previous theme will be gradually ported to Swagger UI as we focused on functionality over prettiness for this release.  ### Update 2.4.0 through 2.4.1  Release notes for the 2.4 series were not written down, so I'll try to do my best to recall features that were introduced at that time.  An [OpenAPI](https://www.openapis.org/) specification was introduced and available under `/rest/v2/openapi.json`, although not fully stabilized.  Add a `/resultSets` endpoint to navigate result sets directly, by ID or by dataset.  Add a `/resultSets/{resultSetId}` endpoint to retrieve a specific result set by its ID. This endpoint can be negotiated with an `Accept: text/tab-separated-values` header to obtain a TSV representation.  Add a `/datasets/{dataset}/analyses/differential/resultSets` endpoint that essentially redirect to a specific `/resultSet` endpoint by dataset ID.  Add an endpoint to retrieve preferred raw expression vectors.  ### Update 2.3.4  November 6th, 2018  November 6th [2.3.4] Bug fixes in the dataset search endpoint.  November 5th [2.3.3] Added filtering parameters to dataset search.  October 25th [2.3.2] Changed behavior of the dataset search endpoint to more closely match the Gemma web interface.  October 2nd [2.3.1] Added group information to the User value object.  September 27th [2.3.0] Breaking change in Taxa: Abbreviation property has been removed and is therefore no longer an accepted identifier.  ### Update 2.2.6  June 7th, 2018  Code maintenance, bug fixes. Geeq scores stable and made public.  June 7th [2.2.6] Added: User authentication endpoint.  May 2nd [2.2.5] Fixed: Cleaned up and optimized platforms/elements endpoint, removed redundant information (recursive properties nesting).  April 12th [2.2.3] Fixed: Array arguments not handling non-string properties properly, e.g. `ncbiIds` of genes.  April 9th [2.2.1] Fixed: Filter argument not working when the filtered field was a primitive type. This most significantly allows filtering by geeq boolean and double properties.  ### Update 2.2.0  February 8th, 2018  Breaking change in the 'Dataset differential analysis' endpoint: - No longer using `qValueThreshold` parameter. - Response format changed, now using `DifferentialExpressionAnalysisValueObject` instead of `DifferentialExpressionValueObject` - [Experimental] Added Geeq (Gene Expression Experiment Quality) scores to the dataset value objects   # noqa: E501

    OpenAPI spec version: 2.7.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from gemmapy.sdk.models.annotation_search_result_value_object import AnnotationSearchResultValueObject
from gemmapy.sdk.models.annotation_value_object import AnnotationValueObject
from gemmapy.sdk.models.annotation_with_usage_statistics_value_object import AnnotationWithUsageStatisticsValueObject
from gemmapy.sdk.models.api_info_value_object import ApiInfoValueObject
from gemmapy.sdk.models.array_design_value_object import ArrayDesignValueObject
from gemmapy.sdk.models.array_design_with_usage_statistics_value_object import ArrayDesignWithUsageStatisticsValueObject
from gemmapy.sdk.models.audit_event_value_object import AuditEventValueObject
from gemmapy.sdk.models.bibliographic_phenotypes_value_object import BibliographicPhenotypesValueObject
from gemmapy.sdk.models.bibliographic_reference_value_object import BibliographicReferenceValueObject
from gemmapy.sdk.models.bio_assay_value_object import BioAssayValueObject
from gemmapy.sdk.models.bio_material_value_object import BioMaterialValueObject
from gemmapy.sdk.models.bio_sequence_value_object import BioSequenceValueObject
from gemmapy.sdk.models.category_with_usage_statistics_value_object import CategoryWithUsageStatisticsValueObject
from gemmapy.sdk.models.characteristic_basic_value_object import CharacteristicBasicValueObject
from gemmapy.sdk.models.characteristic_value_object import CharacteristicValueObject
from gemmapy.sdk.models.citation_value_object import CitationValueObject
from gemmapy.sdk.models.composite_sequence_arg import CompositeSequenceArg
from gemmapy.sdk.models.composite_sequence_value_object import CompositeSequenceValueObject
from gemmapy.sdk.models.contrast_result_value_object import ContrastResultValueObject
from gemmapy.sdk.models.database_entry_arg import DatabaseEntryArg
from gemmapy.sdk.models.database_entry_value_object import DatabaseEntryValueObject
from gemmapy.sdk.models.dataset import Dataset
from gemmapy.sdk.models.dataset1 import Dataset1
from gemmapy.sdk.models.dataset10 import Dataset10
from gemmapy.sdk.models.dataset2 import Dataset2
from gemmapy.sdk.models.dataset3 import Dataset3
from gemmapy.sdk.models.dataset4 import Dataset4
from gemmapy.sdk.models.dataset5 import Dataset5
from gemmapy.sdk.models.dataset6 import Dataset6
from gemmapy.sdk.models.dataset7 import Dataset7
from gemmapy.sdk.models.dataset8 import Dataset8
from gemmapy.sdk.models.dataset9 import Dataset9
from gemmapy.sdk.models.dataset_arg import DatasetArg
from gemmapy.sdk.models.diff_ex_result_set_summary_value_object import DiffExResultSetSummaryValueObject
from gemmapy.sdk.models.differential_expression_analysis_result_set_value_object import DifferentialExpressionAnalysisResultSetValueObject
from gemmapy.sdk.models.differential_expression_analysis_result_value_object import DifferentialExpressionAnalysisResultValueObject
from gemmapy.sdk.models.differential_expression_analysis_value_object import DifferentialExpressionAnalysisValueObject
from gemmapy.sdk.models.experiment_expression_levels_value_object import ExperimentExpressionLevelsValueObject
from gemmapy.sdk.models.experimental_factor_value_object import ExperimentalFactorValueObject
from gemmapy.sdk.models.expression_experiment_set_value_object import ExpressionExperimentSetValueObject
from gemmapy.sdk.models.expression_experiment_value_object import ExpressionExperimentValueObject
from gemmapy.sdk.models.expression_experiment_with_search_result_value_object import ExpressionExperimentWithSearchResultValueObject
from gemmapy.sdk.models.external_database_value_object import ExternalDatabaseValueObject
from gemmapy.sdk.models.factor_value_basic_value_object import FactorValueBasicValueObject
from gemmapy.sdk.models.factor_value_value_object import FactorValueValueObject
from gemmapy.sdk.models.filter_arg_array_design import FilterArgArrayDesign
from gemmapy.sdk.models.filter_arg_expression_analysis_result_set import FilterArgExpressionAnalysisResultSet
from gemmapy.sdk.models.filter_arg_expression_experiment import FilterArgExpressionExperiment
from gemmapy.sdk.models.filtered_and_paginated_response_data_object_array_design_value_object import FilteredAndPaginatedResponseDataObjectArrayDesignValueObject
from gemmapy.sdk.models.filtered_and_paginated_response_data_object_composite_sequence_value_object import FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject
from gemmapy.sdk.models.filtered_and_paginated_response_data_object_differential_expression_analysis_result_set_value_object import FilteredAndPaginatedResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject
from gemmapy.sdk.models.filtered_and_paginated_response_data_object_expression_experiment_value_object import FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
from gemmapy.sdk.models.filtered_and_paginated_response_data_object_gene_value_object import FilteredAndPaginatedResponseDataObjectGeneValueObject
from gemmapy.sdk.models.geeq_value_object import GeeqValueObject
from gemmapy.sdk.models.gene import Gene
from gemmapy.sdk.models.gene1 import Gene1
from gemmapy.sdk.models.gene2 import Gene2
from gemmapy.sdk.models.gene3 import Gene3
from gemmapy.sdk.models.gene4 import Gene4
from gemmapy.sdk.models.gene_arg import GeneArg
from gemmapy.sdk.models.gene_element_expressions_value_object import GeneElementExpressionsValueObject
from gemmapy.sdk.models.gene_ontology_term_value_object import GeneOntologyTermValueObject
from gemmapy.sdk.models.gene_set_value_object import GeneSetValueObject
from gemmapy.sdk.models.gene_value_object import GeneValueObject
from gemmapy.sdk.models.identifiable_value_object import IdentifiableValueObject
from gemmapy.sdk.models.limited_response_data_object_annotation_with_usage_statistics_value_object import LimitedResponseDataObjectAnnotationWithUsageStatisticsValueObject
from gemmapy.sdk.models.limited_response_data_object_array_design_with_usage_statistics_value_object import LimitedResponseDataObjectArrayDesignWithUsageStatisticsValueObject
from gemmapy.sdk.models.measurement_value_object import MeasurementValueObject
from gemmapy.sdk.models.one_of_search_result_value_object_object_result_object import OneOfSearchResultValueObjectObjectResultObject
from gemmapy.sdk.models.ontology_term_value_object import OntologyTermValueObject
from gemmapy.sdk.models.paginated_response_data_object_composite_sequence_value_object import PaginatedResponseDataObjectCompositeSequenceValueObject
from gemmapy.sdk.models.paginated_response_data_object_expression_experiment_value_object import PaginatedResponseDataObjectExpressionExperimentValueObject
from gemmapy.sdk.models.physical_location_value_object import PhysicalLocationValueObject
from gemmapy.sdk.models.platform import Platform
from gemmapy.sdk.models.platform1 import Platform1
from gemmapy.sdk.models.platform2 import Platform2
from gemmapy.sdk.models.platform3 import Platform3
from gemmapy.sdk.models.platform4 import Platform4
from gemmapy.sdk.models.platform5 import Platform5
from gemmapy.sdk.models.platform_arg import PlatformArg
from gemmapy.sdk.models.probe import Probe
from gemmapy.sdk.models.quantitation_type import QuantitationType
from gemmapy.sdk.models.quantitation_type_arg import QuantitationTypeArg
from gemmapy.sdk.models.quantitation_type_value_object import QuantitationTypeValueObject
from gemmapy.sdk.models.queried_and_filtered_and_paginated_response_data_object_expression_experiment_with_search_result_value_object import QueriedAndFilteredAndPaginatedResponseDataObjectExpressionExperimentWithSearchResultValueObject
from gemmapy.sdk.models.queried_and_filtered_response_data_object_category_with_usage_statistics_value_object import QueriedAndFilteredResponseDataObjectCategoryWithUsageStatisticsValueObject
from gemmapy.sdk.models.queried_and_filtered_response_data_object_taxon_with_usage_statistics_value_object import QueriedAndFilteredResponseDataObjectTaxonWithUsageStatisticsValueObject
from gemmapy.sdk.models.response_data_object_api_info_value_object import ResponseDataObjectApiInfoValueObject
from gemmapy.sdk.models.response_data_object_differential_expression_analysis_result_set_value_object import ResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject
from gemmapy.sdk.models.response_data_object_list_annotation_search_result_value_object import ResponseDataObjectListAnnotationSearchResultValueObject
from gemmapy.sdk.models.response_data_object_list_array_design_value_object import ResponseDataObjectListArrayDesignValueObject
from gemmapy.sdk.models.response_data_object_list_bio_assay_value_object import ResponseDataObjectListBioAssayValueObject
from gemmapy.sdk.models.response_data_object_list_differential_expression_analysis_value_object import ResponseDataObjectListDifferentialExpressionAnalysisValueObject
from gemmapy.sdk.models.response_data_object_list_experiment_expression_levels_value_object import ResponseDataObjectListExperimentExpressionLevelsValueObject
from gemmapy.sdk.models.response_data_object_list_gene_ontology_term_value_object import ResponseDataObjectListGeneOntologyTermValueObject
from gemmapy.sdk.models.response_data_object_list_gene_value_object import ResponseDataObjectListGeneValueObject
from gemmapy.sdk.models.response_data_object_list_physical_location_value_object import ResponseDataObjectListPhysicalLocationValueObject
from gemmapy.sdk.models.response_data_object_list_taxon_value_object import ResponseDataObjectListTaxonValueObject
from gemmapy.sdk.models.response_data_object_long import ResponseDataObjectLong
from gemmapy.sdk.models.response_data_object_set_annotation_value_object import ResponseDataObjectSetAnnotationValueObject
from gemmapy.sdk.models.response_data_object_set_quantitation_type_value_object import ResponseDataObjectSetQuantitationTypeValueObject
from gemmapy.sdk.models.response_data_object_simple_svd_value_object import ResponseDataObjectSimpleSVDValueObject
from gemmapy.sdk.models.response_error_object import ResponseErrorObject
from gemmapy.sdk.models.search_result_type import SearchResultType
from gemmapy.sdk.models.search_result_value_object_expression_experiment_value_object import SearchResultValueObjectExpressionExperimentValueObject
from gemmapy.sdk.models.search_result_value_object_object import SearchResultValueObjectObject
from gemmapy.sdk.models.search_results_response_data_object import SearchResultsResponseDataObject
from gemmapy.sdk.models.search_settings_value_object import SearchSettingsValueObject
from gemmapy.sdk.models.simple_svd_value_object import SimpleSVDValueObject
from gemmapy.sdk.models.sort_arg_array_design import SortArgArrayDesign
from gemmapy.sdk.models.sort_arg_expression_analysis_result_set import SortArgExpressionAnalysisResultSet
from gemmapy.sdk.models.sort_arg_expression_experiment import SortArgExpressionExperiment
from gemmapy.sdk.models.sort_arg_taxon import SortArgTaxon
from gemmapy.sdk.models.sort_value_object import SortValueObject
from gemmapy.sdk.models.taxon import Taxon
from gemmapy.sdk.models.taxon1 import Taxon1
from gemmapy.sdk.models.taxon2 import Taxon2
from gemmapy.sdk.models.taxon3 import Taxon3
from gemmapy.sdk.models.taxon4 import Taxon4
from gemmapy.sdk.models.taxon5 import Taxon5
from gemmapy.sdk.models.taxon6 import Taxon6
from gemmapy.sdk.models.taxon_arg import TaxonArg
from gemmapy.sdk.models.taxon_value_object import TaxonValueObject
from gemmapy.sdk.models.taxon_with_usage_statistics_value_object import TaxonWithUsageStatisticsValueObject
from gemmapy.sdk.models.vector_element_value_object import VectorElementValueObject
from gemmapy.sdk.models.well_composed_error_body import WellComposedErrorBody
