from modules.mapi import CustomPaths


def load_bash_func(custom_path: CustomPaths) -> str:
    return "\n".join((
        "# section_edk2",
        f"export EDK_TOOLS_PATH={custom_path.EDK2_PATH}/edk2/BaseTools",
        "function setup_edk2() {",
        "    local current_dir=$(pwd)",
        f"   cd {custom_path.EDK2_PATH}/edk2",
        "    source edksetup.sh BaseTools",
        "    cd $current_dir",
        "    clear",
        "}",
        "",
        "setup_edk2",
        "# section_end",
    ))
