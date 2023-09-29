# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  ## Updates  ### Update 2.7.1  - improved highlights of search results - fix the limit for getDatasetsAnnotations() endpoint to 5000 in the specification - fix missing initialization of datasets retrieved from the cache  Highlights now use Markdown syntax for formatting. Fields for highlighted ontology terms now use complete object path instead of just `term`. Last but not least, highlights from multiple results are merged.  ### Update 2.7.0  New endpoints for counting the number of results: `getNumberOfDatasets`, `getNumberOfPlatforms`, `getNumberOfResultSets`. These endpoints are faster than looking up `totalElements` as no data is retrieved or converted.  Datasets can now be filtered by annotations at the sample, factor value and all levels using the three newly exposed `experimentalDesign.experimentalFactors.factorValues.characteristics`, `bioAssays.sampleUsed.characteristics` and `allCharacteristics` collections. The two useful available properties for filtering are `value` and `valueUri`.  New `getDatasetsAnnotationsUsageStatistics`, `getDatasetsPlatformsUsageStatistics` and `getDatasetsTaxaUsageStatistics` endpoints for retrieving annotations, platforms and taxa used by the matched datasets. The endpoint accepts the same `filter` argument of `getDatasets`, allowing one to easily navigate terms, platforms and taxa available for filtering furthermore.  Properties available for filtering and sorting are enumerated in the description of the corresponding parameter. There's been a number of fixes and additional tests performed to ensure that all advertised properties are working as expected.  The `FilterArg` and `SortArg`-based parameters now have OpenAPI extensions to enumerate available properties in a structured format under the `x-gemma-filterable-properties`key. Possible values are exposed for enumerated types.  ```yaml x-gemma-filterable-properties: - name: technologyType   type: string   allowedValues:   - value: ONECOLOR     label: One Color   - value: SEQUENCING     label: Sequencing   security:     basicAuth: [GROUP_ADMIN]     cookieAuth: [GROUP_ADMIN] ```  Some of the exposed properties such as `geeq.publicSuitabilityScore` require specific authorities to use. This is documented in `x-filterable-properties` by specifying a [Security Requirement Object](https://spec.openapis.org/oas/latest.html#security-requirement-object).  Types that use the `[]` suffix are using sub-queries under the hood. It implies that the entity will be matched if at least one related entity matches the supplied filter. For example, the `characteristics.valueUri = http://purl.obolibrary.org/obo/UBERON_0002107` filter will match datasets with at least one `UBERON:0002107` tag attached.  Filtered endpoints (including paginated and limited ones) now expose a `groupBy` array that enumerates all the properties used to group results. This helps clear confusion about what constitute a business key in the returned response.  ### Update 2.6.1  Add support for filtering platforms by taxon ID, common name, scientific name, etc. for the `/platforms` endpoint.  ### Update 2.6.0  Add a new `externalDatabases` attribute to the main endpoint that displays version of some of the main external databases that we are using. This exposes versions and last updates for genomes, gene annotations, GO terms, and much more!  The `ExternalDatabaseValueObject` now exposes a `description` which provides additional details.  ### Update 2.5.2  Restore `factors` in `BioMaterialValueObject` as it is being still used by our RNA-Seq pipeline. The attribute is deprecated and should not be used and will be removed when we find a suitable alternative.  Introduce a new endpoint to retrieve quantitation types for a given dataset and parameters to retrieve expression data by quantitation type to `getDatasetProcessedExpression` and `getDatasetRawExpression`. As it was too difficult to extends `getDatasetExpression` to also support quantitation type while retaining the filter feature, we decided to deprecate it and reintroduce filtering for both raw and processed expression in the future.  Fix return type for `getResultSets` which was incorrectly referring to a renamed VO.  Annotate all possible types for `SearchResult.resultObject`. This incidentally includes the `GeneSetValueObject` in the specification which is not exposed elsewhere in the API.  ### Update 2.5.1  Restore `objectClass` visibility in `AnnotationValueObject`.  Fix incorrect response types for annotations search endpoints returning datasets.  ### Update 2.5.0  Major cleanups were performed in this release in order to stabilize the specification. Numerous properties from Gemma Web that were never intended to be exposed in Gemma REST have been hidden. It's a bit too much to describe in here, but you can navigate to the schemas section below to get a good glance at the models.  Favour `numberOfSomething` instead of `somethingCount` which is clearer. The older names are kept for backward-compatibility, but should be considered deprecated.  Gene aliases and multifunctionality rank are now filled in `GeneValueObject`.  Uniformly use `TaxonValueObject` to represent taxon. This is breaking change for the `ExpressionExperimentValueObject` and `ArrayDesignValueObject` as their `taxon` property will be an `object` instead of a `string`. Properties such as `taxonId` are now deprecated and `taxon.id` should be used instead.  Entities that have IDs now all inherit from `IdentifiableValueObject`. This implies that you can assume the presence of an `id` in a search result `resultObject` attribute for example.  New `/search` endpoint! for an unified search experience. Annotation-based search endpoints under `/annotations` are now deprecated.  New API docs! While not as nice looking, the previous theme will be gradually ported to Swagger UI as we focused on functionality over prettiness for this release.  ### Update 2.4.0 through 2.4.1  Release notes for the 2.4 series were not written down, so I'll try to do my best to recall features that were introduced at that time.  An [OpenAPI](https://www.openapis.org/) specification was introduced and available under `/rest/v2/openapi.json`, although not fully stabilized.  Add a `/resultSets` endpoint to navigate result sets directly, by ID or by dataset.  Add a `/resultSets/{resultSetId}` endpoint to retrieve a specific result set by its ID. This endpoint can be negotiated with an `Accept: text/tab-separated-values` header to obtain a TSV representation.  Add a `/datasets/{dataset}/analyses/differential/resultSets` endpoint that essentially redirect to a specific `/resultSet` endpoint by dataset ID.  Add an endpoint to retrieve preferred raw expression vectors.  ### Update 2.3.4  November 6th, 2018  November 6th [2.3.4] Bug fixes in the dataset search endpoint.  November 5th [2.3.3] Added filtering parameters to dataset search.  October 25th [2.3.2] Changed behavior of the dataset search endpoint to more closely match the Gemma web interface.  October 2nd [2.3.1] Added group information to the User value object.  September 27th [2.3.0] Breaking change in Taxa: Abbreviation property has been removed and is therefore no longer an accepted identifier.  ### Update 2.2.6  June 7th, 2018  Code maintenance, bug fixes. Geeq scores stable and made public.  June 7th [2.2.6] Added: User authentication endpoint.  May 2nd [2.2.5] Fixed: Cleaned up and optimized platforms/elements endpoint, removed redundant information (recursive properties nesting).  April 12th [2.2.3] Fixed: Array arguments not handling non-string properties properly, e.g. `ncbiIds` of genes.  April 9th [2.2.1] Fixed: Filter argument not working when the filtered field was a primitive type. This most significantly allows filtering by geeq boolean and double properties.  ### Update 2.2.0  February 8th, 2018  Breaking change in the 'Dataset differential analysis' endpoint: - No longer using `qValueThreshold` parameter. - Response format changed, now using `DifferentialExpressionAnalysisValueObject` instead of `DifferentialExpressionValueObject` - [Experimental] Added Geeq (Gene Expression Experiment Quality) scores to the dataset value objects 

    The version of the OpenAPI document: 2.7.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from gemmapy.sdk2.models.array_design_value_object import ArrayDesignValueObject
