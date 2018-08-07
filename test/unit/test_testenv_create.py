import pytest
import subprocess
import os
import sys


@pytest.mark.xfail(reason="not implemented")
def test_pcall(venv, mocker, actioncls):
    action = actioncls()
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    result = tox_testenv_create(venv, action)
    assert result == True

    # Check that pipenv was executed with the correct arguments
    subprocess.Popen.assert_called_once_with(
        [sys.executable, "-m", "pipenv", "--python", "test-python"],
        action=action,
        cwd=venv.path.dirpath(),
        venv=False,
    )
    assert venv.tmpdir.ensure("Pipfile")
