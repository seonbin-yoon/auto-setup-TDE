import subprocess
from pathlib import Path


def run(
        cmds: list[str],
        cwd: Path | None = None,
        env: dict[str, str] | None = None
        ) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmds,
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True
    )
