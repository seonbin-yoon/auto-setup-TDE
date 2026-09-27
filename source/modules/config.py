import configparser
import os
import re
from pathlib import Path

from errors import init_errors
from modules import mapi

__VAR_PATTERN = re.compile(r'\$(\w+|\{[^}]*\})')

def _try_to_path(paths: configparser.SectionProxy, key: str) -> Path:
    raw_path = paths.get(key, "").strip()
    if not raw_path:
        raise init_errors.MissingConfigKeyError(key, "path")

    expanded_path = os.path.expandvars(raw_path).strip()
    if not expanded_path:
        raise init_errors.EmptyExpandedPathError(key, raw_path)

    leftover = __VAR_PATTERN.search(expanded_path)
    if leftover:
        raise init_errors.UnresolvedEnvVarError(key, raw_path, leftover.group())

    try:
        resolved_path = Path(expanded_path).expanduser().resolve()
    except (ValueError, TypeError) as e:
        raise init_errors.InvalidPathStructureError(key, raw_path) from e

    return resolved_path

def load_config(cfg_file_path: str) -> mapi.CustomPaths:
    expanded_path = os.path.expandvars(cfg_file_path)
    cfg_file = Path(expanded_path).expanduser().resolve()

    if cfg_file.name != "global.cfg":
        cfg_file = cfg_file / "global.cfg"

    if not cfg_file.exists() or not cfg_file.is_file():
        raise init_errors.ConfigNotFoundError(str(cfg_file))

    parser = configparser.ConfigParser()

    read_files = parser.read(cfg_file)
    if not read_files:
        raise init_errors.ConfigReadError(str(cfg_file))

    if not parser.has_section("path"):
        raise init_errors.SectionNotFoundError("path")

    paths = parser["path"]

    return mapi.CustomPaths(
        EDK2_PATH=_try_to_path(paths, "EDK2_SRC"),
        QEMU_PATH=_try_to_path(paths, "QEMU_WORKSPACE")
    )
