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
        "category.name":  list(map(lambda x: x.category,d)),
        "category.URI":  list(map(lambda x: x.category_uri,d)),
        "value.name":  list(map(lambda x: x.value,d)),
        "value.URI":  list(map(lambda x: x.value_uri,d))
        })
    
    # df = pd.DataFrame({
    #     "category.name": [access_field(x,'category' for x in d)],
    #     "category.URI": [access_field(x,'category_uri' for x in d)],
    #     "value.name": [access_field(x,'value' for x in d)],
    #     "value.URI": [access_field(x,'value_uri' for x in d)]
    #     })
    
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



def process_DifferentialExpressionAnalysisResultSetValueObject(d:list,api):
    df = pd.DataFrame({})
    
    for x in d:
        if x.analysis.source_experiment is None:
            exp_id = x.analysis.bio_assay_set_id
        else:
            exp_id = x.analysis.source_experiment
        
        if len(x.experimental_factors)==1:
            contrast_id = list(map(lambda y: y.id, x.experimental_factors[0].values))
            baseline_id = x.baseline_group.id
            
            non_control_factors = list(filter(lambda y: y.id != baseline_id,x.experimental_factors[0].values))
            non_control_ids = [x for x in contrast_id if x != baseline_id]
            size = len(non_control_ids)
            
            exp_factors = list(map(lambda y: sub.process_FactorValueValueObject(y), 
                                   non_control_factors))
            
            
            list(it.repeat(sub.access_field(d,'experimental_factor_category','category'),size))
            
            out = pd.DataFrame({
                "result_ID": sub.rep(sub.access_field(x, "id"),size),
                "contrast_ID": non_control_ids,
                "experiment_ID": sub.rep(exp_id,size),
                "factor_category": sub.rep(sub.access_field(x.experimental_factors[0],"category"),size),
                "factor_category_URI" : sub.rep(sub.access_field(x.experimental_factors[0],"category_uri"),size),
                "factor_ID": sub.rep(sub.access_field(x.experimental_factors[0],"id"),size),
                "baseline_factors": sub.rep(sub.process_FactorValueValueObject(x.baseline_group),size),
                "experimental_factors": exp_factors,
                "subsetFactor_subset": sub.rep(not sub.access_field(x,"analysis","subset_factor_value") is None,size),
                "subsetFactor": sub.rep(sub.process_FactorValueValueObject(x.analysis.subset_factor_value), size)
            })
            
            df = pd.concat([df, out])
            
        else:
            return d
            ids = list(map(lambda x: sub.field_in_list(x,'id'),
                      sub.field_in_list(x.experimental_factors,"values")))
            
            factor_ids = sub.field_in_list(x.experimental_factors,'id')
            
            
            # in an effort to standarize the outpurs, we will always put the
            # sort by the factor id no
            order = sub.order(factor_ids)
            ids = [ids[i] for i in order]
            factor_ids.sort()
            
            ids = [[x,y] for x in ids[0] for y in ids[1]]
            
            
            # information provided in a single result set is not sufficient
            # to identify which factor values represent the controls.
            # we use the api object itself to call this one's friends
            # to figure that out
            all_sets = api.raw.get_result_sets(datasets = [exp_id])
            
            
            
            
            return d
        
        
    return df

