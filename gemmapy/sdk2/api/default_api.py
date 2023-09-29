# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  ## Updates  ### Update 2.7.1  - improved highlights of search results - fix the limit for getDatasetsAnnotations() endpoint to 5000 in the specification - fix missing initialization of datasets retrieved from the cache  Highlights now use Markdown syntax for formatting. Fields for highlighted ontology terms now use complete object path instead of just `term`. Last but not least, highlights from multiple results are merged.  ### Update 2.7.0  New endpoints for counting the number of results: `getNumberOfDatasets`, `getNumberOfPlatforms`, `getNumberOfResultSets`. These endpoints are faster than looking up `totalElements` as no data is retrieved or converted.  Datasets can now be filtered by annotations at the sample, factor value and all levels using the three newly exposed `experimentalDesign.experimentalFactors.factorValues.characteristics`, `bioAssays.sampleUsed.characteristics` and `allCharacteristics` collections. The two useful available properties for filtering are `value` and `valueUri`.  New `getDatasetsAnnotationsUsageStatistics`, `getDatasetsPlatformsUsageStatistics` and `getDatasetsTaxaUsageStatistics` endpoints for retrieving annotations, platforms and taxa used by the matched datasets. The endpoint accepts the same `filter` argument of `getDatasets`, allowing one to easily navigate terms, platforms and taxa available for filtering furthermore.  Properties available for filtering and sorting are enumerated in the description of the corresponding parameter. There's been a number of fixes and additional tests performed to ensure that all advertised properties are working as expected.  The `FilterArg` and `SortArg`-based parameters now have OpenAPI extensions to enumerate available properties in a structured format under the `x-gemma-filterable-properties`key. Possible values are exposed for enumerated types.  ```yaml x-gemma-filterable-properties: - name: technologyType   type: string   allowedValues:   - value: ONECOLOR     label: One Color   - value: SEQUENCING     label: Sequencing   security:     basicAuth: [GROUP_ADMIN]     cookieAuth: [GROUP_ADMIN] ```  Some of the exposed properties such as `geeq.publicSuitabilityScore` require specific authorities to use. This is documented in `x-filterable-properties` by specifying a [Security Requirement Object](https://spec.openapis.org/oas/latest.html#security-requirement-object).  Types that use the `[]` suffix are using sub-queries under the hood. It implies that the entity will be matched if at least one related entity matches the supplied filter. For example, the `characteristics.valueUri = http://purl.obolibrary.org/obo/UBERON_0002107` filter will match datasets with at least one `UBERON:0002107` tag attached.  Filtered endpoints (including paginated and limited ones) now expose a `groupBy` array that enumerates all the properties used to group results. This helps clear confusion about what constitute a business key in the returned response.  ### Update 2.6.1  Add support for filtering platforms by taxon ID, common name, scientific name, etc. for the `/platforms` endpoint.  ### Update 2.6.0  Add a new `externalDatabases` attribute to the main endpoint that displays version of some of the main external databases that we are using. This exposes versions and last updates for genomes, gene annotations, GO terms, and much more!  The `ExternalDatabaseValueObject` now exposes a `description` which provides additional details.  ### Update 2.5.2  Restore `factors` in `BioMaterialValueObject` as it is being still used by our RNA-Seq pipeline. The attribute is deprecated and should not be used and will be removed when we find a suitable alternative.  Introduce a new endpoint to retrieve quantitation types for a given dataset and parameters to retrieve expression data by quantitation type to `getDatasetProcessedExpression` and `getDatasetRawExpression`. As it was too difficult to extends `getDatasetExpression` to also support quantitation type while retaining the filter feature, we decided to deprecate it and reintroduce filtering for both raw and processed expression in the future.  Fix return type for `getResultSets` which was incorrectly referring to a renamed VO.  Annotate all possible types for `SearchResult.resultObject`. This incidentally includes the `GeneSetValueObject` in the specification which is not exposed elsewhere in the API.  ### Update 2.5.1  Restore `objectClass` visibility in `AnnotationValueObject`.  Fix incorrect response types for annotations search endpoints returning datasets.  ### Update 2.5.0  Major cleanups were performed in this release in order to stabilize the specification. Numerous properties from Gemma Web that were never intended to be exposed in Gemma REST have been hidden. It's a bit too much to describe in here, but you can navigate to the schemas section below to get a good glance at the models.  Favour `numberOfSomething` instead of `somethingCount` which is clearer. The older names are kept for backward-compatibility, but should be considered deprecated.  Gene aliases and multifunctionality rank are now filled in `GeneValueObject`.  Uniformly use `TaxonValueObject` to represent taxon. This is breaking change for the `ExpressionExperimentValueObject` and `ArrayDesignValueObject` as their `taxon` property will be an `object` instead of a `string`. Properties such as `taxonId` are now deprecated and `taxon.id` should be used instead.  Entities that have IDs now all inherit from `IdentifiableValueObject`. This implies that you can assume the presence of an `id` in a search result `resultObject` attribute for example.  New `/search` endpoint! for an unified search experience. Annotation-based search endpoints under `/annotations` are now deprecated.  New API docs! While not as nice looking, the previous theme will be gradually ported to Swagger UI as we focused on functionality over prettiness for this release.  ### Update 2.4.0 through 2.4.1  Release notes for the 2.4 series were not written down, so I'll try to do my best to recall features that were introduced at that time.  An [OpenAPI](https://www.openapis.org/) specification was introduced and available under `/rest/v2/openapi.json`, although not fully stabilized.  Add a `/resultSets` endpoint to navigate result sets directly, by ID or by dataset.  Add a `/resultSets/{resultSetId}` endpoint to retrieve a specific result set by its ID. This endpoint can be negotiated with an `Accept: text/tab-separated-values` header to obtain a TSV representation.  Add a `/datasets/{dataset}/analyses/differential/resultSets` endpoint that essentially redirect to a specific `/resultSet` endpoint by dataset ID.  Add an endpoint to retrieve preferred raw expression vectors.  ### Update 2.3.4  November 6th, 2018  November 6th [2.3.4] Bug fixes in the dataset search endpoint.  November 5th [2.3.3] Added filtering parameters to dataset search.  October 25th [2.3.2] Changed behavior of the dataset search endpoint to more closely match the Gemma web interface.  October 2nd [2.3.1] Added group information to the User value object.  September 27th [2.3.0] Breaking change in Taxa: Abbreviation property has been removed and is therefore no longer an accepted identifier.  ### Update 2.2.6  June 7th, 2018  Code maintenance, bug fixes. Geeq scores stable and made public.  June 7th [2.2.6] Added: User authentication endpoint.  May 2nd [2.2.5] Fixed: Cleaned up and optimized platforms/elements endpoint, removed redundant information (recursive properties nesting).  April 12th [2.2.3] Fixed: Array arguments not handling non-string properties properly, e.g. `ncbiIds` of genes.  April 9th [2.2.1] Fixed: Filter argument not working when the filtered field was a primitive type. This most significantly allows filtering by geeq boolean and double properties.  ### Update 2.2.0  February 8th, 2018  Breaking change in the 'Dataset differential analysis' endpoint: - No longer using `qValueThreshold` parameter. - Response format changed, now using `DifferentialExpressionAnalysisValueObject` instead of `DifferentialExpressionValueObject` - [Experimental] Added Geeq (Gene Expression Experiment Quality) scores to the dataset value objects 

    The version of the OpenAPI document: 2.7.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr, conint, conlist, constr, validator

from typing import Any, Optional, Union

