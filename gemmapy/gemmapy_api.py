# -*- coding: utf-8 -*-
"""
Gemma python API (https://gemma.msl.ubc.ca/rest/v2/)
"""

import logging
from   gemmapy import sdk
from gemmapy import processors as ps
from gemmapy import validators as vs
from gemmapy import subprocessors as sub

import typing as T
import pandas as pd
import numpy as np
import anndata as ad
from io import StringIO
import warnings
import re

logger = logging.getLogger(__name__)

class GemmaPy(object):
    """
    Main API class
    """

    def __init__(self, auth=None, path="prod"):
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
    def __get_result_set(self, result_set:int, **kwargs):  # noqa: E501
        """Retrieve a single analysis result set by its identifier

        :param int result_set: (required)
        :return: DataFrame
        """
        response = self.raw.get_result_set_as_tsv(result_set, **kwargs)
        
        df = ps.process_de_matrix(response, result_set,self)
        
        return df
        

    
    # /resultSets, get_result_sets -----
    
    def get_result_sets(self,
                        datasets:T.Optional[T.List[T.Union[str,int]]] = None,
                        result_sets:T.Optional[T.List[int]] = None,
                        filter:str = None,
                        offset:int = 0,
                        limit:int = 20,
                        sort:str = "+id",
                        **kwargs):  # noqa: E501
        """Retrieve all result sets matching the provided criteria

        :param str dataset: (required)
        :return: DataFrame
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
    def search_annotations(self, query:T.List[str], **kwargs):  # noqa: E501
        """Search for annotation tags

        :param list[str] query: (required)
        :rtype: ResponseDataObjectListAnnotationSearchResultValueObject
        """
        response = self.raw.search_annotations(query=query, **kwargs)
        return ps.process_search_annotations(response.data)
    

    # /datasets/{dataset}/annotations, get_dataset_annotations ----------
    def get_dataset_annotations(self, dataset:T.Union[str,int], **kwargs):  # noqa: E501
        """Retrieve the annotations analysis of a dataset

        :param str dataset: (required)
        :rtype: ResponseDataObjectSetAnnotationValueObject
        """
        response = self.raw.get_dataset_annotations(dataset, **kwargs)
        df = ps.process_annotations(response.data)
        ps.attach_attributes(df, response.to_dict())
        
        return df
    
    # /datasets/{dataset}/design, get_dataset_design -----
    # this endpoint is not very useful since the names it comes with
    # is annoying to match names provided in the samples endpoint
    # make_design replaces this
    def __get_dataset_design(self, dataset:T.Union[str,int], **kwargs):  # noqa: E501
        """Retrieve the design of a dataset

        :param str dataset: (required)
        :return: DataFrame
        """
        response = self.raw.get_dataset_design(dataset, **kwargs)
        df = ps.process_dataset_design(response)
        
        return df
    
    # /datasets/{datasets}/expressions/differential ------
    # unimplemented
    # not sure how the parameters for this endpoint works and doesn't seem essential
    
    # /datasets/{dataset}/analyses/differential, get_dataset_differential_expression_analyses ------
    def get_dataset_differential_expression_analyses(self, 
                                                     dataset:T.Union[str,int],
                                                     **kwargs):  # noqa: E501
        """Retrieve the differential analyses of a dataset

        :param str dataset: (required)
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :rtype: ResponseDataObjectListDifferentialExpressionAnalysisValueObject
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
    def get_dataset_expression(self, dataset:T.Union[int,str], **kwargs):  # noqa: E501
        """Retrieve the expression data of a dataset

        :param str dataset: (required)
        :param bool filter: Filter results by matching the expression
        :return: DataFrame
        """
        warnings.warn('get_dataset_expression is deprecated, please use get_dataset_processed_expression instead')
        
        return self.get_dataset_processed_expression(dataset,**kwargs)

    
    
    
    # /datasets/{datasets}/expressions/genes/{genes}, get_dataset_expression_for_genes ------
    def get_dataset_expression_for_genes(self,
                                         datasets:T.List[T.Union[str,int]],
                                         genes:T.List[int],
                                         keep_non_specific:bool = False,
                                         consolidate = None,
                                         **kwargs):
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
    def get_dataset_platforms(self, dataset:T.Union[int,str], **kwargs):  # noqa: E501
        """Retrieve the platform of a dataset

        :param str dataset: (required)
        :rtype: ResponseDataObjectListArrayDesignValueObject
        """
        response = self.raw.get_dataset_platforms(dataset, **kwargs)
        df = ps.process_platforms(response.data)
        
        return(df)
    
    
    # datasets/{dataset}/data/processed ------
    
    def get_dataset_processed_expression(self,dataset:T.Union[int,str],**kwargs):
        response = self.raw.get_dataset_processed_expression(dataset, **kwargs)
        
        df = ps.process_expression(response,dataset,self)
        
        return df
    
    # datasets/{dataset}/quantitationTypes get_dataset_quantitation_types ----------
    
    def get_dataset_quantitation_types(self,dataset:T.Union[int,str],**kwargs):
        
        response = self.raw.get_dataset_quantitation_types(dataset, **kwargs)
        df = ps.process_QuantitationTypeValueObject(response)
        
        
        return df

    # datasets/{dataset}/data/raw, get_dataset_raw_expression ---------
    def get_dataset_raw_expression(self,dataset:T.Union[int,str],
                                   quantitation_type:[int],**kwargs):
        
        kwargs = vs.remove_nones(
            quantitation_type = quantitation_type,
            **kwargs)
        
        response = self.raw.get_dataset_raw_expression(dataset, **kwargs)
        
        df = ps.process_expression(response,dataset,self)
        
        return df
    
    
    # datasets/{dataset}/samples, get_dataset_samples --------
    def get_dataset_samples(self, dataset:T.Union[int,str], **kwargs):  # noqa: E501
        """Retrieve the samples of a dataset

        :param str dataset: (required)
        :rtype: ResponseDataObjectListBioAssayValueObject
        """
        response = self.raw.get_dataset_samples(dataset, **kwargs)
        df = ps.process_samples(response.data)
        return df
        
    # datasets/{dataset}/svd --- 
    # not implemented
    
    # datasets, get_datasets ------
    def get_datasets(self,query:T.Optional[str] = None, 
                     filter:T.Optional[str] = None, 
                     taxa:T.Optional[T.List[str]] = None, 
                     uris:T.Optional[T.List[str]] = None,
                     offset:int = 0,
                     limit:int = 20,
                     sort:str = "+id",
                     **kwargs):
        
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
    def get_datasets_by_ids(self, dataset:T.List[T.Union[str,int]],
                            filter:T.Optional[str] = None, 
                            taxa:T.Optional[T.List[str]] = None, 
                            uris:T.Optional[T.List[str]] = None,
                            offset:int = 0,
                            limit:int = 20,
                            sort:str = "+id",
                            **kwargs):  # noqa: E501
        """Retrieve datasets by their identifiers

        :param list[str] dataset: (required)
        :param str filter: Filter results by matching the expression
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :param str sort: Order results by the given property and direction. The '+'
          sign indicate ascending order whereas the '-' indicate descending.
        :rtype: PaginatedResponseDataObjectExpressionExperimentValueObject
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
    
    def get_gene_go_terms(self, gene:T.Union[str,int], **kwargs):  # noqa: E501
        """Retrieve the GO terms associated to a gene

        :param str gene: (required)
        :rtype: ResponseDataObjectListGeneOntologyTermValueObject
        """
        response = self.raw.get_gene_go_terms(gene, **kwargs)
        df = ps.process_GO(response.data)
        return df

    
    # genes/{gene}/locations, get_gene_locations ----
    
    def get_gene_locations(self, gene:T.Union[str,int], **kwargs):  # noqa: E501
        """Retrieve the physical locations of a given gene

        :param str gene: (required)
        :rtype: ResponseDataObjectListPhysicalLocationValueObject
        """
        response = self.raw.get_gene_locations(gene, **kwargs)
        df = ps.process_gene_location(response.data)
        return df
    
    # genes/{gene}/probes, get_gene_probes -----
    
    def get_gene_probes(self, gene:T.Union[str,int],
                        offset:int = 0,
                        limit:int = 20,
                        **kwargs):  # noqa: E501
        """Retrieve the probes associated to a genes

        :param str gene: (required)
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :rtype: PaginatedResponseDataObjectCompositeSequenceValueObject
        """
        kwargs = vs.remove_nones(offset = offset,
                                 limit = limit,
                                 **kwargs)
        
        response = self.raw.get_gene_probes(gene, **kwargs)
        df = ps.process_elements(response.data)
        ps.attach_attributes(df, response.to_dict())
        return df
        
        
    # genes/{genes}, get_genes-------

    def get_genes(self, genes, **kwargs):  # noqa: E501
        """Retrieve genes matching a gene identifier

        :param list[str] genes: (required)
        :rtype: ResponseDataObjectListGeneValueObject
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
    def get_platform_annotations(self, platform, **kwargs):
        """Retrieve the annotations of a given platform

        :param str platform: (required)
        :return: DataFrame
        """
        api_response = self.raw.get_platform_annotations(platform, **kwargs)
        uncomment = api_response.split("\n#")
        api_response = uncomment[len(uncomment)-1]
        uncomment = api_response.split('\n',1)
        api_response = uncomment[len(uncomment)-1]
        return pd.read_csv(StringIO(api_response), sep='\t')

    # platform/{platform}/datasets, get_platform_datasets ----

    def get_platform_datasets(self, platform:T.Union[str,int],
                              offset:int = 0,
                              limit:int = 20,
                              **kwargs):  # noqa: E501
        """Retrieve all experiments within a given platform

        :param str platform: (required)
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :rtype: PaginatedResponseDataObjectExpressionExperimentValueObject
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

    def get_platform_element_genes(self, platform:T.Union[str,int], 
                                   probe:T.Union[str,int],
                                   offset:int = 0,
                                   limit:int = 20,
                                   **kwargs):  # noqa: E501
        """Retrieve the genes associated to a probe in a given platform

        :param str platform: (required)
        :param str probe: (required)
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :rtype: PaginatedResponseDataObjectGeneValueObject
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
                      taxa:T.List[str] = None,
                      offset:int=0,
                      limit:int = 20,
                      sort:str="+id",
                      **kwargs):
        
        
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
    def get_platforms_by_ids(self, platforms:T.List[T.Union[str,int]], 
                             filter:str = None,
                             taxa:T.List[str] = None,
                             offset:int=0,
                             limit:int = 20,
                             sort:str="+id",
                             **kwargs):  # noqa: E501
        """Retrieve all platforms matching a set of platform identifiers

        :param list[str] platform: (required)
        :param str filter: Filter results by matching the expression
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :param str sort: Order results by the given property and direction. The '+'
          sign indicate ascending order whereas the '-' indicate descending.
        :rtype: PaginatedResponseDataObjectArrayDesignValueObject
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
                     taxon:T.Optional[T.Union[str,int]]=None,
                     platform:T.Optional[T.Union[str,int]] = None,
                     limit:int = 100,
                     result_type:str = "experiment",
                     **kwargs):
        
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
    def get_taxa(self, **kwargs):
        response =  self.raw.get_taxa(**kwargs)
        
        df = ps.process_taxon(response.data)
        return df[df.isnull().taxon_name != True]
        
        
    
    # taxa/{taxa}, get_taxa_by_ids -----
    # implemented, hardly needed with 3 taxa  



# Below are "Convenience" (combination) functions

    # set_gemma_user is not needed since it's wrapped in the GemmaPy class
    # get_platform_annotations is the default get_platform_annotations
    

    def make_design(self,samples,meta_type = 'text'):
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
                k:v for k in categories.factor_category for v in text
                })
        elif meta_type == 'uri':
            design_frame = pd.DataFrame({
                k:v for k in categories.factor_category_URI for v in factor_URIs
                })
        elif meta_type =='both':
            design_frame = pd.DataFrame({
                k:v for v in [["|".join([text[i][j],factor_URIs[i][j]]) 
                               for j in range(len(text[i]))] for i in range(len(text))]
                for k in ["|".join([x,y]) for x in categories.factor_category 
                          for y in categories.factor_category_URI]
                })
            
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
        


    def get_dataset_object(self, datasets:T.List[T.Union[str,int]],
                           genes:T.Optional[T.List[T.Union[str,int]]] = None,
                           keep_non_specific = False,
                           consolidate:T.Optional[str] = None,
                           result_sets:T.Optional[T.List[int]] = None,
                           contrasts:T.Optional[T.List[str]] = None,
                           meta_type:str = 'text',
                           output_type:str = 'anndata',
                           **kwargs):
        """Return a data structure including all relevant data related to
        gene expression in a dataset. Either returns an anndata object or 
        a dictionary with all the needed fields.

        :param list[str|int] datasets: Numerical dataset identifier
          dataset short names
        :param list[str,int] genes: (optional) An ncbi gene identifier an, 
          ensembl gene identifier which typically starts with ensg or an 
          official gene symbol approved by hgnc
        :param bool keep_non_specific: False by default. If True, results from 
          probesets that are not specific to the gene will also be returned.
        :param str consolidate: An option for gene expression level consolidation. 
          If empty, will return every probe for the genes. "pickmax" to pick 
          the probe with the highest expression, "pickvar" to pick the prove 
          with the highest variance and "average" for returning the average 
          expression
        :param list[int] result_sets: (optional) Result set IDs of the a 
          differential expression analysis. If provided, the output will only 
          include the samples from the subset used in the result set ID. Must 
          be the same length as datasets. 
        :param list[int] contrasts: (optional) Contrast IDs of a differential 
          expression contrast. Need result_sets to be defined to work. If 
          provided, the output will only include samples relevant to the '
          specific contrats. Must be the same length as datasets.
        :param str meta_type: How should the metadata information should be 
          included. Can be "text", "uri" or "both". "text" and "uri" options
        :param str output_type: Type of the returned object. "anndata" for an 
          AnnData object and "dict" for a dictionary.
        :return: dict | AnnData class object
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
                    logger.warning("WARNING: One or more gene descriptions are missing in Expression table")
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
                                           dataset:T.Optional[T.Union[str,int]] = None, 
                                           result_sets:T.Optional[T.List[T.Union[str,int]]] = None,
                                           readable_contrasts = False, 
                                           **kwargs):
        """Retrieves the differential expression resultSet(s) associated with the dataset.
        If there is more than one resultSet, use get_result_sets() to see the options
        and get the ID you want. Alternatively, you can query the resultSet directly
        if you know its ID beforehand.

        :param str | int dataset: (optional) A dataset identifier.
        :param int result_sets: (optional) result set identifiers. If a dataset
          is not provided, all result sets will be downloaded. If it is provided
          it will only be used to ensure all result sets belong to the dataset.
        :param bool readable_contrasts: (optional) If False (default), the returned columns
          will use internal constrasts IDs as names. Details about the contrasts can be
          accessed using get_dataset_differential_expression_analyses(). If True IDs
          will be replaced with human readable contrast information.
        :return: list[DataFrame]
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
                    cols = [s.replace(str(factors.ID[i]),factors.summary[i]) for s in cols]
                    df.columns = cols
            rss[rs] = df
        return rss
            

    # get_taxa is moved to base. only removes the nameless rat now

    # gemma_call unimplemented, not needed    

    def get_all_pages(self,fun:T.Callable,step_size = 100,**kwargs):
        """
        A convenience function to allow easy iteration over paginated outputs.
        If the function returns a DataFrame output will be merged by the rows,
        if the function returns a list (eg. 'raw' functions) a concatanated list
        will be returned
        
        :param Callable fun: A callable from gemmapy with offset and limit
          functions
        :param int step_size: Size of individual calls to the server. 100 is 
          the maximum value 
        :return: list | DataFrame
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
        

    # filter_properties currently unimplemented. requires keeping the json around
    
    def get_child_terms(self,terms:T.List[str]):
        """
        When querying for ontology terms, Gemma propagates these terms to 
        include any datasets with their child terms in the results. This 
        function returns these children for any number of terms, including all 
        children and the terms itself in the output vector
        
        :param list[str] terms A list of ontology terms
        :return: list[str]
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
