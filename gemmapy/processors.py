#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:29:08 2024

@author: omancarci
"""


import pandas as pd
from io import StringIO



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


def process_search_annotations(d):
    df = pd.DataFrame({
        "category.name":  list(map(lambda x: x.category,d.data)),
        "category.URI":  list(map(lambda x: x.category_uri,d.data)),
        "value.name":  list(map(lambda x: x.value,d.data)),
        "value.URI":  list(map(lambda x: x.value_uri,d.data))
        })
    
    return df