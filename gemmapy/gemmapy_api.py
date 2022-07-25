# coding: utf-8
"""
Gemma python API (https://gemma.msl.ubc.ca/rest/v2/)
"""

import logging
from   gemmapy import sdk
import pandas
import numpy
import anndata
from io import StringIO

logger = logging.getLogger(__name__)

class GemmaPy(object):
    """
    Main API class
    """

    def __init__(self, api_client=None):
        configuration = sdk.Configuration()
        configuration.host = 'dev.gemma.msl.ubc.ca/rest/v2'

        # create an instance of the API class
        self.api = sdk.DefaultApi(sdk.ApiClient(configuration))

    def getDatasetAnnotations(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the annotations analysis of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getDatasetAnnotations(dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: (required)
        :return: ResponseDataObjectSetAnnotationValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_dataset_annotations(dataset, **kwargs)

    def getDatasetDesign(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the design of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getDatasetDesign(dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: (required)
        :return: DataFrame
                 If the method is called asynchronously,
                 returns the request thread.
        """
        api_response = self.api.get_dataset_design(dataset, **kwargs)
        df = pandas.read_csv(StringIO(api_response), sep='\t', comment='#')

        # conditioning: fix Bioassay names, add them index, remove redundant columns
        rowall = [c[c.find('Name=')+5:] for c in df['Bioassay'] if c.find('Name=') >= 0]
        assert len(rowall) == df.shape[0], 'Err1'
        df.index = rowall

        return df.drop(columns=['Bioassay', 'ExternalID'], errors='ignore')

    def getDatasetDEA(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the differential analyses of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getDatasetDEA(dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: (required)
        :param int offset:
        :param int limit:
        :return: ResponseDataObjectListDifferentialExpressionAnalysisValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_dataset_differential_expression_analyses(dataset, **kwargs)

    def getDatasetExpression(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the expression data of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getDatasetExpression(dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: (required)
        :param bool filter:
        :return: DataFrame
                 If the method is called asynchronously,
                 returns the request thread.
        """
        api_response = self.api.get_dataset_expression(dataset, **kwargs)
        df = pandas.read_csv(StringIO(api_response), sep='\t', comment='#', dtype={'Probe':'str'})

        # conditioning: fix names and remove redundant columns
        df = df.drop(columns=['Sequence', 'GemmaId'], errors='ignore')
        df.columns = [c if c.find('Name=') < 0 else c[c.find('Name=')+5:] for c in df.columns]
        return df


    def getDatasetPlatforms(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the platform of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getDatasetPlatforms(dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: (required)
        :return: ResponseDataObjectListArrayDesignValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_dataset_platforms(dataset, **kwargs)

    def getDatasetSamples(self, dataset, **kwargs):  # noqa: E501
        """Retrieve the samples of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getDatasetSamples(dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: (required)
        :param list[str] factor_values:
        :return: ResponseDataObjectListBioAssayValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_dataset_samples(dataset, **kwargs)

    def getDatasetsInfo(self, dataset, **kwargs):  # noqa: E501
        """Retrieve datasets by their identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getDatasetsInfo(dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] dataset: (required)
        :param str filter:
        :param int offset:
        :param int limit:
        :param str sort:
        :return: PaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_datasets_by_ids(dataset, **kwargs)

    def getGeneGO(self, gene, **kwargs):  # noqa: E501
        """Retrieve the GO terms associated to a gene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getGeneGO(gene, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gene: (required)
        :return: ResponseDataObjectListGeneOntologyTermValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_gene_go_terms(gene, **kwargs)

    def getGeneLocation(self, gene, **kwargs):  # noqa: E501
        """Retrieve the physical locations of a given gene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getGeneLocation(gene, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gene: (required)
        :return: ResponseDataObjectListPhysicalLocationValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_gene_locations(gene, **kwargs)

    def getGeneProbes(self, gene, **kwargs):  # noqa: E501
        """Retrieve the probes associated to a genes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getGeneProbes(gene, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gene: (required)
        :param int offset:
        :param int limit:
        :return: PaginatedResponseDataObjectCompositeSequenceValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_gene_probes(gene, **kwargs)

    def getGenesInfo(self, genes, **kwargs):  # noqa: E501
        """Retrieve genes matching a gene identifier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getGenesInfo(genes, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] genes: (required)
        :return: ResponseDataObjectListGeneValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_genes(genes, **kwargs)

    def getPlatformDatasets(self, platform, **kwargs):  # noqa: E501
        """Retrieve all experiments within a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getPlatformDatasets(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str/int platform: (required)
        :param int offset:
        :param int limit:
        :return: PaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_platform_datasets(platform, **kwargs)

    def getPlatformElements(self, platform, probes, **kwargs):  # noqa: E501
        """Retrieve the selected composite sequences for a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getPlatformElements(platform, probes, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str/int platform: (required)
        :param list[str] probes: (required)
        :param int offset:
        :param int limit:
        :return: PaginatedResponseDataObjectCompositeSequenceValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_platform_element(platform, probes, **kwargs)

    def getPlatformElementGenes(self, platform, probe, **kwargs):  # noqa: E501
        """Retrieve the genes associated to a probe in a given platform  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getPlatformElementGenes(platform, probe, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str/int platform: (required)
        :param str probe: (required)
        :param int offset:
        :param int limit:
        :return: PaginatedResponseDataObjectGeneValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_platform_element_genes(platform, probe, **kwargs)

    def getPlatformsInfo(self, platform, **kwargs):  # noqa: E501
        """Retrieve all platforms matching a set of platform identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getPlatformsInfo(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str/int] platform: (required)
        :param str filter:
        :param int offset:
        :param int limit:
        :param str sort:
        :return: PaginatedResponseDataObjectArrayDesignValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.get_platforms_by_ids(platform, **kwargs)

    def getResultSets(self, result_set, **kwargs):  # noqa: E501
        """Retrieve a single analysis result set by its identifier  # noqa: E501

        :param int result_set: (required)
        :return: DataFrame
        """
        api_response = self.api.get_result_set_as_tsv(result_set, **kwargs)
        df = pandas.read_csv(StringIO(api_response), sep='\t', comment='#')
        df = df.drop(columns=['id','probe_id','gene_id','gene_name'], errors='ignore')
        df = df.rename(columns={'probe_name':'Probe','gene_official_symbol':'GeneSymbol',
                                'gene_official_name':'GeneName','gene_ncbi_id':'NCBIid'})
        return df

    def getResultSetsFactors(self, result_set, **kwargs):
        """Retrieve a single analysis result set by its identifier with Factors  # noqa: E501

        :param int result_set: (required)
        :return: DataFrame
        """
        api_response = self.api.get_result_set(result_set, **kwargs)
        df = pandas.DataFrame(columns=['id', 'factorValue', 'category'])
        for f in api_response.data.experimental_factors:
            for v in f.values:
                df = df.append({'id':v.id, 'factorValue':v.factor_value, 'category':v.category},
                               ignore_index=True)
        return df

    def getDatasetResultSets(self, dataset, **kwargs):  # noqa: E501
        """Retrieve all result sets matching the provided criteria  # noqa: E501

        :param str dataset
        :return: DataFrame
        """
        rs = self.api.get_result_sets(datasets=[dataset], **kwargs)
        df = pandas.DataFrame(columns=['resultSet.id','factor.category','factor.level'])
        for d in rs.data:
            cate = ' x '.join(f.category for f in d.experimental_factors)
            leve = '; '.join(f.description for f in d.experimental_factors)
            df = df.append({'resultSet.id': d.id,
                            'factor.category': cate,
                            'factor.level': leve}, ignore_index=True)
        return df

    def searchAnnotations(self, query, **kwargs):  # noqa: E501
        """Search for annotation tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.searchAnnotations(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] query: (required)
        :return: ResponseDataObjectListAnnotationSearchResultValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.search_annotations(query, **kwargs)

    def searchDatasets(self, query, taxon, **kwargs):
        """Retrieve datasets within a given taxa associated to an annotation tags search

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_taxon_datasets(taxon, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Taxon taxon: (required)
        :param list[str] query: (required)
        :param str filter:
        :param int offset:
        :param int limit:
        :param str sort:
        :return: PaginatedResponseDataObjectExpressionExperimentValueObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.api.search_taxon_datasets(taxon, query, **kwargs)

# Below are "Convenience" (combination) functions
    def getDataset(self, dataset, **kwargs):
        """Combines various endpoint calls to return an annotated data object
        of the queried dataset, including expression data and the experimental
        design.

        :param str dataset: (required)
        :return: AnnData class object
        """

        exM = self.getDatasetExpression(dataset, **kwargs)
        des = self.getDatasetDesign(dataset, **kwargs)
        mdata = self.getDatasetsInfo([dataset], **kwargs)

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
        assert set(des.index) < set(exM.columns), 'Err2' # design rows is subset of exM columns
        exM = exM[des.index]

        # make AnnData object
        adata = anndata.AnnData(exM, dtype=numpy.float32)
        if not (genes is None):
            adata.obs = adata.obs.join(genes)
        adata.var = adata.var.join(des)
        adata.uns = mda

        return adata

    def getDatasetDE(self, dataset = None, resultSet = None, all = False, **kwargs):
        """Retrieves the differential expression resultSet(s) associated with the dataset.
        If there is more than one resultSet, use getDatasetResultSets() to see the options
        and get the ID you want. Alternatively, you can query the resultSet directly
        if you know its ID beforehand.

        :param str dataset: (optional)
        :param int resultSet: (optional)
        :param bool all: (optional, default is False; If True, will download all differential
               expression resultSets for the dataset.)
        :return: list[DataFrame] or DataFrame (if there is the list has only 1 element)
        """
        if dataset is not None and resultSet is not None:
            rss = self.getDatasetResultSets(dataset)
            if not resultSet in rss['resultSet.id'].values:
                logger.warning('The queried resultSet is not derived from this dataset. ' 
                               'Check the available resultSets with "getDatasetResultSets()" '
                               'or query without the dataset parameter.')
                return
            resultSet = [resultSet,]
        elif dataset is not None and resultSet is None:
            rss = self.getDatasetResultSets(dataset)
            if rss.shape[0] > 1 and all == False:
                logger.warning('There are multiple resultSets for this dataset. '
                               'Check the available resultSets with "getDatasetResultSets()" or choose all = TRUE')
                return
            elif rss.shape[0] > 1 and all == True:
                resultSet = rss['resultSet.id'].unique()
            else:
                resultSet = rss['resultSet.id']
        elif dataset is None and resultSet is not None:
            resultSet = [resultSet,]
        else:
            print("stop")
            return

        rss = []
        for rs in resultSet:
            df = self.getResultSets(rs)
            fact = self.getResultSetsFactors(rs)
            cols = [s.replace('log2fc','logFoldChange') for s in df.columns]
            for i in range(fact.shape[0]):
                cols = [s.replace(str(fact.loc[i,'id']),fact.loc[i,'factorValue']) for s in cols]
            df.columns = cols
            rss.append(df)

        if len(rss) == 1: rss = rss[0]
        return rss

    # Corresponding gemma.R function doesn't use any endpoint (uses some alternative URL
    # to get info) but has several options allowing to select the ann. type:
    # annotType = c("bioProcess", "noParents", "allParents")
    # This feature is not implemented here, the return value corresponds to "noParents"
    # (as of 2022-05-19)
    def getPlatformAnnotation(self, platform, **kwargs):
        """Retrieve the annotations of a given platform  # noqa: E501

        :param str/int platform: (required)
        :return: DataFrame
        """
        api_response = self.api.get_platform_annotations(platform, **kwargs)
        return pandas.read_csv(StringIO(api_response), sep='\t', comment='#')

# Tests
if __name__ == '__main__':
    # dv temp
    import http.client
    http.client.HTTPConnection.debuglevel = 0 # put 5 to debug

    import sys
    from pprint import pprint

    api_instance = GemmaPy()

    def getDatasetAnnotations_test():
        print('Testing getDatasetAnnotations function:')
        api_response = api_instance.getDatasetAnnotations("GSE46416")
        pprint(api_response.data)
        print('')

    def searchDatasets_test():
        print('Testing searchDatasets function:')
        api_response = api_instance.searchDatasets(["bipolar"], taxon="human", limit=100)
        for d in api_response.data:
            if d.geeq is not None and  d.geeq.batch_corrected:
                print(d.short_name, d.name, d.bio_assay_count)
        print('')

    def getDatasetsInfo_test():
        print('Testing getDatasetsInfo function:')
        api_response = api_instance.getDatasetsInfo(["GSE46416"])
        for d in api_response.data:
            print(d.short_name, d.name, d.id, d.description)
        print('')

    def searchAnnotations_test():
        print('Testing searchAnnotations function:')
        api_response = api_instance.searchAnnotations(["GSE46416"])
        print(api_response.data)

    def getDataset_test():
        print('Testing getDataset function:')
        adata = api_instance.getDataset("GSE46416")
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

    def getDatasetResultSets_test():
        print('Testing getDatasetResultSets function:')
        df = api_instance.getDatasetResultSets('GSE6711')
        print(df)
        df2 = api_instance.getResultSets(485406)
        print(df2)

    def getDatasetDE_test():
        de = api_instance.getDatasetDE('GSE46416')
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

    def getPlatformAnnotation_test():
        print('Testing getPlatformAnnotation function')
        df = api_instance.getPlatformAnnotation('GPL96')
        print(df)

    if len(sys.argv) > 1:
        fname = sys.argv[1]
        dict = vars()
        if fname in dict:
            #print("Calling",fname)
            func = dict[fname]
            func()

    #df2 = api_instance.getResultSets(423177)
    #df2 = api_instance.getResultSetsFactors(423177)
    #df2 = api_instance.getDatasetDE(None,423177)
    #df2 = api_instance.getDatasetDE(None,485406)
    #obj = api_instance.api.get_platforms_by_ids(['GPL96'])
    #df2 = api_instance.getPlatformAnnotation('GPL96')
    #df2 = api_instance.getPlatformsInfo(['GPL96'])
    #print(df2)
