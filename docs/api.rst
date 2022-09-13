
API Reference
=============

Basic package usage:

>>> import gemmapy
>>> api_instance = gemmapy.GemmaPy()
>>> api_response = api_instance.FUNCTION(args)

Where ``FUNCTION`` is one of the methods of the :py:class:`gemmapy.GemmaPy`
class described below. 
Return types (classes) are described in :py:mod:`gemmapy.sdk.models`
(unless they are `Pandas DataFrame <https://pandas.pydata.org/docs/reference/frame.html>`_ 
or `AnnData <https://anndata.readthedocs.io/en/latest/generated/anndata.AnnData.html>`_ objects).


gemmapy Package
---------------

Main package containing :py:class:`~gemmapy.GemmaPy` class described below and :py:mod:`gemmapy.sdk`
subpackage containing lower level swagger generated code. Of the latter only :py:mod:`gemmapy.sdk.models` module is documented here as its classes represent :py:class:`~gemmapy.GemmaPy` method 
return values.

.. _GemmaPy-sec:

gemmapy.GemmaPy Class
---------------------

.. currentmodule:: gemmapy

.. autoclass:: GemmaPy
   :members:

   .. rubric:: Methods

   .. autosummary::

      ~GemmaPy.get_dataset_object
      ~GemmaPy.get_dataset_annotations
      ~GemmaPy.get_differential_expression_values
      ~GemmaPy.get_dataset_differential_expression_analyses
      ~GemmaPy.get_dataset_design
      ~GemmaPy.get_dataset_expression
      ~GemmaPy.get_dataset_platforms
      ~GemmaPy.get_result_sets
      ~GemmaPy.get_dataset_samples
      ~GemmaPy.get_datasets_by_ids
      ~GemmaPy.get_gene_go_terms
      ~GemmaPy.get_gene_locations
      ~GemmaPy.get_gene_probes
      ~GemmaPy.get_genes
      ~GemmaPy.get_platform_annotations
      ~GemmaPy.get_platform_datasets
      ~GemmaPy.get_platform_element_genes
      ~GemmaPy.get_platform_element
      ~GemmaPy.get_platforms_by_ids
      ~GemmaPy.get_result_set
      ~GemmaPy.get_result_set_factors
      ~GemmaPy.search_annotations
      ~GemmaPy.search_datasets

   
gemmapy.sdk.models Subpackage
-----------------------------

The subpackage contains most of classes which instances
are returned by :py:class:`~gemmapy.GemmaPy` methods.

.. automodule:: gemmapy.sdk.models
   :members:
   :undoc-members:
   :imported-members:

