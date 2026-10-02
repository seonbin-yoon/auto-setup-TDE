from textwrap import dedent

from modules.mapi import CustomPaths


def load_bash_func(custom_path: CustomPaths) -> str:
    return dedent(f"""
        # section_auto_setup_tde
        export EDK_TOOLS_PATH={custom_path.EDK2_PATH}/BaseTools
        function setup_edk2() {{
            local current_dir=$(pwd)
            cd {custom_path.EDK2_PATH}/edk2
            source edksetup.sh BaseTools
            cd $current_dir
            clear
        }}

        setup_edk2
        # section_auto_setup_tde_end
    """).strip()
