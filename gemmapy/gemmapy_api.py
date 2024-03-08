# -*- coding: utf-8 -*-
"""
Gemma python API (https://gemma.msl.ubc.ca/rest/v2/)
"""

import logging
from   gemmapy import sdk
from gemmapy import processors as ps
from gemmapy import validators as vs

import typing as T
import pandas
import numpy
import anndata
from io import StringIO
import warnings

logger = logging.getLogger(__name__)

class GemmaPy(object):
    """
    Main API class
    """

    def __init__(self, auth=None, devel=False):
        """
        :param list auth: (optional) A list or tuple of credential strings, e.g.
          (your_username, your_password)
        :param bool devel: (optional) If True development version of Gemma API will be
          used. Default is False.
        """

        configuration = sdk.Configuration()
        if devel:
            configuration.host = 'https://dev.gemma.msl.ubc.ca/rest/v2'

        if auth is not None:
            configuration.username = auth[0]
            configuration.password = auth[1]

        # create an instance of the API class
        self.raw = sdk.DefaultApi(sdk.ApiClient(configuration))


    # /resultSets/count get_number_of_result_sets ------
    # unimplemented
    # we don't need this here, not included
    
    # /resultSets/{resultSet}, get_result_set ------ 
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
                        resultSets:T.Optional[T.List[int]] = None,
                        filter:str = None,
                        offset:int = 0,
                        limit:int = 20,
                        sort:str = "+id",
                        **kwargs):  # noqa: E501
        """Retrieve all result sets matching the provided criteria

        :param str dataset: (required)
        :return: DataFrame
        """
        
        filter = vs.add_to_filter(filter, 'id', resultSets)
        
        
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
        api_response = self.raw.get_dataset_design(dataset, **kwargs)
        df = ps.process_dataset_design(api_response)
        
        return df
    
    # /datasets/{datasets}/expressions/differential ------
    # unimplemented
    # not sure how the parameters for this endpoint works and doesn't seem essential
    
    # /datasets/{dataset}/analyses/differential, get_dataset_differential_expression_analyses ------
    def get_dataset_differential_expression_analyses(self, dataset:T.Union[str,int], **kwargs):  # noqa: E501
        """Retrieve the differential analyses of a dataset

        :param str dataset: (required)
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :rtype: ResponseDataObjectListDifferentialExpressionAnalysisValueObject
        """
        api_response = self.raw.get_dataset_differential_expression_analyses(dataset, **kwargs)
        df = ps.process_dea(api_response.data)
        
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
        
        api_response = self.raw.get_dataset_expression_for_genes(datasets, genes, **kwargs)
        df = ps.process_dataset_gene_expression(api_response.data)
        
        return df
        
    # datasets/{datasets}/expressions/pca -----
    # unimplemented
    
    
    # datasets/{dataset}/platforms ------
    def get_dataset_platforms(self, dataset:T.Union[int,str], **kwargs):  # noqa: E501
        """Retrieve the platform of a dataset

        :param str dataset: (required)
        :rtype: ResponseDataObjectListArrayDesignValueObject
        """
        api_response = self.raw.get_dataset_platforms(dataset, **kwargs)
        df = ps.process_platforms(api_response.data)
        
        return(df)
    
    
    # datasets/{dataset}/data/processed ------
    
    def get_dataset_processed_expression(self,dataset:T.Union[int,str],**kwargs):
        api_response = self.raw.get_dataset_processed_expression(dataset, **kwargs)
        
        df = ps.process_expression(api_response,dataset,self)
        
        return df
    
    
    
    
    # datasets/{dataset}/samples, get_dataset_samples --------
    def get_dataset_samples(self, dataset:T.Union[int,str], **kwargs):  # noqa: E501
        """Retrieve the samples of a dataset

        :param str dataset: (required)
        :rtype: ResponseDataObjectListBioAssayValueObject
        """
        api_response = self.raw.get_dataset_samples(dataset, **kwargs)
        df = ps.process_samples(api_response.data)
        return df
        
    
    
    def get_dataset_quantitation_types(self,dataset,**kwargs):
        return self.raw.get_dataset_quantitation_types(dataset, **kwargs)
    
    def get_dataset_raw_expression(self,dataset,**kwargs):
        api_response = self.raw.get_dataset_raw_expression(dataset, **kwargs)
        uncomment = api_response.split("\n#")
        api_response = uncomment[len(uncomment)-1]
        uncomment = api_response.split('\n',1)
        api_response = uncomment[len(uncomment)-1]
        
        df = pandas.read_csv(StringIO(api_response), sep='\t', dtype={'Probe':'str'})
        
        # conditioning: fix names and remove redundant columns
        df = df.drop(columns=['Sequence', 'GemmaId'], errors='ignore')
        df.columns = [c if c.find('Name=') < 0 else c[c.find('Name=')+5:] for c in df.columns]
        return df
        



    def get_datasets(self,**kwargs):
        return self.raw.get_datasets(**kwargs)

    def get_datasets_by_ids(self, dataset, **kwargs):  # noqa: E501
        """Retrieve datasets by their identifiers

        :param list[str] dataset: (required)
        :param str filter: Filter results by matching the expression
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :param str sort: Order results by the given property and direction. The '+'
          sign indicate ascending order whereas the '-' indicate descending.
        :rtype: PaginatedResponseDataObjectExpressionExperimentValueObject
        """
        return self.raw.get_datasets_by_ids(dataset, **kwargs)

    def get_gene_go_terms(self, gene, **kwargs):  # noqa: E501
        """Retrieve the GO terms associated to a gene

        :param str gene: (required)
        :rtype: ResponseDataObjectListGeneOntologyTermValueObject
        """
        return self.raw.get_gene_go_terms(gene, **kwargs)

    def get_gene_locations(self, gene, **kwargs):  # noqa: E501
        """Retrieve the physical locations of a given gene

        :param str gene: (required)
        :rtype: ResponseDataObjectListPhysicalLocationValueObject
        """
        return self.raw.get_gene_locations(gene, **kwargs)

    def get_gene_probes(self, gene, **kwargs):  # noqa: E501
        """Retrieve the probes associated to a genes

        :param str gene: (required)
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :rtype: PaginatedResponseDataObjectCompositeSequenceValueObject
        """
        return self.raw.get_gene_probes(gene, **kwargs)

    def get_genes(self, genes, **kwargs):  # noqa: E501
        """Retrieve genes matching a gene identifier

        :param list[str] genes: (required)
        :rtype: ResponseDataObjectListGeneValueObject
        """
        return self.raw.get_genes(genes, **kwargs)

    def get_platform_datasets(self, platform, **kwargs):  # noqa: E501
        """Retrieve all experiments within a given platform

        :param str platform: (required)
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :rtype: PaginatedResponseDataObjectExpressionExperimentValueObject
        """
        return self.raw.get_platform_datasets(platform, **kwargs)

    def get_platform_element_genes(self, platform, probe, **kwargs):  # noqa: E501
        """Retrieve the genes associated to a probe in a given platform

        :param str platform: (required)
        :param str probe: (required)
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :rtype: PaginatedResponseDataObjectGeneValueObject
        """
        return self.raw.get_platform_element_genes(platform, probe, **kwargs)

    def get_platforms_by_ids(self, platform, **kwargs):  # noqa: E501
        """Retrieve all platforms matching a set of platform identifiers

        :param list[str] platform: (required)
        :param str filter: Filter results by matching the expression
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :param str sort: Order results by the given property and direction. The '+'
          sign indicate ascending order whereas the '-' indicate descending.
        :rtype: PaginatedResponseDataObjectArrayDesignValueObject
        """
        return self.raw.get_platforms_by_ids(platform, **kwargs)



    def get_result_set_factors(self, result_set, **kwargs):
        """Retrieve a single analysis result set by its identifier with Factors

        :param int result_set: (required)
        :return: DataFrame
        """
        api_response = self.raw.get_result_set(result_set, **kwargs)
        df = pandas.DataFrame(columns=['id', 'factorValue', 'category'])
        for f in api_response.data.experimental_factors:            
            for v in f.values:
                row = pandas.DataFrame([{'id':v.id, 'factorValue':v.factor_value, 'category':v.category}])
                df = pandas.concat([df,row],
                               ignore_index=True)
        return df




    def search_datasets(self, query, taxon, **kwargs):
        """Retrieve datasets within a given taxa associated to an annotation tags search

        :param str taxon: (required)
        :param list[str] query: (required)
        :param str filter: Filter results by matching the expression
        :param int offset: The offset of the first retrieved result
        :param int limit: Limit the number of results retrieved
        :param str sort: Order results by the given property and direction. The '+'
          sign indicate ascending order whereas the '-' indicate descending.
        :rtype: PaginatedResponseDataObjectExpressionExperimentValueObject
        """
        return self.raw.search_taxon_datasets(taxon, query=query, **kwargs)

