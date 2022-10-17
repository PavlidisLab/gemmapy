
Accessing curated gene expression data with GemmaPy
===================================================

..
 | *Dima Vavilov*, *Guillaume Poirier-Morency*
 | *Michael Smith Laboratories, University of British Columbia, Vancouver, Canada*


About Gemma
-----------

`Gemma <https://gemma.msl.ubc.ca/>`_ is a web site, database and a set
of tools for the meta-analysis, re-use and sharing of genomics data,
currently primarily targeted at the analysis of gene expression
profiles.  Gemma contains data from thousands of public studies,
referencing thousands of published papers.  Every dataset in Gemma has
passed a rigorous curation process that re-annotates the expression
platform at the sequence level, which allows for more consistent
cross-platform comparisons and meta-analyses.

For detailed information on the curation process, read this `page
<https://pavlidislab.github.io/Gemma/curation.html>`_ or the latest
`publication
<https://academic.oup.com/database/article/doi/10.1093/database/baab006/6143045>`_.


Installation instructions
-------------------------

.. include:: install.rst


Additional packages
-------------------

For the purpose of making plots in this tutorial the following packages should be installed
and imported: :code:`matplotlib`, :code:`plotnine`.


Downloading expression data
---------------------------

The main goal of this wrapper is to enable easy access to Gemma's curated
datasets for downstream analyses or meta-analyses combining multiple
datasets.  In this example, we want to find datasets that are associated
with bipolar disorder, and we are only interested in human data.  In
addition, we will subset our results to datasets that have been batch
corrected.

>>> import gemmapy
>>> api_instance = gemmapy.GemmaPy()
>>> api_response = api_instance.search_datasets(["bipolar"], taxon="human", limit=100)
>>> api_response.data[0]  # view the object structure
>>> for d in api_response.data:
...   if d.geeq is not None and  d.geeq.batch_corrected:
...     print(d.short_name, d.name, d.bio_assay_count)
... 
GSE35974 Expression data from the human cerebellum brain 144
GSE46416 State- and trait-specific gene expression in euthymia and mania 32

We are left with two datasets. For simplicity, we'll pick 
`GSE46416 <https://gemma.msl.ubc.ca/expressionExperiment/showExpressionExperiment.html?id=8997>`_
since it has the smaller number of samples. Now that we have the ID
for our experiment, we can fetch the data associated with it.

>>> api_response = api_instance.get_datasets_by_ids(["GSE46416"])
>>> for d in api_response.data:
...   print(d.short_name, d.name, d.id)
... 
GSE46416 State- and trait-specific gene expression in euthymia and mania 8997 
>>> print(d.description)
Gene expression profiles of bipolar disorder (BD) patients were assessed during both a manic and a euthymic phase and compared both intra-individually, and with the gene expression profiles of controls.
Last Updated (by provider): Sep 05 2014
Contributors:  Christian C Witt Benedikt Brors Dilafruz Juraeva Jens Treutlein Carsten Sticht Stephanie H Witt Jana Strohmaier Helene Dukal Josef Frank Franziska Degenhardt Markus M Nöthen Sven Cichon Maren Lang Marcella Rietschel Sandra Meier Manuel Mattheisen

To access the expression data in a convenient form, you can use
:py:func:`~gemmapy.GemmaPy.get_dataset_object`. It is a high-level wrapper
that combines various endpoint calls to return an `anndata
<https://anndata.readthedocs.io/>`_ (Annotated Data) object of the
queried dataset for downstream analyses. They include the expression
matrix along with the experimental design, and ensure the sample names
match between both when transforming/subsetting data.

>>> adata = api_instance.get_dataset_object("GSE46416")
>>> print(adata)
AnnData object with n_obs × n_vars = 21986 × 32
    obs: 'GeneSymbol', 'GeneName', 'NCBIid'
    var: 'batch', 'disease'
    uns: 'title', 'abstract', 'url', 'database', 'accession', 'GemmaQualityScore', 'GemmaSuitabilityScore', 'taxon'

To show how subsetting works, we'll keep the manic phase data and the
:code:`reference_subject_role`\s, which refers to the control samples in Gemma
datasets.

