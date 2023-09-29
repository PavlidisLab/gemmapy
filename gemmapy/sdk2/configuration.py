# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  ## Updates  ### Update 2.7.1  - improved highlights of search results - fix the limit for getDatasetsAnnotations() endpoint to 5000 in the specification - fix missing initialization of datasets retrieved from the cache  Highlights now use Markdown syntax for formatting. Fields for highlighted ontology terms now use complete object path instead of just `term`. Last but not least, highlights from multiple results are merged.  ### Update 2.7.0  New endpoints for counting the number of results: `getNumberOfDatasets`, `getNumberOfPlatforms`, `getNumberOfResultSets`. These endpoints are faster than looking up `totalElements` as no data is retrieved or converted.  Datasets can now be filtered by annotations at the sample, factor value and all levels using the three newly exposed `experimentalDesign.experimentalFactors.factorValues.characteristics`, `bioAssays.sampleUsed.characteristics` and `allCharacteristics` collections. The two useful available properties for filtering are `value` and `valueUri`.  New `getDatasetsAnnotationsUsageStatistics`, `getDatasetsPlatformsUsageStatistics` and `getDatasetsTaxaUsageStatistics` endpoints for retrieving annotations, platforms and taxa used by the matched datasets. The endpoint accepts the same `filter` argument of `getDatasets`, allowing one to easily navigate terms, platforms and taxa available for filtering furthermore.  Properties available for filtering and sorting are enumerated in the description of the corresponding parameter. There's been a number of fixes and additional tests performed to ensure that all advertised properties are working as expected.  The `FilterArg` and `SortArg`-based parameters now have OpenAPI extensions to enumerate available properties in a structured format under the `x-gemma-filterable-properties`key. Possible values are exposed for enumerated types.  ```yaml x-gemma-filterable-properties: - name: technologyType   type: string   allowedValues:   - value: ONECOLOR     label: One Color   - value: SEQUENCING     label: Sequencing   security:     basicAuth: [GROUP_ADMIN]     cookieAuth: [GROUP_ADMIN] ```  Some of the exposed properties such as `geeq.publicSuitabilityScore` require specific authorities to use. This is documented in `x-filterable-properties` by specifying a [Security Requirement Object](https://spec.openapis.org/oas/latest.html#security-requirement-object).  Types that use the `[]` suffix are using sub-queries under the hood. It implies that the entity will be matched if at least one related entity matches the supplied filter. For example, the `characteristics.valueUri = http://purl.obolibrary.org/obo/UBERON_0002107` filter will match datasets with at least one `UBERON:0002107` tag attached.  Filtered endpoints (including paginated and limited ones) now expose a `groupBy` array that enumerates all the properties used to group results. This helps clear confusion about what constitute a business key in the returned response.  ### Update 2.6.1  Add support for filtering platforms by taxon ID, common name, scientific name, etc. for the `/platforms` endpoint.  ### Update 2.6.0  Add a new `externalDatabases` attribute to the main endpoint that displays version of some of the main external databases that we are using. This exposes versions and last updates for genomes, gene annotations, GO terms, and much more!  The `ExternalDatabaseValueObject` now exposes a `description` which provides additional details.  ### Update 2.5.2  Restore `factors` in `BioMaterialValueObject` as it is being still used by our RNA-Seq pipeline. The attribute is deprecated and should not be used and will be removed when we find a suitable alternative.  Introduce a new endpoint to retrieve quantitation types for a given dataset and parameters to retrieve expression data by quantitation type to `getDatasetProcessedExpression` and `getDatasetRawExpression`. As it was too difficult to extends `getDatasetExpression` to also support quantitation type while retaining the filter feature, we decided to deprecate it and reintroduce filtering for both raw and processed expression in the future.  Fix return type for `getResultSets` which was incorrectly referring to a renamed VO.  Annotate all possible types for `SearchResult.resultObject`. This incidentally includes the `GeneSetValueObject` in the specification which is not exposed elsewhere in the API.  ### Update 2.5.1  Restore `objectClass` visibility in `AnnotationValueObject`.  Fix incorrect response types for annotations search endpoints returning datasets.  ### Update 2.5.0  Major cleanups were performed in this release in order to stabilize the specification. Numerous properties from Gemma Web that were never intended to be exposed in Gemma REST have been hidden. It's a bit too much to describe in here, but you can navigate to the schemas section below to get a good glance at the models.  Favour `numberOfSomething` instead of `somethingCount` which is clearer. The older names are kept for backward-compatibility, but should be considered deprecated.  Gene aliases and multifunctionality rank are now filled in `GeneValueObject`.  Uniformly use `TaxonValueObject` to represent taxon. This is breaking change for the `ExpressionExperimentValueObject` and `ArrayDesignValueObject` as their `taxon` property will be an `object` instead of a `string`. Properties such as `taxonId` are now deprecated and `taxon.id` should be used instead.  Entities that have IDs now all inherit from `IdentifiableValueObject`. This implies that you can assume the presence of an `id` in a search result `resultObject` attribute for example.  New `/search` endpoint! for an unified search experience. Annotation-based search endpoints under `/annotations` are now deprecated.  New API docs! While not as nice looking, the previous theme will be gradually ported to Swagger UI as we focused on functionality over prettiness for this release.  ### Update 2.4.0 through 2.4.1  Release notes for the 2.4 series were not written down, so I'll try to do my best to recall features that were introduced at that time.  An [OpenAPI](https://www.openapis.org/) specification was introduced and available under `/rest/v2/openapi.json`, although not fully stabilized.  Add a `/resultSets` endpoint to navigate result sets directly, by ID or by dataset.  Add a `/resultSets/{resultSetId}` endpoint to retrieve a specific result set by its ID. This endpoint can be negotiated with an `Accept: text/tab-separated-values` header to obtain a TSV representation.  Add a `/datasets/{dataset}/analyses/differential/resultSets` endpoint that essentially redirect to a specific `/resultSet` endpoint by dataset ID.  Add an endpoint to retrieve preferred raw expression vectors.  ### Update 2.3.4  November 6th, 2018  November 6th [2.3.4] Bug fixes in the dataset search endpoint.  November 5th [2.3.3] Added filtering parameters to dataset search.  October 25th [2.3.2] Changed behavior of the dataset search endpoint to more closely match the Gemma web interface.  October 2nd [2.3.1] Added group information to the User value object.  September 27th [2.3.0] Breaking change in Taxa: Abbreviation property has been removed and is therefore no longer an accepted identifier.  ### Update 2.2.6  June 7th, 2018  Code maintenance, bug fixes. Geeq scores stable and made public.  June 7th [2.2.6] Added: User authentication endpoint.  May 2nd [2.2.5] Fixed: Cleaned up and optimized platforms/elements endpoint, removed redundant information (recursive properties nesting).  April 12th [2.2.3] Fixed: Array arguments not handling non-string properties properly, e.g. `ncbiIds` of genes.  April 9th [2.2.1] Fixed: Filter argument not working when the filtered field was a primitive type. This most significantly allows filtering by geeq boolean and double properties.  ### Update 2.2.0  February 8th, 2018  Breaking change in the 'Dataset differential analysis' endpoint: - No longer using `qValueThreshold` parameter. - Response format changed, now using `DifferentialExpressionAnalysisValueObject` instead of `DifferentialExpressionValueObject` - [Experimental] Added Geeq (Gene Expression Experiment Quality) scores to the dataset value objects 

    The version of the OpenAPI document: 2.7.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import copy
