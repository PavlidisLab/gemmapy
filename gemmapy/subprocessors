#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 02:15:57 2024

@author: omancarci
"""
import pandas as pd



def process_FactorValueValueObject(d):
    return process_FactorValueBasicValueObject(d)

def process_FactorValueBasicValueObject(d):
    if d is None:
        return pd.DataFrame({
            'category': [],
            "category.URI": [],
            'value':[],
            'value.URI':[],
            'predicate':[],
            "predicate.URI":[],
            "object":[],
            "object.URI":[],
            "summary":[],
            "ID":[],
            "factor.ID":[],
            "factor.category":[],
            "factor.category.URI":[]
            })
    elif d.measurement is None:
        return pd.DataFrame({
            'category': [d.category],
            "category.URI": [d.category_uri],
            'value':[d.measurement.value],
            'value.URI':[None],
            'predicate':[None],
            "predicate.URI":[None],
            "object":[None],
            "object.URI":[None],
            "summary":[None],
            "ID":[d.id],
            "factor.ID":[d.experimental_factor_id],
            "factor.category":[d.experimental_factor_category.category],
            "factor.category.URI":[d.experimental_factor_category.category_uri]
            })
    else:
        pass 
    