>>> # Check the levels of the disease factor
>>> adata.var['disease'].unique()
array(['reference_subject_role', 'euthymic_phase_|_Bipolar_Disorder_|',
       'bipolar_disorder_|_manic_phase_|'], dtype=object)

>>> # Subset patients during manic phase and controls
>>> manic=adata[:,(adata.var['disease'] == 'reference_subject_role') |
...               (adata.var['disease'] == 'bipolar_disorder_|_manic_phase_|')].copy()
>>> print(manic)
AnnData object with n_obs × n_vars = 21986 × 21
    obs: 'GeneSymbol', 'GeneName', 'NCBIid'
    var: 'batch', 'disease'
    uns: 'title', 'abstract', 'url', 'database', 'accession', 'GemmaQualityScore', 'GemmaSuitabilityScore', 'taxon'
>>> print(manic.var)
                                                 batch                           disease
Control,1_DE50                       Batch_05_24/11/10            reference_subject_role
Control,12                           Batch_02_26/11/09            reference_subject_role
Control,9                            Batch_01_25/11/09            reference_subject_role
Bipolardisorderpatientmanicphase,5   Batch_05_24/11/10  bipolar_disorder_|_manic_phase_|
Control,15                           Batch_02_26/11/09            reference_subject_role
Bipolardisorderpatientmanicphase,31  Batch_04_02/12/09  bipolar_disorder_|_manic_phase_|
Bipolardisorderpatientmanicphase,29  Batch_03_27/11/09  bipolar_disorder_|_manic_phase_|
Bipolardisorderpatientmanicphase,35  Batch_04_02/12/09  bipolar_disorder_|_manic_phase_|
Bipolardisorderpatientmanicphase,18  Batch_02_26/11/09  bipolar_disorder_|_manic_phase_|
Control,8                            Batch_01_25/11/09            reference_subject_role
Control,3                            Batch_05_24/11/10            reference_subject_role
Control,2_DE23                       Batch_05_24/11/10            reference_subject_role
Control,2_DE40                       Batch_01_25/11/09            reference_subject_role
Bipolardisorderpatientmanicphase,33  Batch_04_02/12/09  bipolar_disorder_|_manic_phase_|
Control,4                            Batch_05_24/11/10            reference_subject_role
Control,1_DE62                       Batch_01_25/11/09            reference_subject_role
Bipolardisorderpatientmanicphase,10  Batch_01_25/11/09  bipolar_disorder_|_manic_phase_|
Bipolardisorderpatientmanicphase,37  Batch_04_02/12/09  bipolar_disorder_|_manic_phase_|
Bipolardisorderpatientmanicphase,23  Batch_03_27/11/09  bipolar_disorder_|_manic_phase_|
Bipolardisorderpatientmanicphase,16  Batch_02_26/11/09  bipolar_disorder_|_manic_phase_|
Bipolardisorderpatientmanicphase,21  Batch_03_27/11/09  bipolar_disorder_|_manic_phase_|

Let's check the expression for every sample to make sure they look OK:

>>> # Plot Expression matrix
>>> import matplotlib.pyplot as plt
>>> plt.figure(figsize=(10,6))
>>> plt.boxplot(manic.X, sym='.')
>>> plt.xticks([])
>>> plt.xlabel('Samples')
>>> plt.ylabel('Expression')
>>> plt.savefig('ded.png')

.. image:: _static/ded.png
   :align: left
   :width: 100%

Gene expression distributions of bipolar patients during manic phase and controls.

You can also use :py:func:`~gemmapy.GemmaPy.get_dataset_expression` to only get the expression 
matrix, and :py:func:`~gemmapy.GemmaPy.get_dataset_design` to get the experimental design matrix.

Differential expression analyses
--------------------------------

Gemma contains precomputed differential expression analyses for most
of its datasets. Analyses can involve more than one factor, such as
"sex" as well as "disease". Some datasets contain more than one
analysis to account for different factors and their interactions. The
results are stored as resultSets, each corresponding to one factor (or
their interaction). You can access them using
:py:func:`~gemmapy.GemmaPy.get_differential_expression_values`. From here on, we can
explore and visualize the data to find the most
differentially-expressed genes:

>>> import gemmapy
>>> import pandas
>>> import numpy as np
>>> api_instance = gemmapy.GemmaPy()
>>> de = api_instance.get_differential_expression_values('GSE46416', readableContrasts=True)
>>> de = de[0]
...
>>> # Classify probes for plotting
>>> de['diffexpr'] = 'No'   # add extra column
>>> de.loc[(de['contrast_bipolar disorder, manic phase_logFoldChange'] > 1.0) &
...        (de['contrast_bipolar disorder, manic phase_pvalue'] < 0.05),'diffexpr'] = 'Up'
>>> de.loc[(de['contrast_bipolar disorder, manic phase_logFoldChange'] < -1.0) &
...        (de['contrast_bipolar disorder, manic phase_pvalue'] < 0.05),'diffexpr'] = 'Down'
...
>>> # Upregulated probes
>>> de_up = de[de['diffexpr']=='Up']
>>> de_up = de_up[['Probe','GeneSymbol', 'contrast_bipolar disorder, manic phase_pvalue',
...         'contrast_bipolar disorder, manic phase_logFoldChange']].sort_values(
...         'contrast_bipolar disorder, manic phase_pvalue')
>>> with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
...         print(de_up[:10])
         Probe GeneSymbol  contrast_bipolar disorder, manic phase_pvalue  \
18835  2319550       RBP7                                       0.000086   
4913   2548699     CYP1B1                                       0.000103   
11877  3907190       SLPI                                       0.000333   
6917   3629103      PCLAF                                       0.000518   
6188   3545525      SLIRP                                       0.000565   
2065   3146433      COX6C                                       0.000920   
4839   2538349        NaN                                       0.001253   
407    2899102       H3C3                                       0.001269   
18009  3635198     BCL2A1                                       0.001800   
18588  2633191      GPR15                                       0.002410   
       contrast_bipolar disorder, manic phase_logFoldChange  
18835                                              1.074     
4913                                               1.322     
11877                                              1.056     
6917                                               1.278     
6188                                               1.349     
2065                                               1.467     
4839                                               1.073     
407                                                1.026     
18009                                              1.080     
18588                                              1.205     

>>> # Downregulated probes
>>> de_dn = de[de['diffexpr']=='Down']
>>> de_dn = de_dn[['Probe','GeneSymbol', 'contrast_bipolar disorder, manic phase_pvalue',
>>>         'contrast_bipolar disorder, manic phase_logFoldChange']].sort_values(
>>>         'contrast_bipolar disorder, manic phase_pvalue')
>>> with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
...         print(de_dn[:10])
         Probe GeneSymbol  contrast_bipolar disorder, manic phase_pvalue  \
18856  2775390        NaN                                       0.000002   
5641   3760268        NaN                                       0.000012   
18194  3124344        NaN                                       0.000139   
1742   3673179        NaN                                       0.000158   
10623  3245871      WDFY4                                       0.000168   
15046  3022689   SND1-IT1                                       0.000227   
9240   2679014        NaN                                       0.000298   
499    4019758        NaN                                       0.000355   
526    3336402      RBM14                                       0.000361   
9901   2880955        NaN                                       0.000374   
       contrast_bipolar disorder, manic phase_logFoldChange  
18856                                             -1.556     
5641                                              -1.851     
18194                                             -1.037     
1742                                              -1.034     
10623                                             -1.157     
15046                                             -1.220     
9240                                              -1.175     
499                                               -1.405     
526                                               -1.071     
9901                                              -1.522     

>>> # Add gene symbols as labels to DE genes
>>> de['delabel'] = ''
>>> de.loc[de['diffexpr']!='No','delabel'] = de.loc[de['diffexpr']!='No','GeneSymbol']
...
>>> # Volcano plot for bipolar patients vs controls
>>> de['-log10(p-value)'] = -np.log10(de['contrast_bipolar disorder, manic phase_pvalue'])
>>> import matplotlib.pyplot as plt
>>> from plotnine import *
>>> plt.figure(figsize=(10,6))
>>> plot=(ggplot(de)
... +aes(
...     x='contrast_bipolar disorder, manic phase_logFoldChange',
...     y='-log10(p-value)',
...     color='diffexpr',
...     labels='delabel'
... )
... +geom_point()
... +geom_hline(yintercept = -np.log10(0.05), color = "gray", linetype = "dashed")
... +geom_vline(xintercept = (-1.0, 1.0), color = "gray", linetype = "dashed")
... +labs(x = "log2(FoldChange)", y = "-log10(p-value)")
... +scale_color_manual(values = ("blue", "black", "red"))+theme_minimal())
... 
>>> plot.save('dea.png', height=6, width=10)

