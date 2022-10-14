import gemmapy
api_instance = gemmapy.GemmaPy()

print("Downloading expression data\nEx1")
api_response = api_instance.search_datasets(["bipolar"], taxon="human", limit=100)
api_response.data[0]  # view the object structure
for d in api_response.data:
  if d.geeq is not None and  d.geeq.batch_corrected:
    print(d.short_name, d.name, d.bio_assay_count)

print("\nEx2")
api_response = api_instance.get_datasets_by_ids(["GSE46416"])
for d in api_response.data:
  print(d.short_name, d.name, d.id)
print("\n",d.description)

print("\nEx3")
adata = api_instance.get_dataset_object("GSE46416")
print(adata)

print("")
adata.var['disease'].unique()

print("")
manic=adata[:,(adata.var['disease'] == 'reference_subject_role') |
                      (adata.var['disease'] == 'bipolar_disorder_|_manic_phase_|')].copy()
print(manic)
print("\n",manic.var)

# -----
print("\nDifferential expression analyses\nEx1")
import pandas
import numpy as np
de = api_instance.get_differential_expression_values('GSE46416', readableContrasts=True)
de = de[0]
# Classify probes for plotting
de['diffexpr'] = 'No'   # add extra column
de.loc[(de['contrast_bipolar disorder, manic phase_logFoldChange'] > 1.0) &
       (de['contrast_bipolar disorder, manic phase_pvalue'] < 0.05),'diffexpr'] = 'Up'
de.loc[(de['contrast_bipolar disorder, manic phase_logFoldChange'] < -1.0) &
       (de['contrast_bipolar disorder, manic phase_pvalue'] < 0.05),'diffexpr'] = 'Down'

# Upregulated probes
de_up = de[de['diffexpr']=='Up']
de_up = de_up[['Probe','GeneSymbol', 'contrast_bipolar disorder, manic phase_pvalue',
        'contrast_bipolar disorder, manic phase_logFoldChange']].sort_values(
        'contrast_bipolar disorder, manic phase_pvalue')
with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
        print(de_up[:10])

print("")
de_dn = de[de['diffexpr']=='Down']
de_dn = de_dn[['Probe','GeneSymbol', 'contrast_bipolar disorder, manic phase_pvalue',
        'contrast_bipolar disorder, manic phase_logFoldChange']].sort_values(
        'contrast_bipolar disorder, manic phase_pvalue')
with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
        print(de_dn[:10])

# -----
print("\nPlatform Annotations\nEx1")
import pandas
api_response = api_instance.get_platform_annotations('GPL96')
with pandas.option_context('display.max_rows', None, 'display.max_columns', None): print(api_response[:6])

print("\nEx2")
api_response = api_instance.get_platform_annotations('Generic_human')
with pandas.option_context('display.max_rows', None, 'display.max_columns', None): print(api_response[:6])

print("\nEx3")
api_response = api_instance.get_genes(['Eno2'])
api_response.data[0] # view the object structure
for d in api_response.data: print("%s %-18s %6d %-30s %-10s %2i %s" %
  (d.official_symbol,d.ensembl_id,d.ncbi_id,d.official_name,
   d.taxon.common_name,d.taxon.id,d.taxon.scientific_name))

print("\nEx4")
probs=api_instance.get_gene_probes(2026)
probs.data[0]  # view the object structure
# print only fields of interest
for d in probs.data[0:6]:
  print("%-10s %-12s %-20s %s %s %s %s" %
 (d.name,d.array_design.short_name,d.array_design.name,d.array_design.taxon.common_name,
  d.array_design.taxon.id,d.array_design.technology_type,d.array_design.troubled))


# -----
print("\nLarger queries\nEx1")
api_instance = gemmapy.GemmaPy()
api_response = api_instance.get_datasets_by_ids(["GSE35974","GSE46416"])
api_response.data[0]  # view the object structure
for d in api_response.data:
  print(d.short_name, d.name, d.id, d.accession, d.bio_assay_count, d.taxon.common_name)

print("\nEx2")
for ofs in [0,5,10]:
    api_response=api_instance.get_platforms_by_ids([],offset=ofs,limit=5)
    for d in api_response.data:
        print(d.id, d.short_name, d.taxon.common_name)
    print('--')

print("\nEx3")
for dataset in ["GSE35974","GSE12649"]:
    api_response = api_instance.get_dataset_annotations(dataset)
    for d in api_response.data:
        print('%s %-15s %-15s %-15s' % (dataset, d.object_class, d.class_name, d.term_name))
    print('--')