from gemmapy.sdk2.models.filtered_and_paginated_response_data_object_array_design_value_object import FilteredAndPaginatedResponseDataObjectArrayDesignValueObject
from gemmapy.sdk2.models.filtered_and_paginated_response_data_object_composite_sequence_value_object import FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject
from gemmapy.sdk2.models.filtered_and_paginated_response_data_object_differential_expression_analysis_result_set_value_object import FilteredAndPaginatedResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject
from gemmapy.sdk2.models.filtered_and_paginated_response_data_object_expression_experiment_value_object import FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
from gemmapy.sdk2.models.filtered_and_paginated_response_data_object_gene_value_object import FilteredAndPaginatedResponseDataObjectGeneValueObject
from gemmapy.sdk2.models.get_dataset_expression_for_genes_genes_parameter_inner import GetDatasetExpressionForGenesGenesParameterInner
from gemmapy.sdk2.models.get_platform_annotations_platform_parameter import GetPlatformAnnotationsPlatformParameter
from gemmapy.sdk2.models.get_platform_element_probes_parameter_inner import GetPlatformElementProbesParameterInner
from gemmapy.sdk2.models.get_result_sets_database_entries_parameter_inner import GetResultSetsDatabaseEntriesParameterInner
from gemmapy.sdk2.models.get_result_sets_datasets_parameter_inner import GetResultSetsDatasetsParameterInner
from gemmapy.sdk2.models.limited_response_data_object_annotation_with_usage_statistics_value_object import LimitedResponseDataObjectAnnotationWithUsageStatisticsValueObject
from gemmapy.sdk2.models.limited_response_data_object_array_design_with_usage_statistics_value_object import LimitedResponseDataObjectArrayDesignWithUsageStatisticsValueObject
from gemmapy.sdk2.models.paginated_response_data_object_composite_sequence_value_object import PaginatedResponseDataObjectCompositeSequenceValueObject
from gemmapy.sdk2.models.paginated_response_data_object_expression_experiment_value_object import PaginatedResponseDataObjectExpressionExperimentValueObject
from gemmapy.sdk2.models.queried_and_filtered_and_paginated_response_data_object_expression_experiment_with_search_result_value_object import QueriedAndFilteredAndPaginatedResponseDataObjectExpressionExperimentWithSearchResultValueObject
from gemmapy.sdk2.models.queried_and_filtered_response_data_object_category_with_usage_statistics_value_object import QueriedAndFilteredResponseDataObjectCategoryWithUsageStatisticsValueObject
from gemmapy.sdk2.models.queried_and_filtered_response_data_object_taxon_with_usage_statistics_value_object import QueriedAndFilteredResponseDataObjectTaxonWithUsageStatisticsValueObject
from gemmapy.sdk2.models.response_data_object_api_info_value_object import ResponseDataObjectApiInfoValueObject
from gemmapy.sdk2.models.response_data_object_differential_expression_analysis_result_set_value_object import ResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject
from gemmapy.sdk2.models.response_data_object_list_annotation_search_result_value_object import ResponseDataObjectListAnnotationSearchResultValueObject
from gemmapy.sdk2.models.response_data_object_list_array_design_value_object import ResponseDataObjectListArrayDesignValueObject
from gemmapy.sdk2.models.response_data_object_list_bio_assay_value_object import ResponseDataObjectListBioAssayValueObject
from gemmapy.sdk2.models.response_data_object_list_differential_expression_analysis_value_object import ResponseDataObjectListDifferentialExpressionAnalysisValueObject
from gemmapy.sdk2.models.response_data_object_list_experiment_expression_levels_value_object import ResponseDataObjectListExperimentExpressionLevelsValueObject
from gemmapy.sdk2.models.response_data_object_list_gene_ontology_term_value_object import ResponseDataObjectListGeneOntologyTermValueObject
from gemmapy.sdk2.models.response_data_object_list_gene_value_object import ResponseDataObjectListGeneValueObject
from gemmapy.sdk2.models.response_data_object_list_physical_location_value_object import ResponseDataObjectListPhysicalLocationValueObject
from gemmapy.sdk2.models.response_data_object_list_taxon_value_object import ResponseDataObjectListTaxonValueObject
from gemmapy.sdk2.models.response_data_object_long import ResponseDataObjectLong
from gemmapy.sdk2.models.response_data_object_set_annotation_value_object import ResponseDataObjectSetAnnotationValueObject
from gemmapy.sdk2.models.response_data_object_set_quantitation_type_value_object import ResponseDataObjectSetQuantitationTypeValueObject
from gemmapy.sdk2.models.response_data_object_simple_svd_value_object import ResponseDataObjectSimpleSVDValueObject
from gemmapy.sdk2.models.search_results_response_data_object import SearchResultsResponseDataObject
from gemmapy.sdk2.models.search_taxon_datasets_taxon_parameter import SearchTaxonDatasetsTaxonParameter