.. image:: _static/dea.png

Differentially-expressed genes in bipolar patients during manic phase versus controls.

Platform Annotations
--------------------

Expression data in Gemma comes with annotations for the gene each
expression profile corresponds to. Using the
:py:func:`~gemmapy.GemmaPy.get_platform_annotations` function, these
annotations can be retrieved independently of the expression data,
along with additional annotations such as Gene Ontology terms.

Examples:

>>> import gemmapy
>>> import pandas
>>> api_instance = gemmapy.GemmaPy()
>>> api_response = api_instance.get_platform_annotations('GPL96')
>>> with pandas.option_context('display.max_rows', None, 'display.max_columns', None): print(api_response[:6])
     ProbeName    GeneSymbols                                      GeneNames  \
0  211750_x_at  TUBA1A|TUBA1C              tubulin alpha 1a|tubulin alpha 1c   
1    216678_at            NaN                                            NaN   
2    216345_at         ZSWIM8             zinc finger SWIM-type containing 8   
3    207273_at            NaN                                            NaN   
4  216025_x_at         CYP2C9  cytochrome P450 family 2 subfamily C member 9   
5  218191_s_at         LMBRD1                      LMBR1 domain containing 1   
                                             GOTerms       GemmaIDs  \
0  GO:0005737|GO:0000166|GO:0051234|GO:0005856|GO...  172797|360802   
1                                                NaN            NaN   
2  GO:0043170|GO:1990234|GO:0044260|GO:0050789|GO...         235733   
3                                                NaN            NaN   
4  GO:0005737|GO:0072330|GO:0008203|GO:0008202|GO...          32964   
5  GO:0043170|GO:0016192|GO:0051234|GO:0044260|GO...         303717   
      NCBIids  
0  7846|84790  
1         NaN  
2       23053  
3         NaN  
4        1559  
5       55788  

>>> api_response = api_instance.get_platform_annotations('Generic_human')
>>> with pandas.option_context('display.max_rows', None, 'display.max_columns', None): print(api_response[:6])
      ProbeName   GeneSymbols  \
0         LCN10         LCN10   
1      STAG3L5P      STAG3L5P   
2  LOC101059976  LOC101059976   
3          GAB3          GAB3   
4  LOC100287155  LOC100287155   
5        RASSF2        RASSF2   
                                           GeneNames  \
0                                       lipocalin 10   
1                stromal antigen 3-like 5 pseudogene   
2  arf-GAP with GTPase, ANK repeat and PH domain-...   
3                  GRB2 associated binding protein 3   
4                  hypothetical protein LOC100287155   
5             Ras association domain family member 2   
                                             GOTerms GemmaIDs    NCBIids  
0        GO:0005576|GO:0005488|GO:0110165|GO:0036094   441399     414332  
1                                                NaN  8799043  101735302  
2                                                NaN  8779607  101059976  
3  GO:0002573|GO:0032502|GO:0030225|GO:0002521|GO...   389635     139716  
4                                                NaN  8090381  100287155  
5  GO:0048585|GO:0005737|GO:0043170|GO:0048584|GO...   201914       9770  

If you are interested in a particular gene, you can see which
platforms include it using
:py:func:`~gemmapy.GemmaPy.get_gene_probes`. Note that functions to
search gene work best with unambigious identifiers rather than symbols.

>>> # lists genes in gemma matching the symbol or identifier
>>> api_response = api_instance.get_genes(['Eno2'])
>>> api_response.data[0] # view the object structure
>>> for d in api_response.data: print("%s %-18s %6d %-30s %-10s %2i %s" %
>>>   (d.official_symbol,d.ensembl_id,d.ncbi_id,d.official_name,
>>>    d.taxon.common_name,d.taxon.id,d.taxon.scientific_name))
... 
ENO2 ENSG00000111674      2026 enolase 2                      human       1 Homo sapiens
Eno2 ENSMUSG00000004267  13807 enolase 2, gamma neuronal      mouse       2 Mus musculus
Eno2 ENSRNOG00000013141  24334 enolase 2                      rat         3 Rattus norvegicus
ENO2 None               856579 phosphopyruvate hydratase ENO2 yeast      11 Saccharomyces cerevisiae
eno2 ENSDARG00000014287 402874 enolase 2                      zebrafish  12 Danio rerio


