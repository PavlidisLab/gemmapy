The package has been tested with Python3.7 but it should work with any Python3 version. 

#. Install it from a local copy (recommended)

   .. code-block:: bash

      git clone git@github.com:PavlidisLab/gemmapy.git
      cd gemmapy
      pip install .

#. Install it from TestPyPI (temporary method) 

   .. code-block:: bash

      pip install -i https://test.pypi.org/simple/ --no-deps gemmapy
      # install dependencies
      pip install urllib3 setuptools certifi anndata six python-dateutil pandas numpy

   .. warning::
      This installation command will change as the first release of the package
      is uploaded to the PyPI repository (vs TestPyPI now).
