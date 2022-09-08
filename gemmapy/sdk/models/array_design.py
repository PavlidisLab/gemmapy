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

class ArrayDesign(object):
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
        'advertised_number_of_design_elements': 'int',
        'alternate_names': 'list[AlternateName]',
        'alternative_to': 'ArrayDesign',
        'composite_sequences': 'list[CompositeSequence]',
        'curation_details': 'CurationDetails',
        'design_provider': 'Contact',
        'external_references': 'list[DatabaseEntry]',
        'merged_into': 'ArrayDesign',
        'mergees': 'list[ArrayDesign]',
        'primary_taxon': 'Taxon',
        'short_name': 'str',
        'subsumed_array_designs': 'list[ArrayDesign]',
        'subsuming_array_design': 'ArrayDesign',
        'technology_type': 'TechnologyType'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'audit_trail': 'auditTrail',
        'advertised_number_of_design_elements': 'advertisedNumberOfDesignElements',
        'alternate_names': 'alternateNames',
        'alternative_to': 'alternativeTo',
        'composite_sequences': 'compositeSequences',
        'curation_details': 'curationDetails',
        'design_provider': 'designProvider',
        'external_references': 'externalReferences',
        'merged_into': 'mergedInto',
        'mergees': 'mergees',
        'primary_taxon': 'primaryTaxon',
        'short_name': 'shortName',
        'subsumed_array_designs': 'subsumedArrayDesigns',
        'subsuming_array_design': 'subsumingArrayDesign',
        'technology_type': 'technologyType'
    }

    def __init__(self, name=None, description=None, id=None, audit_trail=None, advertised_number_of_design_elements=None, alternate_names=None, alternative_to=None, composite_sequences=None, curation_details=None, design_provider=None, external_references=None, merged_into=None, mergees=None, primary_taxon=None, short_name=None, subsumed_array_designs=None, subsuming_array_design=None, technology_type=None):  # noqa: E501
        """ArrayDesign - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._id = None
        self._audit_trail = None
        self._advertised_number_of_design_elements = None
        self._alternate_names = None
        self._alternative_to = None
        self._composite_sequences = None
        self._curation_details = None
        self._design_provider = None
        self._external_references = None
        self._merged_into = None
        self._mergees = None
        self._primary_taxon = None
        self._short_name = None
        self._subsumed_array_designs = None
        self._subsuming_array_design = None
        self._technology_type = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if audit_trail is not None:
            self.audit_trail = audit_trail
        if advertised_number_of_design_elements is not None:
            self.advertised_number_of_design_elements = advertised_number_of_design_elements
        if alternate_names is not None:
            self.alternate_names = alternate_names
        if alternative_to is not None:
            self.alternative_to = alternative_to
        if composite_sequences is not None:
            self.composite_sequences = composite_sequences
        if curation_details is not None:
            self.curation_details = curation_details
        if design_provider is not None:
            self.design_provider = design_provider
        if external_references is not None:
            self.external_references = external_references
        if merged_into is not None:
            self.merged_into = merged_into
        if mergees is not None:
            self.mergees = mergees
        if primary_taxon is not None:
            self.primary_taxon = primary_taxon
        if short_name is not None:
            self.short_name = short_name
        if subsumed_array_designs is not None:
            self.subsumed_array_designs = subsumed_array_designs
        if subsuming_array_design is not None:
            self.subsuming_array_design = subsuming_array_design
        if technology_type is not None:
            self.technology_type = technology_type

    @property
    def name(self):
        """Gets the name of this ArrayDesign.  # noqa: E501


        :return: The name of this ArrayDesign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArrayDesign.


        :param name: The name of this ArrayDesign.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ArrayDesign.  # noqa: E501


        :return: The description of this ArrayDesign.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ArrayDesign.


        :param description: The description of this ArrayDesign.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ArrayDesign.  # noqa: E501


        :return: The id of this ArrayDesign.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArrayDesign.


        :param id: The id of this ArrayDesign.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def audit_trail(self):
        """Gets the audit_trail of this ArrayDesign.  # noqa: E501


        :return: The audit_trail of this ArrayDesign.  # noqa: E501
        :rtype: AuditTrail
        """
        return self._audit_trail

    @audit_trail.setter
    def audit_trail(self, audit_trail):
        """Sets the audit_trail of this ArrayDesign.


        :param audit_trail: The audit_trail of this ArrayDesign.  # noqa: E501
        :type: AuditTrail
        """

        self._audit_trail = audit_trail

    @property
    def advertised_number_of_design_elements(self):
        """Gets the advertised_number_of_design_elements of this ArrayDesign.  # noqa: E501


        :return: The advertised_number_of_design_elements of this ArrayDesign.  # noqa: E501
        :rtype: int
        """
        return self._advertised_number_of_design_elements

    @advertised_number_of_design_elements.setter
    def advertised_number_of_design_elements(self, advertised_number_of_design_elements):
        """Sets the advertised_number_of_design_elements of this ArrayDesign.


        :param advertised_number_of_design_elements: The advertised_number_of_design_elements of this ArrayDesign.  # noqa: E501
        :type: int
        """

        self._advertised_number_of_design_elements = advertised_number_of_design_elements

    @property
    def alternate_names(self):
        """Gets the alternate_names of this ArrayDesign.  # noqa: E501


        :return: The alternate_names of this ArrayDesign.  # noqa: E501
        :rtype: list[AlternateName]
        """
        return self._alternate_names

    @alternate_names.setter
    def alternate_names(self, alternate_names):
        """Sets the alternate_names of this ArrayDesign.


        :param alternate_names: The alternate_names of this ArrayDesign.  # noqa: E501
        :type: list[AlternateName]
        """

        self._alternate_names = alternate_names

    @property
    def alternative_to(self):
        """Gets the alternative_to of this ArrayDesign.  # noqa: E501


        :return: The alternative_to of this ArrayDesign.  # noqa: E501
        :rtype: ArrayDesign
        """
        return self._alternative_to

    @alternative_to.setter
    def alternative_to(self, alternative_to):
        """Sets the alternative_to of this ArrayDesign.


        :param alternative_to: The alternative_to of this ArrayDesign.  # noqa: E501
        :type: ArrayDesign
        """

        self._alternative_to = alternative_to

    @property
    def composite_sequences(self):
        """Gets the composite_sequences of this ArrayDesign.  # noqa: E501


        :return: The composite_sequences of this ArrayDesign.  # noqa: E501
        :rtype: list[CompositeSequence]
        """
        return self._composite_sequences

    @composite_sequences.setter
    def composite_sequences(self, composite_sequences):
        """Sets the composite_sequences of this ArrayDesign.


        :param composite_sequences: The composite_sequences of this ArrayDesign.  # noqa: E501
        :type: list[CompositeSequence]
        """

        self._composite_sequences = composite_sequences

    @property
    def curation_details(self):
        """Gets the curation_details of this ArrayDesign.  # noqa: E501


        :return: The curation_details of this ArrayDesign.  # noqa: E501
        :rtype: CurationDetails
        """
        return self._curation_details

    @curation_details.setter
    def curation_details(self, curation_details):
        """Sets the curation_details of this ArrayDesign.


        :param curation_details: The curation_details of this ArrayDesign.  # noqa: E501
        :type: CurationDetails
        """

        self._curation_details = curation_details

    @property
    def design_provider(self):
        """Gets the design_provider of this ArrayDesign.  # noqa: E501


        :return: The design_provider of this ArrayDesign.  # noqa: E501
        :rtype: Contact
        """
        return self._design_provider

    @design_provider.setter
    def design_provider(self, design_provider):
        """Sets the design_provider of this ArrayDesign.


        :param design_provider: The design_provider of this ArrayDesign.  # noqa: E501
        :type: Contact
        """

        self._design_provider = design_provider

    @property
    def external_references(self):
        """Gets the external_references of this ArrayDesign.  # noqa: E501


        :return: The external_references of this ArrayDesign.  # noqa: E501
        :rtype: list[DatabaseEntry]
        """
        return self._external_references

    @external_references.setter
    def external_references(self, external_references):
        """Sets the external_references of this ArrayDesign.


        :param external_references: The external_references of this ArrayDesign.  # noqa: E501
        :type: list[DatabaseEntry]
        """

        self._external_references = external_references

    @property
    def merged_into(self):
        """Gets the merged_into of this ArrayDesign.  # noqa: E501


        :return: The merged_into of this ArrayDesign.  # noqa: E501
        :rtype: ArrayDesign
        """
        return self._merged_into

    @merged_into.setter
    def merged_into(self, merged_into):
        """Sets the merged_into of this ArrayDesign.


        :param merged_into: The merged_into of this ArrayDesign.  # noqa: E501
        :type: ArrayDesign
        """

        self._merged_into = merged_into

    @property
    def mergees(self):
        """Gets the mergees of this ArrayDesign.  # noqa: E501


        :return: The mergees of this ArrayDesign.  # noqa: E501
        :rtype: list[ArrayDesign]
        """
        return self._mergees

    @mergees.setter
    def mergees(self, mergees):
        """Sets the mergees of this ArrayDesign.


        :param mergees: The mergees of this ArrayDesign.  # noqa: E501
        :type: list[ArrayDesign]
        """

        self._mergees = mergees

    @property
    def primary_taxon(self):
        """Gets the primary_taxon of this ArrayDesign.  # noqa: E501


        :return: The primary_taxon of this ArrayDesign.  # noqa: E501
        :rtype: Taxon
        """
        return self._primary_taxon

    @primary_taxon.setter
    def primary_taxon(self, primary_taxon):
        """Sets the primary_taxon of this ArrayDesign.


        :param primary_taxon: The primary_taxon of this ArrayDesign.  # noqa: E501
        :type: Taxon
        """

        self._primary_taxon = primary_taxon

    @property
    def short_name(self):
        """Gets the short_name of this ArrayDesign.  # noqa: E501


        :return: The short_name of this ArrayDesign.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this ArrayDesign.


        :param short_name: The short_name of this ArrayDesign.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def subsumed_array_designs(self):
        """Gets the subsumed_array_designs of this ArrayDesign.  # noqa: E501


        :return: The subsumed_array_designs of this ArrayDesign.  # noqa: E501
        :rtype: list[ArrayDesign]
        """
        return self._subsumed_array_designs

    @subsumed_array_designs.setter
    def subsumed_array_designs(self, subsumed_array_designs):
        """Sets the subsumed_array_designs of this ArrayDesign.


        :param subsumed_array_designs: The subsumed_array_designs of this ArrayDesign.  # noqa: E501
        :type: list[ArrayDesign]
        """

        self._subsumed_array_designs = subsumed_array_designs

    @property
    def subsuming_array_design(self):
        """Gets the subsuming_array_design of this ArrayDesign.  # noqa: E501


        :return: The subsuming_array_design of this ArrayDesign.  # noqa: E501
        :rtype: ArrayDesign
        """
        return self._subsuming_array_design

    @subsuming_array_design.setter
    def subsuming_array_design(self, subsuming_array_design):
        """Sets the subsuming_array_design of this ArrayDesign.


        :param subsuming_array_design: The subsuming_array_design of this ArrayDesign.  # noqa: E501
        :type: ArrayDesign
        """

        self._subsuming_array_design = subsuming_array_design

    @property
    def technology_type(self):
        """Gets the technology_type of this ArrayDesign.  # noqa: E501


        :return: The technology_type of this ArrayDesign.  # noqa: E501
        :rtype: TechnologyType
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """Sets the technology_type of this ArrayDesign.


        :param technology_type: The technology_type of this ArrayDesign.  # noqa: E501
        :type: TechnologyType
        """

        self._technology_type = technology_type

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
        if issubclass(ArrayDesign, dict):
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
        if not isinstance(other, ArrayDesign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
