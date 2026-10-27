from pathlib import Path
from textwrap import dedent

from errors import edk2_task_errors
from modules import mapi
from modules.mapi import CustomPaths
from packages.edk2 import bashrc


def bashrc_exists(contexts: mapi.Contexts) -> None:
    bashrc_path = Path(contexts.home_path) / ".bashrc"
    if not bashrc_path.exists():
        raise edk2_task_errors.BashrcNotExistsError()

def bashrc_func_exists(contexts: mapi.Contexts) -> None:
    bash_func = bashrc.load_bash_func(contexts.custom_paths)
    bashrc_path = Path(contexts.home_path) / ".bashrc"

    with open(bashrc_path, encoding='utf-8') as f:
        if bash_func in f.read():
            raise edk2_task_errors.BashrcFuncExistsError()

def add_bashrc_func(contexts: mapi.Contexts) -> None:
    bash_func = bashrc.load_bash_func(contexts.custom_paths)
    bashrc_path = Path(contexts.home_path) / ".bashrc"

    with open(bashrc_path, "a", encoding='utf-8') as f:
        f.write(bash_func)

def load_bash_func(custom_path: CustomPaths) -> str:
    return dedent(f"""
        # section_auto_setup_tde
        export EDK_TOOLS_PATH={custom_path.EDK2_PATH}/BaseTools
        pushd {custom_path.EDK2_PATH} > /dev/null
        source edksetup.sh BaseTools > /dev/null
        popd > /dev/null
        # section_auto_setup_tde_end
""")

