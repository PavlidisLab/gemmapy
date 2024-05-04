#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 02:15:57 2024

@author: omancarci
"""
import pandas as pd
import typing as T
import numpy as np
from io import StringIO


import itertools as it

def match(list1, list2):
    return [ list2.index(x) if x in list2 else None for x in list1 ]

# lis[match(to_match,by)] in R
def match_by(lis, to_match, by):
    return [lis[i] for i in match(to_match,by)]
    
def make_dict(keys,values):
    return {keys[i]: values[i] for i in range(len(keys))}

def order(lis:list,decreasing = False):
    out = np.argsort(lis).tolist()
    if decreasing:
        out.reverse()
    return out


# set doesn't preserve order
def unique(lis):
    lis = list(lis)
    out = []
    
    for x in lis:
        if x not in out:
            out.append(x)
    return(out)
    
    

def list_in_list(list1,list2):
    return list(elem in list(list2) for elem in list(list1))


def rep(obj,times):
    return list(it.repeat(obj,times))

def break_list(lis:list):
    out = []
    for x in lis:
        out.extend(x)
    return out

# access_field and field_in_list functions are written with
# tolerance for missing values in mind. they are here
# to prevent small changes in the api from preventing the
# whole functions from working
def access_field(x,*fields,na_type = np.nan):
    if type(x) is dict:
        return access_field_dict(x,*fields,na_type = na_type)
    
    
    target = None
    target_set = False
    for field in fields:
        if not target_set and field in dir(x):
            target = getattr(x, field)
            target_set = True
        elif target is None:
            return na_type
        elif field in dir(target):
            target = getattr(target,field)
        else:
            return na_type
    
    if target is None:
        return na_type
    
    return target

def access_field_dict(x,*fields,na_type = np.nan):
    target = None
    target_set = False
    for field in fields:
        if not target_set and field in x.keys():
            target = x[field]
            target_set= True
        elif target is None:
            return na_type
        elif type(target) is dict and field in target.keys():
            target = target[field]
        else:
            return na_type
        
        if target is None:
            return na_type
        return target

def field_in_list(x:list,*fields, blank_series =  pd.Series(dtype='str'), na_type = np.nan):
    if x is None or len(x)==0:
        return blank_series
    else:
        return [access_field(y,*fields) for y in x]


    

def process_FactorValueValueObject_list(d:T.Optional[list]):
    out = [process_FactorValueBasicValueObject(x) for x in d]
    return pd.concat(out,ignore_index = True)
    

def process_FactorValueValueObject(d):
    return process_FactorValueBasicValueObject(d)

def process_FactorValueBasicValueObject(d):
    if d is None or pd.isna(d):
        return pd.DataFrame({
            'category': [],
            "category_URI": [],
            'value':[],
            'value_URI':[],
            'predicate':[],
            "predicate_URI":[],
            "object":[],
            "object_URI":[],
            "summary":[],
            "ID":[],
            "factor_ID":[],
            "factor_category":[],
            "factor_category_URI":[]
            })
    elif not d.measurement is None:
        return pd.DataFrame({
            'category': [access_field(d,"category")],
            "category_URI": [access_field(d,"category_uri")],
            'value':[access_field(d,"measurement","value")],
            'value_URI':[np.nan],
            'predicate':[np.nan],
            "predicate.URI":[np.nan],
            "object":[np.nan],
            "object_URI":[np.nan],
            "summary":[np.nan],
            "ID":[access_field(d,'id')],
            "factor_ID":[access_field(d,"experimental_factor_id")],
            "factor_category":[access_field(d,"experimental_factor_category","category")],
            "factor_category_URI":[access_field(d,"experimental_factor_category","category_uri")]
            })
    else:
        characteristics = process_CharacteristicValueObject(access_field(d,'characteristics'))
        statements = process_StatementValueObject(access_field(d, 'statements'))
        
        statements.rename(columns = {
            'subject': 'value',
            'subject_URI': 'value_URI',
            'subject_ID': 'value_ID'
            }, inplace = True)
        
        characteristics = characteristics[~characteristics.value_ID.isin(statements.value_ID)]
        
        out = pd.concat([characteristics,statements],ignore_index = True)
        size = out.shape[0]
        
        out["summary"] = rep(access_field(d,'summary'),size)
        out["ID"] = rep(access_field(d,'id'),size)
        out["factor_ID"] = rep(access_field(d,'experimental_factor_id'),size)
        out["factor_category"] = rep(access_field(d,'experimental_factor_category','category'),size)
        out["factor_category_URI"] = rep(access_field(d,'experimental_factor_category','category_uri'),size)
        
        out.drop("value_ID",axis = 1, inplace = True)

        return out 


def process_CharacteristicValueObject(d:T.Optional[list]):
    
    return pd.DataFrame({
        "category": field_in_list(d,'category'),
        "category_URI": field_in_list(d,'category_uri'),
        "value": field_in_list(d,'value'),
        "value_URI": field_in_list(d,'value_uri'),
        "value_ID": field_in_list(d, "value_id"),
        })
    
    

def process_StatementValueObject(d:T.Optional[list]):
    
    df = pd.DataFrame({
        "category": field_in_list(d,'category'),
        "category_URI": field_in_list(d,'category_uri'),
        "subject": field_in_list(d,'subject'),
        "subject_URI":  field_in_list(d,'subject_uri'),
        "subject_ID":  field_in_list(d,'subject_id'),
        "predicate":  field_in_list(d,'subject_uri'),
        "predicate_URI": field_in_list(d,'predicate_uri'),
        "object": field_in_list(d, "object"),
        "object_URI": field_in_list(d, "object_URI")
        })
    
    return df

def read_tsv(d):
    uncomment = d.split("\n#")
    api_response = uncomment[len(uncomment)-1]
    uncomment = api_response.split('\n',1)
    api_response = uncomment[len(uncomment)-1]
    df = pd.read_csv(StringIO(api_response), sep='\t',dtype = {'Probe':str,
                                                               "Sequence": str,
                                                               "GeneSymbol":str,
                                                               "GeneName":str})
    return df



def dict_to_attr(d:dict):
    obj = lambda: None
    for k in d.keys():
        setattr(obj,k,d[k])
    return obj