#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:34:51 2023

@author: omancarci
"""
import logging
from   gemmapy import sdk
from gemmapy import processors as ps
import pandas
import numpy
import anndata
from io import StringIO
from gemmapy.gemmapy_api import GemmaPy

class GemmaPyTables(object):
    
    def __init__(self, auth=None, devel=False):
        print(GemmaPy)
        self.raw_api = GemmaPy(auth = auth, devel = devel)
    
    def get_dataset_annotations(self, dataset, **kwargs):
        api_response = self.raw_api.get_dataset_annotations(dataset,**kwargs)
        return ps.processAnnotations(api_response)
