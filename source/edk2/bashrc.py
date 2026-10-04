from textwrap import dedent

from modules.mapi import CustomPaths


def load_bash_func(custom_path: CustomPaths) -> str:
    return dedent(f"""
        \n# section_auto_setup_tde
        export EDK_TOOLS_PATH={custom_path.EDK2_PATH}/BaseTools
        pushd {custom_path.EDK2_PATH} > /dev/null
        source edksetup.sh BaseTools > /dev/null
        popd > /dev/null
        # section_auto_setup_tde_end
    """).strip()
