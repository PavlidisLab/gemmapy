#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:37:06 2023

@author: omancarci
"""

import pandas as pd




def processAnnotations(d):
    df = pd.DataFrame({
        "class.Name": list(map(lambda x: x.class_name,d.data)),
        "class.URI": list(map(lambda x: x.class_uri,d.data)),
        "term.Name": list(map(lambda x: x.term_name,d.data)),
        "term.URI": list(map(lambda x: x.term_uri,d.data))})
    return df