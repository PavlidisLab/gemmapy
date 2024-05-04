#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:09:30 2024

@author: omancarci
"""

import typing as T


def remove_nones(**kwargs):
    out = kwargs.copy()
    for k in kwargs.keys():
        if kwargs[k] is None:
            out.pop(k)
    return out

def add_to_filter(filt:T.Optional[str], prop: str, terms: T.List[T.Union[str,int]]):
    
    if terms is None:
        return filt
    
    
    if filt is None:
        filt = ""
    
    if len(filt)>0:
        filt = filt + " and "
    
    filt = filt + prop + " in (" +  ",".join([str(x) for x in terms]) + ")"
    
    return filt



def check_result_type(typ:str):
    if typ == 'experiment':
        return "ubic.gemma.model.expression.experiment.ExpressionExperiment"
    if typ == "gene":
        return "ubic.gemma.model.genome.Gene"
    if typ =='platform':
        return 'ubic.gemma.model.expression.arrayDesign.ArrayDesign'
    return typ