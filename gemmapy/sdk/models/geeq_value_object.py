# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  Fix return type for `getResultSets` which was incorrectly referring to a renamed VO.  Remove the `security` requirements by default from the specification, which forced the Python package to supply empty credentials. There is currently no privileged endpoints, although some can return additional results.  ## Updates  ### Update 2.5.1  Restore `objectClass` visibility in `AnnotationValueObject`.  Fix incorrect response types for annotations search endpoints returning datasets.  ### Update 2.5.0  Major cleanups were performed in this release in order to stabilize the specification. Numerous properties from Gemma Web that were never intended to be exposed in Gemma REST have been hidden. It's a bit too much to describe in here, but you can navigate to the schemas section below to get a good glance at the models.  Favour `numberOfSomething` instead of `somethingCount` which is clearer. The older names are kept for backward-compatibility, but should be considered deprecated.  Gene aliases and multifunctionality rank are now filled in `GeneValueObject`.  Uniformly use `TaxonValueObject` to represent taxon. This is breaking change for the `ExpressionExperimentValueObject` and `ArrayDesignValueObject` as their `taxon` property will be an `object` instead of a `string`. Properties such as `taxonId` are now deprecated and `taxon.id` should be used instead.  Entities that have IDs now all inherit from `IdentifiableValueObject`. This implies that you can assume the presence of an `id` in a search result `resultObject` attribute for example.  New `/search` endpoint! for an unified search experience. Annotation-based search endpoints under `/annotations` are now deprecated.  New API docs! While not as nice looking, the previous theme will be gradually ported to Swagger UI as we focused on functionality over prettiness for this release.  ### Update 2.4.0 through 2.4.1  Release notes for the 2.4 series were not written down, so I'll try to do my best to recall features that were introduced at that time.  An [OpenAPI](https://www.openapis.org/) specification was introduced and available under `/rest/v2/openapi.json`, although not fully stabilized.  Add a `/resultSets` endpoint to navigate result sets directly, by ID or by dataset.  Add a `/resultSets/{resultSetId}` endpoint to retrieve a specific result set by its ID. This endpoint can be negotiated with an `Accept: text/tab-separated-values` header to obtain a TSV representation.  Add a `/datasets/{dataset}/analyses/differential/resultSets` endpoint that essentially redirect to a specific `/resultSet` endpoint by dataset ID.  Add an endpoint to retrieve preferred raw expression vectors.  ### Update 2.3.4  November 6th, 2018  November 6th [2.3.4] Bug fixes in the dataset search endpoint.  November 5th [2.3.3] Added filtering parameters to dataset search.  October 25th [2.3.2] Changed behavior of the dataset search endpoint to more closely match the Gemma web interface.  October 2nd [2.3.1] Added group information to the User value object.  September 27th [2.3.0] Breaking change in Taxa: Abbreviation property has been removed and is therefore no longer an accepted identifier.  ### Update 2.2.6  June 7th, 2018  Code maintenance, bug fixes. Geeq scores stable and made public.  June 7th [2.2.6] Added: User authentication endpoint.  May 2nd [2.2.5] Fixed: Cleaned up and optimized platforms/elements endpoint, removed redundant information (recursive properties nesting).  April 12th [2.2.3] Fixed: Array arguments not handling non-string properties properly, e.g. `ncbiIds` of genes.  April 9th [2.2.1] Fixed: Filter argument not working when the filtered field was a primitive type. This most significantly allows filtering by geeq boolean and double properties.  ### Update 2.2.0  February 8th, 2018  Breaking change in the 'Dataset differential analysis' endpoint: - No longer using `qValueThreshold` parameter. - Response format changed, now using `DifferentialExpressionAnalysisValueObject` instead of `DifferentialExpressionValueObject` - [Experimental] Added Geeq (Gene Expression Experiment Quality) scores to the dataset value objects   # noqa: E501

    OpenAPI spec version: 2.5.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GeeqValueObject(object):
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
        'public_quality_score': 'float',
        'public_suitability_score': 'float',
        'no_vectors': 'bool',
        'corr_mat_issues': 'str',
        'replicates_issues': 'str',
        'batch_corrected': 'bool',
        's_score_publication': 'float',
        's_score_platform_amount': 'float',
        's_score_platform_tech_multi': 'float',
        's_score_avg_platform_popularity': 'float',
        's_score_avg_platform_size': 'float',
        's_score_sample_size': 'float',
        's_score_raw_data': 'float',
        's_score_missing_values': 'float',
        'q_score_outliers': 'float',
        'q_score_sample_mean_correlation': 'float',
        'q_score_sample_median_correlation': 'float',
        'q_score_sample_correlation_variance': 'float',
        'q_score_platforms_tech': 'float',
        'q_score_replicates': 'float',
        'q_score_batch_info': 'float',
        'q_score_public_batch_effect': 'float',
        'q_score_public_batch_confound': 'float'
    }

    attribute_map = {
        'id': 'id',
        'public_quality_score': 'publicQualityScore',
        'public_suitability_score': 'publicSuitabilityScore',
        'no_vectors': 'noVectors',
        'corr_mat_issues': 'corrMatIssues',
        'replicates_issues': 'replicatesIssues',
        'batch_corrected': 'batchCorrected',
        's_score_publication': 'sScorePublication',
        's_score_platform_amount': 'sScorePlatformAmount',
        's_score_platform_tech_multi': 'sScorePlatformTechMulti',
        's_score_avg_platform_popularity': 'sScoreAvgPlatformPopularity',
        's_score_avg_platform_size': 'sScoreAvgPlatformSize',
        's_score_sample_size': 'sScoreSampleSize',
        's_score_raw_data': 'sScoreRawData',
        's_score_missing_values': 'sScoreMissingValues',
        'q_score_outliers': 'qScoreOutliers',
        'q_score_sample_mean_correlation': 'qScoreSampleMeanCorrelation',
        'q_score_sample_median_correlation': 'qScoreSampleMedianCorrelation',
        'q_score_sample_correlation_variance': 'qScoreSampleCorrelationVariance',
        'q_score_platforms_tech': 'qScorePlatformsTech',
        'q_score_replicates': 'qScoreReplicates',
        'q_score_batch_info': 'qScoreBatchInfo',
        'q_score_public_batch_effect': 'qScorePublicBatchEffect',
        'q_score_public_batch_confound': 'qScorePublicBatchConfound'
    }

    def __init__(self, id=None, public_quality_score=None, public_suitability_score=None, no_vectors=None, corr_mat_issues=None, replicates_issues=None, batch_corrected=None, s_score_publication=None, s_score_platform_amount=None, s_score_platform_tech_multi=None, s_score_avg_platform_popularity=None, s_score_avg_platform_size=None, s_score_sample_size=None, s_score_raw_data=None, s_score_missing_values=None, q_score_outliers=None, q_score_sample_mean_correlation=None, q_score_sample_median_correlation=None, q_score_sample_correlation_variance=None, q_score_platforms_tech=None, q_score_replicates=None, q_score_batch_info=None, q_score_public_batch_effect=None, q_score_public_batch_confound=None):  # noqa: E501
        """GeeqValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._public_quality_score = None
        self._public_suitability_score = None
        self._no_vectors = None
        self._corr_mat_issues = None
        self._replicates_issues = None
        self._batch_corrected = None
        self._s_score_publication = None
        self._s_score_platform_amount = None
        self._s_score_platform_tech_multi = None
        self._s_score_avg_platform_popularity = None
        self._s_score_avg_platform_size = None
        self._s_score_sample_size = None
        self._s_score_raw_data = None
        self._s_score_missing_values = None
        self._q_score_outliers = None
        self._q_score_sample_mean_correlation = None
        self._q_score_sample_median_correlation = None
        self._q_score_sample_correlation_variance = None
        self._q_score_platforms_tech = None
        self._q_score_replicates = None
        self._q_score_batch_info = None
        self._q_score_public_batch_effect = None
        self._q_score_public_batch_confound = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if public_quality_score is not None:
            self.public_quality_score = public_quality_score
        if public_suitability_score is not None:
            self.public_suitability_score = public_suitability_score
        if no_vectors is not None:
            self.no_vectors = no_vectors
        if corr_mat_issues is not None:
            self.corr_mat_issues = corr_mat_issues
        if replicates_issues is not None:
            self.replicates_issues = replicates_issues
        if batch_corrected is not None:
            self.batch_corrected = batch_corrected
        if s_score_publication is not None:
            self.s_score_publication = s_score_publication
        if s_score_platform_amount is not None:
            self.s_score_platform_amount = s_score_platform_amount
        if s_score_platform_tech_multi is not None:
            self.s_score_platform_tech_multi = s_score_platform_tech_multi
        if s_score_avg_platform_popularity is not None:
            self.s_score_avg_platform_popularity = s_score_avg_platform_popularity
        if s_score_avg_platform_size is not None:
            self.s_score_avg_platform_size = s_score_avg_platform_size
        if s_score_sample_size is not None:
            self.s_score_sample_size = s_score_sample_size
        if s_score_raw_data is not None:
            self.s_score_raw_data = s_score_raw_data
        if s_score_missing_values is not None:
            self.s_score_missing_values = s_score_missing_values
        if q_score_outliers is not None:
            self.q_score_outliers = q_score_outliers
        if q_score_sample_mean_correlation is not None:
            self.q_score_sample_mean_correlation = q_score_sample_mean_correlation
        if q_score_sample_median_correlation is not None:
            self.q_score_sample_median_correlation = q_score_sample_median_correlation
        if q_score_sample_correlation_variance is not None:
            self.q_score_sample_correlation_variance = q_score_sample_correlation_variance
        if q_score_platforms_tech is not None:
            self.q_score_platforms_tech = q_score_platforms_tech
        if q_score_replicates is not None:
            self.q_score_replicates = q_score_replicates
        if q_score_batch_info is not None:
            self.q_score_batch_info = q_score_batch_info
        if q_score_public_batch_effect is not None:
            self.q_score_public_batch_effect = q_score_public_batch_effect
        if q_score_public_batch_confound is not None:
            self.q_score_public_batch_confound = q_score_public_batch_confound

    @property
    def id(self):
        """Gets the id of this GeeqValueObject.  # noqa: E501


        :return: The id of this GeeqValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GeeqValueObject.


        :param id: The id of this GeeqValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def public_quality_score(self):
        """Gets the public_quality_score of this GeeqValueObject.  # noqa: E501


        :return: The public_quality_score of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._public_quality_score

    @public_quality_score.setter
    def public_quality_score(self, public_quality_score):
        """Sets the public_quality_score of this GeeqValueObject.


        :param public_quality_score: The public_quality_score of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._public_quality_score = public_quality_score

    @property
    def public_suitability_score(self):
        """Gets the public_suitability_score of this GeeqValueObject.  # noqa: E501


        :return: The public_suitability_score of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._public_suitability_score

    @public_suitability_score.setter
    def public_suitability_score(self, public_suitability_score):
        """Sets the public_suitability_score of this GeeqValueObject.


        :param public_suitability_score: The public_suitability_score of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._public_suitability_score = public_suitability_score

    @property
    def no_vectors(self):
        """Gets the no_vectors of this GeeqValueObject.  # noqa: E501


        :return: The no_vectors of this GeeqValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._no_vectors

    @no_vectors.setter
    def no_vectors(self, no_vectors):
        """Sets the no_vectors of this GeeqValueObject.


        :param no_vectors: The no_vectors of this GeeqValueObject.  # noqa: E501
        :type: bool
        """

        self._no_vectors = no_vectors

    @property
    def corr_mat_issues(self):
        """Gets the corr_mat_issues of this GeeqValueObject.  # noqa: E501


        :return: The corr_mat_issues of this GeeqValueObject.  # noqa: E501
        :rtype: str
        """
        return self._corr_mat_issues

    @corr_mat_issues.setter
    def corr_mat_issues(self, corr_mat_issues):
        """Sets the corr_mat_issues of this GeeqValueObject.


        :param corr_mat_issues: The corr_mat_issues of this GeeqValueObject.  # noqa: E501
        :type: str
        """

        self._corr_mat_issues = corr_mat_issues

    @property
    def replicates_issues(self):
        """Gets the replicates_issues of this GeeqValueObject.  # noqa: E501


        :return: The replicates_issues of this GeeqValueObject.  # noqa: E501
        :rtype: str
        """
        return self._replicates_issues

    @replicates_issues.setter
    def replicates_issues(self, replicates_issues):
        """Sets the replicates_issues of this GeeqValueObject.


        :param replicates_issues: The replicates_issues of this GeeqValueObject.  # noqa: E501
        :type: str
        """

        self._replicates_issues = replicates_issues

    @property
    def batch_corrected(self):
        """Gets the batch_corrected of this GeeqValueObject.  # noqa: E501


        :return: The batch_corrected of this GeeqValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._batch_corrected

    @batch_corrected.setter
    def batch_corrected(self, batch_corrected):
        """Sets the batch_corrected of this GeeqValueObject.


        :param batch_corrected: The batch_corrected of this GeeqValueObject.  # noqa: E501
        :type: bool
        """

        self._batch_corrected = batch_corrected

    @property
    def s_score_publication(self):
        """Gets the s_score_publication of this GeeqValueObject.  # noqa: E501


        :return: The s_score_publication of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._s_score_publication

    @s_score_publication.setter
    def s_score_publication(self, s_score_publication):
        """Sets the s_score_publication of this GeeqValueObject.


        :param s_score_publication: The s_score_publication of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._s_score_publication = s_score_publication

    @property
    def s_score_platform_amount(self):
        """Gets the s_score_platform_amount of this GeeqValueObject.  # noqa: E501


        :return: The s_score_platform_amount of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._s_score_platform_amount

    @s_score_platform_amount.setter
    def s_score_platform_amount(self, s_score_platform_amount):
        """Sets the s_score_platform_amount of this GeeqValueObject.


        :param s_score_platform_amount: The s_score_platform_amount of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._s_score_platform_amount = s_score_platform_amount

    @property
    def s_score_platform_tech_multi(self):
        """Gets the s_score_platform_tech_multi of this GeeqValueObject.  # noqa: E501


        :return: The s_score_platform_tech_multi of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._s_score_platform_tech_multi

    @s_score_platform_tech_multi.setter
    def s_score_platform_tech_multi(self, s_score_platform_tech_multi):
        """Sets the s_score_platform_tech_multi of this GeeqValueObject.


        :param s_score_platform_tech_multi: The s_score_platform_tech_multi of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._s_score_platform_tech_multi = s_score_platform_tech_multi

    @property
    def s_score_avg_platform_popularity(self):
        """Gets the s_score_avg_platform_popularity of this GeeqValueObject.  # noqa: E501


        :return: The s_score_avg_platform_popularity of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._s_score_avg_platform_popularity

    @s_score_avg_platform_popularity.setter
    def s_score_avg_platform_popularity(self, s_score_avg_platform_popularity):
        """Sets the s_score_avg_platform_popularity of this GeeqValueObject.


        :param s_score_avg_platform_popularity: The s_score_avg_platform_popularity of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._s_score_avg_platform_popularity = s_score_avg_platform_popularity

    @property
    def s_score_avg_platform_size(self):
        """Gets the s_score_avg_platform_size of this GeeqValueObject.  # noqa: E501


        :return: The s_score_avg_platform_size of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._s_score_avg_platform_size

    @s_score_avg_platform_size.setter
    def s_score_avg_platform_size(self, s_score_avg_platform_size):
        """Sets the s_score_avg_platform_size of this GeeqValueObject.


        :param s_score_avg_platform_size: The s_score_avg_platform_size of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._s_score_avg_platform_size = s_score_avg_platform_size

    @property
    def s_score_sample_size(self):
        """Gets the s_score_sample_size of this GeeqValueObject.  # noqa: E501


        :return: The s_score_sample_size of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._s_score_sample_size

    @s_score_sample_size.setter
    def s_score_sample_size(self, s_score_sample_size):
        """Sets the s_score_sample_size of this GeeqValueObject.


        :param s_score_sample_size: The s_score_sample_size of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._s_score_sample_size = s_score_sample_size

    @property
    def s_score_raw_data(self):
        """Gets the s_score_raw_data of this GeeqValueObject.  # noqa: E501


        :return: The s_score_raw_data of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._s_score_raw_data

    @s_score_raw_data.setter
    def s_score_raw_data(self, s_score_raw_data):
        """Sets the s_score_raw_data of this GeeqValueObject.


        :param s_score_raw_data: The s_score_raw_data of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._s_score_raw_data = s_score_raw_data

    @property
    def s_score_missing_values(self):
        """Gets the s_score_missing_values of this GeeqValueObject.  # noqa: E501


        :return: The s_score_missing_values of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._s_score_missing_values

    @s_score_missing_values.setter
    def s_score_missing_values(self, s_score_missing_values):
        """Sets the s_score_missing_values of this GeeqValueObject.


        :param s_score_missing_values: The s_score_missing_values of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._s_score_missing_values = s_score_missing_values

    @property
    def q_score_outliers(self):
        """Gets the q_score_outliers of this GeeqValueObject.  # noqa: E501


        :return: The q_score_outliers of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._q_score_outliers

    @q_score_outliers.setter
    def q_score_outliers(self, q_score_outliers):
        """Sets the q_score_outliers of this GeeqValueObject.


        :param q_score_outliers: The q_score_outliers of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._q_score_outliers = q_score_outliers

    @property
    def q_score_sample_mean_correlation(self):
        """Gets the q_score_sample_mean_correlation of this GeeqValueObject.  # noqa: E501


        :return: The q_score_sample_mean_correlation of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._q_score_sample_mean_correlation

    @q_score_sample_mean_correlation.setter
    def q_score_sample_mean_correlation(self, q_score_sample_mean_correlation):
        """Sets the q_score_sample_mean_correlation of this GeeqValueObject.


        :param q_score_sample_mean_correlation: The q_score_sample_mean_correlation of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._q_score_sample_mean_correlation = q_score_sample_mean_correlation

    @property
    def q_score_sample_median_correlation(self):
        """Gets the q_score_sample_median_correlation of this GeeqValueObject.  # noqa: E501


        :return: The q_score_sample_median_correlation of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._q_score_sample_median_correlation

    @q_score_sample_median_correlation.setter
    def q_score_sample_median_correlation(self, q_score_sample_median_correlation):
        """Sets the q_score_sample_median_correlation of this GeeqValueObject.


        :param q_score_sample_median_correlation: The q_score_sample_median_correlation of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._q_score_sample_median_correlation = q_score_sample_median_correlation

    @property
    def q_score_sample_correlation_variance(self):
        """Gets the q_score_sample_correlation_variance of this GeeqValueObject.  # noqa: E501


        :return: The q_score_sample_correlation_variance of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._q_score_sample_correlation_variance

    @q_score_sample_correlation_variance.setter
    def q_score_sample_correlation_variance(self, q_score_sample_correlation_variance):
        """Sets the q_score_sample_correlation_variance of this GeeqValueObject.


        :param q_score_sample_correlation_variance: The q_score_sample_correlation_variance of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._q_score_sample_correlation_variance = q_score_sample_correlation_variance

    @property
    def q_score_platforms_tech(self):
        """Gets the q_score_platforms_tech of this GeeqValueObject.  # noqa: E501


        :return: The q_score_platforms_tech of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._q_score_platforms_tech

    @q_score_platforms_tech.setter
    def q_score_platforms_tech(self, q_score_platforms_tech):
        """Sets the q_score_platforms_tech of this GeeqValueObject.


        :param q_score_platforms_tech: The q_score_platforms_tech of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._q_score_platforms_tech = q_score_platforms_tech

    @property
    def q_score_replicates(self):
        """Gets the q_score_replicates of this GeeqValueObject.  # noqa: E501


        :return: The q_score_replicates of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._q_score_replicates

    @q_score_replicates.setter
    def q_score_replicates(self, q_score_replicates):
        """Sets the q_score_replicates of this GeeqValueObject.


        :param q_score_replicates: The q_score_replicates of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._q_score_replicates = q_score_replicates

    @property
    def q_score_batch_info(self):
        """Gets the q_score_batch_info of this GeeqValueObject.  # noqa: E501


        :return: The q_score_batch_info of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._q_score_batch_info

    @q_score_batch_info.setter
    def q_score_batch_info(self, q_score_batch_info):
        """Sets the q_score_batch_info of this GeeqValueObject.


        :param q_score_batch_info: The q_score_batch_info of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._q_score_batch_info = q_score_batch_info

    @property
    def q_score_public_batch_effect(self):
        """Gets the q_score_public_batch_effect of this GeeqValueObject.  # noqa: E501


        :return: The q_score_public_batch_effect of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._q_score_public_batch_effect

    @q_score_public_batch_effect.setter
    def q_score_public_batch_effect(self, q_score_public_batch_effect):
        """Sets the q_score_public_batch_effect of this GeeqValueObject.


        :param q_score_public_batch_effect: The q_score_public_batch_effect of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._q_score_public_batch_effect = q_score_public_batch_effect

    @property
    def q_score_public_batch_confound(self):
        """Gets the q_score_public_batch_confound of this GeeqValueObject.  # noqa: E501


        :return: The q_score_public_batch_confound of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._q_score_public_batch_confound

    @q_score_public_batch_confound.setter
    def q_score_public_batch_confound(self, q_score_public_batch_confound):
        """Sets the q_score_public_batch_confound of this GeeqValueObject.


        :param q_score_public_batch_confound: The q_score_public_batch_confound of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._q_score_public_batch_confound = q_score_public_batch_confound

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
        if issubclass(GeeqValueObject, dict):
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
        if not isinstance(other, GeeqValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other