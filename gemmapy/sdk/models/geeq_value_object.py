# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma REST API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  The documentation of the underlying java code can be found [here](https://gemma.msl.ubc.ca/resources/apidocs/ubic/gemma/web/services/rest/package-summary.html). See the [links section](https://gemma.msl.ubc.ca/resources/restapidocs/#footer) in the footer of this page for other relevant links.  Use of this webpage and Gemma web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.   # noqa: E501

    OpenAPI spec version: 2.4.1
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
        'gets_score_publication': 'float',
        'gets_score_platform_amount': 'float',
        'gets_score_platforms_tech_multi': 'float',
        'gets_score_avg_platform_popularity': 'float',
        'gets_score_avg_platform_size': 'float',
        'gets_score_sample_size': 'float',
        'gets_score_raw_data': 'float',
        'gets_score_missing_values': 'float',
        'getq_score_outliers': 'float',
        'getq_score_sample_mean_correlation': 'float',
        'getq_score_sample_median_correlation': 'float',
        'getq_score_sample_correlation_variance': 'float',
        'getq_score_platforms_tech': 'float',
        'getq_score_replicates': 'float',
        'getq_score_batch_info': 'float',
        'getq_score_public_batch_effect': 'float',
        'getq_score_public_batch_confound': 'float',
        'no_vectors': 'bool',
        'corr_mat_issues': 'str',
        'replicates_issues': 'str',
        'batch_corrected': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'public_quality_score': 'publicQualityScore',
        'public_suitability_score': 'publicSuitabilityScore',
        'gets_score_publication': 'getsScorePublication',
        'gets_score_platform_amount': 'getsScorePlatformAmount',
        'gets_score_platforms_tech_multi': 'getsScorePlatformsTechMulti',
        'gets_score_avg_platform_popularity': 'getsScoreAvgPlatformPopularity',
        'gets_score_avg_platform_size': 'getsScoreAvgPlatformSize',
        'gets_score_sample_size': 'getsScoreSampleSize',
        'gets_score_raw_data': 'getsScoreRawData',
        'gets_score_missing_values': 'getsScoreMissingValues',
        'getq_score_outliers': 'getqScoreOutliers',
        'getq_score_sample_mean_correlation': 'getqScoreSampleMeanCorrelation',
        'getq_score_sample_median_correlation': 'getqScoreSampleMedianCorrelation',
        'getq_score_sample_correlation_variance': 'getqScoreSampleCorrelationVariance',
        'getq_score_platforms_tech': 'getqScorePlatformsTech',
        'getq_score_replicates': 'getqScoreReplicates',
        'getq_score_batch_info': 'getqScoreBatchInfo',
        'getq_score_public_batch_effect': 'getqScorePublicBatchEffect',
        'getq_score_public_batch_confound': 'getqScorePublicBatchConfound',
        'no_vectors': 'noVectors',
        'corr_mat_issues': 'corrMatIssues',
        'replicates_issues': 'replicatesIssues',
        'batch_corrected': 'batchCorrected'
    }

    def __init__(self, id=None, public_quality_score=None, public_suitability_score=None, gets_score_publication=None, gets_score_platform_amount=None, gets_score_platforms_tech_multi=None, gets_score_avg_platform_popularity=None, gets_score_avg_platform_size=None, gets_score_sample_size=None, gets_score_raw_data=None, gets_score_missing_values=None, getq_score_outliers=None, getq_score_sample_mean_correlation=None, getq_score_sample_median_correlation=None, getq_score_sample_correlation_variance=None, getq_score_platforms_tech=None, getq_score_replicates=None, getq_score_batch_info=None, getq_score_public_batch_effect=None, getq_score_public_batch_confound=None, no_vectors=None, corr_mat_issues=None, replicates_issues=None, batch_corrected=None):  # noqa: E501
        """GeeqValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._public_quality_score = None
        self._public_suitability_score = None
        self._gets_score_publication = None
        self._gets_score_platform_amount = None
        self._gets_score_platforms_tech_multi = None
        self._gets_score_avg_platform_popularity = None
        self._gets_score_avg_platform_size = None
        self._gets_score_sample_size = None
        self._gets_score_raw_data = None
        self._gets_score_missing_values = None
        self._getq_score_outliers = None
        self._getq_score_sample_mean_correlation = None
        self._getq_score_sample_median_correlation = None
        self._getq_score_sample_correlation_variance = None
        self._getq_score_platforms_tech = None
        self._getq_score_replicates = None
        self._getq_score_batch_info = None
        self._getq_score_public_batch_effect = None
        self._getq_score_public_batch_confound = None
        self._no_vectors = None
        self._corr_mat_issues = None
        self._replicates_issues = None
        self._batch_corrected = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if public_quality_score is not None:
            self.public_quality_score = public_quality_score
        if public_suitability_score is not None:
            self.public_suitability_score = public_suitability_score
        if gets_score_publication is not None:
            self.gets_score_publication = gets_score_publication
        if gets_score_platform_amount is not None:
            self.gets_score_platform_amount = gets_score_platform_amount
        if gets_score_platforms_tech_multi is not None:
            self.gets_score_platforms_tech_multi = gets_score_platforms_tech_multi
        if gets_score_avg_platform_popularity is not None:
            self.gets_score_avg_platform_popularity = gets_score_avg_platform_popularity
        if gets_score_avg_platform_size is not None:
            self.gets_score_avg_platform_size = gets_score_avg_platform_size
        if gets_score_sample_size is not None:
            self.gets_score_sample_size = gets_score_sample_size
        if gets_score_raw_data is not None:
            self.gets_score_raw_data = gets_score_raw_data
        if gets_score_missing_values is not None:
            self.gets_score_missing_values = gets_score_missing_values
        if getq_score_outliers is not None:
            self.getq_score_outliers = getq_score_outliers
        if getq_score_sample_mean_correlation is not None:
            self.getq_score_sample_mean_correlation = getq_score_sample_mean_correlation
        if getq_score_sample_median_correlation is not None:
            self.getq_score_sample_median_correlation = getq_score_sample_median_correlation
        if getq_score_sample_correlation_variance is not None:
            self.getq_score_sample_correlation_variance = getq_score_sample_correlation_variance
        if getq_score_platforms_tech is not None:
            self.getq_score_platforms_tech = getq_score_platforms_tech
        if getq_score_replicates is not None:
            self.getq_score_replicates = getq_score_replicates
        if getq_score_batch_info is not None:
            self.getq_score_batch_info = getq_score_batch_info
        if getq_score_public_batch_effect is not None:
            self.getq_score_public_batch_effect = getq_score_public_batch_effect
        if getq_score_public_batch_confound is not None:
            self.getq_score_public_batch_confound = getq_score_public_batch_confound
        if no_vectors is not None:
            self.no_vectors = no_vectors
        if corr_mat_issues is not None:
            self.corr_mat_issues = corr_mat_issues
        if replicates_issues is not None:
            self.replicates_issues = replicates_issues
        if batch_corrected is not None:
            self.batch_corrected = batch_corrected

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
    def gets_score_publication(self):
        """Gets the gets_score_publication of this GeeqValueObject.  # noqa: E501


        :return: The gets_score_publication of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._gets_score_publication

    @gets_score_publication.setter
    def gets_score_publication(self, gets_score_publication):
        """Sets the gets_score_publication of this GeeqValueObject.


        :param gets_score_publication: The gets_score_publication of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._gets_score_publication = gets_score_publication

    @property
    def gets_score_platform_amount(self):
        """Gets the gets_score_platform_amount of this GeeqValueObject.  # noqa: E501


        :return: The gets_score_platform_amount of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._gets_score_platform_amount

    @gets_score_platform_amount.setter
    def gets_score_platform_amount(self, gets_score_platform_amount):
        """Sets the gets_score_platform_amount of this GeeqValueObject.


        :param gets_score_platform_amount: The gets_score_platform_amount of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._gets_score_platform_amount = gets_score_platform_amount

    @property
    def gets_score_platforms_tech_multi(self):
        """Gets the gets_score_platforms_tech_multi of this GeeqValueObject.  # noqa: E501


        :return: The gets_score_platforms_tech_multi of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._gets_score_platforms_tech_multi

    @gets_score_platforms_tech_multi.setter
    def gets_score_platforms_tech_multi(self, gets_score_platforms_tech_multi):
        """Sets the gets_score_platforms_tech_multi of this GeeqValueObject.


        :param gets_score_platforms_tech_multi: The gets_score_platforms_tech_multi of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._gets_score_platforms_tech_multi = gets_score_platforms_tech_multi

    @property
    def gets_score_avg_platform_popularity(self):
        """Gets the gets_score_avg_platform_popularity of this GeeqValueObject.  # noqa: E501


        :return: The gets_score_avg_platform_popularity of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._gets_score_avg_platform_popularity

    @gets_score_avg_platform_popularity.setter
    def gets_score_avg_platform_popularity(self, gets_score_avg_platform_popularity):
        """Sets the gets_score_avg_platform_popularity of this GeeqValueObject.


        :param gets_score_avg_platform_popularity: The gets_score_avg_platform_popularity of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._gets_score_avg_platform_popularity = gets_score_avg_platform_popularity

    @property
    def gets_score_avg_platform_size(self):
        """Gets the gets_score_avg_platform_size of this GeeqValueObject.  # noqa: E501


        :return: The gets_score_avg_platform_size of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._gets_score_avg_platform_size

    @gets_score_avg_platform_size.setter
    def gets_score_avg_platform_size(self, gets_score_avg_platform_size):
        """Sets the gets_score_avg_platform_size of this GeeqValueObject.


        :param gets_score_avg_platform_size: The gets_score_avg_platform_size of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._gets_score_avg_platform_size = gets_score_avg_platform_size

    @property
    def gets_score_sample_size(self):
        """Gets the gets_score_sample_size of this GeeqValueObject.  # noqa: E501


        :return: The gets_score_sample_size of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._gets_score_sample_size

    @gets_score_sample_size.setter
    def gets_score_sample_size(self, gets_score_sample_size):
        """Sets the gets_score_sample_size of this GeeqValueObject.


        :param gets_score_sample_size: The gets_score_sample_size of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._gets_score_sample_size = gets_score_sample_size

    @property
    def gets_score_raw_data(self):
        """Gets the gets_score_raw_data of this GeeqValueObject.  # noqa: E501


        :return: The gets_score_raw_data of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._gets_score_raw_data

    @gets_score_raw_data.setter
    def gets_score_raw_data(self, gets_score_raw_data):
        """Sets the gets_score_raw_data of this GeeqValueObject.


        :param gets_score_raw_data: The gets_score_raw_data of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._gets_score_raw_data = gets_score_raw_data

    @property
    def gets_score_missing_values(self):
        """Gets the gets_score_missing_values of this GeeqValueObject.  # noqa: E501


        :return: The gets_score_missing_values of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._gets_score_missing_values

    @gets_score_missing_values.setter
    def gets_score_missing_values(self, gets_score_missing_values):
        """Sets the gets_score_missing_values of this GeeqValueObject.


        :param gets_score_missing_values: The gets_score_missing_values of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._gets_score_missing_values = gets_score_missing_values

    @property
    def getq_score_outliers(self):
        """Gets the getq_score_outliers of this GeeqValueObject.  # noqa: E501


        :return: The getq_score_outliers of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._getq_score_outliers

    @getq_score_outliers.setter
    def getq_score_outliers(self, getq_score_outliers):
        """Sets the getq_score_outliers of this GeeqValueObject.


        :param getq_score_outliers: The getq_score_outliers of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._getq_score_outliers = getq_score_outliers

    @property
    def getq_score_sample_mean_correlation(self):
        """Gets the getq_score_sample_mean_correlation of this GeeqValueObject.  # noqa: E501


        :return: The getq_score_sample_mean_correlation of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._getq_score_sample_mean_correlation

    @getq_score_sample_mean_correlation.setter
    def getq_score_sample_mean_correlation(self, getq_score_sample_mean_correlation):
        """Sets the getq_score_sample_mean_correlation of this GeeqValueObject.


        :param getq_score_sample_mean_correlation: The getq_score_sample_mean_correlation of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._getq_score_sample_mean_correlation = getq_score_sample_mean_correlation

    @property
    def getq_score_sample_median_correlation(self):
        """Gets the getq_score_sample_median_correlation of this GeeqValueObject.  # noqa: E501


        :return: The getq_score_sample_median_correlation of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._getq_score_sample_median_correlation

    @getq_score_sample_median_correlation.setter
    def getq_score_sample_median_correlation(self, getq_score_sample_median_correlation):
        """Sets the getq_score_sample_median_correlation of this GeeqValueObject.


        :param getq_score_sample_median_correlation: The getq_score_sample_median_correlation of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._getq_score_sample_median_correlation = getq_score_sample_median_correlation

    @property
    def getq_score_sample_correlation_variance(self):
        """Gets the getq_score_sample_correlation_variance of this GeeqValueObject.  # noqa: E501


        :return: The getq_score_sample_correlation_variance of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._getq_score_sample_correlation_variance

    @getq_score_sample_correlation_variance.setter
    def getq_score_sample_correlation_variance(self, getq_score_sample_correlation_variance):
        """Sets the getq_score_sample_correlation_variance of this GeeqValueObject.


        :param getq_score_sample_correlation_variance: The getq_score_sample_correlation_variance of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._getq_score_sample_correlation_variance = getq_score_sample_correlation_variance

    @property
    def getq_score_platforms_tech(self):
        """Gets the getq_score_platforms_tech of this GeeqValueObject.  # noqa: E501


        :return: The getq_score_platforms_tech of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._getq_score_platforms_tech

    @getq_score_platforms_tech.setter
    def getq_score_platforms_tech(self, getq_score_platforms_tech):
        """Sets the getq_score_platforms_tech of this GeeqValueObject.


        :param getq_score_platforms_tech: The getq_score_platforms_tech of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._getq_score_platforms_tech = getq_score_platforms_tech

    @property
    def getq_score_replicates(self):
        """Gets the getq_score_replicates of this GeeqValueObject.  # noqa: E501


        :return: The getq_score_replicates of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._getq_score_replicates

    @getq_score_replicates.setter
    def getq_score_replicates(self, getq_score_replicates):
        """Sets the getq_score_replicates of this GeeqValueObject.


        :param getq_score_replicates: The getq_score_replicates of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._getq_score_replicates = getq_score_replicates

    @property
    def getq_score_batch_info(self):
        """Gets the getq_score_batch_info of this GeeqValueObject.  # noqa: E501


        :return: The getq_score_batch_info of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._getq_score_batch_info

    @getq_score_batch_info.setter
    def getq_score_batch_info(self, getq_score_batch_info):
        """Sets the getq_score_batch_info of this GeeqValueObject.


        :param getq_score_batch_info: The getq_score_batch_info of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._getq_score_batch_info = getq_score_batch_info

    @property
    def getq_score_public_batch_effect(self):
        """Gets the getq_score_public_batch_effect of this GeeqValueObject.  # noqa: E501


        :return: The getq_score_public_batch_effect of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._getq_score_public_batch_effect

    @getq_score_public_batch_effect.setter
    def getq_score_public_batch_effect(self, getq_score_public_batch_effect):
        """Sets the getq_score_public_batch_effect of this GeeqValueObject.


        :param getq_score_public_batch_effect: The getq_score_public_batch_effect of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._getq_score_public_batch_effect = getq_score_public_batch_effect

    @property
    def getq_score_public_batch_confound(self):
        """Gets the getq_score_public_batch_confound of this GeeqValueObject.  # noqa: E501


        :return: The getq_score_public_batch_confound of this GeeqValueObject.  # noqa: E501
        :rtype: float
        """
        return self._getq_score_public_batch_confound

    @getq_score_public_batch_confound.setter
    def getq_score_public_batch_confound(self, getq_score_public_batch_confound):
        """Sets the getq_score_public_batch_confound of this GeeqValueObject.


        :param getq_score_public_batch_confound: The getq_score_public_batch_confound of this GeeqValueObject.  # noqa: E501
        :type: float
        """

        self._getq_score_public_batch_confound = getq_score_public_batch_confound

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
