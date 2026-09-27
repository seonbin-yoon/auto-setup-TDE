from modules import mapi


def _make_qemu_dir(contexts: mapi.Contexts) -> None:
    new_path = contexts.custom_paths.QEMU_PATH / "hda-contents" / "EFI" / "BOOT"
    new_path.mkdir(parents=True)

def load_func_tasks() -> list[mapi.FunctionTask]:
    make_qemu_dir = mapi.FunctionTask(
        explain_message="Create a QEMU working directory",
        func=_make_qemu_dir
        )

    return [make_qemu_dir]
