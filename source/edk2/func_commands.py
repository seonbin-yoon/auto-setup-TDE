from pathlib import Path

from edk2 import bashrc
from errors import edk2_task_errors
from modules import mapi


def _bashrc_exists(contexts: mapi.Contexts) -> None:
    bashrc_path = Path(contexts.home_path) / ".bashrc"
    if not bashrc_path.exists():
        raise edk2_task_errors.BashrcNotExistsError()

def _bashrc_func_exists(contexts: mapi.Contexts) -> None:
    bash_func = bashrc.load_bash_func(contexts.custom_paths)
    bashrc_path = Path(contexts.home_path) / ".bashrc"

    with open(bashrc_path, encoding='utf-8') as f:
        if bash_func in f.read():
            raise edk2_task_errors.BashrcFuncExistsError()

def _add_bashrc_func(contexts: mapi.Contexts) -> None:
    bash_func = bashrc.load_bash_func(contexts.custom_paths)
    bashrc_path = Path(contexts.home_path) / ".bashrc"

    with open(bashrc_path, "a", encoding='utf-8') as f:
        f.write(bash_func)

def load_func_tasks() -> list[mapi.FunctionTask]:
    bashrc_exists = mapi.FunctionTask(
        explain_message="Check if the bashrc file exists",
        func=_bashrc_exists
    )

    bashrc_func_exists = mapi.FunctionTask(
        explain_message="Check the bashrc file to see if there is a" \
        "function that automatically enables the edk2 build environment.",
        func=_bashrc_func_exists
    )

    add_bashrc_func = mapi.FunctionTask(
        explain_message="Add a function to automatically " \
        "enable the edk2 build environment to bashrc",
        func=_add_bashrc_func
    )

    return [
        bashrc_exists,
        bashrc_func_exists,
        add_bashrc_func
    ]
