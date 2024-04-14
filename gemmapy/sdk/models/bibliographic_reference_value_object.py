# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.7.3
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BibliographicReferenceValueObject(object):
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
        'abstract_text': 'str',
        'author_list': 'str',
        'citation': 'CitationValueObject',
        'experiments': 'list[ExpressionExperimentValueObject]',
        'issue': 'str',
        'pages': 'str',
        'pub_accession': 'str',
        'publication': 'str',
        'publication_date': 'datetime',
        'publisher': 'str',
        'title': 'str',
        'volume': 'str',
        'mesh_terms': 'list[str]',
        'chemicals_terms': 'list[str]',
        'bibliographic_phenotypes': 'list[BibliographicPhenotypesValueObject]',
        'retracted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'abstract_text': 'abstractText',
        'author_list': 'authorList',
        'citation': 'citation',
        'experiments': 'experiments',
        'issue': 'issue',
        'pages': 'pages',
        'pub_accession': 'pubAccession',
        'publication': 'publication',
        'publication_date': 'publicationDate',
        'publisher': 'publisher',
        'title': 'title',
        'volume': 'volume',
        'mesh_terms': 'meshTerms',
        'chemicals_terms': 'chemicalsTerms',
        'bibliographic_phenotypes': 'bibliographicPhenotypes',
        'retracted': 'retracted'
    }

    def __init__(self, id=None, abstract_text=None, author_list=None, citation=None, experiments=None, issue=None, pages=None, pub_accession=None, publication=None, publication_date=None, publisher=None, title=None, volume=None, mesh_terms=None, chemicals_terms=None, bibliographic_phenotypes=None, retracted=None):  # noqa: E501
        """BibliographicReferenceValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._abstract_text = None
        self._author_list = None
        self._citation = None
        self._experiments = None
        self._issue = None
        self._pages = None
        self._pub_accession = None
        self._publication = None
        self._publication_date = None
        self._publisher = None
        self._title = None
        self._volume = None
        self._mesh_terms = None
        self._chemicals_terms = None
        self._bibliographic_phenotypes = None
        self._retracted = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if abstract_text is not None:
            self.abstract_text = abstract_text
        if author_list is not None:
            self.author_list = author_list
        if citation is not None:
            self.citation = citation
        if experiments is not None:
            self.experiments = experiments
        if issue is not None:
            self.issue = issue
        if pages is not None:
            self.pages = pages
        if pub_accession is not None:
            self.pub_accession = pub_accession
        if publication is not None:
            self.publication = publication
        if publication_date is not None:
            self.publication_date = publication_date
        if publisher is not None:
            self.publisher = publisher
        if title is not None:
            self.title = title
        if volume is not None:
            self.volume = volume
        if mesh_terms is not None:
            self.mesh_terms = mesh_terms
        if chemicals_terms is not None:
            self.chemicals_terms = chemicals_terms
        if bibliographic_phenotypes is not None:
            self.bibliographic_phenotypes = bibliographic_phenotypes
        if retracted is not None:
            self.retracted = retracted

    @property
    def id(self):
        """Gets the id of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The id of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BibliographicReferenceValueObject.


        :param id: The id of this BibliographicReferenceValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def abstract_text(self):
        """Gets the abstract_text of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The abstract_text of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._abstract_text

    @abstract_text.setter
    def abstract_text(self, abstract_text):
        """Sets the abstract_text of this BibliographicReferenceValueObject.


        :param abstract_text: The abstract_text of this BibliographicReferenceValueObject.  # noqa: E501
        :type: str
        """

        self._abstract_text = abstract_text

    @property
    def author_list(self):
        """Gets the author_list of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The author_list of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._author_list

    @author_list.setter
    def author_list(self, author_list):
        """Sets the author_list of this BibliographicReferenceValueObject.


        :param author_list: The author_list of this BibliographicReferenceValueObject.  # noqa: E501
        :type: str
        """

        self._author_list = author_list

    @property
    def citation(self):
        """Gets the citation of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The citation of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: CitationValueObject
        """
        return self._citation

    @citation.setter
    def citation(self, citation):
        """Sets the citation of this BibliographicReferenceValueObject.


        :param citation: The citation of this BibliographicReferenceValueObject.  # noqa: E501
        :type: CitationValueObject
        """

        self._citation = citation

    @property
    def experiments(self):
        """Gets the experiments of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The experiments of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: list[ExpressionExperimentValueObject]
        """
        return self._experiments

    @experiments.setter
    def experiments(self, experiments):
        """Sets the experiments of this BibliographicReferenceValueObject.


        :param experiments: The experiments of this BibliographicReferenceValueObject.  # noqa: E501
        :type: list[ExpressionExperimentValueObject]
        """

        self._experiments = experiments

    @property
    def issue(self):
        """Gets the issue of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The issue of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """Sets the issue of this BibliographicReferenceValueObject.


        :param issue: The issue of this BibliographicReferenceValueObject.  # noqa: E501
        :type: str
        """

        self._issue = issue

    @property
    def pages(self):
        """Gets the pages of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The pages of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this BibliographicReferenceValueObject.


        :param pages: The pages of this BibliographicReferenceValueObject.  # noqa: E501
        :type: str
        """

        self._pages = pages

    @property
    def pub_accession(self):
        """Gets the pub_accession of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The pub_accession of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._pub_accession

    @pub_accession.setter
    def pub_accession(self, pub_accession):
        """Sets the pub_accession of this BibliographicReferenceValueObject.


        :param pub_accession: The pub_accession of this BibliographicReferenceValueObject.  # noqa: E501
        :type: str
        """

        self._pub_accession = pub_accession

    @property
    def publication(self):
        """Gets the publication of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The publication of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._publication

    @publication.setter
    def publication(self, publication):
        """Sets the publication of this BibliographicReferenceValueObject.


        :param publication: The publication of this BibliographicReferenceValueObject.  # noqa: E501
        :type: str
        """

        self._publication = publication

    @property
    def publication_date(self):
        """Gets the publication_date of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The publication_date of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this BibliographicReferenceValueObject.


        :param publication_date: The publication_date of this BibliographicReferenceValueObject.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def publisher(self):
        """Gets the publisher of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The publisher of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this BibliographicReferenceValueObject.


        :param publisher: The publisher of this BibliographicReferenceValueObject.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def title(self):
        """Gets the title of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The title of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BibliographicReferenceValueObject.


        :param title: The title of this BibliographicReferenceValueObject.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def volume(self):
        """Gets the volume of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The volume of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this BibliographicReferenceValueObject.


        :param volume: The volume of this BibliographicReferenceValueObject.  # noqa: E501
        :type: str
        """

        self._volume = volume

    @property
    def mesh_terms(self):
        """Gets the mesh_terms of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The mesh_terms of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._mesh_terms

    @mesh_terms.setter
    def mesh_terms(self, mesh_terms):
        """Sets the mesh_terms of this BibliographicReferenceValueObject.


        :param mesh_terms: The mesh_terms of this BibliographicReferenceValueObject.  # noqa: E501
        :type: list[str]
        """

        self._mesh_terms = mesh_terms

    @property
    def chemicals_terms(self):
        """Gets the chemicals_terms of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The chemicals_terms of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._chemicals_terms

    @chemicals_terms.setter
    def chemicals_terms(self, chemicals_terms):
        """Sets the chemicals_terms of this BibliographicReferenceValueObject.


        :param chemicals_terms: The chemicals_terms of this BibliographicReferenceValueObject.  # noqa: E501
        :type: list[str]
        """

        self._chemicals_terms = chemicals_terms

    @property
    def bibliographic_phenotypes(self):
        """Gets the bibliographic_phenotypes of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The bibliographic_phenotypes of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: list[BibliographicPhenotypesValueObject]
        """
        return self._bibliographic_phenotypes

    @bibliographic_phenotypes.setter
    def bibliographic_phenotypes(self, bibliographic_phenotypes):
        """Sets the bibliographic_phenotypes of this BibliographicReferenceValueObject.


        :param bibliographic_phenotypes: The bibliographic_phenotypes of this BibliographicReferenceValueObject.  # noqa: E501
        :type: list[BibliographicPhenotypesValueObject]
        """

        self._bibliographic_phenotypes = bibliographic_phenotypes

    @property
    def retracted(self):
        """Gets the retracted of this BibliographicReferenceValueObject.  # noqa: E501


        :return: The retracted of this BibliographicReferenceValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._retracted

    @retracted.setter
    def retracted(self, retracted):
        """Sets the retracted of this BibliographicReferenceValueObject.


        :param retracted: The retracted of this BibliographicReferenceValueObject.  # noqa: E501
        :type: bool
        """

        self._retracted = retracted

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
        if issubclass(BibliographicReferenceValueObject, dict):
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
        if not isinstance(other, BibliographicReferenceValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
