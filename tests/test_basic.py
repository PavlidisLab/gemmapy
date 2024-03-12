#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:06:47 2024

@author: omancarci
"""
import unittest
import gemmapy
import pandas as pd
from gemmapy import subprocessors as sub

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
        
    def test_get_dataset_annotations(self):
        api = gemmapy.GemmaPy()
        res = api.get_dataset_annotations(1)
        self.assertTrue(type(res) is pd.core.frame.DataFrame)
        self.assertTrue(res.shape[1] == 4)

    def test_get_dataset_design(self):
        api = gemmapy.GemmaPy()
        res = api._GemmaPy__get_dataset_design('1')
        self.assertTrue(type(res) is pd.core.frame.DataFrame)
        
    
    def test_get_dataset_differential_expression_analyses(self):
        api = gemmapy.GemmaPy()

        res = api.get_dataset_differential_expression_analyses(200)
        self.assertTrue(type(res) is pd.core.frame.DataFrame)
        
                        
    def test_result_set_table_compatibility(self):
        api = gemmapy.GemmaPy()
        
        res = api.get_dataset_differential_expression_analyses(200)
        res2 = api.get_result_sets(resultSets = [res.result_ID[0]])
        self.assertTrue(all(
            sub.list_in_list(res2.contrast_ID, res.contrast_ID)
            ))

        
        dif_exp = api._GemmaPy__get_result_set(res.result_ID[0])
        
        expected_cols = ["contrast_" + str(x) +"_log2fc" for x in res2.contrast_ID]
        
        self.assertTrue(all(
            sub.list_in_list(expected_cols,list(dif_exp.columns))
            ))
        
    def test_get_dataset_expression_for_genes(self):
        api = gemmapy.GemmaPy()
        
        res = api.get_dataset_expression_for_genes(datasets = [1,4,2], genes = [10225,2841])
        
        type(list(res.values())[0])
        
        self.assertTrue(all(
            [type(value) is pd.core.frame.DataFrame for value in res.values()]
            ))
        self.assertTrue(res[2].shape == (0,0))
        
        self.assertTrue(res[1].shape[0]>1)
        self.assertTrue(res[4].shape[0]>1)

    def test_get_processed_expression_samples_compatibility(self):
        api = gemmapy.GemmaPy()
        exp = api.get_dataset_processed_expression(2)
        samples = api.get_dataset_samples(2)
    
    def test_get_dataset_raw_expression(self):
        api = gemmapy.GemmaPy()
        exp = api.get_dataset_raw_expression(2,507039)


    
if __name__ == '__main__':
    unittest.main()