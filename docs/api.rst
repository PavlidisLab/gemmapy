API Reference
=============

Basic package usage:

>>> import gemmapy
>>> api_instance = gemmapy.GemmaPy()
>>> api_response = api_instance.FUNCTION(args)

Where ``FUNCTION`` is one of the methods of the :py:class:`gemmapy.GemmaPy`
class described below. 
Return types (classes) are described in `gemmapy.sdk.models Subpackage`_ 
(unless they are `Pandas DataFrame <https://pandas.pydata.org/docs/reference/frame.html>`_ 
or `AnnData <https://anndata.readthedocs.io/en/latest/generated/anndata.AnnData.html>`_ objects).


gemmapy Package
---------------

Main package containing :py:class:`~gemmapy.GemmaPy` class and :py:mod:`gemmapy.sdk`
subpackage containing lower level swagger generated code.

.. 
  currentmodule:: gemmapy.sdk.models

.. automodule:: gemmapy
   :members:
   :undoc-members:
   :imported-members:

gemmapy.sdk.models Subpackage
-----------------------------

The subpackage contains most of classes which instances
are returned by :py:class:`~gemmapy.GemmaPy` methods.

.. automodule:: gemmapy.sdk.models
   :members:
   :undoc-members:
   :imported-members:

