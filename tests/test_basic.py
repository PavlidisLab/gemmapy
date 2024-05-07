#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:06:47 2024

@author: omancarci
"""
import pytest
import gemmapy
import pandas as pd
from gemmapy import _subprocessors as sub
import anndata as ad


api = gemmapy.GemmaPy()

def test_get_result_sets():
    res = api.get_result_sets([200])
    
    assert type(res) is pd.core.frame.DataFrame
    
