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

class PhenotypeAssociation(object):
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
        'name': 'str',
        'description': 'str',
        'id': 'int',
        'audit_trail': 'AuditTrail',
        'evidence_code': 'GOEvidenceCode',
        'is_negative_evidence': 'bool',
        'score': 'str',
        'strength': 'float',
        'gene': 'Gene',
        'phenotypes': 'list[Characteristic]',
        'association_type': 'Characteristic',
        'evidence_source': 'DatabaseEntry',
        'score_type': 'QuantitationType',
        'phenotype_association_publications': 'list[PhenotypeAssociationPublication]',
        'mapping_type': 'PhenotypeMappingType',
        'original_phenotype': 'str',
        'relationship': 'str',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'audit_trail': 'auditTrail',
        'evidence_code': 'evidenceCode',
        'is_negative_evidence': 'isNegativeEvidence',
        'score': 'score',
        'strength': 'strength',
        'gene': 'gene',
        'phenotypes': 'phenotypes',
        'association_type': 'associationType',
        'evidence_source': 'evidenceSource',
        'score_type': 'scoreType',
        'phenotype_association_publications': 'phenotypeAssociationPublications',
        'mapping_type': 'mappingType',
        'original_phenotype': 'originalPhenotype',
        'relationship': 'relationship',
        'last_updated': 'lastUpdated'
    }

    def __init__(self, name=None, description=None, id=None, audit_trail=None, evidence_code=None, is_negative_evidence=None, score=None, strength=None, gene=None, phenotypes=None, association_type=None, evidence_source=None, score_type=None, phenotype_association_publications=None, mapping_type=None, original_phenotype=None, relationship=None, last_updated=None):  # noqa: E501
        """PhenotypeAssociation - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._id = None
        self._audit_trail = None
        self._evidence_code = None
        self._is_negative_evidence = None
        self._score = None
        self._strength = None
        self._gene = None
        self._phenotypes = None
        self._association_type = None
        self._evidence_source = None
        self._score_type = None
        self._phenotype_association_publications = None
        self._mapping_type = None
        self._original_phenotype = None
        self._relationship = None
        self._last_updated = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if audit_trail is not None:
            self.audit_trail = audit_trail
        if evidence_code is not None:
            self.evidence_code = evidence_code
        if is_negative_evidence is not None:
            self.is_negative_evidence = is_negative_evidence
        if score is not None:
            self.score = score
        if strength is not None:
            self.strength = strength
        if gene is not None:
            self.gene = gene
        if phenotypes is not None:
            self.phenotypes = phenotypes
        if association_type is not None:
            self.association_type = association_type
        if evidence_source is not None:
            self.evidence_source = evidence_source
        if score_type is not None:
            self.score_type = score_type
        if phenotype_association_publications is not None:
            self.phenotype_association_publications = phenotype_association_publications
        if mapping_type is not None:
            self.mapping_type = mapping_type
        if original_phenotype is not None:
            self.original_phenotype = original_phenotype
        if relationship is not None:
            self.relationship = relationship
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def name(self):
        """Gets the name of this PhenotypeAssociation.  # noqa: E501


        :return: The name of this PhenotypeAssociation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhenotypeAssociation.


        :param name: The name of this PhenotypeAssociation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this PhenotypeAssociation.  # noqa: E501


        :return: The description of this PhenotypeAssociation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PhenotypeAssociation.


        :param description: The description of this PhenotypeAssociation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this PhenotypeAssociation.  # noqa: E501


        :return: The id of this PhenotypeAssociation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PhenotypeAssociation.


        :param id: The id of this PhenotypeAssociation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def audit_trail(self):
        """Gets the audit_trail of this PhenotypeAssociation.  # noqa: E501


        :return: The audit_trail of this PhenotypeAssociation.  # noqa: E501
        :rtype: AuditTrail
        """
        return self._audit_trail

    @audit_trail.setter
    def audit_trail(self, audit_trail):
        """Sets the audit_trail of this PhenotypeAssociation.


        :param audit_trail: The audit_trail of this PhenotypeAssociation.  # noqa: E501
        :type: AuditTrail
        """

        self._audit_trail = audit_trail

    @property
    def evidence_code(self):
        """Gets the evidence_code of this PhenotypeAssociation.  # noqa: E501


        :return: The evidence_code of this PhenotypeAssociation.  # noqa: E501
        :rtype: GOEvidenceCode
        """
        return self._evidence_code

    @evidence_code.setter
    def evidence_code(self, evidence_code):
        """Sets the evidence_code of this PhenotypeAssociation.


        :param evidence_code: The evidence_code of this PhenotypeAssociation.  # noqa: E501
        :type: GOEvidenceCode
        """

        self._evidence_code = evidence_code

    @property
    def is_negative_evidence(self):
        """Gets the is_negative_evidence of this PhenotypeAssociation.  # noqa: E501


        :return: The is_negative_evidence of this PhenotypeAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._is_negative_evidence

    @is_negative_evidence.setter
    def is_negative_evidence(self, is_negative_evidence):
        """Sets the is_negative_evidence of this PhenotypeAssociation.


        :param is_negative_evidence: The is_negative_evidence of this PhenotypeAssociation.  # noqa: E501
        :type: bool
        """

        self._is_negative_evidence = is_negative_evidence

    @property
    def score(self):
        """Gets the score of this PhenotypeAssociation.  # noqa: E501


        :return: The score of this PhenotypeAssociation.  # noqa: E501
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this PhenotypeAssociation.


        :param score: The score of this PhenotypeAssociation.  # noqa: E501
        :type: str
        """

        self._score = score

    @property
    def strength(self):
        """Gets the strength of this PhenotypeAssociation.  # noqa: E501


        :return: The strength of this PhenotypeAssociation.  # noqa: E501
        :rtype: float
        """
        return self._strength

    @strength.setter
    def strength(self, strength):
        """Sets the strength of this PhenotypeAssociation.


        :param strength: The strength of this PhenotypeAssociation.  # noqa: E501
        :type: float
        """

        self._strength = strength

    @property
    def gene(self):
        """Gets the gene of this PhenotypeAssociation.  # noqa: E501


        :return: The gene of this PhenotypeAssociation.  # noqa: E501
        :rtype: Gene
        """
        return self._gene

    @gene.setter
    def gene(self, gene):
        """Sets the gene of this PhenotypeAssociation.


        :param gene: The gene of this PhenotypeAssociation.  # noqa: E501
        :type: Gene
        """

        self._gene = gene

    @property
    def phenotypes(self):
        """Gets the phenotypes of this PhenotypeAssociation.  # noqa: E501


        :return: The phenotypes of this PhenotypeAssociation.  # noqa: E501
        :rtype: list[Characteristic]
        """
        return self._phenotypes

    @phenotypes.setter
    def phenotypes(self, phenotypes):
        """Sets the phenotypes of this PhenotypeAssociation.


        :param phenotypes: The phenotypes of this PhenotypeAssociation.  # noqa: E501
        :type: list[Characteristic]
        """

        self._phenotypes = phenotypes

    @property
    def association_type(self):
        """Gets the association_type of this PhenotypeAssociation.  # noqa: E501


        :return: The association_type of this PhenotypeAssociation.  # noqa: E501
        :rtype: Characteristic
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        """Sets the association_type of this PhenotypeAssociation.


        :param association_type: The association_type of this PhenotypeAssociation.  # noqa: E501
        :type: Characteristic
        """

        self._association_type = association_type

    @property
    def evidence_source(self):
        """Gets the evidence_source of this PhenotypeAssociation.  # noqa: E501


        :return: The evidence_source of this PhenotypeAssociation.  # noqa: E501
        :rtype: DatabaseEntry
        """
        return self._evidence_source

    @evidence_source.setter
    def evidence_source(self, evidence_source):
        """Sets the evidence_source of this PhenotypeAssociation.


        :param evidence_source: The evidence_source of this PhenotypeAssociation.  # noqa: E501
        :type: DatabaseEntry
        """

        self._evidence_source = evidence_source

    @property
    def score_type(self):
        """Gets the score_type of this PhenotypeAssociation.  # noqa: E501


        :return: The score_type of this PhenotypeAssociation.  # noqa: E501
        :rtype: QuantitationType
        """
        return self._score_type

    @score_type.setter
    def score_type(self, score_type):
        """Sets the score_type of this PhenotypeAssociation.


        :param score_type: The score_type of this PhenotypeAssociation.  # noqa: E501
        :type: QuantitationType
        """

        self._score_type = score_type

    @property
    def phenotype_association_publications(self):
        """Gets the phenotype_association_publications of this PhenotypeAssociation.  # noqa: E501


        :return: The phenotype_association_publications of this PhenotypeAssociation.  # noqa: E501
        :rtype: list[PhenotypeAssociationPublication]
        """
        return self._phenotype_association_publications

    @phenotype_association_publications.setter
    def phenotype_association_publications(self, phenotype_association_publications):
        """Sets the phenotype_association_publications of this PhenotypeAssociation.


        :param phenotype_association_publications: The phenotype_association_publications of this PhenotypeAssociation.  # noqa: E501
        :type: list[PhenotypeAssociationPublication]
        """

        self._phenotype_association_publications = phenotype_association_publications

    @property
    def mapping_type(self):
        """Gets the mapping_type of this PhenotypeAssociation.  # noqa: E501


        :return: The mapping_type of this PhenotypeAssociation.  # noqa: E501
        :rtype: PhenotypeMappingType
        """
        return self._mapping_type

    @mapping_type.setter
    def mapping_type(self, mapping_type):
        """Sets the mapping_type of this PhenotypeAssociation.


        :param mapping_type: The mapping_type of this PhenotypeAssociation.  # noqa: E501
        :type: PhenotypeMappingType
        """

        self._mapping_type = mapping_type

    @property
    def original_phenotype(self):
        """Gets the original_phenotype of this PhenotypeAssociation.  # noqa: E501


        :return: The original_phenotype of this PhenotypeAssociation.  # noqa: E501
        :rtype: str
        """
        return self._original_phenotype

    @original_phenotype.setter
    def original_phenotype(self, original_phenotype):
        """Sets the original_phenotype of this PhenotypeAssociation.


        :param original_phenotype: The original_phenotype of this PhenotypeAssociation.  # noqa: E501
        :type: str
        """

        self._original_phenotype = original_phenotype

    @property
    def relationship(self):
        """Gets the relationship of this PhenotypeAssociation.  # noqa: E501


        :return: The relationship of this PhenotypeAssociation.  # noqa: E501
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this PhenotypeAssociation.


        :param relationship: The relationship of this PhenotypeAssociation.  # noqa: E501
        :type: str
        """

        self._relationship = relationship

    @property
    def last_updated(self):
        """Gets the last_updated of this PhenotypeAssociation.  # noqa: E501


        :return: The last_updated of this PhenotypeAssociation.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this PhenotypeAssociation.


        :param last_updated: The last_updated of this PhenotypeAssociation.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

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
        if issubclass(PhenotypeAssociation, dict):
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
        if not isinstance(other, PhenotypeAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other