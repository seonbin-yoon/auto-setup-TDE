from enum import Enum
from typing import Annotated

import typer

from errors import init_errors
from modules import init
from modules.exit import program_exit


class InstallOption(str, Enum):
    edk2 = "edk2"
    qemu = "qemu"

app = typer.Typer()

@app.command()
def install(
    cfg_file_path: Annotated[
        str,
        typer.Option(help="ToolOS source tree `global.cfg` file location")],
    install_options: Annotated[
        InstallOption,
        typer.Option(help="Types of Build Environments to Setup")
    ]
    ) -> None:
    """Setup your build environment."""

    try:
        program_contexts = init.init(cfg_file_path)
    except init_errors.InitError as e:
        program_exit(1, e)

    match install_options:
        case InstallOption.edk2:
            from edk2 import edk2
            edk2.pre_check(program_contexts.custom_paths.EDK2_PATH)
            edk2.start(program_contexts)
        case InstallOption.qemu:
            from qemu import qemu
            qemu.pre_check(program_contexts.custom_paths.QEMU_PATH)
            qemu.start(program_contexts)

if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        program_exit(130)
    except Exception as e:
        program_exit(
            1,
            "An error occurred while running the program.\n" \
            f"{e}"
        )
