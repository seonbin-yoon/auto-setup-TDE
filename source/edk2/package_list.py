from modules.mapi import PackageManager

NEED_PACKAGES = {
    PackageManager.APT: [
        "build-essential",
        "llvm",
        "llvm-dev",
        "lld",
        "uuid-dev",
        "acpica-tools",
        "clang",
        "clangd",
        "gdb-multiarch",
        "bear"
    ],
    PackageManager.DNF: [
    "@development-tools",  # Ubuntu의 build-essential 대체 (그룹 패키지)
    "llvm",
    "llvm-devel",          # llvm-21-dev 대체 (Fedora는 기본적으로 최신 llvm-devel 사용)
    "lld",
    "libuuid-devel",       # uuid-dev 대체
    "acpica-tools",
    "clang",
    "qemu-system-aarch64", # aarch64 지원을 위해 추가 분리된 패키지 포함
    "edk2-aarch64",        # qemu-efi-aarch64 대체
    "clang-tools-extra",   # clangd를 포함하는 패키지
    "gdb",                 # gdb-multiarch 대체 (Fedora의 기본 gdb는 멀티아키텍처 지원)
    "bear"
    ]
}
