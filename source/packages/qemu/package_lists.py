from modules.mapi import PackageManager

NEED_PACKAGES = {
    PackageManager.APT: [
        "qemu-system-arm",
        "qemu-efi-aarch64",
    ],
    PackageManager.DNF: [
        "edk2-aarch64",
        "qemu-system-aarch64"
    ]
}