import logging
import multiprocessing
import sys
import urllib3

import http.client as httplib

JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems'
}

class Configuration:
    """This class contains various settings of the API client.

    :param host: Base url.
    :param api_key: Dict to store API key(s).
      Each entry in the dict specifies an API key.
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is the API key secret.
    :param api_key_prefix: Dict to store API prefix (e.g. Bearer).
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is an API key prefix when generating the auth data.
    :param username: Username for HTTP basic authentication.
    :param password: Password for HTTP basic authentication.
    :param access_token: Access token.
    :param server_index: Index to servers configuration.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_index: Mapping from operation ID to an index to server
      configuration.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum
      values before.
    :param ssl_ca_cert: str - the path to a file of concatenated CA certificates
      in PEM format.

    :Example:

    API Key Authentication Example.
    Given the following security scheme in the OpenAPI specification:
      components:
        securitySchemes:
          cookieAuth:         # name for the security scheme
            type: apiKey
            in: cookie
            name: JSESSIONID  # cookie name

    You can programmatically set the cookie:

conf = gemmapy.sdk2.Configuration(
    api_key={'cookieAuth': 'abc123'}
    api_key_prefix={'cookieAuth': 'JSESSIONID'}
)

    The following cookie will be added to the HTTP request:
       Cookie: JSESSIONID abc123

    HTTP Basic Authentication Example.
    Given the following security scheme in the OpenAPI specification:
      components:
        securitySchemes:
          http_basic_auth:
            type: http
            scheme: basic

    Configure API client with HTTP basic authentication:

conf = gemmapy.sdk2.Configuration(
    username='the-user',
    password='the-password',
)

    """

    _default = None

    def __init__(self, host=None,
                 api_key=None, api_key_prefix=None,
                 username=None, password=None,
                 access_token=None,
                 server_index=None, server_variables=None,
                 server_operation_index=None, server_operation_variables=None,
                 ssl_ca_cert=None,
                 ) -> None:
        """Constructor
        """
        self._base_path = "https://gemma.msl.ubc.ca/rest/v2" if host is None else host
        """Default Base url
        """
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        """function hook to refresh API key if expired
        """
        self.username = username
        """Username for HTTP basic authentication
        """
        self.password = password
        """Password for HTTP basic authentication
        """
        self.access_token = access_token
        """Access token
        """
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("gemmapy.sdk2")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        self.debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """
        self.tls_server_name = None
        """SSL/TLS Server Name Indication (SNI)
           Set this to the SNI value expected by the server.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = None
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        self.socket_options = None
        """Options to pass down to the underlying urllib3 socket
        """

        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        """datetime format
        """

        self.date_format = "%Y-%m-%d"
        """date format
        """

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default):
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = default

    @classmethod
    def get_default_copy(cls):
        """Deprecated. Please use `get_default` instead.

        Deprecated. Please use `get_default` instead.

        :return: The configuration object.
        """
        return cls.get_default()

    @classmethod
    def get_default(cls):
        """Return the default configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration.

        :return: The configuration object.
        """
        if cls._default is None:
            cls._default = Configuration()
        return cls._default

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier, alias=None):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :param alias: The alternative identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(identifier, self.api_key.get(alias) if alias is not None else None)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(
            basic_auth=username + ':' + password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth = {}
        if self.username is not None and self.password is not None:
            auth['basicAuth'] = {
                'type': 'basic',
                'in': 'header',
                'key': 'Authorization',
                'value': self.get_basic_auth_token()
            }
        if 'cookieAuth' in self.api_key:
            auth['cookieAuth'] = {
                'type': 'api_key',
                'in': 'cookie',
                'key': 'JSESSIONID',
                'value': self.get_api_key_with_prefix(
                    'cookieAuth',
                ),
            }
        return auth

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 2.7.1\n"\
               "SDK Package Version: 0.99.0".\
               format(env=sys.platform, pyversion=sys.version)

    def get_host_settings(self):
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "https://gemma.msl.ubc.ca/rest/v2",
                'description': "Gemma",
            },
            {
                'url': "https://dev.gemma.msl.ubc.ca/rest/v2",
                'description': "Gemma (development server)",
            }
        ]

    def get_host_from_settings(self, index, variables=None, servers=None):
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers)))

        url = server['url']

        # go through variables and replace placeholders
        for variable_name, variable in server.get('variables', {}).items():
            used_value = variables.get(
                variable_name, variable['default_value'])

            if 'enum_values' in variable \
                    and used_value not in variable['enum_values']:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name],
                        variable['enum_values']))

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    @property
    def host(self):
        """Return generated host."""
        return self.get_host_from_settings(self.server_index, variables=self.server_variables)

    @host.setter
    def host(self, value):
        """Fix base path."""
        self._base_path = value
        self.server_index = None