>>> # ncbi id for human ENO2
>>> probs=api_instance.get_gene_probes(2026)
>>> probs.data[0]  # view the object structure
>>> # print only fields of interest
>>> for d in probs.data[0:6]: 
...   print("%-10s %-12s %-20s %s %s %s %s" % 
...  (d.name,d.array_design.short_name,d.array_design.name,d.array_design.taxon.common_name,
...   d.array_design.taxon.id,d.array_design.technology_type,d.array_design.troubled))
20016      GPL3093      LC-25                human 1 TWOCOLOR False
20024      GPL3092      LC-19                human 1 TWOCOLOR False
20024      lymphochip-2 Lymphochip 37k       human 1 TWOCOLOR False
1639       GPL962       CHUGAI 41K           human 1 TWOCOLOR False
35850      NHGRI-6.5k   NHGRI-6.5k           human 1 TWOCOLOR False
201313_at  GPL96        Affymetrix GeneChip Human Genome U133 Array Set HG-U133A human 1 ONECOLOR False


Larger queries
--------------

Some endpoints accept multiple identifiers in a single
function call. For example, getting information on 2 datasets at the
same time.

>>> import gemmapy
>>> api_instance = gemmapy.GemmaPy()
>>> api_response = api_instance.get_datasets_by_ids(["GSE35974","GSE46416"])
>>> api_response.data[0]  # view the object structure
>>> for d in api_response.data:
...   print(d.short_name, d.name, d.id, d.accession, d.bio_assay_count, d.taxon.common_name)
... 
GSE35974 Expression data from the human cerebellum brain 5939 GSE35974 144 human
GSE46416 State- and trait-specific gene expression in euthymia and mania 8997 GSE46416 32 human

To query large amounts of data, the API has a pagination system which
uses the :code:`limit` and :code:`offset` parameters. To avoid overloading the server,
calls are limited to a maximum of 100 entries, so the offset allows
you to get the next batch of entries in the next call(s). For
simplicity, this example shows how pagination works with 5 entries per
query.

>>> for ofs in [0,5,10]:
...     api_response=api_instance.get_platforms_by_ids([],offset=ofs,limit=5)
...     for d in api_response.data:
...         print(d.id, d.short_name, d.taxon.common_name)
...     print('--')
... 
1 GPL96 human
2 GPL1355 rat
3 GPL1261 mouse
4 GPL570 human
5 GPL81 mouse
--
6 GPL85 rat
7 GPL339 mouse
8 GPL91 human
9 GPL890 rat
10 GPL1406 mouse
--
11 GPL891 mouse
12 GPL82 mouse
13 GPL560 mouse
14 GPL1073 mouse
16 GPL369 mouse
--

The rest of the endpoints only support a single identifier:

>>> api_response = api_instance.get_dataset_annotations(["GSE35974","GSE12649"])
...Error Traceback...

In these cases, you will have to loop over all the identifiers you
wish to query and send separate requests:

>>> for dataset in ["GSE35974","GSE12649"]:
...     api_response = api_instance.get_dataset_annotations(dataset)
...     for d in api_response.data:
...         print('%s %-15s %-15s %-15s' % (dataset, d.object_class, d.class_name, d.term_name))
...     print('--')
... 
GSE35974 BioMaterial     biological sex  male           
GSE35974 FactorValue     disease         schizophrenia  
GSE35974 FactorValue     disease         Bipolar Disorder
GSE35974 BioMaterial     biological sex  female         
GSE35974 FactorValue     disease         mental depression
GSE35974 ExperimentTag   organism part   cerebellum     
--
GSE12649 BioMaterial     organism part   reference subject role
GSE12649 ExperimentTag   organism part   prefrontal cortex
GSE12649 BioMaterial     disease         Bipolar Disorder
GSE12649 BioMaterial     disease         schizophrenia  
--