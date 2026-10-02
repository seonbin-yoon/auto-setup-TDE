# Automatic Setup of the ToolOS Development Environment

## Description of this program
- This program was created for developers who wish to contribute to the development of ToolOS.
It automatically configures the environment so that developers do not have to go through the tedious process of manually setting up Edk2—the bootloader framework used by ToolOS—and the QEMU emulator.

## How to Use
1. Clone the ToolOS repository. - `https://github.com/seonbin-yoon/ToolOS`
2. Copy the `global.cfg.example` file located at the root of the ToolOS source tree to `global.cfg`.
3. The `global.cfg` file contains a [path] section. The two values listed in this section, `QEMU_WORKSPACE` and `EDK2_SRC`, are used by the program, so please modify these values to match your environment.
4. After cloning this repository,
navigate to the `bin/installer.dist` folder and
run `installer.bin` with the appropriate arguments to start the installer.
- Example: `./bin/installer.dist/installer.bin --cfg-file-path=~/ToolOS/global.cfg --install-options=edk2`

#### Program Arguments
* `cfg-file-path`: Enter the path to `global.cfg` in the ToolOS source tree.
* `install-options`: Select the development environment you want to configure. You can choose either edk2 or qemu.

## Special Notes
* **This program is not suitable for typical Edk2 development environments. It does not automatically generate target.txt, dsc, and inf files.**
* Note that when entering the path to `global.cfg`, if the filename at the end of the path is not `global.cfg` or is not left blank—for example, **if there is a typo such as `global.cfh`—the program may not be able to locate the configuration file correctly.**
* If the [path] section of the `global.cfg` file
contains a path value that does not follow the format below,
**the program may malfunction.**
- `../ToolOS/`
- `./ToolOS/global.cfg`
- `/home/user/ToolOS`
- `~/ToolOS`
- `$HOME/ToolOS`

## Contributions
* I welcome feedback. If you’d like to provide feedback, please contact me at seonbin.yoon0@gmail.com.