class Edk2TaskError(Exception):
    """EDK2와 관련된 모든 에러"""

class BashrcNotExistsError(Edk2TaskError):
    """bashrc가 존재하지 않음"""
    def __init__(self) -> None:
        super().__init__(
            "[red][ERROR][/red]: The `.bashrc` file does not exist in the home folder."
        )

class BashrcFuncExistsError(Edk2TaskError):
    """edk2 빌드 환경 자동 활성화 함수가 bashrc에 이미 존재함"""
    def __init__(self) -> None:
        super().__init__(
            "[yellow][NOTE] Since there is already a function in bashrc that " \
            "automatically activates the edk2 build environment, " \
            "will skip this step.[/yellow]"
        )

class Edk2ExistsError(Edk2TaskError):
    """EDK2 폴더가 이미 존재함"""
    def __init__(self, folder: str) -> None:
        super().__init__(
            f"[red][ERROR][/red]: The {folder} folder "
            "already exists in the target folder."
        )

