# coding: utf-8

# flake8: noqa
"""
    Gemma RESTful API

    This website documents the usage of the [Gemma REST API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  The documentation of the underlying java code can be found [here](https://gemma.msl.ubc.ca/resources/apidocs/ubic/gemma/web/services/rest/package-summary.html). See the [links section](https://gemma.msl.ubc.ca/resources/restapidocs/#footer) in the footer of this page for other relevant links.  Use of this webpage and Gemma web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.   # noqa: E501

    OpenAPI spec version: 2.4.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from gemmapy.sdk.models.alternate_name import AlternateName
from gemmapy.sdk.models.analysis import Analysis
from gemmapy.sdk.models.annotation_search_result_value_object import AnnotationSearchResultValueObject
from gemmapy.sdk.models.annotation_value_object import AnnotationValueObject
from gemmapy.sdk.models.api_info_value_object import ApiInfoValueObject
from gemmapy.sdk.models.array_design import ArrayDesign
from gemmapy.sdk.models.array_design_value_object import ArrayDesignValueObject
from gemmapy.sdk.models.audit_action import AuditAction
from gemmapy.sdk.models.audit_event import AuditEvent
from gemmapy.sdk.models.audit_event_type import AuditEventType
from gemmapy.sdk.models.audit_event_value_object import AuditEventValueObject
from gemmapy.sdk.models.audit_trail import AuditTrail
from gemmapy.sdk.models.bibliographic_reference import BibliographicReference
from gemmapy.sdk.models.bio_assay_value_object import BioAssayValueObject
from gemmapy.sdk.models.bio_material_value_object import BioMaterialValueObject
from gemmapy.sdk.models.bio_sequence import BioSequence
from gemmapy.sdk.models.bio_sequence2_gene_product import BioSequence2GeneProduct
from gemmapy.sdk.models.bio_sequence_value_object import BioSequenceValueObject
from gemmapy.sdk.models.blat_result_value_object import BlatResultValueObject
from gemmapy.sdk.models.characteristic import Characteristic
from gemmapy.sdk.models.characteristic_basic_value_object import CharacteristicBasicValueObject
from gemmapy.sdk.models.characteristic_value_object import CharacteristicValueObject
from gemmapy.sdk.models.chromosome import Chromosome
from gemmapy.sdk.models.coexpression_value_object_ext import CoexpressionValueObjectExt
from gemmapy.sdk.models.composite_sequence import CompositeSequence
from gemmapy.sdk.models.composite_sequence_arg import CompositeSequenceArg
from gemmapy.sdk.models.composite_sequence_value_object import CompositeSequenceValueObject
from gemmapy.sdk.models.compound import Compound
from gemmapy.sdk.models.contact import Contact
from gemmapy.sdk.models.contrast_result_value_object import ContrastResultValueObject
from gemmapy.sdk.models.curation_details import CurationDetails
from gemmapy.sdk.models.database_entry import DatabaseEntry
from gemmapy.sdk.models.database_entry_arg import DatabaseEntryArg
from gemmapy.sdk.models.database_entry_value_object import DatabaseEntryValueObject
from gemmapy.sdk.models.database_type import DatabaseType
from gemmapy.sdk.models.dataset import Dataset
from gemmapy.sdk.models.dataset1 import Dataset1
from gemmapy.sdk.models.dataset2 import Dataset2
from gemmapy.sdk.models.dataset3 import Dataset3
from gemmapy.sdk.models.dataset4 import Dataset4
from gemmapy.sdk.models.dataset5 import Dataset5
from gemmapy.sdk.models.dataset6 import Dataset6
from gemmapy.sdk.models.dataset7 import Dataset7
from gemmapy.sdk.models.dataset8 import Dataset8
from gemmapy.sdk.models.dataset_arg import DatasetArg
from gemmapy.sdk.models.diff_ex_result_set_summary_value_object import DiffExResultSetSummaryValueObject
from gemmapy.sdk.models.differential_expression_analysis_result_value_object import DifferentialExpressionAnalysisResultValueObject
from gemmapy.sdk.models.differential_expression_analysis_value_object import DifferentialExpressionAnalysisValueObject
from gemmapy.sdk.models.double_matrix_long_integer import DoubleMatrixLongInteger
from gemmapy.sdk.models.experiment_expression_levels_value_object import ExperimentExpressionLevelsValueObject
from gemmapy.sdk.models.experimental_factor_value_object import ExperimentalFactorValueObject
from gemmapy.sdk.models.expression_analysis_result_set_value_object import ExpressionAnalysisResultSetValueObject
from gemmapy.sdk.models.expression_experiment_value_object import ExpressionExperimentValueObject
from gemmapy.sdk.models.external_database import ExternalDatabase
from gemmapy.sdk.models.external_database_value_object import ExternalDatabaseValueObject
from gemmapy.sdk.models.factor_value_basic_value_object import FactorValueBasicValueObject
from gemmapy.sdk.models.factor_value_value_object import FactorValueValueObject
from gemmapy.sdk.models.go_evidence_code import GOEvidenceCode
from gemmapy.sdk.models.geeq_value_object import GeeqValueObject
from gemmapy.sdk.models.gene import Gene
from gemmapy.sdk.models.gene1 import Gene1
from gemmapy.sdk.models.gene2 import Gene2
from gemmapy.sdk.models.gene3 import Gene3
from gemmapy.sdk.models.gene4 import Gene4
from gemmapy.sdk.models.gene5 import Gene5
from gemmapy.sdk.models.gene_alias import GeneAlias
from gemmapy.sdk.models.gene_arg import GeneArg
from gemmapy.sdk.models.gene_element_expressions_value_object import GeneElementExpressionsValueObject
from gemmapy.sdk.models.gene_mapping_summary import GeneMappingSummary
from gemmapy.sdk.models.gene_ontology_term_value_object import GeneOntologyTermValueObject
from gemmapy.sdk.models.gene_product import GeneProduct
from gemmapy.sdk.models.gene_product_value_object import GeneProductValueObject
from gemmapy.sdk.models.gene_set_value_object import GeneSetValueObject
from gemmapy.sdk.models.gene_value_object import GeneValueObject
from gemmapy.sdk.models.general_type import GeneralType
from gemmapy.sdk.models.identifiable_value_object import IdentifiableValueObject
from gemmapy.sdk.models.identifiable_value_object_identifiable import IdentifiableValueObjectIdentifiable
from gemmapy.sdk.models.job_info import JobInfo
from gemmapy.sdk.models.keyword import Keyword
from gemmapy.sdk.models.measurement_value_object import MeasurementValueObject
from gemmapy.sdk.models.medical_subject_heading import MedicalSubjectHeading
from gemmapy.sdk.models.model_with import ModelWith
from gemmapy.sdk.models.multifunctionality import Multifunctionality
from gemmapy.sdk.models.one_of_composite_sequence_arg import OneOfCompositeSequenceArg
from gemmapy.sdk.models.one_of_database_entry_arg import OneOfDatabaseEntryArg
from gemmapy.sdk.models.one_of_dataset_arg import OneOfDatasetArg
from gemmapy.sdk.models.one_of_gene_arg import OneOfGeneArg
from gemmapy.sdk.models.one_of_platform_arg import OneOfPlatformArg
from gemmapy.sdk.models.one_of_taxon_arg import OneOfTaxonArg
from gemmapy.sdk.models.one_of_with import OneOfWith
from gemmapy.sdk.models.one_ofdataset import OneOfdataset
from gemmapy.sdk.models.one_ofdataset1 import OneOfdataset1
from gemmapy.sdk.models.one_ofdataset2 import OneOfdataset2
from gemmapy.sdk.models.one_ofdataset3 import OneOfdataset3
from gemmapy.sdk.models.one_ofdataset4 import OneOfdataset4
from gemmapy.sdk.models.one_ofdataset5 import OneOfdataset5
from gemmapy.sdk.models.one_ofdataset6 import OneOfdataset6
from gemmapy.sdk.models.one_ofdataset7 import OneOfdataset7
from gemmapy.sdk.models.one_ofdataset8 import OneOfdataset8
from gemmapy.sdk.models.one_ofgene import OneOfgene
from gemmapy.sdk.models.one_ofgene1 import OneOfgene1
from gemmapy.sdk.models.one_ofgene2 import OneOfgene2
from gemmapy.sdk.models.one_ofgene3 import OneOfgene3
from gemmapy.sdk.models.one_ofgene4 import OneOfgene4
from gemmapy.sdk.models.one_ofgene5 import OneOfgene5
from gemmapy.sdk.models.one_ofplatform import OneOfplatform
from gemmapy.sdk.models.one_ofplatform1 import OneOfplatform1
from gemmapy.sdk.models.one_ofplatform2 import OneOfplatform2
from gemmapy.sdk.models.one_ofplatform3 import OneOfplatform3
from gemmapy.sdk.models.one_ofplatform4 import OneOfplatform4
from gemmapy.sdk.models.one_ofplatform5 import OneOfplatform5
from gemmapy.sdk.models.one_ofprobe import OneOfprobe
from gemmapy.sdk.models.one_oftaxon import OneOftaxon
from gemmapy.sdk.models.one_oftaxon1 import OneOftaxon1
from gemmapy.sdk.models.one_oftaxon2 import OneOftaxon2
from gemmapy.sdk.models.one_oftaxon3 import OneOftaxon3
from gemmapy.sdk.models.one_oftaxon4 import OneOftaxon4
from gemmapy.sdk.models.one_oftaxon5 import OneOftaxon5
from gemmapy.sdk.models.paginated_response_data_object_array_design_value_object import PaginatedResponseDataObjectArrayDesignValueObject
from gemmapy.sdk.models.paginated_response_data_object_composite_sequence_value_object import PaginatedResponseDataObjectCompositeSequenceValueObject
from gemmapy.sdk.models.paginated_response_data_object_expression_analysis_result_set_value_object import PaginatedResponseDataObjectExpressionAnalysisResultSetValueObject
from gemmapy.sdk.models.paginated_response_data_object_expression_experiment_value_object import PaginatedResponseDataObjectExpressionExperimentValueObject
from gemmapy.sdk.models.paginated_response_data_object_gene_value_object import PaginatedResponseDataObjectGeneValueObject
from gemmapy.sdk.models.phenotype_association import PhenotypeAssociation
from gemmapy.sdk.models.phenotype_association_publication import PhenotypeAssociationPublication
from gemmapy.sdk.models.phenotype_mapping_type import PhenotypeMappingType
from gemmapy.sdk.models.physical_location import PhysicalLocation
from gemmapy.sdk.models.physical_location_value_object import PhysicalLocationValueObject
from gemmapy.sdk.models.platform import Platform
from gemmapy.sdk.models.platform1 import Platform1
from gemmapy.sdk.models.platform2 import Platform2
from gemmapy.sdk.models.platform3 import Platform3
from gemmapy.sdk.models.platform4 import Platform4
from gemmapy.sdk.models.platform5 import Platform5
from gemmapy.sdk.models.platform_arg import PlatformArg
from gemmapy.sdk.models.polymer_type import PolymerType
from gemmapy.sdk.models.primitive_type import PrimitiveType
from gemmapy.sdk.models.probe import Probe
from gemmapy.sdk.models.protocol import Protocol
from gemmapy.sdk.models.quantitation_type import QuantitationType
from gemmapy.sdk.models.response_data_object_api_info_value_object import ResponseDataObjectApiInfoValueObject
from gemmapy.sdk.models.response_data_object_expression_analysis_result_set_value_object import ResponseDataObjectExpressionAnalysisResultSetValueObject
from gemmapy.sdk.models.response_data_object_list_annotation_search_result_value_object import ResponseDataObjectListAnnotationSearchResultValueObject
from gemmapy.sdk.models.response_data_object_list_array_design_value_object import ResponseDataObjectListArrayDesignValueObject
from gemmapy.sdk.models.response_data_object_list_bio_assay_value_object import ResponseDataObjectListBioAssayValueObject
from gemmapy.sdk.models.response_data_object_list_coexpression_value_object_ext import ResponseDataObjectListCoexpressionValueObjectExt
from gemmapy.sdk.models.response_data_object_list_differential_expression_analysis_value_object import ResponseDataObjectListDifferentialExpressionAnalysisValueObject
from gemmapy.sdk.models.response_data_object_list_experiment_expression_levels_value_object import ResponseDataObjectListExperimentExpressionLevelsValueObject
from gemmapy.sdk.models.response_data_object_list_gene_ontology_term_value_object import ResponseDataObjectListGeneOntologyTermValueObject
from gemmapy.sdk.models.response_data_object_list_gene_value_object import ResponseDataObjectListGeneValueObject
from gemmapy.sdk.models.response_data_object_list_physical_location_value_object import ResponseDataObjectListPhysicalLocationValueObject
from gemmapy.sdk.models.response_data_object_list_taxon_value_object import ResponseDataObjectListTaxonValueObject
from gemmapy.sdk.models.response_data_object_set_annotation_value_object import ResponseDataObjectSetAnnotationValueObject
from gemmapy.sdk.models.response_data_object_simple_svd_value_object import ResponseDataObjectSimpleSVDValueObject
from gemmapy.sdk.models.response_error_object import ResponseErrorObject
from gemmapy.sdk.models.scale_type import ScaleType
from gemmapy.sdk.models.search_result_type import SearchResultType
from gemmapy.sdk.models.search_result_value_object import SearchResultValueObject
from gemmapy.sdk.models.search_results_response_data_object import SearchResultsResponseDataObject
from gemmapy.sdk.models.search_settings_value_object import SearchSettingsValueObject
from gemmapy.sdk.models.sequence_type import SequenceType
from gemmapy.sdk.models.simple_svd_value_object import SimpleSVDValueObject
from gemmapy.sdk.models.sort_value_object import SortValueObject
from gemmapy.sdk.models.standard_quantitation_type import StandardQuantitationType
from gemmapy.sdk.models.taxon import Taxon
from gemmapy.sdk.models.taxon1 import Taxon1
from gemmapy.sdk.models.taxon2 import Taxon2
from gemmapy.sdk.models.taxon3 import Taxon3
from gemmapy.sdk.models.taxon4 import Taxon4
from gemmapy.sdk.models.taxon5 import Taxon5
from gemmapy.sdk.models.taxon_arg import TaxonArg
from gemmapy.sdk.models.taxon_value_object import TaxonValueObject
from gemmapy.sdk.models.technology_type import TechnologyType
from gemmapy.sdk.models.three_prime_distance_method import ThreePrimeDistanceMethod
from gemmapy.sdk.models.user import User
from gemmapy.sdk.models.vector_element_value_object import VectorElementValueObject
from gemmapy.sdk.models.well_composed_error_body import WellComposedErrorBody