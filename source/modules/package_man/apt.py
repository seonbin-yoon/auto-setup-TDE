import os
from functools import lru_cache
from pathlib import Path

from modules import mapi, shell


@lru_cache(maxsize=1)
def _get_installed_package_set() -> set[str]:
    result = shell.run(
        ["dpkg-query", "-W", "-f=${Package}\t${db:Status-Status}\n"]
    )

    return {
        parts[0]
        for parts in (
            line.split("\t")
            for line in result.stdout.strip().splitlines()
            if line
        )
        if parts[1] == "installed"
    }

def get_missing_packages(must_to_install_pkgs: list[str]) -> list[str]:
    return [
        pkg for pkg in must_to_install_pkgs if pkg not in _get_installed_package_set()
    ]

def load_envs() -> dict[str, str]:
    env = os.environ.copy()
    env["DEBIAN_FRONTEND"] = "noninteractive"
    return env

def load_shell_tasks(
        run_on_root: bool,
        home_path: Path,
        missing_pkgs: list[str]) \
        -> list[mapi.ShellTask]:
    sudo_prefix = [] if run_on_root else ["sudo", "-E"]

    apt_update_command = [
        *sudo_prefix,
        "apt-get",
        "update"
    ]

    apt_install_command = [
        *sudo_prefix,
        "apt-get",
        "install",
        "-y",
        "--no-install-recommends",
        *missing_pkgs
    ]

    apt_update = mapi.ShellTask(
        explain_message="Update the apt cache",
        path=home_path,
        command=apt_update_command
    )

    apt_install = mapi.ShellTask(
            explain_message="Install Required Packages",
            path=home_path,
            command=apt_install_command
        )

    return [
        apt_update,
        apt_install
    ]
