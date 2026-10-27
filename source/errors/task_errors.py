class TaskError(Exception):
    """작업 실행과 관련된 모든 에러"""

class FailedRunError(TaskError):
    """작업 실행에 실패함"""
    def __init__(self, command: list[str], stderr: str) -> None:
        super().__init__(
            f"[red][ERROR][/red]: The command '{" ".join(command)}' failed to execute."
            "\n\n*** stderr ***\n"
            f"{stderr}"
        )
