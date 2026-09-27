from collections.abc import Generator
from contextlib import contextmanager

from modules.console import console


@contextmanager
def step_status(
    description: str
    ) -> Generator[None, object, None]:
    with console.status(f"{description}", spinner='bouncingBar', speed=0.5):
        try:
            yield
            console.print(
                f"[green][ OK ][/green] {description}"
                )
        except Exception:
            console.print(
                f"[bold red][FAIL][/bold red] {description}"
                )
            raise
