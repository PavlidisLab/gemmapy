#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:29:08 2024

@author: omancarci
"""


import pandas as pd
import numpy as np
from io import StringIO
import typing as T
import warnings
from gemmapy import subprocessors as sub
import itertools as it
import re



def read_tsv(d):
    uncomment = d.split("\n#")
    api_response = uncomment[len(uncomment)-1]
    uncomment = api_response.split('\n',1)
    api_response = uncomment[len(uncomment)-1]
    df = pd.read_csv(StringIO(api_response), sep='\t')
    return df


def process_de_matrix(d):
    df = read_tsv(d)
    df = df.drop(columns=['id','probe_id','gene_id','gene_name'], errors='ignore')
    df = df.rename(columns={'probe_name':'Probe','gene_official_symbol':'GeneSymbol',
                            'gene_official_name':'GeneName','gene_ncbi_id':'NCBIid'})
    return df


def process_search_annotations(d:list):

    
    df = pd.DataFrame({
        "category.name": sub.field_in_list(d,'category'),
        "category.URI": sub.field_in_list(d,'category_uri'),
        "value.name": sub.field_in_list(d,'value'),
        "value.URI": sub.field_in_list(d,'value_uri')
        })
    
    return df

def process_annotations(d:list):
    df = pd.DataFrame({
        "class.name":  list(map(lambda x: x.class_name,d)),
        "class.URI":  list(map(lambda x: x.class_uri,d)),
        "term.name":  list(map(lambda x: x.term_name,d)),
        "term.URI":  list(map(lambda x: x.term_uri,d))
        })
    
    # df = pd.DataFrame({
    #     "class.name":  [access_field(x,'class_name' for x in d)],
    #     "class.URI":  [access_field(x,'class_uri' for x in d)],
    #     "term.name": [access_field(x,'term_name' for x in d)],
    #     "term.URI":  [access_field(x,'term_uri' for x in d)]
    #     })
    
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
        "subsetFactor_subset": [],
        "subsetFactor": [],
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
                    "subsetFactor_subset": sub.rep(not sub.access_field(d[i],"subset_factor_value") is None,size),
                    "subsetFactor": sub.rep(sub.process_FactorValueValueObject(sub.access_field(d[i],"subset_factor_value")), size),
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
        "subsetFactor_subset": [],
        "subsetFactor": []
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
            
            
            
            all_sets = api.raw.get_result_sets(datasets = [experiment_ID])
            non_interaction_sets = list(filter(lambda y: len(y.experimental_factors)==1,all_sets.data))
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
            "subsetFactor_subset": sub.rep(not sub.access_field(x,"analysis","subset_factor_value") is None,size),
            "subsetFactor": sub.rep(sub.process_FactorValueValueObject(x.analysis.subset_factor_value), size)
        })
        
        out_list.append(out)
        
    out = pd.concat(out_list,ignore_index = True)
    
    
    return out

def process_dataset_design(d):
    
    uncomment = d.split("\n#")
    d = uncomment[len(uncomment)-1]
    uncomment = d.split('\n',1)
    d = uncomment[len(uncomment)-1]
    
    df = pd.read_csv(StringIO(d), sep='\t')

    # conditioning: fix Bioassay names, add them index, remove redundant columns
    # rowall = [re.search(r"(?<=Name=).*",x).group() for x in df['Bioassay']]
    rowall = [c[c.find('Name=')+5:] for c in df['Bioassay'] if c.find('Name=') >= 0]
    assert len(rowall) == df.shape[0], 'Err1'
    df.index = rowall

    return df.drop(columns=['Bioassay', 'ExternalID'], errors='ignore')