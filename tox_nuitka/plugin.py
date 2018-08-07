import sys
import os
import tox
from tox import hookimpl
from tox.config import Config


@hookimpl
def tox_testenv_create(venv, action):
    conf = venv.envconfig
    if not conf.nuitka:
        return

    config_interpreter = venv.getsupportedinterpreter()
    args = [sys.executable, "-m", "pip", "install", "nuitka"]

    venv.session.make_emptydir(venv.path)
    basepath = venv.path.dirpath()
    basepath.ensure(dir=1)

    venv._pcall(args, venv=False, action=action, cwd=basepath)

    # Return non-None to indicate the plugin has completed
    return True


@hookimpl
def tox_runtest_pre(venv):
    conf = venv.envconfig
    if not conf.nuitka:
        return

    basepath = venv.session.config.toxinipath.dirpath()
    action = venv.session.newaction(venv, "nuitka")

    for target in conf.nuitka:
        # Compile stage
        args = [sys.executable, "-m", "nuitka"]
        if conf.nuitka_module:
            args.append("--module")
        if conf.nuitka_recurse_all:
            args.append("--recurse-all")
        args.append(target)
        venv._pcall(args, venv=venv, action=action, cwd=basepath)

    # Return non-None to indicate the plugin has completed
    return True


@hookimpl
def tox_addoption(parser):
    parser.add_testenv_attribute(
        name="nuitka",
        type="line-list",
        help="List of Nuitka compile targets",
        default=[],
    )

    parser.add_testenv_attribute(
        name="nuitka_module",
        type="bool",
        help="Nuitka create an extension module executable instead of a program",
        default=False,
    )

    parser.add_testenv_attribute(
        name="nuitka_recurse_all",
        type="bool",
        help="Nuitka compiler recursion all imports",
        default=False,
    )
