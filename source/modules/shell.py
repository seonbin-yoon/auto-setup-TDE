import subprocess
from pathlib import Path


def run(cmds: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmds,
        cwd=cwd,
        capture_output=True,
        text=True
    )

