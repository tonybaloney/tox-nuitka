tox-nuitka
==========

.. image:: https://img.shields.io/pypi/v/tox-nuitka.svg
        :target: https://pypi.python.org/pypi/tox-nuitka

.. image:: https://img.shields.io/travis/tonybaloney/tox-nuitka.svg
        :target: https://travis-ci.org/tonybaloney/tox-nuitka

.. image:: https://codecov.io/gh/tonybaloney/tox-nuitka/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/tonybaloney/tox-nuitka

.. image:: https://pyup.io/repos/github/tonybaloney/tox-nuitka/shield.svg
     :target: https://pyup.io/repos/github/tonybaloney/tox-nuitka/
     :alt: Updates

.. image:: https://pyup.io/repos/github/tonybaloney/tox-nuitka/python-3-shield.svg
     :target: https://pyup.io/repos/github/tonybaloney/tox-nuitka/
     :alt: Python 3

A tox plugin to replace the default use of the CPython compiler with nuitka.

This plugin works by injecting Nuitka as a pip requirement to all test environments and then adding the Nuitka
compile as a pre-test stage.

Installation
------------

.. code-block:: bash

    pip install tox-nuitka

Or, 

.. code-block:: bash

    pipenv install tox-nuitka  

Executing tests
---------------

Each of the commands in your testenv configuration will be compiled by nuitka to execute within the pipenv virtual environment

Example tox.ini
---------------

This simple example will run pytest against your package but compile myapp/main.py using Nuitka.

.. code-block:: 

        [tox]
        envlist = py27, py36, py37

        [testenv]
        nuitka = myapp/main.py
        deps = pytest
        commands = python -m pytest test/

Additional Nuitka configuration is available within the test environment settings.

Currently, the --module and --recurse-all flags are available like this:

.. code-block:: 

        nuitka_module = true
        nuitka_recurse_all = true

Multiple compile targets can be provided

.. code-block:: 

        nuitka = 
                myapp/target1.py
                myapp/target2.py