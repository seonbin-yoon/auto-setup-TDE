from errors import task_errors
from modules import mapi, shell, status, timer
from modules.console import console
from packages.extras import package_lists


def start(contexts: mapi.Contexts) -> None:
    console.print(
        "[bold cyan]--- Let's get started with setting up the "
        "extra development tools for ToolOS ---[/bold cyan]"
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

    if missing_pkgs:
        if contexts.run_on_docker:
            console.print(
            "[yellow][NOTE] This script is currently " \
            "running inside a Docker container. " \
            "The package installation will be reset " \
            "when the container is restarted.[/yellow]"
            )
        shell_tasks = pkg_man.load_shell_tasks(
            contexts.run_on_root,
            contexts.home_path,
            missing_pkgs
            )

        for shell_task in shell_tasks:
            with status.step_status(shell_task.explain_message):
                result = shell.run(shell_task.command, cwd=shell_task.path, env=env)
                if result.returncode:
                    raise task_errors.FailedRunError(shell_task.command, result.stderr)

    console.print(
        "[green][DONE][/green] Finished setting "
        "up the extra development tools."
        )
    console.print(f"Spend time: {timer.spend_time_str(start_time, timer.now_time())}")
