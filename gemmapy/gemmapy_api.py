# -*- coding: utf-8 -*-
"""
Gemma python API (https://gemma.msl.ubc.ca/rest/v2/)
"""

from gemmapy import sdk
from gemmapy import _processors as ps
from gemmapy import _validators as vs
from gemmapy import _subprocessors as sub
from typing import Optional, List, Callable
from pandas import DataFrame
import pandas as pd
import numpy as np
import anndata as ad
from anndata import AnnData
from io import StringIO
import warnings
import re
import json


class GemmaPy(object):
    """
    Main API class
    """

    def __init__(self, auth:list|tuple=None, path="prod"):
        """
        :param list auth: (optional) A list or tuple of credential strings, e.g.
          (your_username, your_password)
        :param bool devel: (optional) If True development version of Gemma API will be
          used. Default is False.
        """

        configuration = sdk.Configuration()
        if path == "prod":
            pass
            # configuration.host = 'https://gemma.msl.ubc.ca/rest/v2'
        elif path == 'dev':
            configuration.host = 'https://dev.gemma.msl.ubc.ca/rest/v2'
        elif path == 'staging':
            configuration.host = "https://staging-gemma.msl.ubc.ca/rest/v2"
        else:
            configuration.host = path
        

        if auth is not None:
            configuration.username = auth[0]
            configuration.password = auth[1]

        # create an instance of the API class
        self.raw = sdk.DefaultApi(sdk.ApiClient(configuration))


    # /resultSets/count get_number_of_result_sets ------
    # unimplemented
    # we don't need this here, not included
    
    # /resultSets/{resultSet}
    # this was only used in the past to access result set metadata by 
    # using a hidden parameter. this information can be accessed using get_result_sets
    # enpoint instead
    
    # /resultSets/{resultSet_}, get_result_set_as_tsv ------ 
    # made internal to not cause unneeded confusion
    # use get_differential_expression_values instead
    def __get_result_set(self, result_set:int, **kwargs):
        """
        
        :param result_set: DESCRIPTION
        :type result_set: int
        :param **kwargs: Additional arguments to pass to raw.get_result_set_as_tsv
        :return: DESCRIPTION
        :rtype: TYPE

        """
        
        response = self.raw.get_result_set(result_set, **kwargs,
                                           _force_table = True)
        
        df = ps.process_de_matrix(response, result_set,self)
        
        return df
        

    
    # /resultSets, get_result_sets -----
    
    def get_result_sets(self,
                        datasets:Optional[List[str|int]] = None,
                        result_sets:Optional[List[int]] = None,
                        filter:str = None,
                        offset:int = 0,
                        limit:int = 20,
                        sort:str = "+id",
                        **kwargs)->DataFrame:
        """Returns queried result set

        Output and usage of this function is mostly identical to 
        get_dataset_differential_expression_analyses. The principal difference
        being the ability to restrict your result sets, being able to query 
        across multiple datasets and being able to use the filter argument to 
        search based on result set properties.


        
        :param datasets: A numerical dataset identifier or a dataset short name, defaults to None
        :type datasets: Optional[List[str|int]], optional
        :param result_sets: 	A result set identifier. Note that result set identifiers are not static and can change when Gemma re-runs analyses internally. Whem using these as inputs, try to make sure you access a currently existing result set ID by basing them on result sets returned for a particular dataset or filter used in get_result_sets, defaults to None
        :type result_sets: Optional[List[int]], optional
        :param filter: Filter results by matching expression. Use 
          filter_properties function to get a list of all available parameters. 
          These properties can be combined using "and" "or" clauses and may 
          contain common operators such as "=", "<" or "in". (e.g. 
          "taxon.commonName = human", "taxon.commonName in (human,mouse), 
          "id < 1000"), defaults to None
        :type filter: str, optional
        :param offset: The offset of the first retrieved result., defaults to 0
        :type offset: int, optional
        :param limit: Limits the result to specified amount of objects.
          Has a maximum value of 100. Use together with offset and the 
          total_elements attribute in the output to compile all data if needed.
          Alternatively get_all_pages function can be used with all functions
          including offset and limit parameters, defaults to 20
        :type limit: int, optional
        :param sort: Order results by the given property and direction. The '+'
          sign indicate ascending order whereas the '-' indicate descending,
          defaults to "+id"
        :type sort: str, optional
        :param **kwargs: Additional arguments to pass to raw.get_result_sets
        :return: A DataFrame with information about the queried result sets. 
          Note that this function does not return differential expression values
          themselves
        
          The fields of the DataFrame are:
            - result_ID: Result set ID of the differential expression analysis. May represent multiple factors in a single model.
            - contrast_ID: Id of the specific contrast factor. Together with the result.ID they uniquely represent a given contrast.
            - experiment_ID: Id of the source experiment
            - factor_category: Category for the contrast
            - factor_category_URI: URI for the baseline category
            - factor_ID: ID of the factor
            - baseline_factors: Characteristics of the baseline. This field is a DataFrame
            - experimental_factors: Characteristics of the experimental group. This field is a DataFrame
            - is_subset: True if the result set belong to a subset, False if not. Subsets are created when performing differential expression to avoid unhelpful comparisons.
            - subset_factor: Characteristics of the subset. This field is a DataFrame
        
        :rtype: DataFrame

        """
        
        filter = vs.add_to_filter(filter, 'id', result_sets)
        
        
        kwargs = vs.remove_nones(
            datasets = datasets,
            filter = filter,
            offset = offset,
            limit = limit,
            sort = sort,
            **kwargs)
        
        response = self.raw.get_result_sets(**kwargs)
        df = ps.process_DifferentialExpressionAnalysisResultSetValueObject(response.data,self)
        ps.attach_attributes(df, response.to_dict())

        return df

    
    # /annotations/search, search_annotations --------
    def search_annotations(self, query:List[str], **kwargs)->DataFrame:
        """
        Search for annotation tags


        :param query: The search query
        :type query: List[str]
        :param **kwargs: Additional arguments to pass to raw.search_annotations
        :return: A DataFrame with annotations matching the given identifiers. 
          The fields of the DataFrame are:
            - category_name: Category that the annotation belongs to
            - category_URI: URI for the category_name
            - value_name: Annotation term
            - value_URI: URI for the value_name
        :rtype: DataFrame

        """

        response = self.raw.search_annotations(query=query, **kwargs)
        return ps.process_search_annotations(response.data)
    

    # /datasets/{dataset}/annotations, get_dataset_annotations ----------
    def get_dataset_annotations(self, dataset:str|int, **kwargs)->DataFrame:
        """
        Retrieve the annotations of a dataset


        :param dataset: 	A numerical dataset identifier or a dataset short name
        :type dataset: str|int
        :param **kwargs: Additional arguments to pass to raw.get_dataset_annotations
        :return: A DataFrame with information about the annotations of the queried dataset. 
          The fields of the DataFrame are:
            - class_name: Name of the annotation class (e.g. organism part)
            - class_URI: URI for the annotation class
            - term_name: Name of the annotation term (e.g. lung)
            - term_URI: URI for the annotation term
            - object_class: Class of object that the term originated from.       
        :rtype: DataFrame

        """

        response = self.raw.get_dataset_annotations(dataset, **kwargs)
        df = ps.process_annotations(response.data)
        ps.attach_attributes(df, response.to_dict())
        
        return df
    
    # /datasets/{dataset}/design, get_dataset_design -----
    # this endpoint is not very useful since the names it comes with
    # is annoying to match names provided in the samples endpoint
    # make_design replaces this
    def __get_dataset_design(self, dataset:str|int, **kwargs):
        """
        
        :param dataset: DESCRIPTION
        :type dataset: str|int
        :param **kwargs: Additional arguments to pass to raw.get_dataset_design
        :type **kwargs: TYPE
        :return: DESCRIPTION
        :rtype: TYPE

        """

        response = self.raw.get_dataset_design(dataset, **kwargs)
        df = ps.process_dataset_design(response)
        
        return df
    
    # /datasets/{datasets}/expressions/differential ------
    # unimplemented
    # not sure how the parameters for this endpoint works and doesn't seem essential
    
    # /datasets/{dataset}/analyses/differential, get_dataset_differential_expression_analyses ------
    def get_dataset_differential_expression_analyses(self, 
                                                     dataset:str|int,
                                                     **kwargs)->DataFrame:
        """Retrieve annotations and surface level stats for a dataset's differential analyses
        
        :param dataset: A numerical dataset identifier or a dataset short name
        :type dataset: str|int
        :param **kwargs: Additional arguments to pass to raw.get_dataset_differential_expression_analyses
        :return: A data table with information about the differential expression
          analysis of the queried dataset. Note that this funciton does not return 
          differential expression values themselves. Use
          get_differential_expression_values to get differential expression
          values (see examples).
          
          The fields of the DataFrame are:
            - result_ID: Result set ID of the differential expression analysis. May represent multiple factors in a single model.
            - contrast_ID: Id of the specific contrast factor. Together with the result.ID they uniquely represent a given contrast.
            - experiment_ID: Id of the source experiment
            - factor_category: Category for the contrast
            - factor_category_URI: URI for the contrast category
            - factor_ID: ID of the factor
            - baseline_factors: Characteristics of the baseline. This field is a DataFrame
            - experimental_factors: Characteristics of the experimental group. This field is a DataFrame
            - isSubset: True if the result set belong to a subset, False if not. 
              Subsets are created when performing differential expression to avoid 
              unhelpful comparisons.
            - subset_factor: Characteristics of the subset. This field is a DataFrame
            - probes_analyzed: Number of probesets represented in the contrast
            - genes_analyzed: Number of genes represented in the contrast
        :rtype: DataFrame

        """
        response = self.raw.get_dataset_differential_expression_analyses(dataset,
                                                                         **kwargs)
        df = ps.process_dea(response.data)
        
        return df
    
    # /datasets/{dataset}/analyses/differential/resultSets -----
    # unimplemented
    # unsure about the distinction between this and the get_dataset_differential_expression_analyses. 
    # seem to contain the reduntant information
    
    
    # /datasets/{dataset}/data -----
    # deprecated, remove later
    def get_dataset_expression(self, dataset:str|int, **kwargs)->DataFrame:
        """
        Deprecated in favour of get_dataset_expression
        """
        warnings.warn('get_dataset_expression is deprecated, please use get_dataset_processed_expression instead')
        
        return self.get_dataset_processed_expression(dataset,**kwargs)

    
    
    
    # /datasets/{datasets}/expressions/genes/{genes}, get_dataset_expression_for_genes ------
    def get_dataset_expression_for_genes(self,
                                         datasets:List[str|int],
                                         genes:List[int],
                                         keep_non_specific:bool = False,
                                         consolidate = None,
                                         **kwargs)->dict[int:DataFrame]:
        """Retrieve the expression data matrix of a set of datasets and genes


        :param datasets: A numerical dataset identifier or a dataset short name
        :type datasets: List[str|int]
        :param genes: An ensembl gene identifier which typically starts with 
          ensg or an ncbi gene identifier or an official gene symbol approved by 
          hgnc
        :type genes: List[int]
        :param keep_non_specific: If True, results from probesets that are not
          specific to the gene will also be returned., defaults to False
        :type keep_non_specific: bool, optional
        :param consolidate: An option for gene expression level consolidation. 
          If empty, will return every probe for the genes. "pickmax" to pick the
          probe with the highest expression, "pickvar" to pick the prove with the 
          highest variance and "average" for returning the average expression, 
          defaults to None
        :type consolidate: TYPE, optional
        :param **kwargs: Additional arguments to pass to raw.get_dataset_expression_for_genes
        :return: A dict of DataFrames keyed to dataset ids
        :rtype: dict[int:DataFrame]

        """
        
        kwargs = vs.remove_nones(
            keep_non_specific = keep_non_specific,
            consolidate = consolidate,
            **kwargs)
        
        response = self.raw.get_dataset_expression_for_genes(datasets, genes, 
                                                             **kwargs)
        df = ps.process_dataset_gene_expression(response.data,self)
        
        return df
        
    # datasets/{datasets}/expressions/pca -----
    # unimplemented
    
    
    # datasets/{dataset}/platforms ------
    def get_dataset_platforms(self, dataset:str|int, **kwargs)->DataFrame:
        """
        
        :param dataset: A numerical dataset identifier or a dataset short name
        :type dataset: str|int
        :param **kwargs: Additional arguments to pass to raw.get_dataset_platforms
        :return: A DataFrame with information about the platforms.
          The fields of the DataFrame are:
                
            - platform_ID: Id number of the platform given by Gemma
            - platform_type: Type of the platform.
            - platform_description: Free text field describing the platform.
            - platform_troubled: Whether the platform is marked as troubled by a Gemma curator.
            - taxon_name: Name of the species
            - taxon_scientific: Scientific name for the taxon
            - taxon_ID: Internal identifier given to the species by Gemma
            - taxon_NCBI: NCBI ID of the taxon
            - taxon_database_name: Underlying database used in Gemma for the taxon
            - taxon_database_ID: ID of the underlying database used in Gemma for the taxon  
        :rtype: DataFrame

        """
        response = self.raw.get_dataset_platforms(dataset, **kwargs)
        df = ps.process_platforms(response.data)
        
        return(df)
    
    
    # datasets/{dataset}/data/processed ------
    
    def get_dataset_processed_expression(self,dataset:str|int,**kwargs)->DataFrame:
        """Retrieve processed expression data of a dataset

        
        :param dataset:  numerical dataset identifier or a dataset short name
        :type dataset: str|int
        :param **kwargs: Additional arguments to pass to raw.get_dataset_processed_expression
        :return: A DataFrame of the expression matrix for the queried dataset
        :rtype: DataFrame

        """
        response = self.raw.get_dataset_processed_expression(dataset, **kwargs)
        
        df = ps.process_expression(response,dataset,self)
        
        return df
    
    # datasets/{dataset}/quantitationTypes get_dataset_quantitation_types ----------
    
    def get_dataset_quantitation_types(self,dataset:int|str,**kwargs)->DataFrame:
        """Retrieve quantitation types of a dataset

        
        :param dataset: 	A numerical dataset identifier or a dataset short name
        :type dataset: int|str
        :param **kwargs: Additional arguments to pass to raw.get_dataset_quantitation_types
        :return: A DataFrame containing the quantitation types
        
          The fields of the output DataFrame are:
            - id: If of the quantitation type. Any raw quantitation type can be
               by get_dataset_raw_expression function using this id.
            - name: Name of the quantitation type
            - description: Description of the quantitation type
            - type: Type of the quantitation type. Either raw or processed. 
              Each dataset will have one processed quantitation type which is the 
              data returned using get_dataset_processed_expression
            - ratio: Whether or not the quanitation type is a ratio of multiple
              quantitation types. Typically TRUE for processed TWOCOLOR quantitation type.
            - preferred: The preferred raw quantitation type. This version is 
              used in generation of the processed data within gemma.
            - recomputed: If TRUE this quantitation type is generated by
              recomputing raw data files Gemma had access to
        :rtype: DataFrame

        """
        
        response = self.raw.get_dataset_quantitation_types(dataset, **kwargs)
        df = ps.process_QuantitationTypeValueObject(response.data)
        
        
        return df

    # datasets/{dataset}/data/raw, get_dataset_raw_expression ---------
    def get_dataset_raw_expression(self,dataset:int|str,
                                   quantitation_type:[int],**kwargs)->DataFrame:
        """
        
        :param dataset: A numerical dataset identifier or a dataset short name
        :type dataset: int|str
        :param quantitation_type: Quantitation type id. These can be acquired 
          using get_dataset_quantitation_types function. This endpoint can only 
          return non-processed quantitation types.
        :type quantitation_type: [int]
        :param **kwargs: Additional arguments to pass to raw.get_dataset_raw_expression
        :return: A DataFrame of the expression matrix for the queried dataset
        :rtype: DataFrame

        """
        
        kwargs = vs.remove_nones(
            quantitation_type = quantitation_type,
            **kwargs)
        
        response = self.raw.get_dataset_raw_expression(dataset, **kwargs)
        
        df = ps.process_expression(response,dataset,self)
        
        return df
    
    
    # datasets/{dataset}/samples, get_dataset_samples --------
    def get_dataset_samples(self, dataset:int|str, **kwargs)->DataFrame:
        """
        Retrieve the samples of a dataset


        :param dataset: A numerical dataset identifier or a dataset short name
        :type dataset: int|str
        :param **kwargs: Additional arguments to pass to raw.get_dataset_samples
        :return: A DataFrame with information about the samples of the queried dataset.
        
          The fields of the DataFrame are:
            - sample_name: Internal name given to the sample.
            - sample_ID: Internal ID of the sample
            - sample_description: Free text description of the sample
            - sample_outlier: Whether or not the sample is marked as an outlier
            - sample_accession: Accession ID of the sample in it's original database
            - sample_database: Database of origin for the sample
            - sample_characteristics: Characteristics of the sample. This field is a data table
            - sample_factor_values: Experimental factor values of the sample. This field is a data table
        :rtype: DataFrame

        """
        response = self.raw.get_dataset_samples(dataset, **kwargs)
        df = ps.process_samples(response.data)
        return df
        
    # datasets/{dataset}/svd --- 
    # not implemented
    
    # datasets, get_datasets ------
    def get_datasets(self,query:Optional[str] = None, 
                     filter:Optional[str] = None, 
                     taxa:Optional[List[str]] = None, 
                     uris:Optional[List[str]] = None,
                     offset:int = 0,
                     limit:int = 20,
                     sort:str = "+id",
                     **kwargs)->DataFrame:
        """
        
        :param query: The search query. Either plain text ('traumatic'), or an 
          ontology term URI ('http://purl.obolibrary.org/obo/UBERON_0002048').
          Datasets that contain the given string in their short of full name will 
          also be matched., defaults to None
        :type query: Optional[str], optional
        :param filter: Filter results by matching expression. Use 
          filter_properties function to get a list of all available parameters. 
          These properties can be combined using "and" "or" clauses and may 
          contain common operators such as "=", "<" or "in". (e.g. 
          "taxon.commonName = human", "taxon.commonName in (human,mouse), 
          "id < 1000"), defaults to None
        :type filter: Optional[str], optional
        :param taxa: A vector of taxon common names (e.g. human, mouse, rat).
          Providing multiple species will return results for all species. These 
          are appended to the filter and equivalent to filtering for 
          taxon.commonName property, defaults to None
        :param taxa: A list of taxon common names (e.g. human, mouse, rat). 
          Providing multiple species will return results for all species. 
          These are appended to the filter and equivalent to filtering for 
          taxon.commonName property, defaults to None
        :type taxa: Optional[List[str]], optional
        :param uris: A vector of ontology term URIs. Providing multiple terms
          will return results containing any of the terms and their children. 
          These are appended to the filter and equivalent to filtering for 
          allCharacteristics.valueUri, defaults to None
        :type uris: Optional[List[str]], optional
        :param offset: The offset of the first retrieved result., defaults to 0
        :type offset: int, optional
        :param limit: Limits the result to specified amount of objects.
          Has a maximum value of 100. Use together with offset and the 
          total_elements attribute in the output to compile all data if needed.
          Alternatively get_all_pages function can be used with all functions
          including offset and limit parameters, defaults to 20
        :type limit: int, optional
        :param sort: Order results by the given property and direction. The '+'
          sign indicate ascending order whereas the '-' indicate descending,
          defaults to "+id"
        :type sort: str, optional
        :param **kwargs: Additional arguments to pass to raw.get_datasets
        :return: A DataFrame with information about the queried dataset(s).
        
          The fields of the DataFrame are:
            - experiment_short_name: Shortname given to the dataset within Gemma. Often corresponds to accession ID
            - experiment_name: Full title of the dataset
            - experiment_ID: Internal ID of the dataset.
            - experiment_description: Description of the dataset
            - experiment_troubled: Did an automatic process within gemma or a curator mark the dataset as "troubled"
            - experiment_accession: Accession ID of the dataset in the external database it was taken from
            - experiment_database: The name of the database where the dataset was taken from
            - experiment_URI: URI of the original database
            - experiment_sample_count: Number of samples in the dataset
            - experiment_batch_effect_text: A text field describing whether the dataset has batch effects
            - experimen_batch_corrected: Whether batch correction has been performed on the dataset.
            - experimen_batch_confound: 0 if batch info isn't available, -1 if batch counfoud is detected, 1 if batch information is available and no batch confound found
            - experimen_batch_effect: -1 if batch p value < 0.0001, 1 if batch p value > 0.1, 0 if otherwise and when there is no batch information is available or when the data is confounded with batches.
            - experimen_raw_data: -1 if no raw data available, 1 if raw data was available. When available, Gemma reprocesses raw data to get expression values and batches
            - geeq_q_score: Data quality score given to the dataset by Gemma.
            - geeq_s_score: Suitability score given to the dataset by Gemma. Refers to factors like batches, platforms and other aspects of experimental design
            - taxon_name: Name of the species
            - taxon_scientific: Scientific name for the taxon
            - taxon_ID: Internal identifier given to the species by Gemma
            - taxon_NCBI: NCBI ID of the taxon
            - taxon_database_name: Underlying database used in Gemma for the taxon
            - taxon_database_ID: ID of the underyling database used in Gemma for the taxon
        :rtype: DataFrame

        """
        
        filter = vs.add_to_filter(filter, 'allCharacteristics.valueUri', uris)
        filter = vs.add_to_filter(filter, 'taxon.commonName', taxa)
        
        kwargs = vs.remove_nones(
            query = query,
            filter = filter,
            offset = offset,
            limit = limit,
            sort = sort,
            **kwargs)
        
        response = self.raw.get_datasets(**kwargs)
        df = ps.process_datasets(response.data)
        ps.attach_attributes(df, response.to_dict())

        
        return df
    
    # datasets/annotations -----
    # currently unimplemented
    
    
    # datasets/{datasets}, get_datasets_by_ids -----
    def get_datasets_by_ids(self, dataset:List[str|int],
                            filter:Optional[str] = None, 
                            taxa:Optional[List[str]] = None, 
                            uris:Optional[List[str]] = None,
                            offset:int = 0,
                            limit:int = 20,
                            sort:str = "+id",
                            **kwargs)->DataFrame:
        """
        
        :param dataset: Numerical dataset identifiers or dataset short names.
        :type dataset: List[str|int]
        :param filter: Filter results by matching expression. Use 
          filter_properties function to get a list of all available parameters. 
          These properties can be combined using "and" "or" clauses and may 
          contain common operators such as "=", "<" or "in". (e.g. 
          "taxon.commonName = human", "taxon.commonName in (human,mouse), 
          "id < 1000"), defaults to None
        :type filter: Optional[str], optional
        :param taxa: A list of taxon common names (e.g. human, mouse, rat). 
          Providing multiple species will return results for all species. 
          These are appended to the filter and equivalent to filtering for 
          taxon.commonName property, defaults to None
        :type taxa: Optional[List[str]], optional
        :param uris: A vector of ontology term URIs. Providing multiple terms
          will return results containing any of the terms and their children. 
          These are appended to the filter and equivalent to filtering for 
          allCharacteristics.valueUri, defaults to None
        :type uris: Optional[List[str]], optional
        :param offset: The offset of the first retrieved result., defaults to 0
        :type offset: int, optional
        :param limit: Limits the result to specified amount of objects.
          Has a maximum value of 100. Use together with offset and the 
          total_elements attribute in the output to compile all data if needed.
          Alternatively get_all_pages function can be used with all functions
          including offset and limit parameters, defaults to 20
        :type limit: int, optional
        :param sort: Order results by the given property and direction. The '+'
          sign indicate ascending order whereas the '-' indicate descending,
          defaults to "+id"
        :type sort: str, optional
        :param **kwargs: Additional arguments to pass to raw.get_datasets_by_ids
        :return: A DataFrame with information about the queried dataset(s).
        
          The fields of the DataFrame are:
            - experiment_short_name: Shortname given to the dataset within Gemma. Often corresponds to accession ID
            - experiment_name: Full title of the dataset
            - experiment_ID: Internal ID of the dataset.
            - experiment_description: Description of the dataset
            - experiment_troubled: Did an automatic process within gemma or a curator mark the dataset as "troubled"
            - experiment_accession: Accession ID of the dataset in the external database it was taken from
            - experiment_database: The name of the database where the dataset was taken from
            - experiment_URI: URI of the original database
            - experiment_sample_count: Number of samples in the dataset
            - experiment_batch_effect_text: A text field describing whether the dataset has batch effects
            - experimen_batch_corrected: Whether batch correction has been performed on the dataset.
            - experimen_batch_confound: 0 if batch info isn't available, -1 if batch counfoud is detected, 1 if batch information is available and no batch confound found
            - experimen_batch_effect: -1 if batch p value < 0.0001, 1 if batch p value > 0.1, 0 if otherwise and when there is no batch information is available or when the data is confounded with batches.
            - experimen_raw_data: -1 if no raw data available, 1 if raw data was available. When available, Gemma reprocesses raw data to get expression values and batches
            - geeq_q_score: Data quality score given to the dataset by Gemma.
            - geeq_s_score: Suitability score given to the dataset by Gemma. Refers to factors like batches, platforms and other aspects of experimental design
            - taxon_name: Name of the species
            - taxon_scientific: Scientific name for the taxon
            - taxon_ID: Internal identifier given to the species by Gemma
            - taxon_NCBI: NCBI ID of the taxon
            - taxon_database_name: Underlying database used in Gemma for the taxon
            - taxon_database_ID: ID of the underyling database used in Gemma for the taxon
        :rtype: DataFrame

        """

        filter = vs.add_to_filter(filter, 'allCharacteristics.valueUri', uris)
        filter = vs.add_to_filter(filter, 'taxon.commonName', taxa)
        
        
        kwargs = vs.remove_nones(
            filter = filter,
            offset = offset,
            limit = limit,
            sort = sort,
            **kwargs)
        
        response = self.raw.get_datasets_by_ids(dataset, **kwargs)
        df = ps.process_datasets(response.data)
        ps.attach_attributes(df, response.to_dict())
        
        return df

    # datasets/categories -----
    # currently unimplemented

    # datasets/taxa -----
    # currently unimplemented

    # datasets/count -----
    # currently unimplemented

    # genes/{gene}/goTerms -------   
    
    def get_gene_go_terms(self, gene:str|int, **kwargs)->DataFrame:
        """
        
        :param gene: An ensembl gene identifier which typically starts with 
          ensg or an ncbi gene identifier or an official gene symbol approved by
          hgnc
        :type gene: str|int
        :param **kwargs: Additional arguments to pass to raw.get_gene_go_terms
        :return: A DataFrame with information about the GO terms assigned to the queried gene
          The fields of the output DataFrame are:
            - term_name: Name of the term
            - term_ID: ID of the term
            - term_URI: URI of the term 
        :rtype: DataFrame

        """
        response = self.raw.get_gene_go_terms(gene, **kwargs)
        df = ps.process_GO(response.data)
        return df

    
    # genes/{gene}/locations, get_gene_locations ----
    
    def get_gene_locations(self, gene:str|int, **kwargs)->DataFrame:
        """
        
        :param gene: DESCRIPTION
        :type gene: str|int
        :param **kwargs: DAdditional arguments to pass to raw.get_gene_locations
        :type **kwargs: TYPE
        :return: A DataFrame with information about the physical location of the queried gene
          The fields of the output DataFrame are:
            - chromosome: Name of the chromosome the gene is located
            - strand: Which strand the gene is located
            - nucleotide: Nucleotide number for the gene
            - length: Gene length
            - taxon_name: Name of the species
            - taxon_scientific: Scientific name for the taxon
            - taxon_ID: Internal identifier given to the species by Gemma
            - taxon_NCBI: NCBI ID of the taxon
            - taxon_database_name: Underlying database used in Gemma for the taxon
            - taxon_database_ID: ID of the underlying database used in Gemma for the taxon      
        :rtype: DataFrame

        """

        response = self.raw.get_gene_locations(gene, **kwargs)
        df = ps.process_gene_location(response.data)
        return df
    
    # genes/{gene}/probes, get_gene_probes -----
    
    def get_gene_probes(self, gene:str|int,
                        offset:int = 0,
                        limit:int = 20,
                        **kwargs)->DataFrame:
        """Retrieve the probes associated to a genes across all platforms
        
        :param gene: An ensembl gene identifier which typically starts with
          ensg or an ncbi gene identifier or an official gene symbol approved by 
          hgnc
        :type gene: str|int
        :param offset: The offset of the first retrieved result., defaults to 0
        :type offset: int, optional
        :param limit: Limits the result to specified amount of objects.
          Has a maximum value of 100. Use together with offset and the 
          total_elements attribute in the output to compile all data if needed.
          Alternatively get_all_pages function can be used with all functions
          including offset and limit parameters, defaults to 20
        :type limit: int, optional
        :param **kwargs: Additional arguments to pass to raw.get_gene_probes
        :return: A DataFrame with information about the probes representing a 
          gene across all platrofms.
        
          The fields of the output DataFrame are:
            - element_name: Name of the element. Typically the probeset name
            - element_description: A free text field providing optional information about the element
            - platform_short_name: Shortname of the platform given by Gemma. Typically the GPL identifier.
            - platform_name: Full name of the platform
            - platform_ID: Id number of the platform given by Gemma
            - platform_type: Type of the platform.
            - platform_description: Free text field describing the platform.
            - platform_troubled: Whether the platform is marked as troubled by a Gemma curator.
            - taxon_name: Name of the species
            - taxon_scientific: Scientific name for the taxon
            - taxon_ID: Internal identifier given to the species by Gemma
            - taxon_NCBI: NCBI ID of the taxon
            - taxon_database_name: Underlying database used in Gemma for the taxon
            - taxon_database_ID: ID of the underlying database used in Gemma for the taxon    
        :rtype: DataFrame

        """
        
        kwargs = vs.remove_nones(offset = offset,
                                 limit = limit,
                                 **kwargs)
        
        response = self.raw.get_gene_probes(gene, **kwargs)
        df = ps.process_elements(response.data)
        ps.attach_attributes(df, response.to_dict())
        return df
        
        
    # genes/{genes}, get_genes-------

    def get_genes(self, genes:int|str, **kwargs)->DataFrame:
        """Retrieve genes matching gene identifiers

        :param genes: An ensembl gene identifier which typically starts with 
          ensg or an ncbi gene identifier or an official gene symbol approved by hgnc
        :type genes: int|str
        :param **kwargs: Additional arguments to pass to raw_get_genes
        :return: A DataFrame with the information about the querried genes.
        
          The fields of the output DataFrame are:
            - gene_symbol: Symbol for the gene
            - gene_ensembl: Ensembl ID for the gene
            - gene_NCBI: NCBI id for the gene
            - gene_name: Name of the gene
            - gene_aliases: Gene aliases. Each row includes a vector
            - gene_MFX_rank: Multifunctionality rank for the gene
            - taxon_name: Name of the species
            - taxon_scientific: Scientific name for the taxon
            - taxon_ID: Internal identifier given to the species by Gemma
            - taxon_NCBI: NCBI ID of the taxon
            - taxon_database_name: Underlying database used in Gemma for the taxon
            - taxon_database_ID: ID of the underlying database used in Gemma for the taxon    
        :rtype: DataFrame

        """

        response = self.raw.get_genes(genes, **kwargs)
        df = ps.process_genes(response.data)
        return df

    # platforms/count -----
    # unimplemented
    
    # platform/{platform}/annotations -----
    # in gemma.R this endpoint isn't implemented and uses a convenience function instead
    # here we just use the enpoint since the added functionality isn't needed

    # Corresponding gemma.R function doesn't use any endpoint (uses some alternative URL
    # to get info) but has several options allowing to select the ann. type:
    # annotType = c("bioProcess", "noParents", "allParents")
    # This feature is not implemented here, the return value corresponds to "noParents"
    # (as of 2022-05-19)
    def get_platform_annotations(self, platform:int|str, **kwargs)->DataFrame:
        """Gets Gemma's platform annotations including mappings of microarray probes to genes.
        
        :param platform: A platform numerical identifier or a platform short name
        :type platform: int|str
        :param **kwargs: Additional arguments to pass to raw.get_platform_annotations
        :type **kwargs: TYPE
        :return: A DataFrame of annotations
        
          - ProbeName: Probeset names provided by the platform. Gene symbols for generic annotations
          - GeneSymbols: Genes that were found to be aligned to the probe sequence. Note that it is possible for probes to be non-specific. Alignment to multiple genes are indicated with gene symbols separated by "|"s
          - GeneNames: Name of the gene
          - GOTerms: GO Terms associated with the genes. annotType argument can be used to choose which terms should be included.
          - GemmaIDs and NCBIids: respective IDs for the genes.
        :rtype: DataFrame

        """
        
        api_response = self.raw.get_platform_annotations(platform, **kwargs)
        uncomment = api_response.split("\n#")
        api_response = uncomment[len(uncomment)-1]
        uncomment = api_response.split('\n',1)
        api_response = uncomment[len(uncomment)-1]
        return pd.read_csv(StringIO(api_response), sep='\t')

    # platform/{platform}/datasets, get_platform_datasets ----

    def get_platform_datasets(self, platform:str|int,
                              offset:int = 0,
                              limit:int = 20,
                              **kwargs)->DataFrame:
        """Retrieve all experiments using a given platform

        
        :param platform: A platform numerical identifier or a platform short name
        :type platform: str|int
        :param offset: The offset of the first retrieved result., defaults to 0
        :type offset: int, optional
        :param limit: Limits the result to specified amount of objects.
          Has a maximum value of 100. Use together with offset and the 
          total_elements attribute in the output to compile all data if needed.
          Alternatively get_all_pages function can be used with all functions
          including offset and limit parameters, defaults to 20
        :type limit: int, optional
        :param **kwargs: Additional arguments to pass to raw.get_platform_datasets
        :return: A DataFrame with information about the queried dataset(s).
        
          The fields of the DataFrame are:
            - experiment_short_name: Shortname given to the dataset within Gemma. Often corresponds to accession ID
            - experiment_name: Full title of the dataset
            - experiment_ID: Internal ID of the dataset.
            - experiment_description: Description of the dataset
            - experiment_troubled: Did an automatic process within gemma or a curator mark the dataset as "troubled"
            - experiment_accession: Accession ID of the dataset in the external database it was taken from
            - experiment_database: The name of the database where the dataset was taken from
            - experiment_URI: URI of the original database
            - experiment_sample_count: Number of samples in the dataset
            - experiment_batch_effect_text: A text field describing whether the dataset has batch effects
            - experimen_batch_corrected: Whether batch correction has been performed on the dataset.
            - experimen_batch_confound: 0 if batch info isn't available, -1 if batch counfoud is detected, 1 if batch information is available and no batch confound found
            - experimen_batch_effect: -1 if batch p value < 0.0001, 1 if batch p value > 0.1, 0 if otherwise and when there is no batch information is available or when the data is confounded with batches.
            - experimen_raw_data: -1 if no raw data available, 1 if raw data was available. When available, Gemma reprocesses raw data to get expression values and batches
            - geeq_q_score: Suitability score given to the dataset by Gemma. Refers to factors like batches, platforms and other aspects of experimental design
            - geeq_s_score: Data quality score given to the dataset by Gemma.
            - taxon_name: Name of the species
            - taxon_scientific: Scientific name for the taxon
            - taxon_ID: Internal identifier given to the species by Gemma
            - taxon_NCBI: NCBI ID of the taxon
            - taxon_database_name: Underlying database used in Gemma for the taxon
            - taxon_database_ID: ID of the underyling database used in Gemma for the taxon
        :rtype: DataFrame

        """
        
        kwargs = vs.remove_nones(offset = offset,
                                 limit = limit,
                                 **kwargs)
        
        
        response = self.raw.get_platform_datasets(platform, **kwargs)
        df = ps.process_datasets(response.data)
        ps.attach_attributes(df, response.to_dict())
        return df

    # platforms/{platform}/elements/{probes} -----
    # not implemented
    
    # platforms/{platform}/elements/{probe}/genes, get_platform_element_genes ----

    def get_platform_element_genes(self, platform:str|int, 
                                   probe:str|int,
                                   offset:int = 0,
                                   limit:int = 20,
                                   **kwargs)->DataFrame:
        
        
        """Retrieve the genes associated to a probe in a given platform
        
        :param platform: A platform numerical identifier or a platform short name
        :type platform: str|int
        :param probe: A probe name or it's numerical identifier
        :type probe: str|int
        :param offset: The offset of the first retrieved result., defaults to 0
        :type offset: int, optional
        :param limit: Limits the result to specified amount of objects.
          Has a maximum value of 100. Use together with offset and the 
          total_elements attribute in the output to compile all data if needed.
          Alternatively get_all_pages function can be used with all functions
          including offset and limit parameters, defaults to 20
        :type limit: int, optional
        :param **kwargs: Additional arguments to pass to raw.get_platform_element_genes
        :type **kwargs: TYPE
        :return: A DataFrame with the information about querried gene(s).
          The fields of the output DataFrame are:
            - gene_symbol: Symbol for the gene
            - gene_ensembl: Ensembl ID for the gene
            - gene_NCBI: NCBI id for the gene
            - gene_name: Name of the gene
            - gene_aliases: Gene aliases. Each row includes a vector
            - gene_MFX_rank: Multifunctionality rank for the gene
            - taxon_name: Name of the species
            - taxon_scientific: Scientific name for the taxon
            - taxon_ID: Internal identifier given to the species by Gemma
            - taxon_NCBI: NCBI ID of the taxon
            - taxon_database_name: Underlying database used in Gemma for the taxon
            - taxon_database_ID: ID of the underlying database used in Gemma for the taxon
        :rtype: DataFrame

        """
        
        kwargs = vs.remove_nones(offset = offset,
                                 limit = limit,
                                 **kwargs)
        
        response =  self.raw.get_platform_element_genes(platform, probe, **kwargs)
        df = ps.process_genes(response.data)
        ps.attach_attributes(df, response.to_dict())
        return df
    # platforms/{platform}/elements ----
    # unimplemented
    # reduntant with annotation files

    # platforms get_platforms -----
    # unimplemented in R but easier to keep things separate here
    def get_platforms(self,
                      filter:str = None,
                      taxa:List[str] = None,
                      offset:int=0,
                      limit:int = 20,
                      sort:str="+id",
                      **kwargs)->DataFrame:
        """
        Retrieve all platforms
        
        :param filter: Filter results by matching expression. Use 
          filter_properties function to get a list of all available parameters.
          These properties can be combined using "and" "or" clauses and may 
          contain common operators such as "=", "<" or "in". (e.g. 
          "taxon.commonName = human", "taxon.commonName in (human,mouse), 
          "id < 1000"), defaults to None
        :type filter: str, optional
        :param taxa: A list of taxon common names (e.g. human, mouse, rat). 
          Providing multiple species will return results for all species. These 
          are appended to the filter and equivalent to filtering for 
          taxon.commonName property, defaults to None
        :type taxa: List[str], optional
        :param offset: The offset of the first retrieved result., defaults to 0
        :type offset: int, optional
        :param limit: Limits the result to specified amount of objects.
          Has a maximum value of 100. Use together with offset and the 
          total_elements attribute in the output to compile all data if needed.
          Alternatively get_all_pages function can be used with all functions
          including offset and limit parameters, defaults to 20
        :type limit: int, optional
        :param sort: Order results by the given property and direction. The '+'
          sign indicate ascending order whereas the '-' indicate descending,
          defaults to "+id"
        :type sort: str, optional
        :param **kwargs: Additional arguments to raw.get_platforms_by_ids
        :return: A DataFrame with information about the platform(s).
        
          The fields of the output DataFrame are:

            - platform_ID: Internal identifier of the platform
            - platform_short_name: Shortname of the platform.
            - platform_name: Full name of the platform.
            - platform_description: Free text description of the platform
            - platform_troubled: Whether or not the platform was marked "troubled" by a Gemma process or a curator
            - platform_experiment_count: Number of experiments using the platform within Gemma
            - platform_type: Technology type for the platform.
            - taxon_name: Name of the species platform was made for
            - taxon_scientific: Scientific name for the taxon
            - taxon_ID: Internal identifier given to the species by Gemma
            - taxon_NCBI: NCBI ID of the taxon
            - taxon_database_name: Underlying database used in Gemma for the taxon
            - taxon_database_ID: ID of the underyling database used in Gemma for the taxon
        :rtype: DataFrame

        """
        
        filter = vs.add_to_filter(filter,"taxon.commonName",taxa)
        
        kwargs = vs.remove_nones(filter = filter,
                                 offset = offset,
                                 limit = limit,
                                 sort = sort,
                                 **kwargs)
        
        response =  self.raw.get_platforms(**kwargs)
        df = ps.process_platforms(response.data)
        ps.attach_attributes(df, response.to_dict())
        return df

    # platforms/{platform}, get_platforms_by_ids ---- 
    def get_platforms_by_ids(self, platforms:List[str|int], 
                             filter:str = None,
                             taxa:List[str] = None,
                             offset:int=0,
                             limit:int = 20,
                             sort:str="+id",
                             **kwargs)->DataFrame:
   
        
        
        """Retrieve platforms by their identifiers

        
        :param platforms: Platform numerical identifiers or platform short names.
        :type platforms: List[str|int]
        :param filter: Filter results by matching expression. Use 
          filter_properties function to get a list of all available parameters.
          These properties can be combined using "and" "or" clauses and may 
          contain common operators such as "=", "<" or "in". (e.g. 
          "taxon.commonName = human", "taxon.commonName in (human,mouse), 
          "id < 1000"), defaults to None
        :type filter: str, optional
        :param taxa: A list of taxon common names (e.g. human, mouse, rat). 
          Providing multiple species will return results for all species. These 
          are appended to the filter and equivalent to filtering for 
          taxon.commonName property, defaults to None
        :type taxa: List[str], optional
        :param offset: The offset of the first retrieved result., defaults to 0
        :type offset: int, optional
        :param limit: Limits the result to specified amount of objects.
          Has a maximum value of 100. Use together with offset and the 
          total_elements attribute in the output to compile all data if needed.
          Alternatively get_all_pages function can be used with all functions
          including offset and limit parameters, defaults to 20
        :type limit: int, optional
        :param sort: Order results by the given property and direction. The '+'
          sign indicate ascending order whereas the '-' indicate descending,
          defaults to "+id"
        :type sort: str, optional
        :param **kwargs: Additional arguments to raw.get_platforms_by_ids
        :return: A DataFrame with information about the platform(s).
        
          The fields of the output DataFrame are:

            - platform_ID: Internal identifier of the platform
            - platform_short_name: Shortname of the platform.
            - platform_name: Full name of the platform.
            - platform_description: Free text description of the platform
            - platform_troubled: Whether or not the platform was marked "troubled" by a Gemma process or a curator
            - platform_experiment_count: Number of experiments using the platform within Gemma
            - platform_type: Technology type for the platform.
            - taxon_name: Name of the species platform was made for
            - taxon_scientific: Scientific name for the taxon
            - taxon_ID: Internal identifier given to the species by Gemma
            - taxon_NCBI: NCBI ID of the taxon
            - taxon_database_name: Underlying database used in Gemma for the taxon
            - taxon_database_ID: ID of the underyling database used in Gemma for the taxon
        :rtype: DataFrame

        """
        filter = vs.add_to_filter(filter,"taxon.commonName",taxa)
        kwargs = vs.remove_nones(filter = filter,
                                 offset = offset,
                                 limit = limit,
                                 sort = sort,
                                 **kwargs)
        
        response =  self.raw.get_platforms_by_ids(platforms, **kwargs)
        df = ps.process_platforms(response.data)
        ps.attach_attributes(df, response.to_dict())
        return df
    
    
    # search search ------
    # this enpdoint is not very useful when specific endpoints exist for specific
    # result types. keeping here for now for compatibility with R
    
    def search_gemma(self,
                     query:str,
                     taxon:Optional[str|int]=None,
                     platform:Optional[str|int] = None,
                     limit:int = 100,
                     result_type:str = "experiment",
                     **kwargs)->list[sdk.SearchResultValueObjectObject]:

        
        """
        Search everything in Gemma
        
        :param query: The search query. Either plain text ('traumatic'), or an 
          ontology term URI ('http://purl.obolibrary.org/obo/UBERON_0002048').
          Datasets that contain the given string in their short of full name
          will also be matched. Can be multiple identifiers separated by commas.
        :type query: str
        :param taxon: A numerical taxon identifier or an ncbi taxon identifier
          or a taxon identifier that matches either its scientific or common
          name, defaults to None
        :type taxon: Optional[str|int], optional
        :param platform: A platform numerical identifier or a platform short 
          name, defaults to None
        :type platform: Optional[str|int], optional
        :param limit: Defaults to 100 with a maximum value of 2000. Limits the
          number of returned results. Note that this function does not support
          pagination., defaults to 100
        :type limit: int, optional
        :param result_type: The kind of results that should be included in the
          output. Can be "experiment", "gene", "platform" or a long object type name,
          documented in the API documentation., defaults to "experiment"
        :type result_type: str, optional
        :param **kwargs: Additional arguments to raw.search
        :return: A list containing the results. Actual results are under the 
          result_object component as dicts
        :rtype: list[sdk.SearchResultValueObjectObject]

        """
        
        result_type = vs.check_result_type(result_type)
        
        kwargs = vs.remove_nones(query =query,
                                 taxon = taxon,
                                 platform = platform,
                                 limit = limit,
                                 result_types = [result_type],
                                 **kwargs)
        
        response = self.raw.search(**kwargs)
        # df = ps.process_search(response.data,result_type)
        
        return response.data
    
    # taxa/{taxon}/genes/{gene}/locations----
    # unimplemented, redundant with get_gene_locations

    # taxa ----
    def get_taxa(self, **kwargs)->DataFrame:
        """
        Get all taxa within Gemma
        
        :param **kwargs: Additional arguments to raw.get_taxa
        :return: A DataFrame including the names, IDs and database information
          about the taxons
        :rtype: DataFrame

        """
        
        response =  self.raw.get_taxa(**kwargs)
        
        df = ps.process_taxon(response.data)
        return df[df.isnull().taxon_name != True]
        
        
    
    # taxa/{taxa}, get_taxa_by_ids -----
    # implemented, hardly needed with 3 taxa  



