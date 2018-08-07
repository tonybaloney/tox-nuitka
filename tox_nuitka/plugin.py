import sys
import os
import tox
from tox import hookimpl
import contextlib


@hookimpl
def tox_testenv_create(venv, action):
    config_interpreter = venv.getsupportedinterpreter()
    args = [sys.executable, "-m", "pip", "install", "nuitka"]

    venv.session.make_emptydir(venv.path)
    basepath = venv.path.dirpath()
    basepath.ensure(dir=1)

    venv._pcall(args, venv=False, action=action, cwd=basepath)

    # Return non-None to indicate the plugin has completed
    return None