# Below are "Convenience" (combination) functions
    def get_dataset_object(self, dataset, **kwargs):
        """Combines various endpoint calls to return an annotated data object
        of the queried dataset, including expression data and the experimental
        design.

        :param str dataset: (required)
        :return: AnnData class object
        """

        exM = self.get_dataset_processed_expression(dataset, **kwargs)
        des = self.get_dataset_design(dataset, **kwargs)
        mdata = self.get_datasets_by_ids([dataset], **kwargs)

        # condition expr. data: add index
        exM.index = exM["Probe"]

        # genes metadata: extract description columns
        try:
            genes = exM[['GeneSymbol', 'GeneName', 'NCBIid']]
        except KeyError:
            logger.warning("WARNING: One or more gene descriptions are missing in Expression table")
            genes = None

        # compile metadata
        mda = {
            'title' : mdata.data[0].name,
            'abstract' : mdata.data[0].description,
            'url' : 'https://gemma.msl.ubc.ca/expressionExperiment/showExpressionExperiment.html?id='+str(mdata.data[0].id),
            'database' : mdata.data[0].external_database,
            'accession' : mdata.data[0].accession,
            'GemmaQualityScore' : mdata.data[0].geeq.public_quality_score,
            'GemmaSuitabilityScore' : mdata.data[0].geeq.public_suitability_score,
            'taxon' : mdata.data[0].taxon
        }

        # final touch
        des = des.filter(items = exM.columns, axis = 0)
        
        
        assert set(des.index) < set(exM.columns), 'Err2' # design rows is subset of exM columns
        exM = exM[des.index]

        # make AnnData object
        adata = anndata.AnnData(exM, dtype=numpy.float32)
        if not (genes is None):
            adata.obs = adata.obs.join(genes)
        adata.var = adata.var.join(des)
        adata.uns = mda

        return adata

    def get_differential_expression_values(self, dataset = None, resultSet = None, readableContrasts = False, **kwargs):
        """Retrieves the differential expression resultSet(s) associated with the dataset.
        If there is more than one resultSet, use get_result_sets() to see the options
        and get the ID you want. Alternatively, you can query the resultSet directly
        if you know its ID beforehand.

        :param str dataset: (optional)
        :param int resultSet: (optional)
        :param bool readableContrasts: (optional) If False (default), the returned columns
          will use internal constrasts IDs as names. Details about the contrasts can be
          accessed using get_dataset_differential_expression_analyses(). If True IDs
          will be replaced with human readable contrast information.
        :return: list[DataFrame]
        """
        if dataset is not None and resultSet is not None:
            rss = self.get_result_sets(dataset)
            if not resultSet in rss['resultSet.id'].values:
                logger.warning('The queried resultSet is not derived from this dataset. ' 
                               'Check the available resultSets with "get_result_sets()" '
                               'or query without the dataset parameter.')
                return
            resultSet = [resultSet,]
        elif dataset is not None and resultSet is None:
            rss = self.get_result_sets(dataset)
            resultSet = rss['resultSet.id'].unique()
        elif dataset is None and resultSet is not None:
            resultSet = [resultSet,]
        else:
            print("stop")
            return

        rss = {}
        for rs in resultSet:
            df = self.get_result_set(rs)
            if readableContrasts:
                fact = self.get_result_set_factors(rs)
                cols = [s.replace('log2fc','logFoldChange') for s in df.columns]
                for i in range(fact.shape[0]):
                    cols = [s.replace(str(fact.loc[i,'id']),fact.loc[i,'factorValue']) for s in cols]
                df.columns = cols
            rss[rs] = df

        return rss

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
        return pandas.read_csv(StringIO(api_response), sep='\t')

    def get_taxa(self, **kwargs):  # noqa: E501
        """Retrieve all available taxa

        :rtype: ResponseDataObjectListTaxonValueObject
        """
        return self.raw.get_taxa(**kwargs)

    def get_taxon_datasets(self, taxon, **kwargs):  # noqa: E501
        """Retrieve the datasets for a given taxon

        :param str/int taxon: (required)

        **taxon** can either be Taxon ID, Taxon NCBI ID, or one of its
        string identifiers: scientific name, common name. It is
        recommended to use Taxon ID for efficiency. Please note, that
        not all taxa have all the possible identifiers available. Use
        the get_taxa_by_ids function to retrieve the necessary
        information. For convenience, below is a list of officially
        supported taxa:

        ==  =========   ======================== ==========
        ID  Comm.name   Scient.name              NcbiID
        ==  =========   ======================== ==========
        1   human       Homo sapiens             9606
        2   mouse       Mus musculus             10090
        3   rat         Rattus norvegicus        10116
        11  yeast       Saccharomyces cerevisiae 4932
        12  zebrafish   Danio rerio              7955
        13  fly         Drosophila melanogaster  7227
        14  worm        Caenorhabditis elegans   6239
        ==  =========   ======================== ==========

        :param str filter:
        :param int offset:
        :param int limit:
        :param str sort:
        :rtype: PaginatedResponseDataObjectExpressionExperimentValueObject
        """
        return self.raw.get_taxon_datasets(taxon, **kwargs)

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
        with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
            print(de_up[:10])

        de_dn = de[de['diffexpr']=='Down']
        de_dn = de_dn[['Probe','GeneSymbol', 'contrast_bipolar disorder, manic phase_pvalue',
                       'contrast_bipolar disorder, manic phase_logFoldChange']].sort_values(
                'contrast_bipolar disorder, manic phase_pvalue')
        print('\nDownregulated probes')
        with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
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
