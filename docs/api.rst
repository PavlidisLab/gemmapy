
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

      ~GemmaPy.getDataset
      ~GemmaPy.getDatasetAnnotations
      ~GemmaPy.getDatasetDE
      ~GemmaPy.getDatasetDEA
      ~GemmaPy.getDatasetDesign
      ~GemmaPy.getDatasetExpression
      ~GemmaPy.getDatasetPlatforms
      ~GemmaPy.getDatasetResultSets
      ~GemmaPy.getDatasetSamples
      ~GemmaPy.getDatasetsInfo
      ~GemmaPy.getGeneGO
      ~GemmaPy.getGeneLocation
      ~GemmaPy.getGeneProbes
      ~GemmaPy.getGenesInfo
      ~GemmaPy.getPlatformAnnotation
      ~GemmaPy.getPlatformDatasets
      ~GemmaPy.getPlatformElementGenes
      ~GemmaPy.getPlatformElements
      ~GemmaPy.getPlatformsInfo
      ~GemmaPy.getResultSets
      ~GemmaPy.getResultSetsFactors
      ~GemmaPy.searchAnnotations
      ~GemmaPy.searchDatasets

   
gemmapy.sdk.models Subpackage
-----------------------------

The subpackage contains most of classes which instances
are returned by :py:class:`~gemmapy.GemmaPy` methods.

.. automodule:: gemmapy.sdk.models
   :members:
   :undoc-members:
   :imported-members:

