
import sys
import gemmapy
import pytest

api = gemmapy.GemmaPy()

# test 8x getDataset... functions
@pytest.mark.parametrize('f', [s for s in dir(api) if s.startswith('get_dataset')])
def test_get_dataset_functions(f):
    func = getattr(api,f)
    if f == 'get_datasets':
        args = tuple()
    elif f.endswith('_for_genes'):
        args = ['GSE46416'], ['BRCA1']
    elif f.endswith('_by_ids'):
        args = ['GSE46416'],
    else:
        args = 'GSE46416',
    res = func(*args)

# test 2x former getDataset... functions
def test_get_differential_expression_values():
    f = 'get_differential_expression_values'
    func = getattr(api,f)
    res = func('GSE46416')

# test 4x getGene... functions
@pytest.mark.parametrize('f', [s for s in dir(api) if s.startswith('get_gene')])
def test_get_gene_functions(f):
    func = getattr(api,f)
    if not f.endswith('_genes'):
        res = func('DYRK1A')
    else:
        res = func(['DYRK1A'])

# test 5x getPlatform... functions
@pytest.mark.parametrize('f', [s for s in dir(api) if s.startswith('get_platform')])
def test_get_platform_functions(f):
    func = getattr(api,f)
    if f == 'get_platform_element':
        res = func("GPL1355", ["AFFX_Rat_beta-actin_M_at"])
    elif f == 'get_platform_element_genes':
        res = func("GPL1355", "AFFX_Rat_beta-actin_M_at")
    elif f == 'get_platforms_by_ids':
        res = func(["GPL1355"])
    else:
        res = func("GPL1355")

# test 2x search... functions
@pytest.mark.parametrize('f', [s for s in dir(api) if s.startswith('search')])
def test_search_functions(f):
    func = getattr(api,f)
    if f == 'search_annotations':
        res = func(['traumatic'])
    elif f == 'search_datasets':
        res = func(['bipolar'],'human')

# test 2x get_tax... functions
@pytest.mark.parametrize('f', ['get_taxa','get_taxon_datasets'])
def test_get_taxa_functions(f):
    func = getattr(api,f)
    if f.endswith('_datasets'):
        res = func('human')
    else:
        res = func()
