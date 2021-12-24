## Usage

### MicroPython scripts

Currently the support for user-written programs is very restricted because of the limitation of MicroPython. Custom scripts can be prefixed with `Pp_` (stands for Pico program) and placed into the root directory for PycOS to recognise it as an executable program. The code must all be placed inside a `main()` function as that is what gets executed.

**Currently, there does not seem to be a way to update the display while PycOS is running a script.**

### UF2 files

A `.uf2` file can be loaded onto the board for executing C/C++ binaries. This can be done by putting the board in bootloader mode and copying the file onto the boards storage.

**This will overwrite the MicroPython firmware so you will have to flash it again after.**

### config.py

`config.py` is the configuration file PycOS uses. It is located in the root directory (of the board) and contains variables in the standard Python syntax. It allows for quick editing of basic system functionality as well as the UI theme, without having to directly modify `main.py`. Each variable is explained within the file as well as its default and recommended values.

### boot.py

The default order of file execution in MicroPython is:

1. `boot.py` (executed when the board boots up)
2. `main.py` (executed after `boot.py`)

PycOS is stored in `main.py`, leaving `boot.py` empty for modifications.

If you choose to, you can write your own boot script to be executed prior to `main.py` and copy it onto the board.

    rshell cp boot.py /pyboard

You can check if there is a boot file on the board by going into the advanced about menu (Menu > About > More info > Advanced).

To delete the `boot.py` file, run [rshell](https://github.com/dhylands/rshell), change directory into `/pyboard`, and remove the file.

    rshell
    cd /pyboard
    rm boot.py
    