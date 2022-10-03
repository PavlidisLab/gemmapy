
import sys
import gemmapy

api = gemmapy.GemmaPy()

out = False
if len(sys.argv)>1 and sys.argv[1].startswith("out"): out = True

# test 8x getDataset... functions
for f in [s for s in dir(api) if s.startswith('get_dataset')]:
    print('testing %s...' % f, end='')
    func = getattr(api,f)
    if not f.endswith('_by_ids'):
        res = func('GSE46416')
    else:
        res = func(['GSE46416'])
    print('ok')
    if out: print(str(res)[:2000])
    
# test 2x former getDataset... functions
for f in ['get_dataset_differential_expression_analyses','get_differential_expression_values']:
#    if f.endswith('_values'): continue
    print('testing %s...' % f, end='')
    func = getattr(api,f)
    res = func('GSE46416')
    print('ok')
    if out: print(str(res)[:2000])

# test 4x getGene... functions
for f in [s for s in dir(api) if s.startswith('get_gene')]:
    print('testing %s...' % f, end='')
    func = getattr(api,f)
    if not f.endswith('_genes'):
        res = func('DYRK1A')
    else:
        res = func(['DYRK1A'])
    print('ok')
    if out: print(str(res)[:2000])

# test 5x getPlatform... functions
for f in [s for s in dir(api) if s.startswith('get_platform')]:
    print('testing %s...' % f, end='')
    func = getattr(api,f)
    if f == 'get_platform_element':
        res = func("GPL1355", ["AFFX_Rat_beta-actin_M_at"])
    elif f == 'get_platform_element_genes':
        res = func("GPL1355", "AFFX_Rat_beta-actin_M_at")
    elif f == 'get_platforms_by_ids':
        res = func(["GPL1355"])
    else:
        res = func("GPL1355")
    print('ok')
    if out: print(str(res)[:2000])


# test 2x search... functions
for f in [s for s in dir(api) if s.startswith('search')]:
    print('testing %s...' % f, end='')
    func = getattr(api,f)
    if f == 'search_annotations':
        res = func(['traumatic'])
    elif f == 'search_datasets':
        res = func(['bipolar'],'human')
    else:
        continue
    print('ok')
    if out: print(str(res)[:2000])

# test 2x get_tax... functions
for f in ['get_taxa','get_taxon_datasets']:
    print('testing %s...' % f, end='')
    func = getattr(api,f)
    if f.endswith('_datasets'):
        res = func('worm')
    else:
        res = func()
    print('ok')
    if out: print(str(res)[:2000])
