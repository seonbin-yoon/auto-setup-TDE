# Automatic Setup of the ToolOS Development Environment

## Description of this program
- This program was created for developers who wish to contribute to the development of ToolOS.
It automatically configures the environment so that developers do not have to go through the tedious process of manually setting up Edk2—the bootloader framework used by ToolOS—and the QEMU emulator.

## Prerequisites & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/seonbin-yoon/ToolOS
```

### 2. Create the Configuration File
Copy the `global.cfg.example` file located at the root of the ToolOS source tree to `global.cfg`.
```bash
cp global.cfg.example global.cfg
```

### 3. Configure the Environment Paths
The `global.cfg` file contains a `[path]` section. The two values listed in this section, `QEMU_WORKSPACE` and `EDK2_SRC`, are used by the program, so please modify these values to match your environment.
#### Example
```ini
EDK2_SRC=~/edk2
QEMU_WORKSPACE=~/qemu
```

### 4. Run the Installer
After cloning this repository, navigate to the `bin/setup.dist` folder and run `setup` with the appropriate arguments to start the installer.
#### Example:  
```bash
./bin/setup.dist/setup --cfg-file=~/ToolOS/global.cfg --install=edk2
```

#### Program Arguments
- `cfg-file`: Enter the path to `global.cfg` in the ToolOS source tree.
- `install`: Select the development environment you want to configure. You can choose `edk2`, `qemu`, or `extras`.
  - The `extras` option installs recommended development tools, including `bear`, `gdb`, and `clangd`.

## Special Notes
- **This program is not suitable for typical Edk2 development environments. It does not automatically generate target.txt, dsc, and inf files.**
- Note that when entering the path to `global.cfg`, if the filename at the end of the path is not `global.cfg` or is not left blank—for example, **if there is a typo such as `global.cfh`—the program may not be able to locate the configuration file correctly.**
- If the [path] section of the `global.cfg` file
contains a path value that does not follow the format below,
**the program may malfunction.**
- `.`
- `./global.cfg`
- `./ToolOS`
- `/home/user/ToolOS`
- `~/ToolOS`
- `${HOME}/ToolOS`

## Contributions
- I welcome feedback. If you’d like to provide feedback, please contact me at seonbin.yoon0@gmail.com.# Automatic Setup of the ToolOS Development Environment
