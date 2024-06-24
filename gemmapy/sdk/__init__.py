# coding: utf-8

# flake8: noqa

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.7.6
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from gemmapy.sdk.api.default_api import DefaultApi
# import ApiClient
from gemmapy.sdk.api_client import ApiClient
from gemmapy.sdk.configuration import Configuration
# import models into sdk package
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
from gemmapy.sdk.models.build_info_value_object import BuildInfoValueObject
from gemmapy.sdk.models.category_with_usage_statistics_value_object import CategoryWithUsageStatisticsValueObject
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
from gemmapy.sdk.models.dataset11 import Dataset11
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
from gemmapy.sdk.models.filtered_and_inferred_and_paginated_response_data_object_expression_experiment_value_object import FilteredAndInferredAndPaginatedResponseDataObjectExpressionExperimentValueObject
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
from gemmapy.sdk.models.gene5 import Gene5
from gemmapy.sdk.models.gene_arg import GeneArg
from gemmapy.sdk.models.gene_element_expressions_value_object import GeneElementExpressionsValueObject
from gemmapy.sdk.models.gene_ontology_term_value_object import GeneOntologyTermValueObject
from gemmapy.sdk.models.gene_set_value_object import GeneSetValueObject
from gemmapy.sdk.models.gene_value_object import GeneValueObject
from gemmapy.sdk.models.measurement_value_object import MeasurementValueObject
from gemmapy.sdk.models.one_of_search_result_value_object_object_result_object import OneOfSearchResultValueObjectObjectResultObject
from gemmapy.sdk.models.ontology_term_value_object import OntologyTermValueObject
from gemmapy.sdk.models.paginated_response_data_object_composite_sequence_value_object import PaginatedResponseDataObjectCompositeSequenceValueObject
from gemmapy.sdk.models.paginated_response_data_object_expression_experiment_value_object import PaginatedResponseDataObjectExpressionExperimentValueObject
from gemmapy.sdk.models.paginated_response_data_object_gene_value_object import PaginatedResponseDataObjectGeneValueObject
from gemmapy.sdk.models.paginated_results_response_data_object_differential_expression_analysis_result_set_value_object import PaginatedResultsResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject
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
from gemmapy.sdk.models.queried_and_filtered_and_inferred_and_limited_response_data_object_annotation_with_usage_statistics_value_object import QueriedAndFilteredAndInferredAndLimitedResponseDataObjectAnnotationWithUsageStatisticsValueObject
from gemmapy.sdk.models.queried_and_filtered_and_inferred_and_limited_response_data_object_array_design_with_usage_statistics_value_object import QueriedAndFilteredAndInferredAndLimitedResponseDataObjectArrayDesignWithUsageStatisticsValueObject
from gemmapy.sdk.models.queried_and_filtered_and_inferred_and_limited_response_data_object_category_with_usage_statistics_value_object import QueriedAndFilteredAndInferredAndLimitedResponseDataObjectCategoryWithUsageStatisticsValueObject
from gemmapy.sdk.models.queried_and_filtered_and_inferred_and_paginated_response_data_object_expression_experiment_with_search_result_value_object import QueriedAndFilteredAndInferredAndPaginatedResponseDataObjectExpressionExperimentWithSearchResultValueObject
from gemmapy.sdk.models.queried_and_filtered_and_inferred_response_data_object_taxon_with_usage_statistics_value_object import QueriedAndFilteredAndInferredResponseDataObjectTaxonWithUsageStatisticsValueObject
from gemmapy.sdk.models.queried_and_filtered_and_paginated_response_data_object_expression_experiment_value_object import QueriedAndFilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
from gemmapy.sdk.models.query_arg import QueryArg
from gemmapy.sdk.models.response_data_object_api_info_value_object import ResponseDataObjectApiInfoValueObject
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
from gemmapy.sdk.models.sort_value_object import SortValueObject
from gemmapy.sdk.models.statement_value_object import StatementValueObject
from gemmapy.sdk.models.taxa import Taxa
from gemmapy.sdk.models.taxon import Taxon
from gemmapy.sdk.models.taxon1 import Taxon1
from gemmapy.sdk.models.taxon2 import Taxon2
from gemmapy.sdk.models.taxon3 import Taxon3
from gemmapy.sdk.models.taxon4 import Taxon4
from gemmapy.sdk.models.taxon5 import Taxon5
from gemmapy.sdk.models.taxon6 import Taxon6
from gemmapy.sdk.models.taxon7 import Taxon7
from gemmapy.sdk.models.taxon8 import Taxon8
from gemmapy.sdk.models.taxon9 import Taxon9
from gemmapy.sdk.models.taxon_arg import TaxonArg
from gemmapy.sdk.models.taxon_value_object import TaxonValueObject
from gemmapy.sdk.models.taxon_with_usage_statistics_value_object import TaxonWithUsageStatisticsValueObject
from gemmapy.sdk.models.vector_element_value_object import VectorElementValueObject
from gemmapy.sdk.models.well_composed_error_body import WellComposedErrorBody
