from modules.mapi import PackageManager

NEED_PACKAGES = {
    PackageManager.APT: [
        "acpica-tools",
        "build-essential",
        "ca-certificates",
        "clang",
        "curl",
        "git",
        "lld",
        "llvm",
        "llvm-dev",
        "uuid-dev"
    ],
    PackageManager.DNF: [
        "@development-tools",
        "acpica-tools",
        "clang",
        "git",
        "libuuid-devel",
        "lld",
        "llvm",
        "llvm-devel",
    ]
}
