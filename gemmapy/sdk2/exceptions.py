# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  ## Updates  ### Update 2.7.1  - improved highlights of search results - fix the limit for getDatasetsAnnotations() endpoint to 5000 in the specification - fix missing initialization of datasets retrieved from the cache  Highlights now use Markdown syntax for formatting. Fields for highlighted ontology terms now use complete object path instead of just `term`. Last but not least, highlights from multiple results are merged.  ### Update 2.7.0  New endpoints for counting the number of results: `getNumberOfDatasets`, `getNumberOfPlatforms`, `getNumberOfResultSets`. These endpoints are faster than looking up `totalElements` as no data is retrieved or converted.  Datasets can now be filtered by annotations at the sample, factor value and all levels using the three newly exposed `experimentalDesign.experimentalFactors.factorValues.characteristics`, `bioAssays.sampleUsed.characteristics` and `allCharacteristics` collections. The two useful available properties for filtering are `value` and `valueUri`.  New `getDatasetsAnnotationsUsageStatistics`, `getDatasetsPlatformsUsageStatistics` and `getDatasetsTaxaUsageStatistics` endpoints for retrieving annotations, platforms and taxa used by the matched datasets. The endpoint accepts the same `filter` argument of `getDatasets`, allowing one to easily navigate terms, platforms and taxa available for filtering furthermore.  Properties available for filtering and sorting are enumerated in the description of the corresponding parameter. There's been a number of fixes and additional tests performed to ensure that all advertised properties are working as expected.  The `FilterArg` and `SortArg`-based parameters now have OpenAPI extensions to enumerate available properties in a structured format under the `x-gemma-filterable-properties`key. Possible values are exposed for enumerated types.  ```yaml x-gemma-filterable-properties: - name: technologyType   type: string   allowedValues:   - value: ONECOLOR     label: One Color   - value: SEQUENCING     label: Sequencing   security:     basicAuth: [GROUP_ADMIN]     cookieAuth: [GROUP_ADMIN] ```  Some of the exposed properties such as `geeq.publicSuitabilityScore` require specific authorities to use. This is documented in `x-filterable-properties` by specifying a [Security Requirement Object](https://spec.openapis.org/oas/latest.html#security-requirement-object).  Types that use the `[]` suffix are using sub-queries under the hood. It implies that the entity will be matched if at least one related entity matches the supplied filter. For example, the `characteristics.valueUri = http://purl.obolibrary.org/obo/UBERON_0002107` filter will match datasets with at least one `UBERON:0002107` tag attached.  Filtered endpoints (including paginated and limited ones) now expose a `groupBy` array that enumerates all the properties used to group results. This helps clear confusion about what constitute a business key in the returned response.  ### Update 2.6.1  Add support for filtering platforms by taxon ID, common name, scientific name, etc. for the `/platforms` endpoint.  ### Update 2.6.0  Add a new `externalDatabases` attribute to the main endpoint that displays version of some of the main external databases that we are using. This exposes versions and last updates for genomes, gene annotations, GO terms, and much more!  The `ExternalDatabaseValueObject` now exposes a `description` which provides additional details.  ### Update 2.5.2  Restore `factors` in `BioMaterialValueObject` as it is being still used by our RNA-Seq pipeline. The attribute is deprecated and should not be used and will be removed when we find a suitable alternative.  Introduce a new endpoint to retrieve quantitation types for a given dataset and parameters to retrieve expression data by quantitation type to `getDatasetProcessedExpression` and `getDatasetRawExpression`. As it was too difficult to extends `getDatasetExpression` to also support quantitation type while retaining the filter feature, we decided to deprecate it and reintroduce filtering for both raw and processed expression in the future.  Fix return type for `getResultSets` which was incorrectly referring to a renamed VO.  Annotate all possible types for `SearchResult.resultObject`. This incidentally includes the `GeneSetValueObject` in the specification which is not exposed elsewhere in the API.  ### Update 2.5.1  Restore `objectClass` visibility in `AnnotationValueObject`.  Fix incorrect response types for annotations search endpoints returning datasets.  ### Update 2.5.0  Major cleanups were performed in this release in order to stabilize the specification. Numerous properties from Gemma Web that were never intended to be exposed in Gemma REST have been hidden. It's a bit too much to describe in here, but you can navigate to the schemas section below to get a good glance at the models.  Favour `numberOfSomething` instead of `somethingCount` which is clearer. The older names are kept for backward-compatibility, but should be considered deprecated.  Gene aliases and multifunctionality rank are now filled in `GeneValueObject`.  Uniformly use `TaxonValueObject` to represent taxon. This is breaking change for the `ExpressionExperimentValueObject` and `ArrayDesignValueObject` as their `taxon` property will be an `object` instead of a `string`. Properties such as `taxonId` are now deprecated and `taxon.id` should be used instead.  Entities that have IDs now all inherit from `IdentifiableValueObject`. This implies that you can assume the presence of an `id` in a search result `resultObject` attribute for example.  New `/search` endpoint! for an unified search experience. Annotation-based search endpoints under `/annotations` are now deprecated.  New API docs! While not as nice looking, the previous theme will be gradually ported to Swagger UI as we focused on functionality over prettiness for this release.  ### Update 2.4.0 through 2.4.1  Release notes for the 2.4 series were not written down, so I'll try to do my best to recall features that were introduced at that time.  An [OpenAPI](https://www.openapis.org/) specification was introduced and available under `/rest/v2/openapi.json`, although not fully stabilized.  Add a `/resultSets` endpoint to navigate result sets directly, by ID or by dataset.  Add a `/resultSets/{resultSetId}` endpoint to retrieve a specific result set by its ID. This endpoint can be negotiated with an `Accept: text/tab-separated-values` header to obtain a TSV representation.  Add a `/datasets/{dataset}/analyses/differential/resultSets` endpoint that essentially redirect to a specific `/resultSet` endpoint by dataset ID.  Add an endpoint to retrieve preferred raw expression vectors.  ### Update 2.3.4  November 6th, 2018  November 6th [2.3.4] Bug fixes in the dataset search endpoint.  November 5th [2.3.3] Added filtering parameters to dataset search.  October 25th [2.3.2] Changed behavior of the dataset search endpoint to more closely match the Gemma web interface.  October 2nd [2.3.1] Added group information to the User value object.  September 27th [2.3.0] Breaking change in Taxa: Abbreviation property has been removed and is therefore no longer an accepted identifier.  ### Update 2.2.6  June 7th, 2018  Code maintenance, bug fixes. Geeq scores stable and made public.  June 7th [2.2.6] Added: User authentication endpoint.  May 2nd [2.2.5] Fixed: Cleaned up and optimized platforms/elements endpoint, removed redundant information (recursive properties nesting).  April 12th [2.2.3] Fixed: Array arguments not handling non-string properties properly, e.g. `ncbiIds` of genes.  April 9th [2.2.1] Fixed: Filter argument not working when the filtered field was a primitive type. This most significantly allows filtering by geeq boolean and double properties.  ### Update 2.2.0  February 8th, 2018  Breaking change in the 'Dataset differential analysis' endpoint: - No longer using `qValueThreshold` parameter. - Response format changed, now using `DifferentialExpressionAnalysisValueObject` instead of `DifferentialExpressionValueObject` - [Experimental] Added Geeq (Gene Expression Experiment Quality) scores to the dataset value objects 

    The version of the OpenAPI document: 2.7.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None,
                 key_type=None) -> None:
        """ Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiAttributeError(OpenApiException, AttributeError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Raised when an attribute reference or assignment fails.

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiAttributeError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiException(OpenApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message

class BadRequestException(ApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        super(BadRequestException, self).__init__(status, reason, http_resp)

class NotFoundException(ApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        super(NotFoundException, self).__init__(status, reason, http_resp)


class UnauthorizedException(ApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        super(UnauthorizedException, self).__init__(status, reason, http_resp)


class ForbiddenException(ApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        super(ForbiddenException, self).__init__(status, reason, http_resp)


class ServiceException(ApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        super(ServiceException, self).__init__(status, reason, http_resp)


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, int):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result