# Below are "Convenience" (combination) functions

    # set_gemma_user is not needed since it's wrapped in the GemmaPy class
    # get_platform_annotations is the default get_platform_annotations
    

    def make_design(self,samples:DataFrame,meta_type:str = 'text')->DataFrame:
        """
        Using on the output of get_dataset_samples, this function creates a
        simplified design table, granting one column to each experimental variable


        :param samples: An output from get_dataset_samples.
        :type samples: DataFrame
        :param meta_type: Type of metadata to include in the output. "text",
          "uri" or "both", defaults to 'text'
        :type meta_type: str, optional
        :return: A DataFrame including the design table for the dataset
        :rtype: DataFrame

        """
        
        categories = pd.concat([x[["factor_ID","factor_category","factor_category_URI"]] 
                                for x in samples.sample_factor_values],
                  ignore_index = True).drop_duplicates()
        
        
        def get_val_uri(x):
            return [",".join([str(z) if z is not None else "" 
                              for z in y[y.factor_ID==x].value_URI]) 
                    for y in samples.sample_factor_values]
        
        factor_URIs = [get_val_uri(x) for x in categories.factor_ID]
        
        def get_text(x):
            def get_summary(y):
                return ','.join([z[1].summary
                                 if z[1].summary is not None else z[1].value 
                                 for z in y[y.factor_ID==x].iterrows()])
            
            return [get_summary(y) for y in samples.sample_factor_values]
            
            
        
        text = [get_text(x) for x in categories.factor_ID]
        
        
        if meta_type =='text':
            design_frame = pd.DataFrame({
                categories.factor_category[i]:text[i] for i in range(len(text))
                })
        elif meta_type == 'uri':
            design_frame = pd.DataFrame({
                categories.factor_category_URI[i]:factor_URIs[i] for i in range(len(factor_URIs))
                })
        elif meta_type =='both':
            merged_name = [["|".join([categories.factor_category[i],
                                      categories.factor_category_URI[i]])] for i in range(len(text))]
            
            merged_col = [["|".join([text[i][j],factor_URIs[i][j]]) 
                           for j in range(len(text[i]))] for i in range(len(text))]
            
            
            design_frame = pd.DataFrame({
                merged_name[i]:merged_col[i]
                for i in range(len(text))})
            
        design_frame.insert(loc = 0,column = "factor_values",
                            value = samples.sample_factor_values)
        design_frame.index = samples.sample_name
        
        return design_frame
        
        
    
    def __subset_factor_values(self,
                               factor_values,
                               differential_expressions:pd.DataFrame,
                               result_set,
                               contrast):
        out = sub.rep(True,len(factor_values))
        if differential_expressions is not None:
            subset = differential_expressions[differential_expressions.result_ID == 
                                     result_set].subset_factor.drop_duplicates()
            # result set should have the same subset for all contrasts
            assert len(subset) == 1
            if subset[0].shape[0]!=0:
                subset_ids = subset[0].ID
                
                in_subset = [any(sub.list_in_list(x.ID, subset_ids)) for x in factor_values]
                
                out = out and in_subset
            
            if contrast is not None:
                cn = differential_expressions[
                    list(differential_expressions.result_ID == result_set) and 
                    list(differential_expressions.contrast_ID == str(contrast))]
                
                baseline_id = list(sub.unique(sub.break_list([list(x.ID) for x in cn.baseline_factors])))
                baseline_factor_id = list(sub.unique(sub.break_list([list(x.factor_ID) for x in cn.baseline_factors])))
                
                contrast_id =  list(sub.unique(sub.break_list([list(x.ID) for x in cn.experimental_factors])))
                contrast_factor_id =  list(sub.unique(sub.break_list([list(x.factor_ID) for x in cn.experimental_factors])))
                
                contrast_id = sub.match_by(contrast_id,baseline_factor_id, contrast_factor_id)
                
                def in_con(factor_value):
                    cond1 = all(sub.list_in_list(contrast_id, factor_value.ID)) or \
                            all(sub.list_in_list(baseline_id,factor_value.ID))                   
                    
                    if len(contrast_id)==2:
                        cond2 = (contrast_id[0] in factor_value.ID and \
                                    baseline_id[1] in factor_value.ID) or \
                            (contrast_id[1] in factor_value.ID and \
                                       baseline_id[0] in factor_value.ID)
                        
                        cond1 = cond1 or cond2
                    
                    return cond1
                        
                in_contrast = [in_con(x) for x in factor_values]
                
                out = out and in_contrast
        
        return out
        


    def get_dataset_object(self, datasets:List[str|int],
                           genes:Optional[List[str|int]] = None,
                           keep_non_specific = False,
                           consolidate:Optional[str] = None,
                           result_sets:Optional[List[int]] = None,
                           contrasts:Optional[List[str]] = None,
                           meta_type:str = 'text',
                           output_type:str = 'anndata',
                           **kwargs)->dict[int:dict|AnnData]:
        
        """Return a data structure including all relevant data related to
        gene expression in a dataset. Either returns an anndata object or 
        a dictionary with all the needed fields.
        
        
        :param datasets: Numerical dataset identifier
          dataset short names
        :type datasets: List[str|int]
        :param genes: An ncbi gene identifier an, 
          ensembl gene identifier which typically starts with ensg or an 
          official gene symbol approved by hgnc, defaults to None
        :type genes: Optional[List[str|int]], optional
        :param keep_non_specific: If True, results from 
          probesets that are not specific to the gene will also be returned,
          defaults to False
        :type keep_non_specific: TYPE, optional
        :param consolidate: DESCRIPTION, An option for gene expression level consolidation. 
          If empty, will return every probe for the genes. "pickmax" to pick 
          the probe with the highest expression, "pickvar" to pick the prove 
          with the highest variance and "average" for returning the average 
          expression to None
        :type consolidate: Optional[str], optional
        :param result_sets: Result set IDs of the a 
          differential expression analysis. If provided, the output will only 
          include the samples from the subset used in the result set ID. Must 
          be the same length as datasets, defaults to None
        :type result_sets: Optional[List[int]], optional
        :param contrasts: Contrast IDs of a differential 
          expression contrast. Need result_sets to be defined to work. If 
          provided, the output will only include samples relevant to the '
          specific contrats. Must be the same length as datasets.
        :param str meta_type: How should the metadata information should be 
          included. Can be "text", "uri" or "both". "text" and "uri" options, defaults to None
        :type contrasts: Optional[List[str]], optional
        :param meta_type: How should the metadata information should be 
          included. Can be "text", "uri" or "both". "text" and "uri" options, defaults to 'text'
        :type meta_type: str, optional
        :param output_type: Type of the returned object. "anndata" for an 
          AnnData object and "dict" for a dictionary populated with DataFrames,
          defaults to 'anndata'
        :type output_type: str, optional
        :param **kwargs: DESCRIPTION
        :type **kwargs: TYPE
        :raises ValueError: DESCRIPTION
        :return: A dictionary containing AnnData objects or nested dictionaries
          that contain expression and sample metada of the requested experiments
        :rtype: dict[int:dict|AnnData]

        """
        

        
        

        
        if output_type not in ["anndata","tidy","dict"]:
            raise ValueError('Please enter a valid output_type. anndata for'
                             '"anndata" objects, "tidy" for long form pandas'
                             'DataFrames, "dict" for dictionaries with separate'
                             'expression and metadata fields'
                              )
            
        unique_sets = list(set(datasets))
        
        metadata = {k:self.get_dataset_samples(k) for k in unique_sets}
        
        
        if genes is None:
            def get_exp(dataset):
                exp = self.get_dataset_processed_expression(dataset)
                meta = metadata[dataset]
                
                if not keep_non_specific:
                    exp = exp[~exp.GeneSymbol.str.contains("|",regex = False,na = True)]
                
                if consolidate is not None and consolidate =='pickmax':
                    mean_exp = exp[meta.sample_name].mean(axis=1,skipna=True)
                    exp = exp.iloc[list(sub.order(mean_exp,decreasing = True))]
                    exp = exp[~exp.duplicated('GeneSymbol')]
                elif consolidate is not None and consolidate == 'pickvar':
                    exp_var = exp[meta.sample_name].var(axis = 1, skipna= True)
                    exp = exp.iloc[list(sub.order(exp_var,decreasing = True))]
                    exp = exp[~exp.duplicated('GeneSymbol')]
                elif consolidate is not None and consolidate == 'average':
                    dups = list(
                        set(list(
                            exp[exp.duplicated("GeneSymbol")]["GeneSymbol"]
                            ))
                        )
                    
                    def get_mean(dup):
                        dup_subset = exp[exp.GeneSymbol == dup]
                        dup_mean =  exp[meta.sample_name].mean(axis = 0)
                        probe = "Averaged from " + " ".join(dup_subset.Probe)
                        
                        gene_info = dup_subset.\
                            loc[:,
                                np.array(~np.array(
                                    sub.list_in_list(
                                        dup_subset.columns,["Probe"] +\
                                            list(meta.sample_name))))].iloc[0].\
                                to_frame().T
                        
                        probe = pd.DataFrame({
                            "Probe": [probe]})
                        data = dup_mean.to_frame().T
                        return pd.concat([probe,gene_info.reset_index(drop = True),data],
                                         axis = 1)
                    
                    dup_means = [get_mean(dup) for dup in dups]
                    exp = pd.concat([exp[~exp.GeneSymbol.isin(dups)]] + dup_means, 
                                    ignore_index = True)
                return exp
            #get_exp
            
            expression = {k:get_exp(k) for k in unique_sets}
            
        else:
            expression = self.\
                get_dataset_expression_for_genes(unique_sets,
                                                 genes = genes,
                                                 keep_non_specific = keep_non_specific,
                                                 consolidate = consolidate)
        
        designs = {k:self.make_design(metadata[k]) for k in metadata.keys()}
        dat = self.get_datasets_by_ids(unique_sets)
        def pack_data(i):
            dataset = datasets[i]
            packed_info = {
                "design":designs[dataset].copy(),
                "exp": expression[dataset].copy(),
                "dat": dat[(dat.experiment_ID == dataset) | \
                           (dat.experiment_short_name == dataset)].copy().reset_index(),
                "result_set": None,
                "contrasts": None
                }
            
            
            if result_sets is not None:
                packed_info['result_set'] = result_sets[i]
            if contrasts is not None:
                packed_info['contrasts'] = contrasts[i]
            # reordering to match expression/metadata no longer necesarry
            
            diff = self.get_dataset_differential_expression_analyses(dataset)
            
            if result_sets is not None:
                gene_info = packed_info['exp'].\
                    columns[[not x 
                             for x in sub.list_in_list(packed_info['exp'].columns,
                                                       packed_info['design'].index)]]
                
                cons = None if contrasts is None else contrasts[i]
                
                relevant = self.__subset_factor_values(packed_info['design'].\
                                                       factor_values,
                                                       diff,
                                                       result_sets[i],
                                                       cons)
                packed_info['design'] = packed_info['design'][relevant]
                packed_info['exp'] = packed_info['exp'][gene_info.append(packed_info['design'].index)]
                
                    
            return packed_info
        
        
        
        # packed_data = [pack_data(i) for i in range(len(datasets))]
        packed_data = [pack_data(i) for i in range(len(datasets))]
        keys = [str(x['dat'].experiment_ID[0]) for x in packed_data]

        if result_sets is not None:
            keys = [keys[i] + "_" + str(result_sets[i]) for i in range(len(datasets))]
            if contrasts is not None:
                keys = [keys[i] + "_" + str(contrasts[i]) for i in range(len(datasets))] 
        
        packed_data = {keys[i]:packed_data[i] for i in range(len(datasets))}
        
        
        
        if output_type == 'anndata':
            def make_anndata(pack):
                pack['exp'].index = pack['exp']['Probe']
                try: 
                    gene_data = pack['exp'][['GeneSymbol', 'NCBIid']]
                except KeyError:
                    warnings.warn("WARNING: One or more gene descriptions are missing in Expression table")
                    gene_data = None
                
                mda = {
                    'title': pack['dat'].experiment_name[0],
                    'abstract': pack['dat'].experiment_description[0],
                    'url': 'https://gemma.msl.ubc.ca/expressionExperiment/showExpressionExperiment.html?id='+ \
                        str(pack['dat'].experiment_ID[0]),
                    'database': pack['dat'].experiment_database[0],
                    'accesion':  pack['dat'].experiment_accession[0],
                    "GemmaQualityScore":  pack['dat'].geeq_q_score[0],
                    "GemmaSuitabilityScore":  pack['dat'].geeq_s_score[0],
                    "taxon":  pack['dat'].taxon_name[0]
                    }
                
                exp = pack['exp'][pack['design'].index]
                adata = ad.AnnData(exp)
                if not (gene_data is None):
                    adata.obs = adata.obs.join(gene_data)
                    
                
                adata.var = adata.var.join(pack['design'])
                adata.uns = mda
                return adata
            # make_anndata
            
            
            out = {k:make_anndata(packed_data[k]) for k in packed_data.keys()}
        elif output_type == 'dict':
            out = packed_data
        elif output_type == "tidy":
            pass
        return out

    def get_differential_expression_values(self, 
                                           dataset:Optional[str|int] = None, 
                                           result_sets:Optional[List[str|int]] = None,
                                           readable_contrasts:bool = False, 
                                           **kwargs)->List[DataFrame]:
        """
        Retrieves the differential expression resultSet(s) associated with the dataset.
        If there is more than one resultSet, use get_result_sets() to see the options
        and get the ID you want. Alternatively, you can query the resultSet directly
        if you know its ID beforehand.
        
        In Gemma each result set corresponds to the estimated effects 
        associated with a single factor in the design, and each can have 
        multiple contrasts (for each level compared to baseline). Thus a 
        dataset with a 2x3 factorial design will have two result sets, one of 
        which will have one contrast, and one having two contrasts.
        
        The methodology for differential expression is explained in `Curation 
        of over 10000 transcriptomic studies to enable data reuse <https://doi.org/10.1093/database/baab006>`_.
        Briefly, differential expression analysis is performed on the dataset
        based on the annotated experimental design with up two three potentially
        nested factors. Gemma attempts to automatically assign baseline conditions
        for each factor. In the absence of a clear control condition, a baseline 
        is arbitrarily selected. A generalized linear model with empirical Bayes
        shrinkage of t-statistics is fit to the data for each platform element 
        (probe/gene) using an implementation of the limma algorithm. For 
        RNA-seq data, we use weighted regression, applying the voom algorithm
        to compute weights from the mean–variance relationship of the data. 
        Contrasts of each condition are then computed compared to the selected 
        baseline. In some situations, Gemma will split the data into subsets for
        analysis. A typical such situation is when a ‘batch’ factor is present 
        and confounded with another factor, the subsets being determined by the
        levels of the confounding factor.
        
        
        :param dataset: A dataset identifier, defaults to None
        :type dataset: Optional[str|int], optional
        :param result_sets: result set identifiers. If a dataset
          is not provided, all result sets will be downloaded. If it is provided
          it will only be used to ensure all result sets belong to the dataset, defaults to None
        :type result_sets: Optional[List[str|int]], optional
        :param readable_contrasts: If False (default), the returned columns
          will use internal constrasts IDs as names. Details about the contrasts can be
          accessed using get_dataset_differential_expression_analyses(). If True IDs
          will be replaced with human readable contrast information, defaults to False
        :type readable_contrasts: bool, optional
        :param **kwargs: 
        :type **kwargs: TYPE
        :raises ValueError: Will return a value error if neither result_sets nor a dataset
          is provided
        :return: A list of data frames with differential expression values per result set.
        :rtype: List[DataFrame]

        """
        if dataset is not None and result_sets is not None:
            diffs =  self.get_dataset_differential_expression_analyses(dataset)
            rss = diffs.result_ID
            if not all(sub.list_in_list(result_sets, rss)):
                warnings.warn('The queried resultSet is not derived from this dataset. ' 
                              'Check the available resultSets with "get_result_sets()" '
                              'or query without the dataset parameter.')
                return
        elif dataset is not None and result_sets is None:
            diffs =  self.get_dataset_differential_expression_analyses(dataset)
            result_sets = diffs.result_ID.unique()
        elif dataset is None and result_sets is None:
            raise ValueError('You must specify a dataset or result_sets')
            
        rss = {}
        if readable_contrasts:
            all_factors =  self.get_result_sets(result_sets = result_sets)
        
        for rs in result_sets:
            df = self.__get_result_set(rs)
            if readable_contrasts:
                factors = pd.concat(
                    list(all_factors[all_factors.result_ID == rs].experimental_factors)
                    ).drop_duplicates()
                cols = [s.replace('log2fc','logFoldChange') for s in df.columns]
                for i in range(factors.shape[0]):
                    cols = [s.replace(str(list(factors.ID)[i]),list(factors.summary)[i]) for s in cols]
                df.columns = cols
            rss[rs] = df
        return rss
            

    # get_taxa is moved to base. only removes the nameless rat now

    # gemma_call unimplemented, not needed    

    def get_all_pages(self,fun:Callable,step_size:int = 100,**kwargs)->list|DataFrame:
        """
        A convenience function to allow easy iteration over paginated outputs.
        If the function returns a DataFrame output will be merged by the rows,
        if the function returns a list (eg. 'raw' functions) a concatanated list
        will be returned
        
        
        :param fun: A callable from gemmapy with offset and limit
          functions
        :type fun: Callable
        :param step_size: Size of individual calls to the server. 100 is 
          the maximum value and the default.
        :type step_size: int, optional
        :param **kwargs: arguments for the callable fun
        :return: A DataFrame or a list containing all the output depending on 
          output of the callable
        :rtype: list|DataFrame
        """

        out = []        
        poke_call = fun(limit =1,**kwargs)
        
        if type(poke_call) == pd.core.frame.DataFrame:
            count = poke_call.attributes["total_elements"]
        else:
            count = poke_call.total_elements
        
        for i in range(0,count,step_size):
            out.append(fun(limit = step_size,offset = i,**kwargs))
        
        if type(poke_call) == pd.core.frame.DataFrame:
            return pd.concat(out,ignore_index = True)
        else:
            return sub.break_list([x.data for x in out])
        

    
    def filter_properties(self, output_type:str = 'DataFrame')->dict|DataFrame:
        """
        Some functions such as get_datasets and get_platforms include a filter
        argument that allows creation of more complex queries. This function 
        returns a list of supported properties to be used in those filters
        
        :param output_type: Type to return. "DataFrame" or "dict", defaults to 'DataFrame'
        :type output_type: str, optional
        :return: DataFrame or dict containing supported properties and their data types
        :rtype: dict|DataFrame

        """
        
        d = self.raw.api_client.rest_client.GET("https://gemma.msl.ubc.ca/rest/v2/openapi.json").urllib3_response
        api_file = json.loads(d.data)
        
        dataset_filter = api_file["components"]["schemas"]["FilterArgExpressionExperiment"]["x-gemma-filterable-properties"]
        
        platform_filter = api_file["components"]["schemas"]["FilterArgArrayDesign"]["x-gemma-filterable-properties"]
        
        result_set_filter = api_file["components"]["schemas"]["FilterArgExpressionAnalysisResultSet"]["x-gemma-filterable-properties"]
        
        if output_type == 'DataFrame':
            return {
                "dataset":pd.DataFrame({
                    "name": sub.field_in_list(dataset_filter,'name'),
                    "type": sub.field_in_list(dataset_filter,'type'),
                    "description": sub.field_in_list(dataset_filter,'description')
                    }),
                "platform":pd.DataFrame({
                    "name": sub.field_in_list(platform_filter,'name'),
                    "type": sub.field_in_list(platform_filter,'type'),
                    "description": sub.field_in_list(platform_filter,'description')
                    }),
                "result_set":pd.DataFrame({
                    "name": sub.field_in_list(result_set_filter,'name'),
                    "type": sub.field_in_list(result_set_filter,'type'),
                    "description": sub.field_in_list(result_set_filter,'description')
                    })
                }
        elif output_type == 'dict':
            return {
                "dataset": {x['name']:{"type":x['type'],
                                              "description":sub.access_field(x,'description',None)} for x in dataset_filter},
                'platform':{x['name']:{"type":x['type'],
                                              "description":sub.access_field(x,'description',None)} for x in platform_filter},
                'result_set':{x['name']:{"type":x['type'],
                                              "description":sub.access_field(x,'description',None)} for x in result_set_filter}
                
                }
            
        
    
    def get_child_terms(self,terms:List[str])->List[str]:
        """
        When querying for ontology terms, Gemma propagates these terms to 
        include any datasets with their child terms in the results. This 
        function returns these children for any number of terms, including all 
        children and the terms itself in the output vector
        
        :param terms: A list of ontology terms
        :type terms: List[str]
        :return: An array containing descendends of the annotation terms, 
        including the terms themselves
        :rtype: List[str]

        """
        
        output = self.get_datasets(uris=terms)
        
        return re.findall(r'http.*?(?=,|\))',output.attributes['filter'])
    
    # update_results currenty unimplemented and not really essential


