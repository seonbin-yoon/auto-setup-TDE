
from modules import mapi
from packages.edk2 import bashrc


def load_func_tasks() -> list[mapi.FunctionTask]:
    bashrc_exists = mapi.FunctionTask(
        explain_message="Check if the bashrc file exists",
        func=bashrc.bashrc_exists
    )

    bashrc_func_exists = mapi.FunctionTask(
        explain_message="Check the bashrc file to see if there is a"
        "function that automatically enables the edk2 build environment.",
        func=bashrc.bashrc_func_exists
    )

    add_bashrc_func = mapi.FunctionTask(
        explain_message="Add a function to automatically "
        "enable the edk2 build environment to bashrc",
        func=bashrc.add_bashrc_func
    )

    return [
        bashrc_exists,
        bashrc_func_exists,
        add_bashrc_func
    ]
