import pytest
import py
import subprocess
import os
import sys

from tox_nuitka.plugin import tox_runtest_pre


def test_pcall(venv, mocker):
    """
    Test that nuitka is called with compile targets
    """
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    assert isinstance(venv.envconfig.nuitka, list)

    result = tox_runtest_pre(venv)
    assert result == True

    # Check that pipenv was executed with the correct arguments
    subprocess.Popen.assert_called_once_with(
        [sys.executable, "-m", "nuitka", "test/foo.py"],
        cwd=py.path.local(os.getcwd()),
        venv=venv,
        action=True,
    )


def test_no_pcall(venv, mocker):
    """
    Test that if the user did not specify any compile targets, nuitka is not installed
    """
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    venv.envconfig.nuitka = None
    result = tox_runtest_pre(venv)
    assert result == None

    # Check that pipenv was executed with the correct arguments
    subprocess.Popen.assert_not_called()


def test_pcall_recurse(venv, mocker):
    """
    Test that nuitka is called with recurse all
    """
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    assert isinstance(venv.envconfig.nuitka, list)
    venv.envconfig.nuitka_recurse_all = True
    result = tox_runtest_pre(venv)
    assert result == True

    # Check that pipenv was executed with the correct arguments
    subprocess.Popen.assert_called_once_with(
        [sys.executable, "-m", "nuitka", "--recurse-all", "test/foo.py"],
        cwd=py.path.local(os.getcwd()),
        venv=venv,
        action=True,
    )


def test_pcall_module(venv, mocker):
    """
    Test nuitka is called in module mode
    """
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    assert isinstance(venv.envconfig.nuitka, list)
    venv.envconfig.nuitka_module = True
    result = tox_runtest_pre(venv)
    assert result == True

    # Check that pipenv was executed with the correct arguments
    subprocess.Popen.assert_called_once_with(
        [sys.executable, "-m", "nuitka", "--module", "test/foo.py"],
        cwd=py.path.local(os.getcwd()),
        venv=venv,
        action=True,
    )