from gemmapy.sdk2.models.bibliographic_reference_value_object import BibliographicReferenceValueObject
from gemmapy.sdk2.models.bio_sequence_value_object import BioSequenceValueObject
from gemmapy.sdk2.models.characteristic_value_object import CharacteristicValueObject
from gemmapy.sdk2.models.composite_sequence_value_object import CompositeSequenceValueObject
from gemmapy.sdk2.models.expression_experiment_set_value_object import ExpressionExperimentSetValueObject
from gemmapy.sdk2.models.expression_experiment_value_object import ExpressionExperimentValueObject
from gemmapy.sdk2.models.gene_set_value_object import GeneSetValueObject
from gemmapy.sdk2.models.gene_value_object import GeneValueObject
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

SEARCHRESULTVALUEOBJECTOBJECTRESULTOBJECT_ONE_OF_SCHEMAS = ["ArrayDesignValueObject", "BibliographicReferenceValueObject", "BioSequenceValueObject", "CharacteristicValueObject", "CompositeSequenceValueObject", "ExpressionExperimentSetValueObject", "ExpressionExperimentValueObject", "GeneSetValueObject", "GeneValueObject"]

class SearchResultValueObjectObjectResultObject(BaseModel):
    """
    SearchResultValueObjectObjectResultObject
    """
    # data type: ArrayDesignValueObject
    oneof_schema_1_validator: Optional[ArrayDesignValueObject] = None
    # data type: BibliographicReferenceValueObject
    oneof_schema_2_validator: Optional[BibliographicReferenceValueObject] = None
    # data type: BioSequenceValueObject
    oneof_schema_3_validator: Optional[BioSequenceValueObject] = None
    # data type: CompositeSequenceValueObject
    oneof_schema_4_validator: Optional[CompositeSequenceValueObject] = None
    # data type: ExpressionExperimentValueObject
    oneof_schema_5_validator: Optional[ExpressionExperimentValueObject] = None
    # data type: ExpressionExperimentSetValueObject
    oneof_schema_6_validator: Optional[ExpressionExperimentSetValueObject] = None
    # data type: GeneValueObject
    oneof_schema_7_validator: Optional[GeneValueObject] = None
    # data type: GeneSetValueObject
    oneof_schema_8_validator: Optional[GeneSetValueObject] = None
    # data type: CharacteristicValueObject
    oneof_schema_9_validator: Optional[CharacteristicValueObject] = None
    if TYPE_CHECKING:
        actual_instance: Union[ArrayDesignValueObject, BibliographicReferenceValueObject, BioSequenceValueObject, CharacteristicValueObject, CompositeSequenceValueObject, ExpressionExperimentSetValueObject, ExpressionExperimentValueObject, GeneSetValueObject, GeneValueObject]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(SEARCHRESULTVALUEOBJECTOBJECTRESULTOBJECT_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = SearchResultValueObjectObjectResultObject.construct()
        error_messages = []
        match = 0
        # validate data type: ArrayDesignValueObject
        if not isinstance(v, ArrayDesignValueObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ArrayDesignValueObject`")
        else:
            match += 1
        # validate data type: BibliographicReferenceValueObject
        if not isinstance(v, BibliographicReferenceValueObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BibliographicReferenceValueObject`")
        else:
            match += 1
        # validate data type: BioSequenceValueObject
        if not isinstance(v, BioSequenceValueObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BioSequenceValueObject`")
        else:
            match += 1
        # validate data type: CompositeSequenceValueObject
        if not isinstance(v, CompositeSequenceValueObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CompositeSequenceValueObject`")
        else:
            match += 1
        # validate data type: ExpressionExperimentValueObject
        if not isinstance(v, ExpressionExperimentValueObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExpressionExperimentValueObject`")
        else:
            match += 1
        # validate data type: ExpressionExperimentSetValueObject
        if not isinstance(v, ExpressionExperimentSetValueObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExpressionExperimentSetValueObject`")
        else:
            match += 1
        # validate data type: GeneValueObject
        if not isinstance(v, GeneValueObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GeneValueObject`")
        else:
            match += 1
        # validate data type: GeneSetValueObject
        if not isinstance(v, GeneSetValueObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GeneSetValueObject`")
        else:
            match += 1
        # validate data type: CharacteristicValueObject
        if not isinstance(v, CharacteristicValueObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CharacteristicValueObject`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SearchResultValueObjectObjectResultObject with oneOf schemas: ArrayDesignValueObject, BibliographicReferenceValueObject, BioSequenceValueObject, CharacteristicValueObject, CompositeSequenceValueObject, ExpressionExperimentSetValueObject, ExpressionExperimentValueObject, GeneSetValueObject, GeneValueObject. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SearchResultValueObjectObjectResultObject with oneOf schemas: ArrayDesignValueObject, BibliographicReferenceValueObject, BioSequenceValueObject, CharacteristicValueObject, CompositeSequenceValueObject, ExpressionExperimentSetValueObject, ExpressionExperimentValueObject, GeneSetValueObject, GeneValueObject. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> SearchResultValueObjectObjectResultObject:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> SearchResultValueObjectObjectResultObject:
        """Returns the object represented by the json string"""
        instance = SearchResultValueObjectObjectResultObject.construct()
        error_messages = []
        match = 0

        # deserialize data into ArrayDesignValueObject
        try:
            instance.actual_instance = ArrayDesignValueObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BibliographicReferenceValueObject
        try:
            instance.actual_instance = BibliographicReferenceValueObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BioSequenceValueObject
        try:
            instance.actual_instance = BioSequenceValueObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CompositeSequenceValueObject
        try:
            instance.actual_instance = CompositeSequenceValueObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExpressionExperimentValueObject
        try:
            instance.actual_instance = ExpressionExperimentValueObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExpressionExperimentSetValueObject
        try:
            instance.actual_instance = ExpressionExperimentSetValueObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GeneValueObject
        try:
            instance.actual_instance = GeneValueObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GeneSetValueObject
        try:
            instance.actual_instance = GeneSetValueObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CharacteristicValueObject
        try:
            instance.actual_instance = CharacteristicValueObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SearchResultValueObjectObjectResultObject with oneOf schemas: ArrayDesignValueObject, BibliographicReferenceValueObject, BioSequenceValueObject, CharacteristicValueObject, CompositeSequenceValueObject, ExpressionExperimentSetValueObject, ExpressionExperimentValueObject, GeneSetValueObject, GeneValueObject. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SearchResultValueObjectObjectResultObject with oneOf schemas: ArrayDesignValueObject, BibliographicReferenceValueObject, BioSequenceValueObject, CharacteristicValueObject, CompositeSequenceValueObject, ExpressionExperimentSetValueObject, ExpressionExperimentValueObject, GeneSetValueObject, GeneValueObject. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