from gemmapy.sdk2.api_client import ApiClient
from gemmapy.sdk2.api_response import ApiResponse
from gemmapy.sdk2.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_api_info(self, **kwargs) -> ResponseDataObjectApiInfoValueObject:  # noqa: E501
        """Retrieve an object with basic API information  # noqa: E501

        The payload contains a list of featured external databases that Gemma uses under the `externalDatabases` field. Those are mainly genomic references and sources of gene annotations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_api_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectApiInfoValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_api_info_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_api_info_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_api_info_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve an object with basic API information  # noqa: E501

        The payload contains a list of featured external databases that Gemma uses under the `externalDatabases` field. Those are mainly genomic references and sources of gene annotations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_api_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectApiInfoValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_info" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_annotations(self, dataset : Any, **kwargs) -> ResponseDataObjectSetAnnotationValueObject:  # noqa: E501
        """Retrieve the annotations of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_annotations(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectSetAnnotationValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_annotations_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_annotations_with_http_info(dataset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_annotations_with_http_info(self, dataset : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the annotations of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_annotations_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectSetAnnotationValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'dataset'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_annotations" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "ResponseDataObjectSetAnnotationValueObject",
            '404': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/datasets/{dataset}/annotations', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_design(self, dataset : Any, **kwargs) -> bytearray:  # noqa: E501
        """Retrieve the design of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_design(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_design_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_design_with_http_info(dataset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_design_with_http_info(self, dataset : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the design of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_design_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'dataset'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_design" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
            '404': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/datasets/{dataset}/design', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_differential_expression(self, datasets : conlist(GetResultSetsDatasetsParameterInner), diff_ex_set : Optional[StrictInt] = None, threshold : Optional[Union[StrictFloat, StrictInt]] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, keep_non_specific : Optional[StrictBool] = None, consolidate : Optional[StrictStr] = None, **kwargs) -> ResponseDataObjectListExperimentExpressionLevelsValueObject:  # noqa: E501
        """Retrieve the expression levels of a set of datasets subject to a threshold on their differential expressions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression(datasets, diff_ex_set, threshold, limit, keep_non_specific, consolidate, async_req=True)
        >>> result = thread.get()

        :param datasets: (required)
        :type datasets: List[GetResultSetsDatasetsParameterInner]
        :param diff_ex_set:
        :type diff_ex_set: int
        :param threshold:
        :type threshold: float
        :param limit:
        :type limit: int
        :param keep_non_specific:
        :type keep_non_specific: bool
        :param consolidate:
        :type consolidate: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListExperimentExpressionLevelsValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_differential_expression_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_differential_expression_with_http_info(datasets, diff_ex_set, threshold, limit, keep_non_specific, consolidate, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_differential_expression_with_http_info(self, datasets : conlist(GetResultSetsDatasetsParameterInner), diff_ex_set : Optional[StrictInt] = None, threshold : Optional[Union[StrictFloat, StrictInt]] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, keep_non_specific : Optional[StrictBool] = None, consolidate : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the expression levels of a set of datasets subject to a threshold on their differential expressions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression_with_http_info(datasets, diff_ex_set, threshold, limit, keep_non_specific, consolidate, async_req=True)
        >>> result = thread.get()

        :param datasets: (required)
        :type datasets: List[GetResultSetsDatasetsParameterInner]
        :param diff_ex_set:
        :type diff_ex_set: int
        :param threshold:
        :type threshold: float
        :param limit:
        :type limit: int
        :param keep_non_specific:
        :type keep_non_specific: bool
        :param consolidate:
        :type consolidate: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListExperimentExpressionLevelsValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'datasets',
            'diff_ex_set',
            'threshold',
            'limit',
            'keep_non_specific',
            'consolidate'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_differential_expression" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['datasets']:
            _path_params['datasets'] = _params['datasets']
            _collection_formats['datasets'] = 'csv'


        # process the query parameters
        _query_params = []
        if _params.get('diff_ex_set') is not None:  # noqa: E501
            _query_params.append(('diffExSet', _params['diff_ex_set']))

        if _params.get('threshold') is not None:  # noqa: E501
            _query_params.append(('threshold', _params['threshold']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('keep_non_specific') is not None:  # noqa: E501
            _query_params.append(('keepNonSpecific', _params['keep_non_specific']))

        if _params.get('consolidate') is not None:  # noqa: E501
            _query_params.append(('consolidate', _params['consolidate']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/datasets/{datasets}/expressions/differential', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_differential_expression_analyses(self, dataset : Any, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> ResponseDataObjectListDifferentialExpressionAnalysisValueObject:  # noqa: E501
        """Retrieve annotations and surface level stats for a dataset's differential analyses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression_analyses(dataset, offset, limit, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListDifferentialExpressionAnalysisValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_differential_expression_analyses_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_differential_expression_analyses_with_http_info(dataset, offset, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_differential_expression_analyses_with_http_info(self, dataset : Any, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve annotations and surface level stats for a dataset's differential analyses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression_analyses_with_http_info(dataset, offset, limit, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListDifferentialExpressionAnalysisValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'dataset',
            'offset',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_differential_expression_analyses" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']


        # process the query parameters
        _query_params = []
        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "ResponseDataObjectListDifferentialExpressionAnalysisValueObject",
            '404': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/datasets/{dataset}/analyses/differential', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_differential_expression_analyses_result_sets(self, dataset : Any, **kwargs) -> None:  # noqa: E501
        """Retrieve the result sets of all differential analyses of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression_analyses_result_sets(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_differential_expression_analyses_result_sets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_differential_expression_analyses_result_sets_with_http_info(dataset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_differential_expression_analyses_result_sets_with_http_info(self, dataset : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the result sets of all differential analyses of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression_analyses_result_sets_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'dataset'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_differential_expression_analyses_result_sets" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/datasets/{dataset}/analyses/differential/resultSets', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_expression(self, dataset : Any, filter : Optional[StrictBool] = None, **kwargs) -> bytearray:  # noqa: E501
        """(Deprecated) Retrieve processed expression data of a dataset  # noqa: E501

        This endpoint is deprecated and getDatasetProcessedExpression() should be used instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression(dataset, filter, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param filter:
        :type filter: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_expression_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_expression_with_http_info(dataset, filter, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_expression_with_http_info(self, dataset : Any, filter : Optional[StrictBool] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """(Deprecated) Retrieve processed expression data of a dataset  # noqa: E501

        This endpoint is deprecated and getDatasetProcessedExpression() should be used instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression_with_http_info(dataset, filter, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param filter:
        :type filter: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        warnings.warn("GET /datasets/{dataset}/data is deprecated.", DeprecationWarning)

        _params = locals()

        _all_params = [
            'dataset',
            'filter'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_expression" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']


        # process the query parameters
        _query_params = []
        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
            '204': None,
            '404': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/datasets/{dataset}/data', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_expression_for_genes(self, datasets : conlist(GetResultSetsDatasetsParameterInner), genes : conlist(GetDatasetExpressionForGenesGenesParameterInner), keep_non_specific : Optional[StrictBool] = None, consolidate : Optional[StrictStr] = None, **kwargs) -> ResponseDataObjectListExperimentExpressionLevelsValueObject:  # noqa: E501
        """Retrieve the expression data matrix of a set of datasets and genes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression_for_genes(datasets, genes, keep_non_specific, consolidate, async_req=True)
        >>> result = thread.get()

        :param datasets: (required)
        :type datasets: List[GetResultSetsDatasetsParameterInner]
        :param genes: (required)
        :type genes: List[GetDatasetExpressionForGenesGenesParameterInner]
        :param keep_non_specific:
        :type keep_non_specific: bool
        :param consolidate:
        :type consolidate: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListExperimentExpressionLevelsValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_expression_for_genes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_expression_for_genes_with_http_info(datasets, genes, keep_non_specific, consolidate, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_expression_for_genes_with_http_info(self, datasets : conlist(GetResultSetsDatasetsParameterInner), genes : conlist(GetDatasetExpressionForGenesGenesParameterInner), keep_non_specific : Optional[StrictBool] = None, consolidate : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the expression data matrix of a set of datasets and genes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression_for_genes_with_http_info(datasets, genes, keep_non_specific, consolidate, async_req=True)
        >>> result = thread.get()

        :param datasets: (required)
        :type datasets: List[GetResultSetsDatasetsParameterInner]
        :param genes: (required)
        :type genes: List[GetDatasetExpressionForGenesGenesParameterInner]
        :param keep_non_specific:
        :type keep_non_specific: bool
        :param consolidate:
        :type consolidate: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListExperimentExpressionLevelsValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'datasets',
            'genes',
            'keep_non_specific',
            'consolidate'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_expression_for_genes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['datasets']:
            _path_params['datasets'] = _params['datasets']
            _collection_formats['datasets'] = 'csv'

        if _params['genes']:
            _path_params['genes'] = _params['genes']
            _collection_formats['genes'] = 'csv'


        # process the query parameters
        _query_params = []
        if _params.get('keep_non_specific') is not None:  # noqa: E501
            _query_params.append(('keepNonSpecific', _params['keep_non_specific']))

        if _params.get('consolidate') is not None:  # noqa: E501
            _query_params.append(('consolidate', _params['consolidate']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/datasets/{datasets}/expressions/genes/{genes}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_expression_pca(self, datasets : conlist(GetResultSetsDatasetsParameterInner), component : Optional[StrictInt] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, keep_non_specific : Optional[StrictBool] = None, consolidate : Optional[StrictStr] = None, **kwargs) -> ResponseDataObjectListExperimentExpressionLevelsValueObject:  # noqa: E501
        """Retrieve the principal components (PCA) of a set of datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression_pca(datasets, component, limit, keep_non_specific, consolidate, async_req=True)
        >>> result = thread.get()

        :param datasets: (required)
        :type datasets: List[GetResultSetsDatasetsParameterInner]
        :param component:
        :type component: int
        :param limit:
        :type limit: int
        :param keep_non_specific:
        :type keep_non_specific: bool
        :param consolidate:
        :type consolidate: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListExperimentExpressionLevelsValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_expression_pca_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_expression_pca_with_http_info(datasets, component, limit, keep_non_specific, consolidate, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_expression_pca_with_http_info(self, datasets : conlist(GetResultSetsDatasetsParameterInner), component : Optional[StrictInt] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, keep_non_specific : Optional[StrictBool] = None, consolidate : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the principal components (PCA) of a set of datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression_pca_with_http_info(datasets, component, limit, keep_non_specific, consolidate, async_req=True)
        >>> result = thread.get()

        :param datasets: (required)
        :type datasets: List[GetResultSetsDatasetsParameterInner]
        :param component:
        :type component: int
        :param limit:
        :type limit: int
        :param keep_non_specific:
        :type keep_non_specific: bool
        :param consolidate:
        :type consolidate: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListExperimentExpressionLevelsValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'datasets',
            'component',
            'limit',
            'keep_non_specific',
            'consolidate'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_expression_pca" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['datasets']:
            _path_params['datasets'] = _params['datasets']
            _collection_formats['datasets'] = 'csv'


        # process the query parameters
        _query_params = []
        if _params.get('component') is not None:  # noqa: E501
            _query_params.append(('component', _params['component']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('keep_non_specific') is not None:  # noqa: E501
            _query_params.append(('keepNonSpecific', _params['keep_non_specific']))

        if _params.get('consolidate') is not None:  # noqa: E501
            _query_params.append(('consolidate', _params['consolidate']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/datasets/{datasets}/expressions/pca', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_platforms(self, dataset : Any, **kwargs) -> ResponseDataObjectListArrayDesignValueObject:  # noqa: E501
        """Retrieve the platforms of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_platforms(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListArrayDesignValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_platforms_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_platforms_with_http_info(dataset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_platforms_with_http_info(self, dataset : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the platforms of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_platforms_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListArrayDesignValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'dataset'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_platforms" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "ResponseDataObjectListArrayDesignValueObject",
            '404': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/datasets/{dataset}/platforms', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_processed_expression(self, dataset : Any, **kwargs) -> bytearray:  # noqa: E501
        """Retrieve processed expression data of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_processed_expression(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_processed_expression_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_processed_expression_with_http_info(dataset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_processed_expression_with_http_info(self, dataset : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve processed expression data of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_processed_expression_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'dataset'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_processed_expression" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
            '404': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/datasets/{dataset}/data/processed', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_quantitation_types(self, dataset : Any, **kwargs) -> ResponseDataObjectSetQuantitationTypeValueObject:  # noqa: E501
        """Retrieve quantitation types of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_quantitation_types(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectSetQuantitationTypeValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_quantitation_types_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_quantitation_types_with_http_info(dataset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_quantitation_types_with_http_info(self, dataset : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve quantitation types of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_quantitation_types_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectSetQuantitationTypeValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'dataset'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_quantitation_types" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/datasets/{dataset}/quantitationTypes', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_raw_expression(self, dataset : Any, quantitation_type : Optional[Any] = None, **kwargs) -> bytearray:  # noqa: E501
        """Retrieve raw expression data of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_raw_expression(dataset, quantitation_type, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param quantitation_type:
        :type quantitation_type: GetDatasetRawExpressionQuantitationTypeParameter
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_raw_expression_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_raw_expression_with_http_info(dataset, quantitation_type, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_raw_expression_with_http_info(self, dataset : Any, quantitation_type : Optional[Any] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve raw expression data of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_raw_expression_with_http_info(dataset, quantitation_type, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param quantitation_type:
        :type quantitation_type: GetDatasetRawExpressionQuantitationTypeParameter
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'dataset',
            'quantitation_type'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_raw_expression" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']


        # process the query parameters
        _query_params = []
        if _params.get('quantitation_type') is not None:  # noqa: E501
            _query_params.append(('quantitationType', _params['quantitation_type']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
            '404': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/datasets/{dataset}/data/raw', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_samples(self, dataset : Any, **kwargs) -> ResponseDataObjectListBioAssayValueObject:  # noqa: E501
        """Retrieve the samples of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_samples(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListBioAssayValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_samples_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_samples_with_http_info(dataset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_samples_with_http_info(self, dataset : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the samples of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_samples_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListBioAssayValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'dataset'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_samples" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "ResponseDataObjectListBioAssayValueObject",
            '404': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/datasets/{dataset}/samples', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_dataset_svd(self, dataset : Any, **kwargs) -> ResponseDataObjectSimpleSVDValueObject:  # noqa: E501
        """Retrieve the singular value decomposition (SVD) of a dataset expression data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_svd(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectSimpleSVDValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_dataset_svd_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_dataset_svd_with_http_info(dataset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dataset_svd_with_http_info(self, dataset : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the singular value decomposition (SVD) of a dataset expression data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_svd_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: GetResultSetsDatasetsParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectSimpleSVDValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'dataset'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_svd" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "ResponseDataObjectSimpleSVDValueObject",
            '404': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/datasets/{dataset}/svd', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_datasets(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> QueriedAndFilteredAndPaginatedResponseDataObjectExpressionExperimentWithSearchResultValueObject:  # noqa: E501
        """Retrieve all datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets(query, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: QueriedAndFilteredAndPaginatedResponseDataObjectExpressionExperimentWithSearchResultValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_datasets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_datasets_with_http_info(query, filter, offset, limit, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def get_datasets_with_http_info(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve all datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_with_http_info(query, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(QueriedAndFilteredAndPaginatedResponseDataObjectExpressionExperimentWithSearchResultValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query',
            'filter',
            'offset',
            'limit',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/datasets', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_datasets_annotations_usage_statistics(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, exclude : Annotated[Optional[conlist(StrictStr, min_items=1, unique_items=True)], Field(description="List of fields to exclude from the payload. Only `parentTerms` can be excluded.")] = None, limit : Annotated[Optional[conint(strict=True, le=5000, ge=1)], Field(description="Maximum number of annotations to returned; capped at 5000.")] = None, min_frequency : Annotated[Optional[StrictInt], Field(description="Minimum number of associated datasets to report an annotation. If used, the limit will default to 5000.")] = None, category : Annotated[Optional[StrictStr], Field(description="A category URI to restrict reported annotations. If unspecified, annotations from all categories are reported. If empty, uncategorized terms are reported.")] = None, **kwargs) -> LimitedResponseDataObjectAnnotationWithUsageStatisticsValueObject:  # noqa: E501
        """Retrieve usage statistics of annotations among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_annotations_usage_statistics(query, filter, exclude, limit, min_frequency, category, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param exclude: List of fields to exclude from the payload. Only `parentTerms` can be excluded.
        :type exclude: List[str]
        :param limit: Maximum number of annotations to returned; capped at 5000.
        :type limit: int
        :param min_frequency: Minimum number of associated datasets to report an annotation. If used, the limit will default to 5000.
        :type min_frequency: int
        :param category: A category URI to restrict reported annotations. If unspecified, annotations from all categories are reported. If empty, uncategorized terms are reported.
        :type category: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: LimitedResponseDataObjectAnnotationWithUsageStatisticsValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_datasets_annotations_usage_statistics_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_datasets_annotations_usage_statistics_with_http_info(query, filter, exclude, limit, min_frequency, category, **kwargs)  # noqa: E501

    @validate_arguments
    def get_datasets_annotations_usage_statistics_with_http_info(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, exclude : Annotated[Optional[conlist(StrictStr, min_items=1, unique_items=True)], Field(description="List of fields to exclude from the payload. Only `parentTerms` can be excluded.")] = None, limit : Annotated[Optional[conint(strict=True, le=5000, ge=1)], Field(description="Maximum number of annotations to returned; capped at 5000.")] = None, min_frequency : Annotated[Optional[StrictInt], Field(description="Minimum number of associated datasets to report an annotation. If used, the limit will default to 5000.")] = None, category : Annotated[Optional[StrictStr], Field(description="A category URI to restrict reported annotations. If unspecified, annotations from all categories are reported. If empty, uncategorized terms are reported.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve usage statistics of annotations among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_annotations_usage_statistics_with_http_info(query, filter, exclude, limit, min_frequency, category, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param exclude: List of fields to exclude from the payload. Only `parentTerms` can be excluded.
        :type exclude: List[str]
        :param limit: Maximum number of annotations to returned; capped at 5000.
        :type limit: int
        :param min_frequency: Minimum number of associated datasets to report an annotation. If used, the limit will default to 5000.
        :type min_frequency: int
        :param category: A category URI to restrict reported annotations. If unspecified, annotations from all categories are reported. If empty, uncategorized terms are reported.
        :type category: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(LimitedResponseDataObjectAnnotationWithUsageStatisticsValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query',
            'filter',
            'exclude',
            'limit',
            'min_frequency',
            'category'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets_annotations_usage_statistics" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('exclude') is not None:  # noqa: E501
            _query_params.append(('exclude', _params['exclude']))
            _collection_formats['exclude'] = 'multi'

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('min_frequency') is not None:  # noqa: E501
            _query_params.append(('minFrequency', _params['min_frequency']))

        if _params.get('category') is not None:  # noqa: E501
            _query_params.append(('category', _params['category']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/datasets/annotations', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_datasets_by_ids(self, dataset : conlist(GetResultSetsDatasetsParameterInner), filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject:  # noqa: E501
        """Retrieve datasets by their identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_by_ids(dataset, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: List[GetResultSetsDatasetsParameterInner]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_datasets_by_ids_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_datasets_by_ids_with_http_info(dataset, filter, offset, limit, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def get_datasets_by_ids_with_http_info(self, dataset : conlist(GetResultSetsDatasetsParameterInner), filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve datasets by their identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_by_ids_with_http_info(dataset, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param dataset: (required)
        :type dataset: List[GetResultSetsDatasetsParameterInner]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'dataset',
            'filter',
            'offset',
            'limit',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets_by_ids" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['dataset']:
            _path_params['dataset'] = _params['dataset']
            _collection_formats['dataset'] = 'csv'


        # process the query parameters
        _query_params = []
        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/datasets/{dataset}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_datasets_categories_usage_statistics(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, **kwargs) -> QueriedAndFilteredResponseDataObjectCategoryWithUsageStatisticsValueObject:  # noqa: E501
        """Retrieve usage statistics of categories among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_categories_usage_statistics(query, filter, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: QueriedAndFilteredResponseDataObjectCategoryWithUsageStatisticsValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_datasets_categories_usage_statistics_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_datasets_categories_usage_statistics_with_http_info(query, filter, **kwargs)  # noqa: E501

    @validate_arguments
    def get_datasets_categories_usage_statistics_with_http_info(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve usage statistics of categories among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_categories_usage_statistics_with_http_info(query, filter, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(QueriedAndFilteredResponseDataObjectCategoryWithUsageStatisticsValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query',
            'filter'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets_categories_usage_statistics" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/datasets/categories', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_datasets_platforms_usage_statistics(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> LimitedResponseDataObjectArrayDesignWithUsageStatisticsValueObject:  # noqa: E501
        """Retrieve usage statistics of platforms among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_platforms_usage_statistics(query, filter, limit, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: LimitedResponseDataObjectArrayDesignWithUsageStatisticsValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_datasets_platforms_usage_statistics_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_datasets_platforms_usage_statistics_with_http_info(query, filter, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_datasets_platforms_usage_statistics_with_http_info(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve usage statistics of platforms among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_platforms_usage_statistics_with_http_info(query, filter, limit, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(LimitedResponseDataObjectArrayDesignWithUsageStatisticsValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query',
            'filter',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets_platforms_usage_statistics" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/datasets/platforms', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_datasets_taxa_usage_statistics(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, **kwargs) -> QueriedAndFilteredResponseDataObjectTaxonWithUsageStatisticsValueObject:  # noqa: E501
        """Retrieve taxa usage statistics for datasets matching the provided query and filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_taxa_usage_statistics(query, filter, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: QueriedAndFilteredResponseDataObjectTaxonWithUsageStatisticsValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_datasets_taxa_usage_statistics_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_datasets_taxa_usage_statistics_with_http_info(query, filter, **kwargs)  # noqa: E501

    @validate_arguments
    def get_datasets_taxa_usage_statistics_with_http_info(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve taxa usage statistics for datasets matching the provided query and filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_taxa_usage_statistics_with_http_info(query, filter, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(QueriedAndFilteredResponseDataObjectTaxonWithUsageStatisticsValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query',
            'filter'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets_taxa_usage_statistics" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/datasets/taxa', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_gene_go_terms(self, gene : Any, **kwargs) -> ResponseDataObjectListGeneOntologyTermValueObject:  # noqa: E501
        """Retrieve the GO terms associated to a gene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_go_terms(gene, async_req=True)
        >>> result = thread.get()

        :param gene: (required)
        :type gene: GetDatasetExpressionForGenesGenesParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListGeneOntologyTermValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_gene_go_terms_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_gene_go_terms_with_http_info(gene, **kwargs)  # noqa: E501

    @validate_arguments
    def get_gene_go_terms_with_http_info(self, gene : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the GO terms associated to a gene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_go_terms_with_http_info(gene, async_req=True)
        >>> result = thread.get()

        :param gene: (required)
        :type gene: GetDatasetExpressionForGenesGenesParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListGeneOntologyTermValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'gene'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gene_go_terms" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['gene']:
            _path_params['gene'] = _params['gene']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/genes/{gene}/goTerms', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_gene_locations(self, gene : Any, **kwargs) -> ResponseDataObjectListPhysicalLocationValueObject:  # noqa: E501
        """Retrieve the physical locations of a given gene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_locations(gene, async_req=True)
        >>> result = thread.get()

        :param gene: (required)
        :type gene: GetDatasetExpressionForGenesGenesParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListPhysicalLocationValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_gene_locations_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_gene_locations_with_http_info(gene, **kwargs)  # noqa: E501

    @validate_arguments
    def get_gene_locations_with_http_info(self, gene : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the physical locations of a given gene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_locations_with_http_info(gene, async_req=True)
        >>> result = thread.get()

        :param gene: (required)
        :type gene: GetDatasetExpressionForGenesGenesParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListPhysicalLocationValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'gene'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gene_locations" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['gene']:
            _path_params['gene'] = _params['gene']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/genes/{gene}/locations', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_gene_locations_in_taxon(self, taxon : Any, gene : Any, **kwargs) -> ResponseDataObjectListPhysicalLocationValueObject:  # noqa: E501
        """Retrieve physical locations for a given gene and taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_locations_in_taxon(taxon, gene, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param gene: (required)
        :type gene: GetDatasetExpressionForGenesGenesParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListPhysicalLocationValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_gene_locations_in_taxon_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_gene_locations_in_taxon_with_http_info(taxon, gene, **kwargs)  # noqa: E501

    @validate_arguments
    def get_gene_locations_in_taxon_with_http_info(self, taxon : Any, gene : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve physical locations for a given gene and taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_locations_in_taxon_with_http_info(taxon, gene, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param gene: (required)
        :type gene: GetDatasetExpressionForGenesGenesParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListPhysicalLocationValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'taxon',
            'gene'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gene_locations_in_taxon" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['taxon']:
            _path_params['taxon'] = _params['taxon']

        if _params['gene']:
            _path_params['gene'] = _params['gene']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/taxa/{taxon}/genes/{gene}/locations', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_gene_probes(self, gene : Any, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject:  # noqa: E501
        """Retrieve the probes associated to a genes across all platforms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_probes(gene, offset, limit, async_req=True)
        >>> result = thread.get()

        :param gene: (required)
        :type gene: GetDatasetExpressionForGenesGenesParameterInner
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_gene_probes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_gene_probes_with_http_info(gene, offset, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_gene_probes_with_http_info(self, gene : Any, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the probes associated to a genes across all platforms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_probes_with_http_info(gene, offset, limit, async_req=True)
        >>> result = thread.get()

        :param gene: (required)
        :type gene: GetDatasetExpressionForGenesGenesParameterInner
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'gene',
            'offset',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gene_probes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['gene']:
            _path_params['gene'] = _params['gene']


        # process the query parameters
        _query_params = []
        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/genes/{gene}/probes', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_genes(self, genes : conlist(GetDatasetExpressionForGenesGenesParameterInner), **kwargs) -> ResponseDataObjectListGeneValueObject:  # noqa: E501
        """Retrieve genes matching gene identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_genes(genes, async_req=True)
        >>> result = thread.get()

        :param genes: (required)
        :type genes: List[GetDatasetExpressionForGenesGenesParameterInner]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListGeneValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_genes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_genes_with_http_info(genes, **kwargs)  # noqa: E501

    @validate_arguments
    def get_genes_with_http_info(self, genes : conlist(GetDatasetExpressionForGenesGenesParameterInner), **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve genes matching gene identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_genes_with_http_info(genes, async_req=True)
        >>> result = thread.get()

        :param genes: (required)
        :type genes: List[GetDatasetExpressionForGenesGenesParameterInner]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListGeneValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'genes'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_genes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['genes']:
            _path_params['genes'] = _params['genes']
            _collection_formats['genes'] = 'csv'


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/genes/{genes}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_number_of_datasets(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, **kwargs) -> ResponseDataObjectLong:  # noqa: E501
        """Count datasets matching the provided query and  filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_datasets(query, filter, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectLong
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_number_of_datasets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_number_of_datasets_with_http_info(query, filter, **kwargs)  # noqa: E501

    @validate_arguments
    def get_number_of_datasets_with_http_info(self, query : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Count datasets matching the provided query and  filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_datasets_with_http_info(query, filter, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectLong, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query',
            'filter'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_number_of_datasets" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/datasets/count', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_number_of_platforms(self, filter : Optional[StrictStr] = None, **kwargs) -> ResponseDataObjectLong:  # noqa: E501
        """Count platforms matching the provided filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_platforms(filter, async_req=True)
        >>> result = thread.get()

        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectLong
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_number_of_platforms_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_number_of_platforms_with_http_info(filter, **kwargs)  # noqa: E501

    @validate_arguments
    def get_number_of_platforms_with_http_info(self, filter : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Count platforms matching the provided filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_platforms_with_http_info(filter, async_req=True)
        >>> result = thread.get()

        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectLong, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'filter'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_number_of_platforms" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/platforms/count', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_number_of_result_sets(self, filter : Optional[StrictStr] = None, **kwargs) -> ResponseDataObjectLong:  # noqa: E501
        """Count result sets matching the provided filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_result_sets(filter, async_req=True)
        >>> result = thread.get()

        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectLong
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_number_of_result_sets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_number_of_result_sets_with_http_info(filter, **kwargs)  # noqa: E501

    @validate_arguments
    def get_number_of_result_sets_with_http_info(self, filter : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Count result sets matching the provided filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_result_sets_with_http_info(filter, async_req=True)
        >>> result = thread.get()

        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectLong, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'filter'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_number_of_result_sets" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/resultSets/count', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_platform_annotations(self, platform : Any, **kwargs) -> bytearray:  # noqa: E501
        """Retrieve the annotations of a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_annotations(platform, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_platform_annotations_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_platform_annotations_with_http_info(platform, **kwargs)  # noqa: E501

    @validate_arguments
    def get_platform_annotations_with_http_info(self, platform : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the annotations of a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_annotations_with_http_info(platform, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'platform'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platform_annotations" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['platform']:
            _path_params['platform'] = _params['platform']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
        }

        return self.api_client.call_api(
            '/platforms/{platform}/annotations', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_platform_datasets(self, platform : Any, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> PaginatedResponseDataObjectExpressionExperimentValueObject:  # noqa: E501
        """Retrieve all experiments using a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_datasets(platform, offset, limit, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PaginatedResponseDataObjectExpressionExperimentValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_platform_datasets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_platform_datasets_with_http_info(platform, offset, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_platform_datasets_with_http_info(self, platform : Any, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve all experiments using a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_datasets_with_http_info(platform, offset, limit, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PaginatedResponseDataObjectExpressionExperimentValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'platform',
            'offset',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platform_datasets" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['platform']:
            _path_params['platform'] = _params['platform']


        # process the query parameters
        _query_params = []
        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/platforms/{platform}/datasets', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_platform_element(self, platform : Any, probes : conlist(GetPlatformElementProbesParameterInner), offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject:  # noqa: E501
        """Retrieve the selected probes for a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_element(platform, probes, offset, limit, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param probes: (required)
        :type probes: List[GetPlatformElementProbesParameterInner]
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_platform_element_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_platform_element_with_http_info(platform, probes, offset, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_platform_element_with_http_info(self, platform : Any, probes : conlist(GetPlatformElementProbesParameterInner), offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the selected probes for a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_element_with_http_info(platform, probes, offset, limit, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param probes: (required)
        :type probes: List[GetPlatformElementProbesParameterInner]
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'platform',
            'probes',
            'offset',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platform_element" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['platform']:
            _path_params['platform'] = _params['platform']

        if _params['probes']:
            _path_params['probes'] = _params['probes']
            _collection_formats['probes'] = 'csv'


        # process the query parameters
        _query_params = []
        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/platforms/{platform}/elements/{probes}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_platform_element_genes(self, platform : Any, probe : Any, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectGeneValueObject:  # noqa: E501
        """Retrieve the genes associated to a probe in a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_element_genes(platform, probe, offset, limit, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param probe: (required)
        :type probe: GetPlatformElementProbesParameterInner
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectGeneValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_platform_element_genes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_platform_element_genes_with_http_info(platform, probe, offset, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_platform_element_genes_with_http_info(self, platform : Any, probe : Any, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the genes associated to a probe in a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_element_genes_with_http_info(platform, probe, offset, limit, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param probe: (required)
        :type probe: GetPlatformElementProbesParameterInner
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectGeneValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'platform',
            'probe',
            'offset',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platform_element_genes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['platform']:
            _path_params['platform'] = _params['platform']

        if _params['probe']:
            _path_params['probe'] = _params['probe']


        # process the query parameters
        _query_params = []
        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/platforms/{platform}/elements/{probe}/genes', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_platform_elements(self, platform : Any, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> PaginatedResponseDataObjectCompositeSequenceValueObject:  # noqa: E501
        """Retrieve the probes for a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_elements(platform, offset, limit, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PaginatedResponseDataObjectCompositeSequenceValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_platform_elements_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_platform_elements_with_http_info(platform, offset, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_platform_elements_with_http_info(self, platform : Any, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the probes for a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_elements_with_http_info(platform, offset, limit, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PaginatedResponseDataObjectCompositeSequenceValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'platform',
            'offset',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platform_elements" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['platform']:
            _path_params['platform'] = _params['platform']


        # process the query parameters
        _query_params = []
        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/platforms/{platform}/elements', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_platforms(self, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectArrayDesignValueObject:  # noqa: E501
        """Retrieve all platforms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platforms(filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectArrayDesignValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_platforms_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_platforms_with_http_info(filter, offset, limit, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def get_platforms_with_http_info(self, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve all platforms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platforms_with_http_info(filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectArrayDesignValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'filter',
            'offset',
            'limit',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platforms" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/platforms', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_platforms_by_ids(self, platform : conlist(GetPlatformAnnotationsPlatformParameter), filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectArrayDesignValueObject:  # noqa: E501
        """Retrieve all platforms matching a set of platform identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platforms_by_ids(platform, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: List[GetPlatformAnnotationsPlatformParameter]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectArrayDesignValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_platforms_by_ids_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_platforms_by_ids_with_http_info(platform, filter, offset, limit, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def get_platforms_by_ids_with_http_info(self, platform : conlist(GetPlatformAnnotationsPlatformParameter), filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve all platforms matching a set of platform identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platforms_by_ids_with_http_info(platform, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param platform: (required)
        :type platform: List[GetPlatformAnnotationsPlatformParameter]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectArrayDesignValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'platform',
            'filter',
            'offset',
            'limit',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platforms_by_ids" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['platform']:
            _path_params['platform'] = _params['platform']
            _collection_formats['platform'] = 'csv'


        # process the query parameters
        _query_params = []
        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/platforms/{platform}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_result_set(self, result_set : StrictInt, **kwargs) -> ResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject:  # noqa: E501
        """Retrieve a single analysis result set by its identifier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_set(result_set, async_req=True)
        >>> result = thread.get()

        :param result_set: (required)
        :type result_set: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_result_set_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_result_set_with_http_info(result_set, **kwargs)  # noqa: E501

    @validate_arguments
    def get_result_set_with_http_info(self, result_set : StrictInt, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve a single analysis result set by its identifier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_set_with_http_info(result_set, async_req=True)
        >>> result = thread.get()

        :param result_set: (required)
        :type result_set: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'result_set'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_set" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['result_set']:
            _path_params['resultSet'] = _params['result_set']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "ResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject",
            '404': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/resultSets/{resultSet}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_result_set_as_tsv(self, result_set_ : StrictInt, **kwargs) -> bytearray:  # noqa: E501
        """Retrieve a single analysis result set by its identifier as a tab-separated values  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_set_as_tsv(result_set_, async_req=True)
        >>> result = thread.get()

        :param result_set_: (required)
        :type result_set_: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_result_set_as_tsv_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_result_set_as_tsv_with_http_info(result_set_, **kwargs)  # noqa: E501

    @validate_arguments
    def get_result_set_as_tsv_with_http_info(self, result_set_ : StrictInt, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve a single analysis result set by its identifier as a tab-separated values  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_set_as_tsv_with_http_info(result_set_, async_req=True)
        >>> result = thread.get()

        :param result_set_: (required)
        :type result_set_: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'result_set_'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_set_as_tsv" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['result_set_']:
            _path_params['resultSet_'] = _params['result_set_']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
            '404': None,
        }

        return self.api_client.call_api(
            '/resultSets/{resultSet_}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_result_sets(self, datasets : Optional[conlist(GetResultSetsDatasetsParameterInner)] = None, database_entries : Optional[conlist(GetResultSetsDatabaseEntriesParameterInner)] = None, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject:  # noqa: E501
        """Retrieve all result sets matching the provided criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_sets(datasets, database_entries, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param datasets:
        :type datasets: List[GetResultSetsDatasetsParameterInner]
        :param database_entries:
        :type database_entries: List[GetResultSetsDatabaseEntriesParameterInner]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_result_sets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_result_sets_with_http_info(datasets, database_entries, filter, offset, limit, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def get_result_sets_with_http_info(self, datasets : Optional[conlist(GetResultSetsDatasetsParameterInner)] = None, database_entries : Optional[conlist(GetResultSetsDatabaseEntriesParameterInner)] = None, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve all result sets matching the provided criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_sets_with_http_info(datasets, database_entries, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param datasets:
        :type datasets: List[GetResultSetsDatasetsParameterInner]
        :param database_entries:
        :type database_entries: List[GetResultSetsDatabaseEntriesParameterInner]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'datasets',
            'database_entries',
            'filter',
            'offset',
            'limit',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_sets" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('datasets') is not None:  # noqa: E501
            _query_params.append(('datasets', _params['datasets']))
            _collection_formats['datasets'] = 'csv'

        if _params.get('database_entries') is not None:  # noqa: E501
            _query_params.append(('databaseEntries', _params['database_entries']))
            _collection_formats['databaseEntries'] = 'csv'

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/resultSets', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_taxa(self, **kwargs) -> ResponseDataObjectListTaxonValueObject:  # noqa: E501
        """Retrieve all available taxa  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxa(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListTaxonValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_taxa_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_taxa_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_taxa_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve all available taxa  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxa_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListTaxonValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_taxa" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/taxa', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_taxa_by_ids(self, taxa : conlist(SearchTaxonDatasetsTaxonParameter), **kwargs) -> ResponseDataObjectListTaxonValueObject:  # noqa: E501
        """Retrieve taxa by their identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxa_by_ids(taxa, async_req=True)
        >>> result = thread.get()

        :param taxa: (required)
        :type taxa: List[SearchTaxonDatasetsTaxonParameter]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListTaxonValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_taxa_by_ids_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_taxa_by_ids_with_http_info(taxa, **kwargs)  # noqa: E501

    @validate_arguments
    def get_taxa_by_ids_with_http_info(self, taxa : conlist(SearchTaxonDatasetsTaxonParameter), **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve taxa by their identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxa_by_ids_with_http_info(taxa, async_req=True)
        >>> result = thread.get()

        :param taxa: (required)
        :type taxa: List[SearchTaxonDatasetsTaxonParameter]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListTaxonValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'taxa'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_taxa_by_ids" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['taxa']:
            _path_params['taxa'] = _params['taxa']
            _collection_formats['taxa'] = 'csv'


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/taxa/{taxa}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_taxon_datasets(self, taxon : Any, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject:  # noqa: E501
        """Retrieve the datasets for a given taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_datasets(taxon, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_taxon_datasets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_taxon_datasets_with_http_info(taxon, filter, offset, limit, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def get_taxon_datasets_with_http_info(self, taxon : Any, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the datasets for a given taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_datasets_with_http_info(taxon, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'taxon',
            'filter',
            'offset',
            'limit',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_taxon_datasets" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['taxon']:
            _path_params['taxon'] = _params['taxon']


        # process the query parameters
        _query_params = []
        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/taxa/{taxon}/datasets', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_taxon_genes(self, taxon : Any, gene : Any, **kwargs) -> ResponseDataObjectListGeneValueObject:  # noqa: E501
        """Retrieve all genes in a given taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_genes(taxon, gene, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param gene: (required)
        :type gene: GetDatasetExpressionForGenesGenesParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListGeneValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_taxon_genes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_taxon_genes_with_http_info(taxon, gene, **kwargs)  # noqa: E501

    @validate_arguments
    def get_taxon_genes_with_http_info(self, taxon : Any, gene : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve all genes in a given taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_genes_with_http_info(taxon, gene, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param gene: (required)
        :type gene: GetDatasetExpressionForGenesGenesParameterInner
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListGeneValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'taxon',
            'gene'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_taxon_genes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['taxon']:
            _path_params['taxon'] = _params['taxon']

        if _params['gene']:
            _path_params['gene'] = _params['gene']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/taxa/{taxon}/genes/{gene}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_taxon_genes_overlapping_chromosome(self, taxon : Any, chromosome : StrictStr, start : StrictInt, size : StrictInt, strand : Optional[StrictStr] = None, **kwargs) -> ResponseDataObjectListGeneValueObject:  # noqa: E501
        """Retrieve genes overlapping a given region in a taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_genes_overlapping_chromosome(taxon, chromosome, start, size, strand, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param chromosome: (required)
        :type chromosome: str
        :param start: (required)
        :type start: int
        :param size: (required)
        :type size: int
        :param strand:
        :type strand: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListGeneValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_taxon_genes_overlapping_chromosome_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_taxon_genes_overlapping_chromosome_with_http_info(taxon, chromosome, start, size, strand, **kwargs)  # noqa: E501

    @validate_arguments
    def get_taxon_genes_overlapping_chromosome_with_http_info(self, taxon : Any, chromosome : StrictStr, start : StrictInt, size : StrictInt, strand : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve genes overlapping a given region in a taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_genes_overlapping_chromosome_with_http_info(taxon, chromosome, start, size, strand, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param chromosome: (required)
        :type chromosome: str
        :param start: (required)
        :type start: int
        :param size: (required)
        :type size: int
        :param strand:
        :type strand: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListGeneValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'taxon',
            'chromosome',
            'start',
            'size',
            'strand'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_taxon_genes_overlapping_chromosome" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['taxon']:
            _path_params['taxon'] = _params['taxon']

        if _params['chromosome']:
            _path_params['chromosome'] = _params['chromosome']


        # process the query parameters
        _query_params = []
        if _params.get('strand') is not None:  # noqa: E501
            _query_params.append(('strand', _params['strand']))

        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('size') is not None:  # noqa: E501
            _query_params.append(('size', _params['size']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/taxa/{taxon}/chromosomes/{chromosome}/genes', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def search(self, query : Optional[StrictStr] = None, taxon : Optional[Any] = None, platform : Optional[Any] = None, result_types : Optional[conlist(StrictStr)] = None, limit : Annotated[Optional[conint(strict=True, le=2000, ge=1)], Field(description="Maximum number of search results to return; capped at 2000 unless `resultObject` is excluded.")] = None, exclude : Annotated[Optional[conlist(StrictStr, min_items=1, unique_items=True)], Field(description="List of fields to exclude from the payload. Only `resultObject` is supported.")] = None, **kwargs) -> SearchResultsResponseDataObject:  # noqa: E501
        """Search everything in Gemma  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search(query, taxon, platform, result_types, limit, exclude, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param taxon:
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param platform:
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param result_types:
        :type result_types: List[str]
        :param limit: Maximum number of search results to return; capped at 2000 unless `resultObject` is excluded.
        :type limit: int
        :param exclude: List of fields to exclude from the payload. Only `resultObject` is supported.
        :type exclude: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SearchResultsResponseDataObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the search_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.search_with_http_info(query, taxon, platform, result_types, limit, exclude, **kwargs)  # noqa: E501

    @validate_arguments
    def search_with_http_info(self, query : Optional[StrictStr] = None, taxon : Optional[Any] = None, platform : Optional[Any] = None, result_types : Optional[conlist(StrictStr)] = None, limit : Annotated[Optional[conint(strict=True, le=2000, ge=1)], Field(description="Maximum number of search results to return; capped at 2000 unless `resultObject` is excluded.")] = None, exclude : Annotated[Optional[conlist(StrictStr, min_items=1, unique_items=True)], Field(description="List of fields to exclude from the payload. Only `resultObject` is supported.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Search everything in Gemma  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_with_http_info(query, taxon, platform, result_types, limit, exclude, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: str
        :param taxon:
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param platform:
        :type platform: GetPlatformAnnotationsPlatformParameter
        :param result_types:
        :type result_types: List[str]
        :param limit: Maximum number of search results to return; capped at 2000 unless `resultObject` is excluded.
        :type limit: int
        :param exclude: List of fields to exclude from the payload. Only `resultObject` is supported.
        :type exclude: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SearchResultsResponseDataObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query',
            'taxon',
            'platform',
            'result_types',
            'limit',
            'exclude'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))

        if _params.get('taxon') is not None:  # noqa: E501
            _query_params.append(('taxon', _params['taxon']))

        if _params.get('platform') is not None:  # noqa: E501
            _query_params.append(('platform', _params['platform']))

        if _params.get('result_types') is not None:  # noqa: E501
            _query_params.append(('resultTypes', _params['result_types']))
            _collection_formats['resultTypes'] = 'multi'

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('exclude') is not None:  # noqa: E501
            _query_params.append(('exclude', _params['exclude']))
            _collection_formats['exclude'] = 'multi'

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
        }

        return self.api_client.call_api(
            '/search', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def search_annotations(self, query : Optional[conlist(StrictStr)] = None, **kwargs) -> ResponseDataObjectListAnnotationSearchResultValueObject:  # noqa: E501
        """Search for annotation tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_annotations(query, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListAnnotationSearchResultValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the search_annotations_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.search_annotations_with_http_info(query, **kwargs)  # noqa: E501

    @validate_arguments
    def search_annotations_with_http_info(self, query : Optional[conlist(StrictStr)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Search for annotation tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_annotations_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListAnnotationSearchResultValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_annotations" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))
            _collection_formats['query'] = 'csv'

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "ResponseDataObjectListAnnotationSearchResultValueObject",
            '400': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/annotations/search', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def search_annotations_by_path_query(self, query : conlist(StrictStr), **kwargs) -> ResponseDataObjectListAnnotationSearchResultValueObject:  # noqa: E501
        """(Deprecated) Search for annotation tags  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_annotations_by_path_query(query, async_req=True)
        >>> result = thread.get()

        :param query: (required)
        :type query: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseDataObjectListAnnotationSearchResultValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the search_annotations_by_path_query_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.search_annotations_by_path_query_with_http_info(query, **kwargs)  # noqa: E501

    @validate_arguments
    def search_annotations_by_path_query_with_http_info(self, query : conlist(StrictStr), **kwargs) -> ApiResponse:  # noqa: E501
        """(Deprecated) Search for annotation tags  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_annotations_by_path_query_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param query: (required)
        :type query: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseDataObjectListAnnotationSearchResultValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        warnings.warn("GET /annotations/search/{query} is deprecated.", DeprecationWarning)

        _params = locals()

        _all_params = [
            'query'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_annotations_by_path_query" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['query']:
            _path_params['query'] = _params['query']
            _collection_formats['query'] = 'csv'


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "ResponseDataObjectListAnnotationSearchResultValueObject",
            '400': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/annotations/search/{query}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def search_datasets(self, query : Optional[conlist(StrictStr)] = None, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject:  # noqa: E501
        """(Deprecated) Retrieve datasets associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of the getDatasets() endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_datasets(query, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: List[str]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the search_datasets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.search_datasets_with_http_info(query, filter, offset, limit, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def search_datasets_with_http_info(self, query : Optional[conlist(StrictStr)] = None, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """(Deprecated) Retrieve datasets associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of the getDatasets() endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_datasets_with_http_info(query, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param query:
        :type query: List[str]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        warnings.warn("GET /annotations/search/datasets is deprecated.", DeprecationWarning)

        _params = locals()

        _all_params = [
            'query',
            'filter',
            'offset',
            'limit',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_datasets" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))
            _collection_formats['query'] = 'csv'

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject",
            '400': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/annotations/search/datasets', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def search_datasets_by_query_in_path(self, query : conlist(StrictStr), filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject:  # noqa: E501
        """(Deprecated) Retrieve datasets associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_datasets_by_query_in_path(query, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param query: (required)
        :type query: List[str]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the search_datasets_by_query_in_path_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.search_datasets_by_query_in_path_with_http_info(query, filter, offset, limit, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def search_datasets_by_query_in_path_with_http_info(self, query : conlist(StrictStr), filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """(Deprecated) Retrieve datasets associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_datasets_by_query_in_path_with_http_info(query, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param query: (required)
        :type query: List[str]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        warnings.warn("GET /annotations/search/{query}/datasets is deprecated.", DeprecationWarning)

        _params = locals()

        _all_params = [
            'query',
            'filter',
            'offset',
            'limit',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_datasets_by_query_in_path" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['query']:
            _path_params['query'] = _params['query']
            _collection_formats['query'] = 'csv'


        # process the query parameters
        _query_params = []
        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject",
            '400': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/annotations/search/{query}/datasets', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def search_taxon_datasets(self, taxon : Any, query : Optional[conlist(StrictStr)] = None, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject:  # noqa: E501
        """(Deprecated) Retrieve datasets within a given taxa associated to an annotation tags search  # noqa: E501

        Use getDatasets() with a `query` parameter and a `filter` parameter with `taxon.id = {taxon} or taxon.commonName = {taxon} or taxon.scientificName = {taxon}` to restrict the taxon instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_taxon_datasets(taxon, query, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param query:
        :type query: List[str]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the search_taxon_datasets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.search_taxon_datasets_with_http_info(taxon, query, filter, offset, limit, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def search_taxon_datasets_with_http_info(self, taxon : Any, query : Optional[conlist(StrictStr)] = None, filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """(Deprecated) Retrieve datasets within a given taxa associated to an annotation tags search  # noqa: E501

        Use getDatasets() with a `query` parameter and a `filter` parameter with `taxon.id = {taxon} or taxon.commonName = {taxon} or taxon.scientificName = {taxon}` to restrict the taxon instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_taxon_datasets_with_http_info(taxon, query, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param query:
        :type query: List[str]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        warnings.warn("GET /annotations/{taxon}/search/datasets is deprecated.", DeprecationWarning)

        _params = locals()

        _all_params = [
            'taxon',
            'query',
            'filter',
            'offset',
            'limit',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_taxon_datasets" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['taxon']:
            _path_params['taxon'] = _params['taxon']


        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))
            _collection_formats['query'] = 'csv'

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject",
            '400': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/annotations/{taxon}/search/datasets', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def search_taxon_datasets_by_query_in_path(self, taxon : Any, query : conlist(StrictStr), filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject:  # noqa: E501
        """(Deprecated) Retrieve datasets within a given taxa associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_taxon_datasets_by_query_in_path(taxon, query, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param query: (required)
        :type query: List[str]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the search_taxon_datasets_by_query_in_path_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.search_taxon_datasets_by_query_in_path_with_http_info(taxon, query, filter, offset, limit, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def search_taxon_datasets_by_query_in_path_with_http_info(self, taxon : Any, query : conlist(StrictStr), filter : Optional[StrictStr] = None, offset : Optional[conint(strict=True, ge=0)] = None, limit : Optional[conint(strict=True, le=100, ge=1)] = None, sort : Optional[constr(strict=True)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """(Deprecated) Retrieve datasets within a given taxa associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_taxon_datasets_by_query_in_path_with_http_info(taxon, query, filter, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param taxon: (required)
        :type taxon: SearchTaxonDatasetsTaxonParameter
        :param query: (required)
        :type query: List[str]
        :param filter:
        :type filter: str
        :param offset:
        :type offset: int
        :param limit:
        :type limit: int
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject, status_code(int), headers(HTTPHeaderDict))
        """

        warnings.warn("GET /annotations/{taxon}/search/{query}/datasets is deprecated.", DeprecationWarning)

        _params = locals()

        _all_params = [
            'taxon',
            'query',
            'filter',
            'offset',
            'limit',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_taxon_datasets_by_query_in_path" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['taxon']:
            _path_params['taxon'] = _params['taxon']

        if _params['query']:
            _path_params['query'] = _params['query']
            _collection_formats['query'] = 'csv'


        # process the query parameters
        _query_params = []
        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject",
            '400': "ResponseErrorObject",
        }

        return self.api_client.call_api(
            '/annotations/{taxon}/search/{query}/datasets', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
