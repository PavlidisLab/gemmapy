#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:29:08 2024

@author: omancarci
"""


import pandas as pd
import numpy as np
import typing as T
import warnings
from gemmapy import _subprocessors as sub
import itertools as it
import re






def process_de_matrix(d,rs,api):
    df = sub.read_tsv(d)
    df = df.drop(columns=['id','probe_id','gene_id','gene_name'], errors='ignore')
    df = df.rename(columns={'probe_name':'Probe','gene_official_symbol':'GeneSymbol',
                            'gene_official_name':'GeneName','gene_ncbi_id':'NCBIid'})
    
    i_regex = r"contrast_[0-9]+?_[0-9]+?_"
    
    if any([not re.search(i_regex,x) is None for x in df.columns]):
        result_set = api.get_result_sets(result_sets = [rs])
        to_rename = [x for x in df.columns if not re.search(i_regex,x) is None]
        
        def rename(name,result_set):
            x = name.split('_')
            if x[1] + "_" + x[2] in list(result_set.contrast_ID):
                return name
            else:
                assert x[2] + "_" + x[1]  in list(result_set.contrast_ID)
                x[1], x[2] = x[2], x[1]
                return '_'.join(x)
        
        new_name = [rename(x,result_set) for x in to_rename]
        
        rename_dict = sub.make_dict(to_rename, new_name)
        # rename_dict = {new_name[i]: to_rename[i] for i in range(len(new_name))}
        df = df.rename(columns = rename_dict)
    
    return df


def process_search_annotations(d:list):

    
    df = pd.DataFrame({
        "category_name": sub.field_in_list(d,'category'),
        "category_URI": sub.field_in_list(d,'category_uri'),
        "value_name": sub.field_in_list(d,'value'),
        "value_URI": sub.field_in_list(d,'value_uri')
        })
    
    return df

def process_annotations(d:list):
    
    df = pd.DataFrame({
        "class_name": sub.field_in_list(d,"class_name"),
        "class_URI": sub.field_in_list(d,"class_uri"),
        "term_name": sub.field_in_list(d,"term_name"),
        "term_URI": sub.field_in_list(d,"term_uri"),
        "object_class": sub.field_in_list(d,"object_class"),
        })
    
    return df

def attach_attributes(df:pd.DataFrame,attributes:dict,pop:T.List= ['data']):
    for x in pop:
        attributes.pop(x)
    # pandas warns about setting columns. we are not trying to set columns so
    # we should be fine
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        df.attributes = attributes

def process_dea(d):
    df = pd.DataFrame({
        "result_ID":pd.Series(dtype='int'),
        "contrast_ID": [],
        "experiment_ID": pd.Series(dtype='int'),
        "factor_category": [],
        "factor_category_URI" : [],
        "factor_ID": [],
        "baseline_factors": [],
        "experimental_factors": [],
        "is_subset": pd.Series(dtype='bool'),
        "subset_factor": [],
        "probes_analyzed": pd.Series(dtype='int'),
        "genes_analyzed": pd.Series(dtype='int')
    })
    out_list = [df]
    
    rs = sub.field_in_list(d,'result_sets')
    result_ids = [sub.field_in_list(x,'id') for x in rs]
    
    for i in range(len(result_ids)):
        
        if d[i].source_experiment is None:
            experiment_ID = d[i].bio_assay_set_id
        else:
            experiment_ID = d[i].source_experiment   
            
        for j in range(len(result_ids[i])):

            # re-order experimental factors based on their IDs to ensure compatibility
            # with dif exp tables
            factor_ids = sub.field_in_list(d[i].result_sets[j].experimental_factors,'id')
            order = sub.order(factor_ids)
            d[i].result_sets[j].experimental_factors = [d[i].result_sets[j].experimental_factors[k] for k in order]
            exp_factors = d[i].result_sets[j].experimental_factors
            
            if len(exp_factors) == 1:
                contrast_id = [x.id for x in exp_factors[0].values]
                baseline_id = d[i].result_sets[j].baseline_group.id
                
                non_control_factors = [x for x in exp_factors[0].values if x.id != baseline_id]
                contrast_id = [str(x) for x in contrast_id if x != baseline_id]
                size = len(contrast_id)
                
                experimental_factors = [sub.process_FactorValueValueObject(x) for x in non_control_factors]
                baseline_factors =  sub.process_FactorValueBasicValueObject(d[i].result_sets[j].baseline_group) 
                
            else:
                ids = list(map(lambda y: sub.field_in_list(y,'id'),
                          sub.field_in_list(exp_factors,"values")))
                ids = [[x,y] for x in ids[0] for y in ids[1]]
                
                baseline_ids = [x for x in sub.field_in_list(d[i].result_sets,"baseline_group",'id') if not x is np.nan]
                
                relevant_ids = [x for x in ids if not any(sub.list_in_list(x, baseline_ids))]
                
                fac_vals = [sub.access_field(y,'values') for y in exp_factors]
                all_factors = pd.concat(
                    [sub.process_FactorValueValueObject_list(y) for y in fac_vals],
                    ignore_index = True
                    )
                
                baseline_factors = all_factors.loc[all_factors.ID.isin(baseline_ids)]
                experimental_factors = [
                    all_factors.loc[all_factors.ID.isin(y)]
                    for y in relevant_ids]
                size = len(experimental_factors)
                
                contrast_id = [str(y[0]) + "_" + str(y[1]) for y in  relevant_ids]
                
            factor_category = ",".join(sub.field_in_list(exp_factors,'category'))
            factor_category_URI = ",".join(sub.field_in_list(exp_factors,'category_uri'))
            factor_ID = ",".join([str(y) for y in sub.field_in_list(exp_factors,'id')])
        
            out =  pd.DataFrame({
                    "result_ID": sub.rep(sub.access_field(d[i].result_sets[j], "id"),size),
                    "contrast_ID": contrast_id,
                    "experiment_ID": sub.rep(experiment_ID,size),
                    "factor_category": sub.rep(factor_category,size),
                    "factor_category_URI" : sub.rep(factor_category_URI,size),
                    "factor_ID": sub.rep(factor_ID,size),
                    "baseline_factors": sub.rep(baseline_factors,size),
                    "experimental_factors": experimental_factors,
                    "is_subset": sub.rep(not sub.access_field(d[i],"subset_factor_value") is None,size),
                    "subset_factor": sub.rep(sub.process_FactorValueValueObject(sub.access_field(d[i],"subset_factor_value")), size),
                    "probes_analyzed": sub.rep(d[i].result_sets[j].number_of_probes_analyzed,size),
                    "genes_analyzed": sub.rep(d[i].result_sets[j].number_of_genes_analyzed,size)
            })
                
            out_list.append(out) 
                
    
    df = pd.concat(out_list,ignore_index = True)
    return df

def process_DifferentialExpressionAnalysisResultSetValueObject(d:list,api):
    df = pd.DataFrame({
        "result_ID":pd.Series(dtype='int'),
        "contrast_ID": [],
        "experiment_ID": pd.Series(dtype='int'),
        "factor_category": [],
        "factor_category_URI" : [],
        "factor_ID": [],
        "baseline_factors": [],
        "experimental_factors": [],
        "is_subset": pd.Series(dtype='bool'),
        "subset_factor": []
    })
    out_list = [df]
    for x in d:
        if x.analysis.source_experiment is None:
            experiment_ID = x.analysis.bio_assay_set_id
        else:
            experiment_ID = x.analysis.source_experiment
        
        
        # re-order experimental factors based on their IDs to ensure compatibility
        # with dif exp tables
        factor_ids = sub.field_in_list(x.experimental_factors,'id')
        order = sub.order(factor_ids)
        x.experimental_factors = [x.experimental_factors[i] for i in order]
        
        
        if len(x.experimental_factors)==1:
            contrast_id = [x.id for x in x.experimental_factors[0].values]
            baseline_id = x.baseline_group.id
            
            non_control_factors = [x for x in x.experimental_factors[0].values if x.id != baseline_id]
            contrast_id = [str(x) for x in contrast_id if x != baseline_id]
            size = len(contrast_id)
            
            experimental_factors = [sub.process_FactorValueValueObject(x) for x in non_control_factors]

            
            baseline_factors =  sub.process_FactorValueBasicValueObject(x.baseline_group)           
            
        else:
            ids = list(map(lambda y: sub.field_in_list(y,'id'),
                      sub.field_in_list(x.experimental_factors,"values")))
            ids = [[x,y] for x in ids[0] for y in ids[1]]

            factor_ids = sub.field_in_list(x.experimental_factors,'id')
            
                        
            subset_factor = sub.process_FactorValueValueObject(x.analysis.subset_factor_value)
            
            all_sets = api.raw.get_result_sets(datasets = [experiment_ID])
            
            all_sets = [y for y in all_sets.data if 
                        subset_factor.ID.isin(
                            sub.process_FactorValueValueObject(y.analysis.subset_factor_value).ID).all()]
            
            
            non_interaction_sets = list(filter(lambda y: len(y.experimental_factors)==1,all_sets))
            baseline_ids = sub.field_in_list(non_interaction_sets,"baseline_group",'id')
            
            relevant_ids = [x for x in ids if not any(sub.list_in_list(x, baseline_ids))]
            
            fac_vals = [sub.access_field(y,'values') for y in x.experimental_factors]
            all_factors = pd.concat(
                [sub.process_FactorValueValueObject_list(y) for y in fac_vals],
                ignore_index = True
                )
            
            baseline_factors = all_factors.loc[all_factors.ID.isin(baseline_ids)]
            experimental_factors = [
                all_factors.loc[all_factors.ID.isin(y)]
                for y in relevant_ids]
            size = len(experimental_factors)
            contrast_id = [str(y[0]) + "_" + str(y[1]) for y in  relevant_ids]
        
        
        
        factor_category = ",".join(sub.field_in_list(x.experimental_factors,'category'))
        factor_category_URI = ",".join(sub.field_in_list(x.experimental_factors,'category_uri'))
        factor_ID = ",".join([str(y) for y in sub.field_in_list(x.experimental_factors,'id')])
        out =  pd.DataFrame({
            "result_ID": sub.rep(sub.access_field(x, "id"),size),
            "contrast_ID": contrast_id,
            "experiment_ID": sub.rep(experiment_ID,size),
            "factor_category": sub.rep(factor_category,size),
            "factor_category_URI" : sub.rep(factor_category_URI,size),
            "factor_ID": sub.rep(factor_ID,size),
            "baseline_factors": sub.rep(baseline_factors,size),
            "experimental_factors": experimental_factors,
            "is_subset": sub.rep(not sub.access_field(x,"analysis","subset_factor_value",na_type = None) is None,size),
            "subset_factor": sub.rep(sub.process_FactorValueValueObject(x.analysis.subset_factor_value), size)
        })
        
        out_list.append(out)
    out = pd.concat(out_list,ignore_index = True)
    
    
    return out

def process_dataset_design(d):
    df = sub.read_tsv(d)

    # conditioning: fix Bioassay names, add them index, remove redundant columns
    # rowall = [re.search(r"(?<=Name=).*",x).group() for x in df['Bioassay']]
    rowall = [c[c.find('Name=')+5:] for c in df['Bioassay'] if c.find('Name=') >= 0]
    assert len(rowall) == df.shape[0], 'Err1'
    df.index = rowall

    return df.drop(columns=['Bioassay', 'ExternalID'], errors='ignore')




def process_dataset_gene_expression(d:list,self):
    out = {}
    datasets = sub.field_in_list(d,'dataset_id')
    for i in range(len(d)):
        x = d[i]
        dataset = datasets[i]
        
        if len(x.gene_expression_levels) == 0:
            dataset_exp = pd.DataFrame({})
        else:
            def compile_exp_frame(gene_expression_levels):
                y = gene_expression_levels
                
                def get_expression_row(bio_assay_expression_levels):
                    z = bio_assay_expression_levels.copy()
                    for k in z.keys():
                        z[k] = [z[k]]
                        out = pd.DataFrame(z)
                        return out
                    
                    
                out = pd.concat(
                    [get_expression_row(z.bio_assay_expression_levels) for z in y.vectors],
                    ignore_index = True)
                nrows = out.shape[0]
                out.insert(0,"NCBIid",sub.rep(y.gene_ncbi_id,nrows))
                out.insert(0,"GeneSymbol",sub.rep(y.gene_official_symbol,nrows))
                out.insert(0,"Probe",sub.field_in_list(y.vectors,'design_element_name'))
                return out
            dataset_exp = pd.concat([compile_exp_frame(y) for y in x.gene_expression_levels],ignore_index = True)
        
        samples = self.get_dataset_samples(dataset)
        
        dataset_exp = \
            dataset_exp.\
                reindex(
                    columns = \
                        list(dataset_exp.columns[~np.array(
                            sub.list_in_list(dataset_exp.columns,
                                             samples.sample_name))]) + \
                            list(samples.sample_name))
        
        out.update({dataset:dataset_exp })


    return out

def process_platforms(d:list):
    
    df = pd.DataFrame({
        "platform_ID": sub.field_in_list(d,"id"),
        "platform_short_name": sub.field_in_list(d,"short_name"),
        "platform_name": sub.field_in_list(d,"name"),
        "platform_description": sub.field_in_list(d,"description"),
        "platform_troubled": sub.field_in_list(d,"troubled"),
        "platform_experiment_count": sub.field_in_list(d,"expression_experiment_count"),
        "platform_type": sub.field_in_list(d,"technology_type")
        })
        
    taxon = process_taxon(sub.field_in_list(d,'taxon'))
    
    return pd.concat([df, taxon], axis=1)

def process_taxon(d:list):
    df = pd.DataFrame({
        "taxon_name": sub.field_in_list(d,"common_name"),
        "taxon_scientific": sub.field_in_list(d,"scientific_name"),
        "taxon_ID": sub.field_in_list(d,"id"),
        "taxon_NCBI": sub.field_in_list(d,"ncbi_id"),
        "taxon_database_name": sub.field_in_list(d,"external_database","name"),
        "taxon_database_ID": sub.field_in_list(d,"external_database",'id'),
        })
    
    return df


def process_expression(d, dataset, api):
    # dataset 2 is an example why this more complex renaming is needed
    # check a non gsm study too since R's make names might be handling
    # more non-uniformities
    df = sub.read_tsv(d)
    m_cols = list(df.columns)
    samples = api.raw.get_dataset_samples(dataset).data
    sample_ids = sub.field_in_list(samples,"sample",'name')
    sample_names = sub.field_in_list(samples,"name")
    
    sample_ids = [x.replace("|",".") for x in sample_ids]
    
    def find_match(x):
        match = None
        for i in range(len(m_cols)):
            if m_cols[i].find(x+"_") != -1:
                match = i
        return match
    
    sample_matches = [find_match(x) for x in sample_ids]
    
    
    rename_dict = sub.make_dict([m_cols[i] for i in sample_matches],sample_names)

    df = df.rename(columns = rename_dict)
    
    assert all(sub.list_in_list(sample_names,list(df.columns)))
    
    df = df.drop(columns=['Sequence', 'GemmaId'], errors='ignore')
    
    non_samples = [x for x in list(df.columns) if not x in sample_names]
    df = df.reindex(columns = non_samples + sample_names)
    
    return df

def process_samples(d:list):
    
    df = pd.DataFrame({
        "sample_name": sub.field_in_list(d,"name"),
        "sample_ID": sub.field_in_list(d,"sample",'id'),
        "sample_description": sub.field_in_list(d,"description"),
        "sample_outlier": sub.field_in_list(d,"outlier"),
        "sample_accession": sub.field_in_list(d,"accession","accession"),
        "sample_database": sub.field_in_list(d,"accession","external_database",'name'),
        "sample_characteristics": [sub.process_CharacteristicValueObject(x).drop("value_ID",axis = 1) 
                                   for x in sub.field_in_list(d,"sample","characteristics")],
        "sample_factor_values": [sub.process_FactorValueValueObject_list(x)
                                for x in sub.field_in_list(d,"sample","factor_value_objects")]
        
        })
    
    return df

def process_datasets(d:list):
    df = pd.DataFrame({
        "experiment_short_name": sub.field_in_list(d,"short_name"),
        "experiment_name": sub.field_in_list(d,"name"),
        "experiment_ID": sub.field_in_list(d,"id"),
        "experiment_description": sub.field_in_list(d,"description"),
        "experiment_troubled": sub.field_in_list(d,"troubled"),
        "experiment_accession": sub.field_in_list(d,"accession"),
        "experiment_database":sub.field_in_list(d,"external_database"),
        "experiment_URI":sub.field_in_list(d,"external_uri"),
        "experiment_sample_count": sub.field_in_list(d,"bio_assay_count"),
        "experiment_last_updated":  sub.field_in_list(d,"last_updated"),
        "experiment_batch_effect_text":sub.field_in_list(d,"batch_effect"),
        "experiment_batch_corrected":sub.field_in_list(d,"geeq","batch_corrected"),
        "experiment_batch_confound":sub.field_in_list(d,"geeq","q_score_public_batch_confound"),
        "experiment_batch_effect":sub.field_in_list(d,"geeq","q_score_public_batch_effect"),
        "experiment_raw_data":sub.field_in_list(d,"geeq","s_score_raw_data"),
        "geeq_q_score":sub.field_in_list(d,"geeq","public_quality_score"),
        "geeq_s_score":sub.field_in_list(d,"geeq","public_suitability_score")
        })
    
    taxon = process_taxon(sub.field_in_list(d,'taxon'))
    
    return pd.concat([df, taxon], axis=1)

def process_QuantitationTypeValueObject(d:list):
    df = pd.DataFrame({
        "ID": sub.field_in_list(d,"id"),
        "name": sub.field_in_list(d,"name"),
        "description": sub.field_in_list(d,"description"),
        "type": ["processed" if "ProcessedExpressionDataVector" in x else "raw" for x in sub.field_in_list(d,"vector_type")],
        "ratio": sub.field_in_list(d,"is_ratio"),
        "scale": sub.field_in_list(d,"scale"),
        "preferred": sub.field_in_list(d,"is_preferred"),
        "recomputed": sub.field_in_list(d,"is_recomputed_from_raw_data")
        })
    return df

def process_GO(d:list):
    df = pd.DataFrame({
        'term_name': sub.field_in_list(d,'term'),
        'term_ID': sub.field_in_list(d,'go_id'),
        'term_URI': sub.field_in_list(d,'uri')
        })
    return df


def process_gene_location(d:list):
    df = pd.DataFrame({
        'chromosome': sub.field_in_list(d,'chromosome'),
        'strand': sub.field_in_list(d,'strand'),
        'nucleotide': sub.field_in_list(d,'nucleotide'),
        'length': sub.field_in_list(d,'nucleotide_length')
        })    
    taxon = process_taxon(sub.field_in_list(d,'taxon'))
    return pd.concat([df, taxon], axis=1)

def process_elements(d:list):
    df =  pd.DataFrame({
        'element_name': sub.field_in_list(d,'name'),
        'element_description': sub.field_in_list(d,'description')
        })
    array = process_gemma_array(sub.field_in_list(d,"array_design"))
    
    return pd.concat([df, array], axis=1)

def process_gemma_array(d:list):
    df =  pd.DataFrame({
        'platform_short_name': sub.field_in_list(d,'short_name'),
        'platform_name': sub.field_in_list(d,'name'),
        'platform_ID': sub.field_in_list(d,'id'),
        'platform_type': sub.field_in_list(d,'technology_type'),
        'platform_description': sub.field_in_list(d,'description'),
        'platform_troubled': sub.field_in_list(d,'troubled')
        })
    taxon = process_taxon(sub.field_in_list(d,'taxon'))
    return pd.concat([df, taxon], axis=1)


def process_genes(d:list):
    df = pd.DataFrame({
        "gene_symbol": sub.field_in_list(d,'official_symbol'),
        "gene_ensembl": sub.field_in_list(d,'ensembl_id'),
        "gene_NCBI": sub.field_in_list(d,'ncbi_id'),
        "gene_name":  sub.field_in_list(d,'official_name'),
        "gene_aliases":sub.field_in_list(d,'aliases'),
        "gene_MFX_rank": sub.field_in_list(d,'multifunctionality_rank')
        })
    
    taxon = process_taxon(sub.field_in_list(d,'taxon'))
    
    return pd.concat([df, taxon], axis=1)

def process_search(d:list,result_type):
    if result_type == "ubic.gemma.model.expression.experiment.ExpressionExperiment":
        return process_datasets(sub.field_in_list(d,'result_object'))
    if result_type == "ubic.gemma.model.genome.Gene":
        return process_genes(sub.field_in_list(d,'result_object'))
    if result_type ==  "ubic.gemma.model.expression.arrayDesign.ArrayDesign":
        return process_platforms(sub.field_in_list(d,'result_object'))
    return sub.field_in_list(d,'result_object')


