#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:06:47 2024

@author: omancarci
"""
import unittest
import gemmapy
import pandas as pd

class TestProcessedEndpoints(unittest.TestCase):
    
    def test_get_result_sets(self):
        api = gemmapy.GemmaPy()
        res = api.get_result_sets([200])
        self.assertTrue(type(res) is pd.core.frame.DataFrame)

        res2 = api.get_result_sets(resultSets = [res.result_ID[0]])
        self.assertTrue(type(res2) is pd.core.frame.DataFrame)

        self.assertTrue(res.shape[1] == 10)
        self.assertTrue(res2.shape[1] == 10)
        self.assertTrue(res.shape[0] > 0)
        self.assertTrue(res2.shape[0] > 0)

        self.assertTrue(len(set(res2.result_ID)) == 1)
        
        self.assertTrue(res2.result_ID[0] in list(res.result_ID))

    def test_search_annotations(self):
        api = gemmapy.GemmaPy()
        res = api.search_annotations(query = ['traumatic'])
        self.assertTrue(type(res) is pd.core.frame.DataFrame)

        self.assertTrue(res.shape[1] == 4)
        self.assertTrue(res.shape[0] > 0)
        res2 = api.search_annotations(query = ['gibberish'])
        self.assertTrue(type(res2) is pd.core.frame.DataFrame)
        self.assertTrue(res2.shape[0] ==0)
        self.assertTrue(res2.shape[1] == 4)

    def test_get_dataset_design(self):
        api = gemmapy.GemmaPy()
        res = api.get_dataset_design('1')
        self.assertTrue(type(res) is pd.core.frame.DataFrame)
        
    
    def test_get_dataset_differential_expression_analyses(self):
        api = gemmapy.GemmaPy()

        res = api.get_dataset_differential_expression_analyses(200)
        self.assertTrue(type(res) is pd.core.frame.DataFrame)

        res2 = api.get_result_sets([200])
        
        self.assertTrue(all(res.contrast_ID == res2.contrast_ID))


    
if __name__ == '__main__':
    unittest.main()