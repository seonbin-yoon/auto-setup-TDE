from functools import lru_cache
from pathlib import Path

from modules import mapi, shell


@lru_cache(maxsize=1)
def _get_installed_package_set() -> set[str]:
    installed: set[str] = set()

    # 1. 설치된 단일 RPM 패키지 목록 가져오기
    # --queryformat "%{NAME}\n"을 사용하여 패키지 이름만 추출
    rpm_result = shell.run(
        ["rpm", "-qa", "--queryformat", "%{NAME}\n"]
    )
    for line in rpm_result.stdout.strip().splitlines():
        installed.add(line.strip())

    # 2. 설치된 DNF 패키지 그룹 목록 가져오기
    # -v 옵션으로 그룹 ID(예: development-tools)를 파악
    group_result = shell.run(
        ["dnf", "group", "list", "-v", "--installed", "-q"]
    )
    for line in group_result.stdout.strip().splitlines():
        if "(" in line and ")" in line:
            # 출력 예: "   Development Tools (development-tools)"
            # 그룹 ID만 추출하여 "@"를 붙여 세트에 추가
            group_id = line.split("(")[-1].split(")")[0].strip()
            installed.add(f"@{group_id}")

    return installed

def _is_package_installed(package_name: str) -> bool:
    return package_name in _get_installed_package_set()

def get_missing_packages(must_to_install_pkgs: list[str]) -> list[str]:
    return [pkg for pkg in must_to_install_pkgs if not _is_package_installed(pkg)]


def load_shell_tasks(
        run_on_root: bool,
        home_path: Path,
        need_to_install_packages: list[str]) \
    -> list[mapi.ShellTask]:
    dnf_install_command = [
        "dnf",
        "install",
        "-y",
        "--setopt=install_weak_deps=False",
        *need_to_install_packages,
    ]

    if not run_on_root:
        dnf_install_command.insert(0, "sudo")

    dnf_install = mapi.ShellTask(
        explain_message="Install Required Packages",
        path=home_path,
        command=dnf_install_command,
    )

    return [dnf_install]
