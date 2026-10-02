import os
import platform
import sys
from pathlib import Path

import distro
from errors import init_errors

from modules import config, mapi, shell, status
from modules.console import console


def _run_on_docker() -> bool:
    return Path('/.dockerenv').exists()

def _run_on_root() -> bool:
    return os.geteuid() == 0

def _get_linux_distro() -> mapi.PackageManager:
    current_os = platform.system()

    if current_os != "Linux":
        raise init_errors.UnsupportedOSError(current_os)

    linux_distro = distro.id().lower()

    match linux_distro:
        case "debian" | "ubuntu":
            return mapi.PackageManager.APT
        case "rhel" | "fedora":
            return mapi.PackageManager.DNF
        case _:
            raise init_errors.UnsupportedDistroError(linux_distro)

def init(cfg_file_path: str) -> mapi.Contexts:
    if not console.is_terminal:
        console.print("The program starts in automatic mode")
    else:
        console.clear()

    console.print(
        "[bold cyan]--- Checks the conditions " \
        "under which the script runs ---[/bold cyan]"
        )

    linux_distro = _get_linux_distro()

    if not console.is_terminal and not _run_on_root():
        with status.step_status("Check root privileges in redirection environment"):
            raise init_errors.NoRootPrivilegesError()

    if not _run_on_root():
        with status.step_status("Borrow Root Privileges for Package Installation"):
            if shell.run(["sudo", "-v"]).returncode:
                raise init_errors.SudoError()

    with status.step_status("Collect runtime context"):
        return mapi.Contexts(
            run_on_root=_run_on_root(),
            run_on_docker=_run_on_docker(),
            custom_paths=config.load_config(cfg_file_path),
            package_manager=linux_distro,
            home_path=Path.home(),
            program_path=Path(sys.argv[0]).absolute(),
        )

