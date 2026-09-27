class InitError(Exception):
    """초기화와 관련된 모든 에러"""

class UnsupportedOSError(InitError):
    """지원되지 않는 OS"""
    def __init__(self, os: str) -> None:
        super().__init__(
            f"[red][ERROR][/red]: {os} is not a supported operating system.\n\n"
            "Among Linux distributions, this script only supports " \
            "those that use dnf or apt as their package manager."
            )

class UnsupportedDistroError(InitError):
    """지원되지 않는 OS"""
    def __init__(self, distro: str) -> None:
        super().__init__(
            f"[red][ERROR][/red]: {distro} is an unsupported Linux distribution.\n\n"
            "Among Linux distributions, this script only supports " \
            "those that use dnf or apt as their package manager."
            )

class SudoError(InitError):
    """Sudo 인증 실패함"""
    def __init__(self) -> None:
        super().__init__("Sudo auth failed")

class NoRootPrivilegesError(InitError):
    """root 권한이 없음"""
    def __init__(self) -> None:
        super().__init__(
            "[red][ERROR][/red]: Ran the script in a redirection " \
            "environment without root privileges."
            )

class ConfigNotFoundError(InitError):
    """설정 파일을 찾을 수 없음"""
    def __init__(self, cfg_file_path: str) -> None:
        super().__init__(
            f"The configuration file cannot be found.\n"
            f"{cfg_file_path}: Is this where the configuration file is located?"
            )

class ConfigReadError(InitError):
    """설정 파일을 읽을 수 없음"""
    def __init__(self, cfg_file_path: str) -> None:
        super().__init__(f"Failed to read config file: {cfg_file_path}")

class SectionNotFoundError(InitError):
    """설정 파일에 찾는 섹션이 없음"""
    def __init__(self, section: str) -> None:
        super().__init__(f"Missing required section: {section}")

class MissingConfigKeyError(InitError):
    """설정 파일에 키가 없거나 값이 비어있음"""
    def __init__(self, key: str, section: str) -> None:
        super().__init__(f"Missing or empty key: '{key}' in [{section}]")

class EmptyExpandedPathError(InitError):
    """환경변수 치환 결과가 빈 문자열음"""
    def __init__(self, key: str, value: str) -> None:
        super().__init__(f"Path expanded to empty string for key: '{key}': '{value}'")

class UnresolvedEnvVarError(InitError):
    """환경변수 표기가 치환되지 않고 남아있음"""
    def __init__(self, key: str, value: str, var_name: str):
        super().__init__(
            f"Unresolved environment variable '{var_name}' for key: '{key}': '{value}'"
        )

class InvalidPathStructureError(InitError):
    """치환은 됐지만 경로 구조 자체가 유효하지 않음"""
    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value
        super().__init__(f"Invalid path structure for '{key}': '{value}'")

