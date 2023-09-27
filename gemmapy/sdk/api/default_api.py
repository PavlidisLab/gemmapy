# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  ## Updates  ### Update 2.7.1  - improved highlights of search results - fix the limit for getDatasetsAnnotations() endpoint to 5000 in the specification - fix missing initialization of datasets retrieved from the cache  Highlights now use Markdown syntax for formatting. Fields for highlighted ontology terms now use complete object path instead of just `term`. Last but not least, highlights from multiple results are merged.  ### Update 2.7.0  New endpoints for counting the number of results: `getNumberOfDatasets`, `getNumberOfPlatforms`, `getNumberOfResultSets`. These endpoints are faster than looking up `totalElements` as no data is retrieved or converted.  Datasets can now be filtered by annotations at the sample, factor value and all levels using the three newly exposed `experimentalDesign.experimentalFactors.factorValues.characteristics`, `bioAssays.sampleUsed.characteristics` and `allCharacteristics` collections. The two useful available properties for filtering are `value` and `valueUri`.  New `getDatasetsAnnotationsUsageStatistics`, `getDatasetsPlatformsUsageStatistics` and `getDatasetsTaxaUsageStatistics` endpoints for retrieving annotations, platforms and taxa used by the matched datasets. The endpoint accepts the same `filter` argument of `getDatasets`, allowing one to easily navigate terms, platforms and taxa available for filtering furthermore.  Properties available for filtering and sorting are enumerated in the description of the corresponding parameter. There's been a number of fixes and additional tests performed to ensure that all advertised properties are working as expected.  The `FilterArg` and `SortArg`-based parameters now have OpenAPI extensions to enumerate available properties in a structured format under the `x-gemma-filterable-properties`key. Possible values are exposed for enumerated types.  ```yaml x-gemma-filterable-properties: - name: technologyType   type: string   allowedValues:   - value: ONECOLOR     label: One Color   - value: SEQUENCING     label: Sequencing   security:     basicAuth: [GROUP_ADMIN]     cookieAuth: [GROUP_ADMIN] ```  Some of the exposed properties such as `geeq.publicSuitabilityScore` require specific authorities to use. This is documented in `x-filterable-properties` by specifying a [Security Requirement Object](https://spec.openapis.org/oas/latest.html#security-requirement-object).  Types that use the `[]` suffix are using sub-queries under the hood. It implies that the entity will be matched if at least one related entity matches the supplied filter. For example, the `characteristics.valueUri = http://purl.obolibrary.org/obo/UBERON_0002107` filter will match datasets with at least one `UBERON:0002107` tag attached.  Filtered endpoints (including paginated and limited ones) now expose a `groupBy` array that enumerates all the properties used to group results. This helps clear confusion about what constitute a business key in the returned response.  ### Update 2.6.1  Add support for filtering platforms by taxon ID, common name, scientific name, etc. for the `/platforms` endpoint.  ### Update 2.6.0  Add a new `externalDatabases` attribute to the main endpoint that displays version of some of the main external databases that we are using. This exposes versions and last updates for genomes, gene annotations, GO terms, and much more!  The `ExternalDatabaseValueObject` now exposes a `description` which provides additional details.  ### Update 2.5.2  Restore `factors` in `BioMaterialValueObject` as it is being still used by our RNA-Seq pipeline. The attribute is deprecated and should not be used and will be removed when we find a suitable alternative.  Introduce a new endpoint to retrieve quantitation types for a given dataset and parameters to retrieve expression data by quantitation type to `getDatasetProcessedExpression` and `getDatasetRawExpression`. As it was too difficult to extends `getDatasetExpression` to also support quantitation type while retaining the filter feature, we decided to deprecate it and reintroduce filtering for both raw and processed expression in the future.  Fix return type for `getResultSets` which was incorrectly referring to a renamed VO.  Annotate all possible types for `SearchResult.resultObject`. This incidentally includes the `GeneSetValueObject` in the specification which is not exposed elsewhere in the API.  ### Update 2.5.1  Restore `objectClass` visibility in `AnnotationValueObject`.  Fix incorrect response types for annotations search endpoints returning datasets.  ### Update 2.5.0  Major cleanups were performed in this release in order to stabilize the specification. Numerous properties from Gemma Web that were never intended to be exposed in Gemma REST have been hidden. It's a bit too much to describe in here, but you can navigate to the schemas section below to get a good glance at the models.  Favour `numberOfSomething` instead of `somethingCount` which is clearer. The older names are kept for backward-compatibility, but should be considered deprecated.  Gene aliases and multifunctionality rank are now filled in `GeneValueObject`.  Uniformly use `TaxonValueObject` to represent taxon. This is breaking change for the `ExpressionExperimentValueObject` and `ArrayDesignValueObject` as their `taxon` property will be an `object` instead of a `string`. Properties such as `taxonId` are now deprecated and `taxon.id` should be used instead.  Entities that have IDs now all inherit from `IdentifiableValueObject`. This implies that you can assume the presence of an `id` in a search result `resultObject` attribute for example.  New `/search` endpoint! for an unified search experience. Annotation-based search endpoints under `/annotations` are now deprecated.  New API docs! While not as nice looking, the previous theme will be gradually ported to Swagger UI as we focused on functionality over prettiness for this release.  ### Update 2.4.0 through 2.4.1  Release notes for the 2.4 series were not written down, so I'll try to do my best to recall features that were introduced at that time.  An [OpenAPI](https://www.openapis.org/) specification was introduced and available under `/rest/v2/openapi.json`, although not fully stabilized.  Add a `/resultSets` endpoint to navigate result sets directly, by ID or by dataset.  Add a `/resultSets/{resultSetId}` endpoint to retrieve a specific result set by its ID. This endpoint can be negotiated with an `Accept: text/tab-separated-values` header to obtain a TSV representation.  Add a `/datasets/{dataset}/analyses/differential/resultSets` endpoint that essentially redirect to a specific `/resultSet` endpoint by dataset ID.  Add an endpoint to retrieve preferred raw expression vectors.  ### Update 2.3.4  November 6th, 2018  November 6th [2.3.4] Bug fixes in the dataset search endpoint.  November 5th [2.3.3] Added filtering parameters to dataset search.  October 25th [2.3.2] Changed behavior of the dataset search endpoint to more closely match the Gemma web interface.  October 2nd [2.3.1] Added group information to the User value object.  September 27th [2.3.0] Breaking change in Taxa: Abbreviation property has been removed and is therefore no longer an accepted identifier.  ### Update 2.2.6  June 7th, 2018  Code maintenance, bug fixes. Geeq scores stable and made public.  June 7th [2.2.6] Added: User authentication endpoint.  May 2nd [2.2.5] Fixed: Cleaned up and optimized platforms/elements endpoint, removed redundant information (recursive properties nesting).  April 12th [2.2.3] Fixed: Array arguments not handling non-string properties properly, e.g. `ncbiIds` of genes.  April 9th [2.2.1] Fixed: Filter argument not working when the filtered field was a primitive type. This most significantly allows filtering by geeq boolean and double properties.  ### Update 2.2.0  February 8th, 2018  Breaking change in the 'Dataset differential analysis' endpoint: - No longer using `qValueThreshold` parameter. - Response format changed, now using `DifferentialExpressionAnalysisValueObject` instead of `DifferentialExpressionValueObject` - [Experimental] Added Geeq (Gene Expression Experiment Quality) scores to the dataset value objects   # noqa: E501

    OpenAPI spec version: 2.7.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gemmapy.sdk.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_api_info(self, **kwargs):  # noqa: E501
        """Retrieve an object with basic API information  # noqa: E501

        The payload contains a list of featured external databases that Gemma uses under the `externalDatabases` field. Those are mainly genomic references and sources of gene annotations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_api_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :return: ResponseDataObjectApiInfoValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_api_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_api_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_api_info_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve an object with basic API information  # noqa: E501

        The payload contains a list of featured external databases that Gemma uses under the `externalDatabases` field. Those are mainly genomic references and sources of gene annotations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_api_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :return: ResponseDataObjectApiInfoValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectApiInfoValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_annotations(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the annotations of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_annotations(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset dataset: (required)
        :return: ResponseDataObjectSetAnnotationValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_annotations_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_annotations_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_dataset_annotations_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the annotations of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_annotations_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset dataset: (required)
        :return: ResponseDataObjectSetAnnotationValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_annotations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_dataset_annotations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}/annotations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectSetAnnotationValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_design(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the design of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_design(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset1 dataset: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_design_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_design_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_dataset_design_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the design of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_design_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset1 dataset: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_design" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_dataset_design`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}/design', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_differential_expression(self, datasets, **kwargs):  # noqa: E501
        """Retrieve the expression levels of a set of datasets subject to a threshold on their differential expressions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression(datasets, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] datasets: (required)
        :param int diff_ex_set:
        :param float threshold:
        :param int limit:
        :param bool keep_non_specific:
        :param str consolidate:
        :return: ResponseDataObjectListExperimentExpressionLevelsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_differential_expression_with_http_info(datasets, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_differential_expression_with_http_info(datasets, **kwargs)  # noqa: E501
            return data

    def get_dataset_differential_expression_with_http_info(self, datasets, **kwargs):  # noqa: E501
        """Retrieve the expression levels of a set of datasets subject to a threshold on their differential expressions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression_with_http_info(datasets, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] datasets: (required)
        :param int diff_ex_set:
        :param float threshold:
        :param int limit:
        :param bool keep_non_specific:
        :param str consolidate:
        :return: ResponseDataObjectListExperimentExpressionLevelsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasets', 'diff_ex_set', 'threshold', 'limit', 'keep_non_specific', 'consolidate']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_differential_expression" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'datasets' is set
        if ('datasets' not in params or
                params['datasets'] is None):
            raise ValueError("Missing the required parameter `datasets` when calling `get_dataset_differential_expression`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'datasets' in params:
            path_params['datasets'] = params['datasets']  # noqa: E501
            collection_formats['datasets'] = ''  # noqa: E501

        query_params = []
        if 'diff_ex_set' in params:
            query_params.append(('diffExSet', params['diff_ex_set']))  # noqa: E501
        if 'threshold' in params:
            query_params.append(('threshold', params['threshold']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'keep_non_specific' in params:
            query_params.append(('keepNonSpecific', params['keep_non_specific']))  # noqa: E501
        if 'consolidate' in params:
            query_params.append(('consolidate', params['consolidate']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{datasets}/expressions/differential', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListExperimentExpressionLevelsValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_differential_expression_analyses(self, dataset, **kwargs):  # noqa: E501
        """Retrieve annotations and surface level stats for a dataset's differential analyses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression_analyses(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset2 dataset: (required)
        :param int offset:
        :param int limit:
        :return: ResponseDataObjectListDifferentialExpressionAnalysisValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_differential_expression_analyses_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_differential_expression_analyses_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_dataset_differential_expression_analyses_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve annotations and surface level stats for a dataset's differential analyses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression_analyses_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset2 dataset: (required)
        :param int offset:
        :param int limit:
        :return: ResponseDataObjectListDifferentialExpressionAnalysisValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_differential_expression_analyses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_dataset_differential_expression_analyses`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}/analyses/differential', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListDifferentialExpressionAnalysisValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_differential_expression_analyses_result_sets(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the result sets of all differential analyses of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression_analyses_result_sets(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset3 dataset: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_differential_expression_analyses_result_sets_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_differential_expression_analyses_result_sets_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_dataset_differential_expression_analyses_result_sets_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the result sets of all differential analyses of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_differential_expression_analyses_result_sets_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset3 dataset: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_differential_expression_analyses_result_sets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_dataset_differential_expression_analyses_result_sets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}/analyses/differential/resultSets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_expression(self, dataset, **kwargs):  # noqa: E501
        """Retrieve processed expression data of a dataset  # noqa: E501

        This endpoint is deprecated and getDatasetProcessedExpression() should be used instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset4 dataset: (required)
        :param bool filter:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_expression_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_expression_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_dataset_expression_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve processed expression data of a dataset  # noqa: E501

        This endpoint is deprecated and getDatasetProcessedExpression() should be used instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset4 dataset: (required)
        :param bool filter:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_expression" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_dataset_expression`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}/data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_expression_for_genes(self, datasets, genes, **kwargs):  # noqa: E501
        """Retrieve the expression data matrix of a set of datasets and genes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression_for_genes(datasets, genes, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] datasets: (required)
        :param list[object] genes: (required)
        :param bool keep_non_specific:
        :param str consolidate:
        :return: ResponseDataObjectListExperimentExpressionLevelsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_expression_for_genes_with_http_info(datasets, genes, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_expression_for_genes_with_http_info(datasets, genes, **kwargs)  # noqa: E501
            return data

    def get_dataset_expression_for_genes_with_http_info(self, datasets, genes, **kwargs):  # noqa: E501
        """Retrieve the expression data matrix of a set of datasets and genes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression_for_genes_with_http_info(datasets, genes, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] datasets: (required)
        :param list[object] genes: (required)
        :param bool keep_non_specific:
        :param str consolidate:
        :return: ResponseDataObjectListExperimentExpressionLevelsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasets', 'genes', 'keep_non_specific', 'consolidate']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_expression_for_genes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'datasets' is set
        if ('datasets' not in params or
                params['datasets'] is None):
            raise ValueError("Missing the required parameter `datasets` when calling `get_dataset_expression_for_genes`")  # noqa: E501
        # verify the required parameter 'genes' is set
        if ('genes' not in params or
                params['genes'] is None):
            raise ValueError("Missing the required parameter `genes` when calling `get_dataset_expression_for_genes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'datasets' in params:
            path_params['datasets'] = params['datasets']  # noqa: E501
            collection_formats['datasets'] = ''  # noqa: E501
        if 'genes' in params:
            path_params['genes'] = params['genes']  # noqa: E501
            collection_formats['genes'] = ''  # noqa: E501

        query_params = []
        if 'keep_non_specific' in params:
            query_params.append(('keepNonSpecific', params['keep_non_specific']))  # noqa: E501
        if 'consolidate' in params:
            query_params.append(('consolidate', params['consolidate']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{datasets}/expressions/genes/{genes}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListExperimentExpressionLevelsValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_expression_pca(self, datasets, **kwargs):  # noqa: E501
        """Retrieve the principal components (PCA) of a set of datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression_pca(datasets, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] datasets: (required)
        :param int component:
        :param int limit:
        :param bool keep_non_specific:
        :param str consolidate:
        :return: ResponseDataObjectListExperimentExpressionLevelsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_expression_pca_with_http_info(datasets, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_expression_pca_with_http_info(datasets, **kwargs)  # noqa: E501
            return data

    def get_dataset_expression_pca_with_http_info(self, datasets, **kwargs):  # noqa: E501
        """Retrieve the principal components (PCA) of a set of datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_expression_pca_with_http_info(datasets, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] datasets: (required)
        :param int component:
        :param int limit:
        :param bool keep_non_specific:
        :param str consolidate:
        :return: ResponseDataObjectListExperimentExpressionLevelsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasets', 'component', 'limit', 'keep_non_specific', 'consolidate']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_expression_pca" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'datasets' is set
        if ('datasets' not in params or
                params['datasets'] is None):
            raise ValueError("Missing the required parameter `datasets` when calling `get_dataset_expression_pca`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'datasets' in params:
            path_params['datasets'] = params['datasets']  # noqa: E501
            collection_formats['datasets'] = ''  # noqa: E501

        query_params = []
        if 'component' in params:
            query_params.append(('component', params['component']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'keep_non_specific' in params:
            query_params.append(('keepNonSpecific', params['keep_non_specific']))  # noqa: E501
        if 'consolidate' in params:
            query_params.append(('consolidate', params['consolidate']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{datasets}/expressions/pca', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListExperimentExpressionLevelsValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_platforms(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the platforms of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_platforms(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset5 dataset: (required)
        :return: ResponseDataObjectListArrayDesignValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_platforms_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_platforms_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_dataset_platforms_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the platforms of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_platforms_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset5 dataset: (required)
        :return: ResponseDataObjectListArrayDesignValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_platforms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_dataset_platforms`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}/platforms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListArrayDesignValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_processed_expression(self, dataset, **kwargs):  # noqa: E501
        """Retrieve processed expression data of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_processed_expression(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset6 dataset: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_processed_expression_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_processed_expression_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_dataset_processed_expression_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve processed expression data of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_processed_expression_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset6 dataset: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_processed_expression" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_dataset_processed_expression`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}/data/processed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_quantitation_types(self, dataset, **kwargs):  # noqa: E501
        """Retrieve quantitation types of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_quantitation_types(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset7 dataset: (required)
        :return: ResponseDataObjectSetQuantitationTypeValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_quantitation_types_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_quantitation_types_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_dataset_quantitation_types_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve quantitation types of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_quantitation_types_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset7 dataset: (required)
        :return: ResponseDataObjectSetQuantitationTypeValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_quantitation_types" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_dataset_quantitation_types`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}/quantitationTypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectSetQuantitationTypeValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_raw_expression(self, dataset, **kwargs):  # noqa: E501
        """Retrieve raw expression data of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_raw_expression(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset8 dataset: (required)
        :param QuantitationType quantitation_type:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_raw_expression_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_raw_expression_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_dataset_raw_expression_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve raw expression data of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_raw_expression_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset8 dataset: (required)
        :param QuantitationType quantitation_type:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'quantitation_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_raw_expression" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_dataset_raw_expression`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []
        if 'quantitation_type' in params:
            query_params.append(('quantitationType', params['quantitation_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}/data/raw', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_samples(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the samples of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_samples(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset9 dataset: (required)
        :return: ResponseDataObjectListBioAssayValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_samples_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_samples_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_dataset_samples_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the samples of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_samples_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset9 dataset: (required)
        :return: ResponseDataObjectListBioAssayValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_samples" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_dataset_samples`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}/samples', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListBioAssayValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_svd(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the singular value decomposition (SVD) of a dataset expression data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_svd(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset10 dataset: (required)
        :return: ResponseDataObjectSimpleSVDValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_svd_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_svd_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_dataset_svd_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the singular value decomposition (SVD) of a dataset expression data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_svd_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Dataset10 dataset: (required)
        :return: ResponseDataObjectSimpleSVDValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_svd" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_dataset_svd`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}/svd', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectSimpleSVDValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_datasets(self, **kwargs):  # noqa: E501
        """Retrieve all datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: QueriedAndFilteredAndPaginatedResponseDataObjectExpressionExperimentWithSearchResultValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_datasets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_datasets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_datasets_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: QueriedAndFilteredAndPaginatedResponseDataObjectExpressionExperimentWithSearchResultValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'filter', 'offset', 'limit', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QueriedAndFilteredAndPaginatedResponseDataObjectExpressionExperimentWithSearchResultValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_datasets_annotations_usage_statistics(self, **kwargs):  # noqa: E501
        """Retrieve usage statistics of annotations among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_annotations_usage_statistics(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :param list[str] exclude: List of fields to exclude from the payload. Only `parentTerms` can be excluded.
        :param int limit: Maximum number of annotations to returned; capped at 5000.
        :param int min_frequency: Minimum number of associated datasets to report an annotation. If used, the limit will default to 5000.
        :param str category: A category URI to restrict reported annotations. If unspecified, annotations from all categories are reported. If empty, uncategorized terms are reported.
        :return: LimitedResponseDataObjectAnnotationWithUsageStatisticsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_datasets_annotations_usage_statistics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_datasets_annotations_usage_statistics_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_datasets_annotations_usage_statistics_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve usage statistics of annotations among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_annotations_usage_statistics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :param list[str] exclude: List of fields to exclude from the payload. Only `parentTerms` can be excluded.
        :param int limit: Maximum number of annotations to returned; capped at 5000.
        :param int min_frequency: Minimum number of associated datasets to report an annotation. If used, the limit will default to 5000.
        :param str category: A category URI to restrict reported annotations. If unspecified, annotations from all categories are reported. If empty, uncategorized terms are reported.
        :return: LimitedResponseDataObjectAnnotationWithUsageStatisticsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'filter', 'exclude', 'limit', 'min_frequency', 'category']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets_annotations_usage_statistics" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'exclude' in params:
            query_params.append(('exclude', params['exclude']))  # noqa: E501
            collection_formats['exclude'] = 'multi'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'min_frequency' in params:
            query_params.append(('minFrequency', params['min_frequency']))  # noqa: E501
        if 'category' in params:
            query_params.append(('category', params['category']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/annotations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LimitedResponseDataObjectAnnotationWithUsageStatisticsValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_datasets_by_ids(self, dataset, **kwargs):  # noqa: E501
        """Retrieve datasets by their identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_by_ids(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] dataset: (required)
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_datasets_by_ids_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_datasets_by_ids_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_datasets_by_ids_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Retrieve datasets by their identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_by_ids_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] dataset: (required)
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'filter', 'offset', 'limit', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets_by_ids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_datasets_by_ids`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501
            collection_formats['dataset'] = ''  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{dataset}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_datasets_categories_usage_statistics(self, **kwargs):  # noqa: E501
        """Retrieve usage statistics of categories among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_categories_usage_statistics(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :return: QueriedAndFilteredResponseDataObjectCategoryWithUsageStatisticsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_datasets_categories_usage_statistics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_datasets_categories_usage_statistics_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_datasets_categories_usage_statistics_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve usage statistics of categories among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_categories_usage_statistics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :return: QueriedAndFilteredResponseDataObjectCategoryWithUsageStatisticsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets_categories_usage_statistics" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QueriedAndFilteredResponseDataObjectCategoryWithUsageStatisticsValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_datasets_platforms_usage_statistics(self, **kwargs):  # noqa: E501
        """Retrieve usage statistics of platforms among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_platforms_usage_statistics(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :param int limit:
        :return: LimitedResponseDataObjectArrayDesignWithUsageStatisticsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_datasets_platforms_usage_statistics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_datasets_platforms_usage_statistics_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_datasets_platforms_usage_statistics_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve usage statistics of platforms among datasets matching the provided query and filter  # noqa: E501

        Usage statistics are aggregated across experiment tags, samples and factor values mentioned in the experimental design.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_platforms_usage_statistics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :param int limit:
        :return: LimitedResponseDataObjectArrayDesignWithUsageStatisticsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets_platforms_usage_statistics" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/platforms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LimitedResponseDataObjectArrayDesignWithUsageStatisticsValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_datasets_taxa_usage_statistics(self, **kwargs):  # noqa: E501
        """Retrieve taxa usage statistics for datasets matching the provided query and filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_taxa_usage_statistics(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :return: QueriedAndFilteredResponseDataObjectTaxonWithUsageStatisticsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_datasets_taxa_usage_statistics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_datasets_taxa_usage_statistics_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_datasets_taxa_usage_statistics_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve taxa usage statistics for datasets matching the provided query and filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_datasets_taxa_usage_statistics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :return: QueriedAndFilteredResponseDataObjectTaxonWithUsageStatisticsValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets_taxa_usage_statistics" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/taxa', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QueriedAndFilteredResponseDataObjectTaxonWithUsageStatisticsValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_gene_go_terms(self, gene, **kwargs):  # noqa: E501
        """Retrieve the GO terms associated to a gene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_go_terms(gene, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Gene gene: (required)
        :return: ResponseDataObjectListGeneOntologyTermValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gene_go_terms_with_http_info(gene, **kwargs)  # noqa: E501
        else:
            (data) = self.get_gene_go_terms_with_http_info(gene, **kwargs)  # noqa: E501
            return data

    def get_gene_go_terms_with_http_info(self, gene, **kwargs):  # noqa: E501
        """Retrieve the GO terms associated to a gene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_go_terms_with_http_info(gene, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Gene gene: (required)
        :return: ResponseDataObjectListGeneOntologyTermValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gene']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gene_go_terms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gene' is set
        if ('gene' not in params or
                params['gene'] is None):
            raise ValueError("Missing the required parameter `gene` when calling `get_gene_go_terms`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gene' in params:
            path_params['gene'] = params['gene']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/genes/{gene}/goTerms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListGeneOntologyTermValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_gene_locations(self, gene, **kwargs):  # noqa: E501
        """Retrieve the physical locations of a given gene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_locations(gene, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Gene1 gene: (required)
        :return: ResponseDataObjectListPhysicalLocationValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gene_locations_with_http_info(gene, **kwargs)  # noqa: E501
        else:
            (data) = self.get_gene_locations_with_http_info(gene, **kwargs)  # noqa: E501
            return data

    def get_gene_locations_with_http_info(self, gene, **kwargs):  # noqa: E501
        """Retrieve the physical locations of a given gene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_locations_with_http_info(gene, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Gene1 gene: (required)
        :return: ResponseDataObjectListPhysicalLocationValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gene']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gene_locations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gene' is set
        if ('gene' not in params or
                params['gene'] is None):
            raise ValueError("Missing the required parameter `gene` when calling `get_gene_locations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gene' in params:
            path_params['gene'] = params['gene']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/genes/{gene}/locations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListPhysicalLocationValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_gene_locations_in_taxon(self, taxon, gene, **kwargs):  # noqa: E501
        """Retrieve physical locations for a given gene and taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_locations_in_taxon(taxon, gene, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon3 taxon: (required)
        :param Gene3 gene: (required)
        :return: ResponseDataObjectListPhysicalLocationValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gene_locations_in_taxon_with_http_info(taxon, gene, **kwargs)  # noqa: E501
        else:
            (data) = self.get_gene_locations_in_taxon_with_http_info(taxon, gene, **kwargs)  # noqa: E501
            return data

    def get_gene_locations_in_taxon_with_http_info(self, taxon, gene, **kwargs):  # noqa: E501
        """Retrieve physical locations for a given gene and taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_locations_in_taxon_with_http_info(taxon, gene, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon3 taxon: (required)
        :param Gene3 gene: (required)
        :return: ResponseDataObjectListPhysicalLocationValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['taxon', 'gene']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gene_locations_in_taxon" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'taxon' is set
        if ('taxon' not in params or
                params['taxon'] is None):
            raise ValueError("Missing the required parameter `taxon` when calling `get_gene_locations_in_taxon`")  # noqa: E501
        # verify the required parameter 'gene' is set
        if ('gene' not in params or
                params['gene'] is None):
            raise ValueError("Missing the required parameter `gene` when calling `get_gene_locations_in_taxon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'taxon' in params:
            path_params['taxon'] = params['taxon']  # noqa: E501
        if 'gene' in params:
            path_params['gene'] = params['gene']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/taxa/{taxon}/genes/{gene}/locations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListPhysicalLocationValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_gene_probes(self, gene, **kwargs):  # noqa: E501
        """Retrieve the probes associated to a genes across all platforms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_probes(gene, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Gene2 gene: (required)
        :param int offset:
        :param int limit:
        :return: FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gene_probes_with_http_info(gene, **kwargs)  # noqa: E501
        else:
            (data) = self.get_gene_probes_with_http_info(gene, **kwargs)  # noqa: E501
            return data

    def get_gene_probes_with_http_info(self, gene, **kwargs):  # noqa: E501
        """Retrieve the probes associated to a genes across all platforms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gene_probes_with_http_info(gene, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Gene2 gene: (required)
        :param int offset:
        :param int limit:
        :return: FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gene', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gene_probes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gene' is set
        if ('gene' not in params or
                params['gene'] is None):
            raise ValueError("Missing the required parameter `gene` when calling `get_gene_probes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gene' in params:
            path_params['gene'] = params['gene']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/genes/{gene}/probes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_genes(self, genes, **kwargs):  # noqa: E501
        """Retrieve genes matching gene identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_genes(genes, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] genes: (required)
        :return: ResponseDataObjectListGeneValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_genes_with_http_info(genes, **kwargs)  # noqa: E501
        else:
            (data) = self.get_genes_with_http_info(genes, **kwargs)  # noqa: E501
            return data

    def get_genes_with_http_info(self, genes, **kwargs):  # noqa: E501
        """Retrieve genes matching gene identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_genes_with_http_info(genes, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] genes: (required)
        :return: ResponseDataObjectListGeneValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['genes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_genes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'genes' is set
        if ('genes' not in params or
                params['genes'] is None):
            raise ValueError("Missing the required parameter `genes` when calling `get_genes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'genes' in params:
            path_params['genes'] = params['genes']  # noqa: E501
            collection_formats['genes'] = ''  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/genes/{genes}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListGeneValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_number_of_datasets(self, **kwargs):  # noqa: E501
        """Count datasets matching the provided query and  filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_datasets(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :return: ResponseDataObjectLong
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_number_of_datasets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_number_of_datasets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_number_of_datasets_with_http_info(self, **kwargs):  # noqa: E501
        """Count datasets matching the provided query and  filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_datasets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param FilterArgExpressionExperiment filter:
        :return: ResponseDataObjectLong
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_number_of_datasets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectLong',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_number_of_platforms(self, **kwargs):  # noqa: E501
        """Count platforms matching the provided filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_platforms(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param FilterArgArrayDesign filter:
        :return: ResponseDataObjectLong
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_number_of_platforms_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_number_of_platforms_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_number_of_platforms_with_http_info(self, **kwargs):  # noqa: E501
        """Count platforms matching the provided filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_platforms_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param FilterArgArrayDesign filter:
        :return: ResponseDataObjectLong
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_number_of_platforms" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platforms/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectLong',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_number_of_result_sets(self, **kwargs):  # noqa: E501
        """Count result sets matching the provided filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_result_sets(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param FilterArgExpressionAnalysisResultSet filter:
        :return: ResponseDataObjectLong
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_number_of_result_sets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_number_of_result_sets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_number_of_result_sets_with_http_info(self, **kwargs):  # noqa: E501
        """Count result sets matching the provided filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_number_of_result_sets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param FilterArgExpressionAnalysisResultSet filter:
        :return: ResponseDataObjectLong
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_number_of_result_sets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/resultSets/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectLong',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_platform_annotations(self, platform, **kwargs):  # noqa: E501
        """Retrieve the annotations of a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_annotations(platform, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Platform platform: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_platform_annotations_with_http_info(platform, **kwargs)  # noqa: E501
        else:
            (data) = self.get_platform_annotations_with_http_info(platform, **kwargs)  # noqa: E501
            return data

    def get_platform_annotations_with_http_info(self, platform, **kwargs):  # noqa: E501
        """Retrieve the annotations of a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_annotations_with_http_info(platform, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Platform platform: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platform_annotations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'platform' is set
        if ('platform' not in params or
                params['platform'] is None):
            raise ValueError("Missing the required parameter `platform` when calling `get_platform_annotations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'platform' in params:
            path_params['platform'] = params['platform']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platforms/{platform}/annotations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_platform_datasets(self, platform, **kwargs):  # noqa: E501
        """Retrieve all experiments using a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_datasets(platform, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Platform1 platform: (required)
        :param int offset:
        :param int limit:
        :return: PaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_platform_datasets_with_http_info(platform, **kwargs)  # noqa: E501
        else:
            (data) = self.get_platform_datasets_with_http_info(platform, **kwargs)  # noqa: E501
            return data

    def get_platform_datasets_with_http_info(self, platform, **kwargs):  # noqa: E501
        """Retrieve all experiments using a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_datasets_with_http_info(platform, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Platform1 platform: (required)
        :param int offset:
        :param int limit:
        :return: PaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platform_datasets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'platform' is set
        if ('platform' not in params or
                params['platform'] is None):
            raise ValueError("Missing the required parameter `platform` when calling `get_platform_datasets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'platform' in params:
            path_params['platform'] = params['platform']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platforms/{platform}/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedResponseDataObjectExpressionExperimentValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_platform_element(self, platform, probes, **kwargs):  # noqa: E501
        """Retrieve the selected probes for a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_element(platform, probes, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Platform2 platform: (required)
        :param list[object] probes: (required)
        :param int offset:
        :param int limit:
        :return: FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_platform_element_with_http_info(platform, probes, **kwargs)  # noqa: E501
        else:
            (data) = self.get_platform_element_with_http_info(platform, probes, **kwargs)  # noqa: E501
            return data

    def get_platform_element_with_http_info(self, platform, probes, **kwargs):  # noqa: E501
        """Retrieve the selected probes for a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_element_with_http_info(platform, probes, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Platform2 platform: (required)
        :param list[object] probes: (required)
        :param int offset:
        :param int limit:
        :return: FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform', 'probes', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platform_element" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'platform' is set
        if ('platform' not in params or
                params['platform'] is None):
            raise ValueError("Missing the required parameter `platform` when calling `get_platform_element`")  # noqa: E501
        # verify the required parameter 'probes' is set
        if ('probes' not in params or
                params['probes'] is None):
            raise ValueError("Missing the required parameter `probes` when calling `get_platform_element`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'platform' in params:
            path_params['platform'] = params['platform']  # noqa: E501
        if 'probes' in params:
            path_params['probes'] = params['probes']  # noqa: E501
            collection_formats['probes'] = ''  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platforms/{platform}/elements/{probes}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectCompositeSequenceValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_platform_element_genes(self, platform, probe, **kwargs):  # noqa: E501
        """Retrieve the genes associated to a probe in a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_element_genes(platform, probe, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Platform3 platform: (required)
        :param Probe probe: (required)
        :param int offset:
        :param int limit:
        :return: FilteredAndPaginatedResponseDataObjectGeneValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_platform_element_genes_with_http_info(platform, probe, **kwargs)  # noqa: E501
        else:
            (data) = self.get_platform_element_genes_with_http_info(platform, probe, **kwargs)  # noqa: E501
            return data

    def get_platform_element_genes_with_http_info(self, platform, probe, **kwargs):  # noqa: E501
        """Retrieve the genes associated to a probe in a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_element_genes_with_http_info(platform, probe, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Platform3 platform: (required)
        :param Probe probe: (required)
        :param int offset:
        :param int limit:
        :return: FilteredAndPaginatedResponseDataObjectGeneValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform', 'probe', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platform_element_genes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'platform' is set
        if ('platform' not in params or
                params['platform'] is None):
            raise ValueError("Missing the required parameter `platform` when calling `get_platform_element_genes`")  # noqa: E501
        # verify the required parameter 'probe' is set
        if ('probe' not in params or
                params['probe'] is None):
            raise ValueError("Missing the required parameter `probe` when calling `get_platform_element_genes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'platform' in params:
            path_params['platform'] = params['platform']  # noqa: E501
        if 'probe' in params:
            path_params['probe'] = params['probe']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platforms/{platform}/elements/{probe}/genes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectGeneValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_platform_elements(self, platform, **kwargs):  # noqa: E501
        """Retrieve the probes for a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_elements(platform, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Platform4 platform: (required)
        :param int offset:
        :param int limit:
        :return: PaginatedResponseDataObjectCompositeSequenceValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_platform_elements_with_http_info(platform, **kwargs)  # noqa: E501
        else:
            (data) = self.get_platform_elements_with_http_info(platform, **kwargs)  # noqa: E501
            return data

    def get_platform_elements_with_http_info(self, platform, **kwargs):  # noqa: E501
        """Retrieve the probes for a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_elements_with_http_info(platform, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Platform4 platform: (required)
        :param int offset:
        :param int limit:
        :return: PaginatedResponseDataObjectCompositeSequenceValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platform_elements" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'platform' is set
        if ('platform' not in params or
                params['platform'] is None):
            raise ValueError("Missing the required parameter `platform` when calling `get_platform_elements`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'platform' in params:
            path_params['platform'] = params['platform']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platforms/{platform}/elements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedResponseDataObjectCompositeSequenceValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_platforms(self, **kwargs):  # noqa: E501
        """Retrieve all platforms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platforms(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param FilterArgArrayDesign filter:
        :param int offset:
        :param int limit:
        :param SortArgArrayDesign sort:
        :return: FilteredAndPaginatedResponseDataObjectArrayDesignValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_platforms_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_platforms_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_platforms_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all platforms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platforms_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param FilterArgArrayDesign filter:
        :param int offset:
        :param int limit:
        :param SortArgArrayDesign sort:
        :return: FilteredAndPaginatedResponseDataObjectArrayDesignValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'offset', 'limit', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platforms" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platforms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectArrayDesignValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_platforms_by_ids(self, platform, **kwargs):  # noqa: E501
        """Retrieve all platforms matching a set of platform identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platforms_by_ids(platform, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] platform: (required)
        :param FilterArgArrayDesign filter:
        :param int offset:
        :param int limit:
        :param SortArgArrayDesign sort:
        :return: FilteredAndPaginatedResponseDataObjectArrayDesignValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_platforms_by_ids_with_http_info(platform, **kwargs)  # noqa: E501
        else:
            (data) = self.get_platforms_by_ids_with_http_info(platform, **kwargs)  # noqa: E501
            return data

    def get_platforms_by_ids_with_http_info(self, platform, **kwargs):  # noqa: E501
        """Retrieve all platforms matching a set of platform identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platforms_by_ids_with_http_info(platform, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] platform: (required)
        :param FilterArgArrayDesign filter:
        :param int offset:
        :param int limit:
        :param SortArgArrayDesign sort:
        :return: FilteredAndPaginatedResponseDataObjectArrayDesignValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform', 'filter', 'offset', 'limit', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_platforms_by_ids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'platform' is set
        if ('platform' not in params or
                params['platform'] is None):
            raise ValueError("Missing the required parameter `platform` when calling `get_platforms_by_ids`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'platform' in params:
            path_params['platform'] = params['platform']  # noqa: E501
            collection_formats['platform'] = ''  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platforms/{platform}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectArrayDesignValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_result_set(self, result_set, **kwargs):  # noqa: E501
        """Retrieve a single analysis result set by its identifier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_set(result_set, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param int result_set: (required)
        :return: ResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_result_set_with_http_info(result_set, **kwargs)  # noqa: E501
        else:
            (data) = self.get_result_set_with_http_info(result_set, **kwargs)  # noqa: E501
            return data

    def get_result_set_with_http_info(self, result_set, **kwargs):  # noqa: E501
        """Retrieve a single analysis result set by its identifier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_set_with_http_info(result_set, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param int result_set: (required)
        :return: ResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['result_set']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'result_set' is set
        if ('result_set' not in params or
                params['result_set'] is None):
            raise ValueError("Missing the required parameter `result_set` when calling `get_result_set`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'result_set' in params:
            path_params['resultSet'] = params['result_set']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/resultSets/{resultSet}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_result_set_as_tsv(self, result_set_, **kwargs):  # noqa: E501
        """Retrieve a single analysis result set by its identifier as a tab-separated values  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_set_as_tsv(result_set_, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param int result_set_: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_result_set_as_tsv_with_http_info(result_set_, **kwargs)  # noqa: E501
        else:
            (data) = self.get_result_set_as_tsv_with_http_info(result_set_, **kwargs)  # noqa: E501
            return data

    def get_result_set_as_tsv_with_http_info(self, result_set_, **kwargs):  # noqa: E501
        """Retrieve a single analysis result set by its identifier as a tab-separated values  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_set_as_tsv_with_http_info(result_set_, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param int result_set_: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['result_set_']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_set_as_tsv" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'result_set_' is set
        if ('result_set_' not in params or
                params['result_set_'] is None):
            raise ValueError("Missing the required parameter `result_set_` when calling `get_result_set_as_tsv`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'result_set_' in params:
            path_params['resultSet_'] = params['result_set_']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/resultSets/{resultSet_}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_result_sets(self, **kwargs):  # noqa: E501
        """Retrieve all result sets matching the provided criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_sets(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] datasets:
        :param list[object] database_entries:
        :param FilterArgExpressionAnalysisResultSet filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionAnalysisResultSet sort:
        :return: FilteredAndPaginatedResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_result_sets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_result_sets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_result_sets_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all result sets matching the provided criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result_sets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] datasets:
        :param list[object] database_entries:
        :param FilterArgExpressionAnalysisResultSet filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionAnalysisResultSet sort:
        :return: FilteredAndPaginatedResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasets', 'database_entries', 'filter', 'offset', 'limit', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_sets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasets' in params:
            query_params.append(('datasets', params['datasets']))  # noqa: E501
            collection_formats['datasets'] = 'csv'  # noqa: E501
        if 'database_entries' in params:
            query_params.append(('databaseEntries', params['database_entries']))  # noqa: E501
            collection_formats['databaseEntries'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/resultSets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectDifferentialExpressionAnalysisResultSetValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_taxa(self, **kwargs):  # noqa: E501
        """Retrieve all available taxa  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxa(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :return: ResponseDataObjectListTaxonValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_taxa_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_taxa_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_taxa_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all available taxa  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxa_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :return: ResponseDataObjectListTaxonValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_taxa" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/taxa', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListTaxonValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_taxa_by_ids(self, taxa, **kwargs):  # noqa: E501
        """Retrieve taxa by their identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxa_by_ids(taxa, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] taxa: (required)
        :return: ResponseDataObjectListTaxonValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_taxa_by_ids_with_http_info(taxa, **kwargs)  # noqa: E501
        else:
            (data) = self.get_taxa_by_ids_with_http_info(taxa, **kwargs)  # noqa: E501
            return data

    def get_taxa_by_ids_with_http_info(self, taxa, **kwargs):  # noqa: E501
        """Retrieve taxa by their identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxa_by_ids_with_http_info(taxa, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[object] taxa: (required)
        :return: ResponseDataObjectListTaxonValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['taxa']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_taxa_by_ids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'taxa' is set
        if ('taxa' not in params or
                params['taxa'] is None):
            raise ValueError("Missing the required parameter `taxa` when calling `get_taxa_by_ids`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'taxa' in params:
            path_params['taxa'] = params['taxa']  # noqa: E501
            collection_formats['taxa'] = ''  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/taxa/{taxa}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListTaxonValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_taxon_datasets(self, taxon, **kwargs):  # noqa: E501
        """Retrieve the datasets for a given taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_datasets(taxon, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon4 taxon: (required)
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgTaxon sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_taxon_datasets_with_http_info(taxon, **kwargs)  # noqa: E501
        else:
            (data) = self.get_taxon_datasets_with_http_info(taxon, **kwargs)  # noqa: E501
            return data

    def get_taxon_datasets_with_http_info(self, taxon, **kwargs):  # noqa: E501
        """Retrieve the datasets for a given taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_datasets_with_http_info(taxon, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon4 taxon: (required)
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgTaxon sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['taxon', 'filter', 'offset', 'limit', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_taxon_datasets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'taxon' is set
        if ('taxon' not in params or
                params['taxon'] is None):
            raise ValueError("Missing the required parameter `taxon` when calling `get_taxon_datasets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'taxon' in params:
            path_params['taxon'] = params['taxon']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/taxa/{taxon}/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_taxon_genes(self, taxon, gene, **kwargs):  # noqa: E501
        """Retrieve all genes in a given taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_genes(taxon, gene, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon5 taxon: (required)
        :param Gene4 gene: (required)
        :return: ResponseDataObjectListGeneValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_taxon_genes_with_http_info(taxon, gene, **kwargs)  # noqa: E501
        else:
            (data) = self.get_taxon_genes_with_http_info(taxon, gene, **kwargs)  # noqa: E501
            return data

    def get_taxon_genes_with_http_info(self, taxon, gene, **kwargs):  # noqa: E501
        """Retrieve all genes in a given taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_genes_with_http_info(taxon, gene, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon5 taxon: (required)
        :param Gene4 gene: (required)
        :return: ResponseDataObjectListGeneValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['taxon', 'gene']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_taxon_genes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'taxon' is set
        if ('taxon' not in params or
                params['taxon'] is None):
            raise ValueError("Missing the required parameter `taxon` when calling `get_taxon_genes`")  # noqa: E501
        # verify the required parameter 'gene' is set
        if ('gene' not in params or
                params['gene'] is None):
            raise ValueError("Missing the required parameter `gene` when calling `get_taxon_genes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'taxon' in params:
            path_params['taxon'] = params['taxon']  # noqa: E501
        if 'gene' in params:
            path_params['gene'] = params['gene']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/taxa/{taxon}/genes/{gene}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListGeneValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_taxon_genes_overlapping_chromosome(self, taxon, chromosome, start, size, **kwargs):  # noqa: E501
        """Retrieve genes overlapping a given region in a taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_genes_overlapping_chromosome(taxon, chromosome, start, size, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon6 taxon: (required)
        :param str chromosome: (required)
        :param int start: (required)
        :param int size: (required)
        :param str strand:
        :return: ResponseDataObjectListGeneValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_taxon_genes_overlapping_chromosome_with_http_info(taxon, chromosome, start, size, **kwargs)  # noqa: E501
        else:
            (data) = self.get_taxon_genes_overlapping_chromosome_with_http_info(taxon, chromosome, start, size, **kwargs)  # noqa: E501
            return data

    def get_taxon_genes_overlapping_chromosome_with_http_info(self, taxon, chromosome, start, size, **kwargs):  # noqa: E501
        """Retrieve genes overlapping a given region in a taxon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_taxon_genes_overlapping_chromosome_with_http_info(taxon, chromosome, start, size, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon6 taxon: (required)
        :param str chromosome: (required)
        :param int start: (required)
        :param int size: (required)
        :param str strand:
        :return: ResponseDataObjectListGeneValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['taxon', 'chromosome', 'start', 'size', 'strand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_taxon_genes_overlapping_chromosome" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'taxon' is set
        if ('taxon' not in params or
                params['taxon'] is None):
            raise ValueError("Missing the required parameter `taxon` when calling `get_taxon_genes_overlapping_chromosome`")  # noqa: E501
        # verify the required parameter 'chromosome' is set
        if ('chromosome' not in params or
                params['chromosome'] is None):
            raise ValueError("Missing the required parameter `chromosome` when calling `get_taxon_genes_overlapping_chromosome`")  # noqa: E501
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `get_taxon_genes_overlapping_chromosome`")  # noqa: E501
        # verify the required parameter 'size' is set
        if ('size' not in params or
                params['size'] is None):
            raise ValueError("Missing the required parameter `size` when calling `get_taxon_genes_overlapping_chromosome`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'taxon' in params:
            path_params['taxon'] = params['taxon']  # noqa: E501
        if 'chromosome' in params:
            path_params['chromosome'] = params['chromosome']  # noqa: E501

        query_params = []
        if 'strand' in params:
            query_params.append(('strand', params['strand']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/taxa/{taxon}/chromosomes/{chromosome}/genes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListGeneValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search(self, **kwargs):  # noqa: E501
        """Search everything in Gemma  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param Taxon2 taxon:
        :param Platform5 platform:
        :param list[str] result_types:
        :param int limit: Maximum number of search results to return; capped at 2000 unless `resultObject` is excluded.
        :param list[str] exclude: List of fields to exclude from the payload. Only `resultObject` is supported.
        :return: SearchResultsResponseDataObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_with_http_info(self, **kwargs):  # noqa: E501
        """Search everything in Gemma  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param str query:
        :param Taxon2 taxon:
        :param Platform5 platform:
        :param list[str] result_types:
        :param int limit: Maximum number of search results to return; capped at 2000 unless `resultObject` is excluded.
        :param list[str] exclude: List of fields to exclude from the payload. Only `resultObject` is supported.
        :return: SearchResultsResponseDataObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'taxon', 'platform', 'result_types', 'limit', 'exclude']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'taxon' in params:
            query_params.append(('taxon', params['taxon']))  # noqa: E501
        if 'platform' in params:
            query_params.append(('platform', params['platform']))  # noqa: E501
        if 'result_types' in params:
            query_params.append(('resultTypes', params['result_types']))  # noqa: E501
            collection_formats['resultTypes'] = 'multi'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'exclude' in params:
            query_params.append(('exclude', params['exclude']))  # noqa: E501
            collection_formats['exclude'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchResultsResponseDataObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_annotations(self, **kwargs):  # noqa: E501
        """Search for annotation tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_annotations(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[str] query:
        :return: ResponseDataObjectListAnnotationSearchResultValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_annotations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_annotations_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_annotations_with_http_info(self, **kwargs):  # noqa: E501
        """Search for annotation tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_annotations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[str] query:
        :return: ResponseDataObjectListAnnotationSearchResultValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_annotations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
            collection_formats['query'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/annotations/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListAnnotationSearchResultValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_annotations_by_path_query(self, query, **kwargs):  # noqa: E501
        """Search for annotation tags  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_annotations_by_path_query(query, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[str] query: (required)
        :return: ResponseDataObjectListAnnotationSearchResultValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_annotations_by_path_query_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_annotations_by_path_query_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_annotations_by_path_query_with_http_info(self, query, **kwargs):  # noqa: E501
        """Search for annotation tags  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_annotations_by_path_query_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[str] query: (required)
        :return: ResponseDataObjectListAnnotationSearchResultValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_annotations_by_path_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_annotations_by_path_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'query' in params:
            path_params['query'] = params['query']  # noqa: E501
            collection_formats['query'] = ''  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/annotations/search/{query}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDataObjectListAnnotationSearchResultValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_datasets(self, **kwargs):  # noqa: E501
        """Retrieve datasets associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of the getDatasets() endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_datasets(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[str] query:
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_datasets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_datasets_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_datasets_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve datasets associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of the getDatasets() endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_datasets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[str] query:
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'filter', 'offset', 'limit', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_datasets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
            collection_formats['query'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/annotations/search/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_datasets_by_query_in_path(self, query, **kwargs):  # noqa: E501
        """Retrieve datasets associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_datasets_by_query_in_path(query, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[str] query: (required)
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_datasets_by_query_in_path_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_datasets_by_query_in_path_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_datasets_by_query_in_path_with_http_info(self, query, **kwargs):  # noqa: E501
        """Retrieve datasets associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_datasets_by_query_in_path_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param list[str] query: (required)
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'filter', 'offset', 'limit', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_datasets_by_query_in_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_datasets_by_query_in_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'query' in params:
            path_params['query'] = params['query']  # noqa: E501
            collection_formats['query'] = ''  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/annotations/search/{query}/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_taxon_datasets(self, taxon, **kwargs):  # noqa: E501
        """Retrieve datasets within a given taxa associated to an annotation tags search  # noqa: E501

        Use getDatasets() with a `query` parameter and a `filter` parameter with `taxon.id = {taxon} or taxon.commonName = {taxon} or taxon.scientificName = {taxon}` to restrict the taxon instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_taxon_datasets(taxon, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon taxon: (required)
        :param list[str] query:
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_taxon_datasets_with_http_info(taxon, **kwargs)  # noqa: E501
        else:
            (data) = self.search_taxon_datasets_with_http_info(taxon, **kwargs)  # noqa: E501
            return data

    def search_taxon_datasets_with_http_info(self, taxon, **kwargs):  # noqa: E501
        """Retrieve datasets within a given taxa associated to an annotation tags search  # noqa: E501

        Use getDatasets() with a `query` parameter and a `filter` parameter with `taxon.id = {taxon} or taxon.commonName = {taxon} or taxon.scientificName = {taxon}` to restrict the taxon instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_taxon_datasets_with_http_info(taxon, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon taxon: (required)
        :param list[str] query:
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['taxon', 'query', 'filter', 'offset', 'limit', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_taxon_datasets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'taxon' is set
        if ('taxon' not in params or
                params['taxon'] is None):
            raise ValueError("Missing the required parameter `taxon` when calling `search_taxon_datasets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'taxon' in params:
            path_params['taxon'] = params['taxon']  # noqa: E501

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
            collection_formats['query'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/annotations/{taxon}/search/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_taxon_datasets_by_query_in_path(self, taxon, query, **kwargs):  # noqa: E501
        """Retrieve datasets within a given taxa associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_taxon_datasets_by_query_in_path(taxon, query, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon1 taxon: (required)
        :param list[str] query: (required)
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_taxon_datasets_by_query_in_path_with_http_info(taxon, query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_taxon_datasets_by_query_in_path_with_http_info(taxon, query, **kwargs)  # noqa: E501
            return data

    def search_taxon_datasets_by_query_in_path_with_http_info(self, taxon, query, **kwargs):  # noqa: E501
        """Retrieve datasets within a given taxa associated to an annotation tags search  # noqa: E501

        This is deprecated in favour of passing `query` as a query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_taxon_datasets_by_query_in_path_with_http_info(taxon, query, async_req=True)
        >>> result = thread.get()

        :param bool async_req:
        :param Taxon1 taxon: (required)
        :param list[str] query: (required)
        :param FilterArgExpressionExperiment filter:
        :param int offset:
        :param int limit:
        :param SortArgExpressionExperiment sort:
        :return: FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['taxon', 'query', 'filter', 'offset', 'limit', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_taxon_datasets_by_query_in_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'taxon' is set
        if ('taxon' not in params or
                params['taxon'] is None):
            raise ValueError("Missing the required parameter `taxon` when calling `search_taxon_datasets_by_query_in_path`")  # noqa: E501
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_taxon_datasets_by_query_in_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'taxon' in params:
            path_params['taxon'] = params['taxon']  # noqa: E501
        if 'query' in params:
            path_params['query'] = params['query']  # noqa: E501
            collection_formats['query'] = ''  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/annotations/{taxon}/search/{query}/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilteredAndPaginatedResponseDataObjectExpressionExperimentValueObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
