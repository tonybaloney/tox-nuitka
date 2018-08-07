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

This simple example will test against Python 2.7 and 3.6 using pytest to execute the tests.

.. code-block:: 

        [tox]
        envlist = py27, py36

        [testenv]
        deps = 
        pytest
        pytest-mock
        commands = python -m pytest test/


