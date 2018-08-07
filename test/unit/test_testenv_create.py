import pytest
import subprocess
import os
import sys

from tox_nuitka.plugin import tox_testenv_create


def test_pcall(venv, mocker, actioncls):
    """
    Test that if the user did not specify any compile targets, nuitka is not installed
    """
    action = actioncls()
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    result = tox_testenv_create(venv, action)
    assert result == True

    # Check that pipenv was executed with the correct arguments
    subprocess.Popen.assert_called_once_with(
        [sys.executable, "-m", "pip", "install", "nuitka"],
        action=action,
        cwd=venv.path.dirpath(),
        venv=False,
    )


def test_no_pcall(venv, mocker, actioncls):
    """
    Test that if the user did not specify any compile targets, nuitka is not installed
    """
    action = actioncls()
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    venv.envconfig.nuitka = None
    result = tox_testenv_create(venv, action)
    assert result == None

    # Check that pipenv was executed with the correct arguments
    subprocess.Popen.assert_not_called()
