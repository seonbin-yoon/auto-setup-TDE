import importlib
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from functools import cached_property
from pathlib import Path
from typing import Protocol, cast


@dataclass(slots=True, frozen=True)
class CustomPaths:
    EDK2_PATH: Path
    QEMU_PATH: Path

@dataclass(slots=True, frozen=True)
class ShellTask:
    explain_message: str
    path: Path
    command: list[str]

@dataclass(slots=True, frozen=True)
class FunctionTask:
    explain_message: str
    func: Callable[..., object]

class PackageManagerImpl(Protocol):
    def load_shell_tasks(
            self,
            run_on_root: bool,
            home_path: Path,
            need_to_install_packages: list[str]
            ) -> list[ShellTask]: ...
    def get_missing_packages(
            self,
            must_to_install_pkgs: list[str]
            ) -> list[str]: ...

class PackageManager(Enum):
    APT = "apt"
    DNF = "dnf"

    @cached_property
    def impl(self) -> PackageManagerImpl:
        return cast(
            PackageManagerImpl,
            importlib.import_module(f"modules.package_man.{self.value}")
            )

@dataclass(slots=True, frozen=True)
class Contexts:
    run_on_root: bool
    run_on_docker: bool
    custom_paths: CustomPaths
    package_manager: PackageManager
    home_path: Path
    program_path: Path


