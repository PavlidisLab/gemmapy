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

class BlatResultValueObject(object):
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
        'block_count': 'int',
        'block_sizes': 'str',
        'identity': 'float',
        'matches': 'int',
        'mismatches': 'int',
        'ns': 'int',
        'query_end': 'int',
        'query_gap_bases': 'int',
        'query_gap_count': 'int',
        'query_sequence': 'BioSequenceValueObject',
        'query_start': 'int',
        'query_starts': 'str',
        'rep_matches': 'int',
        'score': 'float',
        'strand': 'str',
        'target_chromosome_name': 'str',
        'target_database': 'str',
        'taxon': 'TaxonValueObject',
        'target_end': 'int',
        'target_gap_bases': 'int',
        'target_gap_count': 'int',
        'target_start': 'int',
        'target_starts': 'str'
    }

    attribute_map = {
        'id': 'id',
        'block_count': 'blockCount',
        'block_sizes': 'blockSizes',
        'identity': 'identity',
        'matches': 'matches',
        'mismatches': 'mismatches',
        'ns': 'ns',
        'query_end': 'queryEnd',
        'query_gap_bases': 'queryGapBases',
        'query_gap_count': 'queryGapCount',
        'query_sequence': 'querySequence',
        'query_start': 'queryStart',
        'query_starts': 'queryStarts',
        'rep_matches': 'repMatches',
        'score': 'score',
        'strand': 'strand',
        'target_chromosome_name': 'targetChromosomeName',
        'target_database': 'targetDatabase',
        'taxon': 'taxon',
        'target_end': 'targetEnd',
        'target_gap_bases': 'targetGapBases',
        'target_gap_count': 'targetGapCount',
        'target_start': 'targetStart',
        'target_starts': 'targetStarts'
    }

    def __init__(self, id=None, block_count=None, block_sizes=None, identity=None, matches=None, mismatches=None, ns=None, query_end=None, query_gap_bases=None, query_gap_count=None, query_sequence=None, query_start=None, query_starts=None, rep_matches=None, score=None, strand=None, target_chromosome_name=None, target_database=None, taxon=None, target_end=None, target_gap_bases=None, target_gap_count=None, target_start=None, target_starts=None):  # noqa: E501
        """BlatResultValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._block_count = None
        self._block_sizes = None
        self._identity = None
        self._matches = None
        self._mismatches = None
        self._ns = None
        self._query_end = None
        self._query_gap_bases = None
        self._query_gap_count = None
        self._query_sequence = None
        self._query_start = None
        self._query_starts = None
        self._rep_matches = None
        self._score = None
        self._strand = None
        self._target_chromosome_name = None
        self._target_database = None
        self._taxon = None
        self._target_end = None
        self._target_gap_bases = None
        self._target_gap_count = None
        self._target_start = None
        self._target_starts = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if block_count is not None:
            self.block_count = block_count
        if block_sizes is not None:
            self.block_sizes = block_sizes
        if identity is not None:
            self.identity = identity
        if matches is not None:
            self.matches = matches
        if mismatches is not None:
            self.mismatches = mismatches
        if ns is not None:
            self.ns = ns
        if query_end is not None:
            self.query_end = query_end
        if query_gap_bases is not None:
            self.query_gap_bases = query_gap_bases
        if query_gap_count is not None:
            self.query_gap_count = query_gap_count
        if query_sequence is not None:
            self.query_sequence = query_sequence
        if query_start is not None:
            self.query_start = query_start
        if query_starts is not None:
            self.query_starts = query_starts
        if rep_matches is not None:
            self.rep_matches = rep_matches
        if score is not None:
            self.score = score
        if strand is not None:
            self.strand = strand
        if target_chromosome_name is not None:
            self.target_chromosome_name = target_chromosome_name
        if target_database is not None:
            self.target_database = target_database
        if taxon is not None:
            self.taxon = taxon
        if target_end is not None:
            self.target_end = target_end
        if target_gap_bases is not None:
            self.target_gap_bases = target_gap_bases
        if target_gap_count is not None:
            self.target_gap_count = target_gap_count
        if target_start is not None:
            self.target_start = target_start
        if target_starts is not None:
            self.target_starts = target_starts

    @property
    def id(self):
        """Gets the id of this BlatResultValueObject.  # noqa: E501


        :return: The id of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BlatResultValueObject.


        :param id: The id of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def block_count(self):
        """Gets the block_count of this BlatResultValueObject.  # noqa: E501


        :return: The block_count of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._block_count

    @block_count.setter
    def block_count(self, block_count):
        """Sets the block_count of this BlatResultValueObject.


        :param block_count: The block_count of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._block_count = block_count

    @property
    def block_sizes(self):
        """Gets the block_sizes of this BlatResultValueObject.  # noqa: E501


        :return: The block_sizes of this BlatResultValueObject.  # noqa: E501
        :rtype: str
        """
        return self._block_sizes

    @block_sizes.setter
    def block_sizes(self, block_sizes):
        """Sets the block_sizes of this BlatResultValueObject.


        :param block_sizes: The block_sizes of this BlatResultValueObject.  # noqa: E501
        :type: str
        """

        self._block_sizes = block_sizes

    @property
    def identity(self):
        """Gets the identity of this BlatResultValueObject.  # noqa: E501


        :return: The identity of this BlatResultValueObject.  # noqa: E501
        :rtype: float
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this BlatResultValueObject.


        :param identity: The identity of this BlatResultValueObject.  # noqa: E501
        :type: float
        """

        self._identity = identity

    @property
    def matches(self):
        """Gets the matches of this BlatResultValueObject.  # noqa: E501


        :return: The matches of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this BlatResultValueObject.


        :param matches: The matches of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._matches = matches

    @property
    def mismatches(self):
        """Gets the mismatches of this BlatResultValueObject.  # noqa: E501


        :return: The mismatches of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._mismatches

    @mismatches.setter
    def mismatches(self, mismatches):
        """Sets the mismatches of this BlatResultValueObject.


        :param mismatches: The mismatches of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._mismatches = mismatches

    @property
    def ns(self):
        """Gets the ns of this BlatResultValueObject.  # noqa: E501


        :return: The ns of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._ns

    @ns.setter
    def ns(self, ns):
        """Sets the ns of this BlatResultValueObject.


        :param ns: The ns of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._ns = ns

    @property
    def query_end(self):
        """Gets the query_end of this BlatResultValueObject.  # noqa: E501


        :return: The query_end of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._query_end

    @query_end.setter
    def query_end(self, query_end):
        """Sets the query_end of this BlatResultValueObject.


        :param query_end: The query_end of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._query_end = query_end

    @property
    def query_gap_bases(self):
        """Gets the query_gap_bases of this BlatResultValueObject.  # noqa: E501


        :return: The query_gap_bases of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._query_gap_bases

    @query_gap_bases.setter
    def query_gap_bases(self, query_gap_bases):
        """Sets the query_gap_bases of this BlatResultValueObject.


        :param query_gap_bases: The query_gap_bases of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._query_gap_bases = query_gap_bases

    @property
    def query_gap_count(self):
        """Gets the query_gap_count of this BlatResultValueObject.  # noqa: E501


        :return: The query_gap_count of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._query_gap_count

    @query_gap_count.setter
    def query_gap_count(self, query_gap_count):
        """Sets the query_gap_count of this BlatResultValueObject.


        :param query_gap_count: The query_gap_count of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._query_gap_count = query_gap_count

    @property
    def query_sequence(self):
        """Gets the query_sequence of this BlatResultValueObject.  # noqa: E501


        :return: The query_sequence of this BlatResultValueObject.  # noqa: E501
        :rtype: BioSequenceValueObject
        """
        return self._query_sequence

    @query_sequence.setter
    def query_sequence(self, query_sequence):
        """Sets the query_sequence of this BlatResultValueObject.


        :param query_sequence: The query_sequence of this BlatResultValueObject.  # noqa: E501
        :type: BioSequenceValueObject
        """

        self._query_sequence = query_sequence

    @property
    def query_start(self):
        """Gets the query_start of this BlatResultValueObject.  # noqa: E501


        :return: The query_start of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._query_start

    @query_start.setter
    def query_start(self, query_start):
        """Sets the query_start of this BlatResultValueObject.


        :param query_start: The query_start of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._query_start = query_start

    @property
    def query_starts(self):
        """Gets the query_starts of this BlatResultValueObject.  # noqa: E501


        :return: The query_starts of this BlatResultValueObject.  # noqa: E501
        :rtype: str
        """
        return self._query_starts

    @query_starts.setter
    def query_starts(self, query_starts):
        """Sets the query_starts of this BlatResultValueObject.


        :param query_starts: The query_starts of this BlatResultValueObject.  # noqa: E501
        :type: str
        """

        self._query_starts = query_starts

    @property
    def rep_matches(self):
        """Gets the rep_matches of this BlatResultValueObject.  # noqa: E501


        :return: The rep_matches of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._rep_matches

    @rep_matches.setter
    def rep_matches(self, rep_matches):
        """Sets the rep_matches of this BlatResultValueObject.


        :param rep_matches: The rep_matches of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._rep_matches = rep_matches

    @property
    def score(self):
        """Gets the score of this BlatResultValueObject.  # noqa: E501


        :return: The score of this BlatResultValueObject.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this BlatResultValueObject.


        :param score: The score of this BlatResultValueObject.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def strand(self):
        """Gets the strand of this BlatResultValueObject.  # noqa: E501


        :return: The strand of this BlatResultValueObject.  # noqa: E501
        :rtype: str
        """
        return self._strand

    @strand.setter
    def strand(self, strand):
        """Sets the strand of this BlatResultValueObject.


        :param strand: The strand of this BlatResultValueObject.  # noqa: E501
        :type: str
        """

        self._strand = strand

    @property
    def target_chromosome_name(self):
        """Gets the target_chromosome_name of this BlatResultValueObject.  # noqa: E501


        :return: The target_chromosome_name of this BlatResultValueObject.  # noqa: E501
        :rtype: str
        """
        return self._target_chromosome_name

    @target_chromosome_name.setter
    def target_chromosome_name(self, target_chromosome_name):
        """Sets the target_chromosome_name of this BlatResultValueObject.


        :param target_chromosome_name: The target_chromosome_name of this BlatResultValueObject.  # noqa: E501
        :type: str
        """

        self._target_chromosome_name = target_chromosome_name

    @property
    def target_database(self):
        """Gets the target_database of this BlatResultValueObject.  # noqa: E501


        :return: The target_database of this BlatResultValueObject.  # noqa: E501
        :rtype: str
        """
        return self._target_database

    @target_database.setter
    def target_database(self, target_database):
        """Sets the target_database of this BlatResultValueObject.


        :param target_database: The target_database of this BlatResultValueObject.  # noqa: E501
        :type: str
        """

        self._target_database = target_database

    @property
    def taxon(self):
        """Gets the taxon of this BlatResultValueObject.  # noqa: E501


        :return: The taxon of this BlatResultValueObject.  # noqa: E501
        :rtype: TaxonValueObject
        """
        return self._taxon

    @taxon.setter
    def taxon(self, taxon):
        """Sets the taxon of this BlatResultValueObject.


        :param taxon: The taxon of this BlatResultValueObject.  # noqa: E501
        :type: TaxonValueObject
        """

        self._taxon = taxon

    @property
    def target_end(self):
        """Gets the target_end of this BlatResultValueObject.  # noqa: E501


        :return: The target_end of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._target_end

    @target_end.setter
    def target_end(self, target_end):
        """Sets the target_end of this BlatResultValueObject.


        :param target_end: The target_end of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._target_end = target_end

    @property
    def target_gap_bases(self):
        """Gets the target_gap_bases of this BlatResultValueObject.  # noqa: E501


        :return: The target_gap_bases of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._target_gap_bases

    @target_gap_bases.setter
    def target_gap_bases(self, target_gap_bases):
        """Sets the target_gap_bases of this BlatResultValueObject.


        :param target_gap_bases: The target_gap_bases of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._target_gap_bases = target_gap_bases

    @property
    def target_gap_count(self):
        """Gets the target_gap_count of this BlatResultValueObject.  # noqa: E501


        :return: The target_gap_count of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._target_gap_count

    @target_gap_count.setter
    def target_gap_count(self, target_gap_count):
        """Sets the target_gap_count of this BlatResultValueObject.


        :param target_gap_count: The target_gap_count of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._target_gap_count = target_gap_count

    @property
    def target_start(self):
        """Gets the target_start of this BlatResultValueObject.  # noqa: E501


        :return: The target_start of this BlatResultValueObject.  # noqa: E501
        :rtype: int
        """
        return self._target_start

    @target_start.setter
    def target_start(self, target_start):
        """Sets the target_start of this BlatResultValueObject.


        :param target_start: The target_start of this BlatResultValueObject.  # noqa: E501
        :type: int
        """

        self._target_start = target_start

    @property
    def target_starts(self):
        """Gets the target_starts of this BlatResultValueObject.  # noqa: E501


        :return: The target_starts of this BlatResultValueObject.  # noqa: E501
        :rtype: str
        """
        return self._target_starts

    @target_starts.setter
    def target_starts(self, target_starts):
        """Sets the target_starts of this BlatResultValueObject.


        :param target_starts: The target_starts of this BlatResultValueObject.  # noqa: E501
        :type: str
        """

        self._target_starts = target_starts

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
        if issubclass(BlatResultValueObject, dict):
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
        if not isinstance(other, BlatResultValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
