#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 02:15:57 2024

@author: omancarci
"""
import pandas as pd
import typing as T
import numpy as np

import itertools as it


def order(lis:list):
    return np.argsort(lis).tolist()

def list_in_list(list1,list2):
    return list(elem in list1 for elem in list2)


def rep(obj,times):
    return list(it.repeat(obj,times))

# tolerance for missing values
def access_field(x,*fields,na_type = np.nan):
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
    
    return target


def field_in_list(x,*fields, na_type = np.nan):
    if x is None:
        return []
    else:
        return [access_field(y,*fields) for y in x]


def process_FactorValueValueObject(d):
    return process_FactorValueBasicValueObject(d)

def process_FactorValueBasicValueObject(d):
    if d is None:
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
    elif d.measurement is None:
        return pd.DataFrame({
            'category': [access_field(d,"category")],
            "category_URI": [access_field(d,"category_uri")],
            'value':[access_field(d,"measurement","value")],
            'value_URI':[None],
            'predicate':[None],
            "predicate.URI":[None],
            "object":[None],
            "object_URI":[None],
            "summary":[None],
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
        
        out = pd.concat([characteristics,statements])
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

