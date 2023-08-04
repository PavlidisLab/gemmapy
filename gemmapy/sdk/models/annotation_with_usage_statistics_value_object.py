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

class AnnotationWithUsageStatisticsValueObject(object):
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
        'class_uri': 'str',
        'class_name': 'str',
        'term_uri': 'str',
        'term_name': 'str',
        'evidence_code': 'str',
        'number_of_expression_experiments': 'int',
        'parent_terms': 'list[OntologyTermValueObject]'
    }

    attribute_map = {
        'class_uri': 'classUri',
        'class_name': 'className',
        'term_uri': 'termUri',
        'term_name': 'termName',
        'evidence_code': 'evidenceCode',
        'number_of_expression_experiments': 'numberOfExpressionExperiments',
        'parent_terms': 'parentTerms'
    }

    def __init__(self, class_uri=None, class_name=None, term_uri=None, term_name=None, evidence_code=None, number_of_expression_experiments=None, parent_terms=None):  # noqa: E501
        """AnnotationWithUsageStatisticsValueObject - a model defined in Swagger"""  # noqa: E501
        self._class_uri = None
        self._class_name = None
        self._term_uri = None
        self._term_name = None
        self._evidence_code = None
        self._number_of_expression_experiments = None
        self._parent_terms = None
        self.discriminator = None
        if class_uri is not None:
            self.class_uri = class_uri
        if class_name is not None:
            self.class_name = class_name
        if term_uri is not None:
            self.term_uri = term_uri
        if term_name is not None:
            self.term_name = term_name
        if evidence_code is not None:
            self.evidence_code = evidence_code
        if number_of_expression_experiments is not None:
            self.number_of_expression_experiments = number_of_expression_experiments
        if parent_terms is not None:
            self.parent_terms = parent_terms

    @property
    def class_uri(self):
        """Gets the class_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The class_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._class_uri

    @class_uri.setter
    def class_uri(self, class_uri):
        """Sets the class_uri of this AnnotationWithUsageStatisticsValueObject.


        :param class_uri: The class_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._class_uri = class_uri

    @property
    def class_name(self):
        """Gets the class_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The class_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this AnnotationWithUsageStatisticsValueObject.


        :param class_name: The class_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._class_name = class_name

    @property
    def term_uri(self):
        """Gets the term_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The term_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._term_uri

    @term_uri.setter
    def term_uri(self, term_uri):
        """Sets the term_uri of this AnnotationWithUsageStatisticsValueObject.


        :param term_uri: The term_uri of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._term_uri = term_uri

    @property
    def term_name(self):
        """Gets the term_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The term_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._term_name

    @term_name.setter
    def term_name(self, term_name):
        """Sets the term_name of this AnnotationWithUsageStatisticsValueObject.


        :param term_name: The term_name of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._term_name = term_name

    @property
    def evidence_code(self):
        """Gets the evidence_code of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The evidence_code of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: str
        """
        return self._evidence_code

    @evidence_code.setter
    def evidence_code(self, evidence_code):
        """Sets the evidence_code of this AnnotationWithUsageStatisticsValueObject.


        :param evidence_code: The evidence_code of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: str
        """

        self._evidence_code = evidence_code

    @property
    def number_of_expression_experiments(self):
        """Gets the number_of_expression_experiments of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The number_of_expression_experiments of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: int
        """
        return self._number_of_expression_experiments

    @number_of_expression_experiments.setter
    def number_of_expression_experiments(self, number_of_expression_experiments):
        """Sets the number_of_expression_experiments of this AnnotationWithUsageStatisticsValueObject.


        :param number_of_expression_experiments: The number_of_expression_experiments of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: int
        """

        self._number_of_expression_experiments = number_of_expression_experiments

    @property
    def parent_terms(self):
        """Gets the parent_terms of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501


        :return: The parent_terms of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :rtype: list[OntologyTermValueObject]
        """
        return self._parent_terms

    @parent_terms.setter
    def parent_terms(self, parent_terms):
        """Sets the parent_terms of this AnnotationWithUsageStatisticsValueObject.


        :param parent_terms: The parent_terms of this AnnotationWithUsageStatisticsValueObject.  # noqa: E501
        :type: list[OntologyTermValueObject]
        """

        self._parent_terms = parent_terms

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
        if issubclass(AnnotationWithUsageStatisticsValueObject, dict):
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
        if not isinstance(other, AnnotationWithUsageStatisticsValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
