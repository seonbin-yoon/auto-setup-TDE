import sys
from typing import NoReturn

from modules.console import console


def program_exit(exit_code: int = 0, message: object = None) \
    -> NoReturn:

    if message and exit_code:
        console.print("[red]" + "-" * 50 + "ERROR" + "-" * 50 + "[/red]")
        console.print(str(message), highlight=False)
        console.print("[red]" + "-" * 50 + "ERROR" + "-" * 50 + "[/red]")
    elif message and not exit_code:
        console.print(str(message), highlight=False)

    sys.exit(exit_code)
