from functools import lru_cache
from pathlib import Path

from modules import mapi, shell


@lru_cache(maxsize=1)
def get_installed_package_set() -> set[str]:
    result = shell.run(
        ["dpkg-query", "-W", "-f=${Package}\t${db:Status-Status}\n"]
    )

    installed: set[str] = set()
    for line in result.stdout.strip().splitlines():
        parts = line.split("\t")
        if len(parts) == 2 and parts[1] == "installed":
            installed.add(parts[0])

    return installed

def _is_package_installed(package_name: str) -> bool:
    return package_name in get_installed_package_set()

def get_missing_packages(must_to_install_pkgs: list[str]) -> list[str]:
    return [pkg for pkg in must_to_install_pkgs if not _is_package_installed(pkg)]

def load_shell_tasks(
        run_on_root: bool,
        home_path: Path,
        need_to_install_packages: list[str]) \
    -> list[mapi.ShellTask]:
    apt_update_command = [
        "apt-get",
        "update"
    ]

    apt_install_command = [
        "apt-get",
        "install",
        "-y",
        "--no-install-recommends",
        *need_to_install_packages
    ]

    if not run_on_root:
        apt_update_command.insert(0, "sudo")
        apt_install_command.insert(0, "sudo")

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
