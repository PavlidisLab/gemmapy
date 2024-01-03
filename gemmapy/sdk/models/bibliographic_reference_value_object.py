# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  ## Updates  ### Update 2.7.1  - improved highlights of search results - fix the limit for getDatasetsAnnotations() endpoint to 5000 in the specification - fix missing initialization of datasets retrieved from the cache  Highlights now use Markdown syntax for formatting. Fields for highlighted ontology terms now use complete object path instead of just `term`. Last but not least, highlights from multiple results are merged.  ### Update 2.7.0  New endpoints for counting the number of results: `getNumberOfDatasets`, `getNumberOfPlatforms`, `getNumberOfResultSets`. These endpoints are faster than looking up `totalElements` as no data is retrieved or converted.  Datasets can now be filtered by annotations at the sample, factor value and all levels using the three newly exposed `experimentalDesign.experimentalFactors.factorValues.characteristics`, `bioAssays.sampleUsed.characteristics` and `allCharacteristics` collections. The two useful available properties for filtering are `value` and `valueUri`.  New `getDatasetsAnnotationsUsageStatistics`, `getDatasetsPlatformsUsageStatistics` and `getDatasetsTaxaUsageStatistics` endpoints for retrieving annotations, platforms and taxa used by the matched datasets. The endpoint accepts the same `filter` argument of `getDatasets`, allowing one to easily navigate terms, platforms and taxa available for filtering furthermore.  Properties available for filtering and sorting are enumerated in the description of the corresponding parameter. There's been a number of fixes and additional tests performed to ensure that all advertised properties are working as expected.  The `FilterArg` and `SortArg`-based parameters now have OpenAPI extensions to enumerate available properties in a structured format under the `x-gemma-filterable-properties`key. Possible values are exposed for enumerated types.  ```yaml x-gemma-filterable-properties: - name: technologyType   type: string   allowedValues:   - value: ONECOLOR     label: One Color   - value: SEQUENCING     label: Sequencing   security:     basicAuth: [GROUP_ADMIN]     cookieAuth: [GROUP_ADMIN] ```  Some of the exposed properties such as `geeq.publicSuitabilityScore` require specific authorities to use. This is documented in `x-filterable-properties` by specifying a [Security Requirement Object](https://spec.openapis.org/oas/latest.html#security-requirement-object).  Types that use the `[]` suffix are using sub-queries under the hood. It implies that the entity will be matched if at least one related entity matches the supplied filter. For example, the `characteristics.valueUri = http://purl.obolibrary.org/obo/UBERON_0002107` filter will match datasets with at least one `UBERON:0002107` tag attached.  Filtered endpoints (including paginated and limited ones) now expose a `groupBy` array that enumerates all the properties used to group results. This helps clear confusion about what constitute a business key in the returned response.  ### Update 2.6.1  Add support for filtering platforms by taxon ID, common name, scientific name, etc. for the `/platforms` endpoint.  ### Update 2.6.0  Add a new `externalDatabases` attribute to the main endpoint that displays version of some of the main external databases that we are using. This exposes versions and last updates for genomes, gene annotations, GO terms, and much more!  The `ExternalDatabaseValueObject` now exposes a `description` which provides additional details.  ### Update 2.5.2  Restore `factors` in `BioMaterialValueObject` as it is being still used by our RNA-Seq pipeline. The attribute is deprecated and should not be used and will be removed when we find a suitable alternative.  Introduce a new endpoint to retrieve quantitation types for a given dataset and parameters to retrieve expression data by quantitation type to `getDatasetProcessedExpression` and `getDatasetRawExpression`. As it was too difficult to extends `getDatasetExpression` to also support quantitation type while retaining the filter feature, we decided to deprecate it and reintroduce filtering for both raw and processed expression in the future.  Fix return type for `getResultSets` which was incorrectly referring to a renamed VO.  Annotate all possible types for `SearchResult.resultObject`. This incidentally includes the `GeneSetValueObject` in the specification which is not exposed elsewhere in the API.  ### Update 2.5.1  Restore `objectClass` visibility in `AnnotationValueObject`.  Fix incorrect response types for annotations search endpoints returning datasets.  ### Update 2.5.0  Major cleanups were performed in this release in order to stabilize the specification. Numerous properties from Gemma Web that were never intended to be exposed in Gemma REST have been hidden. It's a bit too much to describe in here, but you can navigate to the schemas section below to get a good glance at the models.  Favour `numberOfSomething` instead of `somethingCount` which is clearer. The older names are kept for backward-compatibility, but should be considered deprecated.  Gene aliases and multifunctionality rank are now filled in `GeneValueObject`.  Uniformly use `TaxonValueObject` to represent taxon. This is breaking change for the `ExpressionExperimentValueObject` and `ArrayDesignValueObject` as their `taxon` property will be an `object` instead of a `string`. Properties such as `taxonId` are now deprecated and `taxon.id` should be used instead.  Entities that have IDs now all inherit from `IdentifiableValueObject`. This implies that you can assume the presence of an `id` in a search result `resultObject` attribute for example.  New `/search` endpoint! for an unified search experience. Annotation-based search endpoints under `/annotations` are now deprecated.  New API docs! While not as nice looking, the previous theme will be gradually ported to Swagger UI as we focused on functionality over prettiness for this release.  ### Update 2.4.0 through 2.4.1  Release notes for the 2.4 series were not written down, so I'll try to do my best to recall features that were introduced at that time.  An [OpenAPI](https://www.openapis.org/) specification was introduced and available under `/rest/v2/openapi.json`, although not fully stabilized.  Add a `/resultSets` endpoint to navigate result sets directly, by ID or by dataset.  Add a `/resultSets/{resultSetId}` endpoint to retrieve a specific result set by its ID. This endpoint can be negotiated with an `Accept: text/tab-separated-values` header to obtain a TSV representation.  Add a `/datasets/{dataset}/analyses/differential/resultSets` endpoint that essentially redirect to a specific `/resultSet` endpoint by dataset ID.  Add an endpoint to retrieve preferred raw expression vectors.  ### Update 2.3.4  November 6th, 2018  November 6th [2.3.4] Bug fixes in the dataset search endpoint.  November 5th [2.3.3] Added filtering parameters to dataset search.  October 25th [2.3.2] Changed behavior of the dataset search endpoint to more closely match the Gemma web interface.  October 2nd [2.3.1] Added group information to the User value object.  September 27th [2.3.0] Breaking change in Taxa: Abbreviation property has been removed and is therefore no longer an accepted identifier.  ### Update 2.2.6  June 7th, 2018  Code maintenance, bug fixes. Geeq scores stable and made public.  June 7th [2.2.6] Added: User authentication endpoint.  May 2nd [2.2.5] Fixed: Cleaned up and optimized platforms/elements endpoint, removed redundant information (recursive properties nesting).  April 12th [2.2.3] Fixed: Array arguments not handling non-string properties properly, e.g. `ncbiIds` of genes.  April 9th [2.2.1] Fixed: Filter argument not working when the filtered field was a primitive type. This most significantly allows filtering by geeq boolean and double properties.  ### Update 2.2.0  February 8th, 2018  Breaking change in the 'Dataset differential analysis' endpoint: - No longer using `qValueThreshold` parameter. - Response format changed, now using `DifferentialExpressionAnalysisValueObject` instead of `DifferentialExpressionValueObject` - [Experimental] Added Geeq (Gene Expression Experiment Quality) scores to the dataset value objects   # noqa: E501

    OpenAPI spec version: 2.7.1
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
