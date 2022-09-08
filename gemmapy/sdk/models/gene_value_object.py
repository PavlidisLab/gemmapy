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

class GeneValueObject(object):
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
        'aliases': 'list[str]',
        'associated_experiment_count': 'int',
        'composite_sequence_count': 'int',
        'gene_sets': 'list[GeneSetValueObject]',
        'homologues': 'list[GeneValueObject]',
        'is_query': 'bool',
        'multifunctionality_rank': 'float',
        'ncbi_id': 'int',
        'ensembl_id': 'str',
        'node_degree_neg_ranks': 'list[float]',
        'node_degree_pos_ranks': 'list[float]',
        'node_degrees_neg': 'list[int]',
        'node_degrees_pos': 'list[int]',
        'num_go_terms': 'int',
        'official_name': 'str',
        'official_symbol': 'str',
        'phenotypes': 'list[CharacteristicValueObject]',
        'platform_count': 'int',
        'score': 'float',
        'taxon_common_name': 'str',
        'taxon_id': 'int',
        'taxon_scientific_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'aliases': 'aliases',
        'associated_experiment_count': 'associatedExperimentCount',
        'composite_sequence_count': 'compositeSequenceCount',
        'gene_sets': 'geneSets',
        'homologues': 'homologues',
        'is_query': 'isQuery',
        'multifunctionality_rank': 'multifunctionalityRank',
        'ncbi_id': 'ncbiId',
        'ensembl_id': 'ensemblId',
        'node_degree_neg_ranks': 'nodeDegreeNegRanks',
        'node_degree_pos_ranks': 'nodeDegreePosRanks',
        'node_degrees_neg': 'nodeDegreesNeg',
        'node_degrees_pos': 'nodeDegreesPos',
        'num_go_terms': 'numGoTerms',
        'official_name': 'officialName',
        'official_symbol': 'officialSymbol',
        'phenotypes': 'phenotypes',
        'platform_count': 'platformCount',
        'score': 'score',
        'taxon_common_name': 'taxonCommonName',
        'taxon_id': 'taxonId',
        'taxon_scientific_name': 'taxonScientificName'
    }

    def __init__(self, id=None, aliases=None, associated_experiment_count=None, composite_sequence_count=None, gene_sets=None, homologues=None, is_query=None, multifunctionality_rank=None, ncbi_id=None, ensembl_id=None, node_degree_neg_ranks=None, node_degree_pos_ranks=None, node_degrees_neg=None, node_degrees_pos=None, num_go_terms=None, official_name=None, official_symbol=None, phenotypes=None, platform_count=None, score=None, taxon_common_name=None, taxon_id=None, taxon_scientific_name=None):  # noqa: E501
        """GeneValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._aliases = None
        self._associated_experiment_count = None
        self._composite_sequence_count = None
        self._gene_sets = None
        self._homologues = None
        self._is_query = None
        self._multifunctionality_rank = None
        self._ncbi_id = None
        self._ensembl_id = None
        self._node_degree_neg_ranks = None
        self._node_degree_pos_ranks = None
        self._node_degrees_neg = None
        self._node_degrees_pos = None
        self._num_go_terms = None
        self._official_name = None
        self._official_symbol = None
        self._phenotypes = None
        self._platform_count = None
        self._score = None
        self._taxon_common_name = None
        self._taxon_id = None
        self._taxon_scientific_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if aliases is not None:
            self.aliases = aliases
        if associated_experiment_count is not None:
            self.associated_experiment_count = associated_experiment_count
        if composite_sequence_count is not None:
            self.composite_sequence_count = composite_sequence_count
        if gene_sets is not None:
            self.gene_sets = gene_sets
        if homologues is not None:
            self.homologues = homologues
        if is_query is not None:
            self.is_query = is_query
        if multifunctionality_rank is not None:
            self.multifunctionality_rank = multifunctionality_rank
        if ncbi_id is not None:
            self.ncbi_id = ncbi_id
        if ensembl_id is not None:
            self.ensembl_id = ensembl_id
        if node_degree_neg_ranks is not None:
            self.node_degree_neg_ranks = node_degree_neg_ranks
        if node_degree_pos_ranks is not None:
            self.node_degree_pos_ranks = node_degree_pos_ranks
        if node_degrees_neg is not None:
            self.node_degrees_neg = node_degrees_neg
        if node_degrees_pos is not None:
            self.node_degrees_pos = node_degrees_pos
        if num_go_terms is not None:
            self.num_go_terms = num_go_terms
        if official_name is not None:
            self.official_name = official_name
        if official_symbol is not None:
            self.official_symbol = official_symbol
        if phenotypes is not None:
            self.phenotypes = phenotypes
        if platform_count is not None:
            self.platform_count = platform_count
        if score is not None:
            self.score = score
        if taxon_common_name is not None:
            self.taxon_common_name = taxon_common_name
        if taxon_id is not None:
            self.taxon_id = taxon_id
        if taxon_scientific_name is not None:
            self.taxon_scientific_name = taxon_scientific_name

    @property
    def id(self):
        """Gets the id of this GeneValueObject.  # noqa: E501


        :return: The id of this GeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GeneValueObject.


        :param id: The id of this GeneValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def aliases(self):
        """Gets the aliases of this GeneValueObject.  # noqa: E501


        :return: The aliases of this GeneValueObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this GeneValueObject.


        :param aliases: The aliases of this GeneValueObject.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def associated_experiment_count(self):
        """Gets the associated_experiment_count of this GeneValueObject.  # noqa: E501


        :return: The associated_experiment_count of this GeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._associated_experiment_count

    @associated_experiment_count.setter
    def associated_experiment_count(self, associated_experiment_count):
        """Sets the associated_experiment_count of this GeneValueObject.


        :param associated_experiment_count: The associated_experiment_count of this GeneValueObject.  # noqa: E501
        :type: int
        """

        self._associated_experiment_count = associated_experiment_count

    @property
    def composite_sequence_count(self):
        """Gets the composite_sequence_count of this GeneValueObject.  # noqa: E501


        :return: The composite_sequence_count of this GeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._composite_sequence_count

    @composite_sequence_count.setter
    def composite_sequence_count(self, composite_sequence_count):
        """Sets the composite_sequence_count of this GeneValueObject.


        :param composite_sequence_count: The composite_sequence_count of this GeneValueObject.  # noqa: E501
        :type: int
        """

        self._composite_sequence_count = composite_sequence_count

    @property
    def gene_sets(self):
        """Gets the gene_sets of this GeneValueObject.  # noqa: E501


        :return: The gene_sets of this GeneValueObject.  # noqa: E501
        :rtype: list[GeneSetValueObject]
        """
        return self._gene_sets

    @gene_sets.setter
    def gene_sets(self, gene_sets):
        """Sets the gene_sets of this GeneValueObject.


        :param gene_sets: The gene_sets of this GeneValueObject.  # noqa: E501
        :type: list[GeneSetValueObject]
        """

        self._gene_sets = gene_sets

    @property
    def homologues(self):
        """Gets the homologues of this GeneValueObject.  # noqa: E501


        :return: The homologues of this GeneValueObject.  # noqa: E501
        :rtype: list[GeneValueObject]
        """
        return self._homologues

    @homologues.setter
    def homologues(self, homologues):
        """Sets the homologues of this GeneValueObject.


        :param homologues: The homologues of this GeneValueObject.  # noqa: E501
        :type: list[GeneValueObject]
        """

        self._homologues = homologues

    @property
    def is_query(self):
        """Gets the is_query of this GeneValueObject.  # noqa: E501


        :return: The is_query of this GeneValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_query

    @is_query.setter
    def is_query(self, is_query):
        """Sets the is_query of this GeneValueObject.


        :param is_query: The is_query of this GeneValueObject.  # noqa: E501
        :type: bool
        """

        self._is_query = is_query

    @property
    def multifunctionality_rank(self):
        """Gets the multifunctionality_rank of this GeneValueObject.  # noqa: E501


        :return: The multifunctionality_rank of this GeneValueObject.  # noqa: E501
        :rtype: float
        """
        return self._multifunctionality_rank

    @multifunctionality_rank.setter
    def multifunctionality_rank(self, multifunctionality_rank):
        """Sets the multifunctionality_rank of this GeneValueObject.


        :param multifunctionality_rank: The multifunctionality_rank of this GeneValueObject.  # noqa: E501
        :type: float
        """

        self._multifunctionality_rank = multifunctionality_rank

    @property
    def ncbi_id(self):
        """Gets the ncbi_id of this GeneValueObject.  # noqa: E501


        :return: The ncbi_id of this GeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._ncbi_id

    @ncbi_id.setter
    def ncbi_id(self, ncbi_id):
        """Sets the ncbi_id of this GeneValueObject.


        :param ncbi_id: The ncbi_id of this GeneValueObject.  # noqa: E501
        :type: int
        """

        self._ncbi_id = ncbi_id

    @property
    def ensembl_id(self):
        """Gets the ensembl_id of this GeneValueObject.  # noqa: E501


        :return: The ensembl_id of this GeneValueObject.  # noqa: E501
        :rtype: str
        """
        return self._ensembl_id

    @ensembl_id.setter
    def ensembl_id(self, ensembl_id):
        """Sets the ensembl_id of this GeneValueObject.


        :param ensembl_id: The ensembl_id of this GeneValueObject.  # noqa: E501
        :type: str
        """

        self._ensembl_id = ensembl_id

    @property
    def node_degree_neg_ranks(self):
        """Gets the node_degree_neg_ranks of this GeneValueObject.  # noqa: E501


        :return: The node_degree_neg_ranks of this GeneValueObject.  # noqa: E501
        :rtype: list[float]
        """
        return self._node_degree_neg_ranks

    @node_degree_neg_ranks.setter
    def node_degree_neg_ranks(self, node_degree_neg_ranks):
        """Sets the node_degree_neg_ranks of this GeneValueObject.


        :param node_degree_neg_ranks: The node_degree_neg_ranks of this GeneValueObject.  # noqa: E501
        :type: list[float]
        """

        self._node_degree_neg_ranks = node_degree_neg_ranks

    @property
    def node_degree_pos_ranks(self):
        """Gets the node_degree_pos_ranks of this GeneValueObject.  # noqa: E501


        :return: The node_degree_pos_ranks of this GeneValueObject.  # noqa: E501
        :rtype: list[float]
        """
        return self._node_degree_pos_ranks

    @node_degree_pos_ranks.setter
    def node_degree_pos_ranks(self, node_degree_pos_ranks):
        """Sets the node_degree_pos_ranks of this GeneValueObject.


        :param node_degree_pos_ranks: The node_degree_pos_ranks of this GeneValueObject.  # noqa: E501
        :type: list[float]
        """

        self._node_degree_pos_ranks = node_degree_pos_ranks

    @property
    def node_degrees_neg(self):
        """Gets the node_degrees_neg of this GeneValueObject.  # noqa: E501


        :return: The node_degrees_neg of this GeneValueObject.  # noqa: E501
        :rtype: list[int]
        """
        return self._node_degrees_neg

    @node_degrees_neg.setter
    def node_degrees_neg(self, node_degrees_neg):
        """Sets the node_degrees_neg of this GeneValueObject.


        :param node_degrees_neg: The node_degrees_neg of this GeneValueObject.  # noqa: E501
        :type: list[int]
        """

        self._node_degrees_neg = node_degrees_neg

    @property
    def node_degrees_pos(self):
        """Gets the node_degrees_pos of this GeneValueObject.  # noqa: E501


        :return: The node_degrees_pos of this GeneValueObject.  # noqa: E501
        :rtype: list[int]
        """
        return self._node_degrees_pos

    @node_degrees_pos.setter
    def node_degrees_pos(self, node_degrees_pos):
        """Sets the node_degrees_pos of this GeneValueObject.


        :param node_degrees_pos: The node_degrees_pos of this GeneValueObject.  # noqa: E501
        :type: list[int]
        """

        self._node_degrees_pos = node_degrees_pos

    @property
    def num_go_terms(self):
        """Gets the num_go_terms of this GeneValueObject.  # noqa: E501


        :return: The num_go_terms of this GeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._num_go_terms

    @num_go_terms.setter
    def num_go_terms(self, num_go_terms):
        """Sets the num_go_terms of this GeneValueObject.


        :param num_go_terms: The num_go_terms of this GeneValueObject.  # noqa: E501
        :type: int
        """

        self._num_go_terms = num_go_terms

    @property
    def official_name(self):
        """Gets the official_name of this GeneValueObject.  # noqa: E501


        :return: The official_name of this GeneValueObject.  # noqa: E501
        :rtype: str
        """
        return self._official_name

    @official_name.setter
    def official_name(self, official_name):
        """Sets the official_name of this GeneValueObject.


        :param official_name: The official_name of this GeneValueObject.  # noqa: E501
        :type: str
        """

        self._official_name = official_name

    @property
    def official_symbol(self):
        """Gets the official_symbol of this GeneValueObject.  # noqa: E501


        :return: The official_symbol of this GeneValueObject.  # noqa: E501
        :rtype: str
        """
        return self._official_symbol

    @official_symbol.setter
    def official_symbol(self, official_symbol):
        """Sets the official_symbol of this GeneValueObject.


        :param official_symbol: The official_symbol of this GeneValueObject.  # noqa: E501
        :type: str
        """

        self._official_symbol = official_symbol

    @property
    def phenotypes(self):
        """Gets the phenotypes of this GeneValueObject.  # noqa: E501


        :return: The phenotypes of this GeneValueObject.  # noqa: E501
        :rtype: list[CharacteristicValueObject]
        """
        return self._phenotypes

    @phenotypes.setter
    def phenotypes(self, phenotypes):
        """Sets the phenotypes of this GeneValueObject.


        :param phenotypes: The phenotypes of this GeneValueObject.  # noqa: E501
        :type: list[CharacteristicValueObject]
        """

        self._phenotypes = phenotypes

    @property
    def platform_count(self):
        """Gets the platform_count of this GeneValueObject.  # noqa: E501


        :return: The platform_count of this GeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._platform_count

    @platform_count.setter
    def platform_count(self, platform_count):
        """Sets the platform_count of this GeneValueObject.


        :param platform_count: The platform_count of this GeneValueObject.  # noqa: E501
        :type: int
        """

        self._platform_count = platform_count

    @property
    def score(self):
        """Gets the score of this GeneValueObject.  # noqa: E501


        :return: The score of this GeneValueObject.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this GeneValueObject.


        :param score: The score of this GeneValueObject.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def taxon_common_name(self):
        """Gets the taxon_common_name of this GeneValueObject.  # noqa: E501


        :return: The taxon_common_name of this GeneValueObject.  # noqa: E501
        :rtype: str
        """
        return self._taxon_common_name

    @taxon_common_name.setter
    def taxon_common_name(self, taxon_common_name):
        """Sets the taxon_common_name of this GeneValueObject.


        :param taxon_common_name: The taxon_common_name of this GeneValueObject.  # noqa: E501
        :type: str
        """

        self._taxon_common_name = taxon_common_name

    @property
    def taxon_id(self):
        """Gets the taxon_id of this GeneValueObject.  # noqa: E501


        :return: The taxon_id of this GeneValueObject.  # noqa: E501
        :rtype: int
        """
        return self._taxon_id

    @taxon_id.setter
    def taxon_id(self, taxon_id):
        """Sets the taxon_id of this GeneValueObject.


        :param taxon_id: The taxon_id of this GeneValueObject.  # noqa: E501
        :type: int
        """

        self._taxon_id = taxon_id

    @property
    def taxon_scientific_name(self):
        """Gets the taxon_scientific_name of this GeneValueObject.  # noqa: E501


        :return: The taxon_scientific_name of this GeneValueObject.  # noqa: E501
        :rtype: str
        """
        return self._taxon_scientific_name

    @taxon_scientific_name.setter
    def taxon_scientific_name(self, taxon_scientific_name):
        """Sets the taxon_scientific_name of this GeneValueObject.


        :param taxon_scientific_name: The taxon_scientific_name of this GeneValueObject.  # noqa: E501
        :type: str
        """

        self._taxon_scientific_name = taxon_scientific_name

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
        if issubclass(GeneValueObject, dict):
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
        if not isinstance(other, GeneValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
