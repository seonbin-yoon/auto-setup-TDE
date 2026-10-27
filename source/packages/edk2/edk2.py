from pathlib import Path

from errors import edk2_task_errors, task_errors
from modules import mapi, shell, status, timer
from modules.console import console
from packages.edk2 import func_cmds, package_lists, shell_cmds


def pre_check(edk2_path: Path) -> None:
    console.print("[bold cyan]--- Pre-installation inspection ---[/bold cyan]")
    with status.step_status(
        "Checking to see if the edk2 folder already exists in the target folder.."
        ):
        if edk2_path.exists():
            raise edk2_task_errors.Edk2ExistsError(str(edk2_path))

def start(contexts: mapi.Contexts) -> None:
    console.print(
        "[bold cyan]--- Let's get started with setting up the "
        "edk2 compilation environment for ToolOS development ---[/bold cyan]"
        )

    start_time = timer.now_time()
    pkg_man = contexts.package_manager.impl
    must_to_install_pkgs = package_lists.NEED_PACKAGES[contexts.package_manager]
    env = pkg_man.load_envs()

    with status.step_status("Checking for missing apt packages on the device.."):
        missing_pkgs = pkg_man.get_missing_packages(must_to_install_pkgs)

    console.print(
        "[yellow][NOTE] Must install the following packages[/yellow]: "
        f"{", ".join(must_to_install_pkgs)}",
        highlight=False)
    console.print(
        "[yellow][NOTE] Missing packages on the device[/yellow]: "
        f"{', '.join(sorted(missing_pkgs))
        if missing_pkgs else 'None'}",
        highlight=False)

    if contexts.run_on_docker:
        console.print(
        "[yellow][NOTE] This script is currently "
        "running inside a Docker container. "
        "The package installation will be reset "
        "when the container is restarted.[/yellow]"
        )

    shell_tasks = pkg_man.load_shell_tasks(
        contexts.run_on_root,
        contexts.home_path,
        missing_pkgs
        )

    shell_tasks.extend(shell_cmds.load_shell_tasks(contexts))

    for shell_task in shell_tasks:
        with status.step_status(shell_task.explain_message):
            result = shell.run(shell_task.command, cwd=shell_task.path, env=env)
            if result.returncode:
                raise task_errors.FailedRunError(shell_task.command, result.stderr)

    func_tasks = func_cmds.load_func_tasks()
    for func_task in func_tasks:
        try:
            with status.step_status(func_task.explain_message):
                func_task.func(contexts)
        except edk2_task_errors.BashrcFuncExistsError as e:
            console.print(str(e))
            break

    console.print(
        "[yellow][NOTE] source ~/.bashrc or logout and "
        "back in for the changes to take effect![/yellow]"
        )
    console.print(
        "[green][DONE][/green] Finished setting "
        "up the edk2 compilation environment."
        )
    console.print(f"Spend time: {timer.spend_time_str(start_time, timer.now_time())}")