# Tests
if __name__ == '__main__':
    # dv temp
    import http.client
    http.client.HTTPConnection.debuglevel = 0 # put 5 to debug

    import sys
    from pprint import pprint

    api_instance = GemmaPy()

    def get_dataset_annotations_test():
        print('Testing get_dataset_annotations function:')
        api_response = api_instance.get_dataset_annotations("GSE46416")
        pprint(api_response.data)
        print('')

    def search_datasets_test():
        print('Testing search_datasets function:')
        api_response = api_instance.search_datasets(["bipolar"], taxon="human", limit=100)
        for d in api_response.data:
            if d.geeq is not None and  d.geeq.batch_corrected:
                print(d.short_name, d.name, d.bio_assay_count)
        print('')

    def get_datasets_by_ids_test():
        print('Testing get_datasets_by_ids function:')
        api_response = api_instance.get_datasets_by_ids(["GSE46416"])
        for d in api_response.data:
            print(d.short_name, d.name, d.id, d.description)
        print('')

    def search_annotations_test():
        print('Testing search_annotations function:')
        api_response = api_instance.search_annotations(["GSE46416"])
        print(api_response.data)

    def get_dataset_object_test():
        print('Testing get_dataset_object function:')
        adata = api_instance.get_dataset_object("GSE46416")
        print(adata)
        print('\nUnstructured Info:')
        for l in adata.uns: print('%s: %s' % (l, adata.uns[l]))
        print('')
        print('Observation metadata:')
        print(adata.obs.iloc[1:10])
        print('')
        print('Vars metadata:')
        print(adata.var.iloc[1:10])
        print('')
        print('Data:')
        print(adata.X)
        print('')

        print('Subsetting the Experiment\nDisease levels')
        print(adata.var['disease'].unique())
        print('\nSubset: patients during manic phase and controls')
        manic=adata[:,(adata.var['disease'] == 'reference_subject_role') |
                      (adata.var['disease'] == 'bipolar_disorder_|_manic_phase_|')].copy()
        print(manic)
        print(manic.var)

    def get_result_sets_test():
        print('Testing get_result_sets function:')
        df = api_instance.get_result_sets('GSE6711')
        print(df)
        df2 = api_instance.get_result_set(485406)
        print(df2)

    def get_differential_expression_values_test():
        de = api_instance.get_differential_expression_values('GSE46416')
        de['diffexpr'] = 'No'   # add extra column
        #de['diffexpr'][(de['contrast_bipolar disorder, manic phase_logFoldChange']>1.0) &
        #               (de['contrast_bipolar disorder, manic phase_pvalue']<0.05)] = 'Up'
        de.loc[(de['contrast_bipolar disorder, manic phase_logFoldChange'] > 1.0) &
                       (de['contrast_bipolar disorder, manic phase_pvalue'] < 0.05),'diffexpr'] = 'Up'
        de.loc[(de['contrast_bipolar disorder, manic phase_logFoldChange'] < -1.0) &
                       (de['contrast_bipolar disorder, manic phase_pvalue'] < 0.05),'diffexpr'] = 'Down'
        de_up = de[de['diffexpr']=='Up']
        de_up = de_up[['Probe','GeneSymbol', 'contrast_bipolar disorder, manic phase_pvalue',
                       'contrast_bipolar disorder, manic phase_logFoldChange']].sort_values(
                'contrast_bipolar disorder, manic phase_pvalue')
        print('Upregulated probes')
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(de_up[:10])

        de_dn = de[de['diffexpr']=='Down']
        de_dn = de_dn[['Probe','GeneSymbol', 'contrast_bipolar disorder, manic phase_pvalue',
                       'contrast_bipolar disorder, manic phase_logFoldChange']].sort_values(
                'contrast_bipolar disorder, manic phase_pvalue')
        print('\nDownregulated probes')
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(de_dn[:10])

    def get_platform_annotations_test():
        print('Testing get_platform_annotations function')
        df = api_instance.get_platform_annotations('GPL96')
        print(df)

    if len(sys.argv) > 1:
        fname = sys.argv[1]
        dict = vars()
        if fname in dict:
            #print("Calling",fname)
            func = dict[fname]
            func()
