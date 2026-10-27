from modules.mapi import PackageManager

NEED_PACKAGES = {
    PackageManager.APT: [
        "bear",
        "clangd",
        "gdb-multiarch"
    ],
    PackageManager.DNF: [
        "bear",
        "clang-tools-extra",
        "gdb"
    ]
}
