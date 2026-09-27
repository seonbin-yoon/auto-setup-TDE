class QemuTaskError(Exception):
    """QEMU와 관련된 모든 에러"""

class QemuExistsError(QemuTaskError):
    """QEMU가 이미 존재함"""
    def __init__(self, folder: str) -> None:
        super().__init__(
            f"[red][ERROR][/red]: The {folder} folder "
            "already exists in the target folder."
        )
