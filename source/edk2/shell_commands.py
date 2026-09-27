from modules import mapi


def load_shell_tasks(contexts: mapi.Contexts) -> list[mapi.ShellTask]:
    git_clone = mapi.ShellTask(
        explain_message= "Download the edk2 source code",
        command= [
            "git",
            "clone",
            "--depth",
            "1",
            "https://github.com/tianocore/edk2",
            f"{contexts.custom_paths.EDK2_PATH}"
            ],
        path= contexts.home_path,
    )

    git_init = mapi.ShellTask(
        explain_message= "Initialize a Submodule",
        command = ["git", "submodule", "update", "--init"],
        path= contexts.custom_paths.EDK2_PATH,
    )

    complie_base_tools = mapi.ShellTask(
                explain_message = "Compilie the Build Tool",
                command = ["make", "-C", "BaseTools"],
                path = contexts.custom_paths.EDK2_PATH,
    )

    edksetup_sh = mapi.ShellTask(
                explain_message = "Run edksetup.sh",
                path = contexts.custom_paths.EDK2_PATH,
                command  = ["bash", "-c", "source edksetup.sh"],
    )

    complie_base_tools2 = mapi.ShellTask(
                explain_message = "Compilie the Build Tool x2",
                command = ["make", "-C", "BaseTools"],
                path = contexts.custom_paths.EDK2_PATH,
    )

    return [
        git_clone,
        git_init,
        complie_base_tools,
        edksetup_sh,
        complie_base_tools2
    ]

