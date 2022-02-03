# PycOS

An open source operating system (mostly just a GUI) designed primarily for the Raspberry Pi Pico, written entirely in MicroPython.

"PycOS" is an combination of the words Python, Pico and OS.

**Currently in a semi-working state, with a few incomplete features.**

## Overview

### Features

* Support for custom themes
* Dedicated configuration file
* Overclocking/underclocking support
* Quick access to bootloader
* Support for custom scripts

### Future plans

* Further UI improvements
* More customisation options
* Improved scripting support
* Desktop client for easy interfacing with the device

## Compatibility

| Displays | Compatible | Notes |
|---|---|---|
| [Pimoroni Pico Display Pack](https://shop.pimoroni.com/products/pico-display-pack) | Yes (tested) | Everything functions correctly |
| [Pimoroni Pico Display Pack 2.0](https://shop.pimoroni.com/products/pico-display-pack-2-0) | No (working on compatibility)| Requires a different display module to work and UI elements are not fully optimised |

| Boards | Compatible | Notes |
|---|---|---|
| [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) | Yes (tested) | Everything functions correctly |
| [Pimoroni Pico LiPo](https://shop.pimoroni.com/products/pimoroni-pico-lipo) | Yes (tested) | Everything functions correctly |

| Firmware | Compatible | Notes |
|---|---|---|
| [Version 0.3.2 (MicroPython v1.17)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.3.2) | Yes (tested) | If you experience problems with Version 0.3.x (MicroPython v1.17) use [Version 0.2.7 (MicroPython v1.16)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.7) as backup. |
| [Version 0.3.1 (MicroPython v1.17)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.3.1) | Yes (tested) | If you experience problems with Version 0.3.x (MicroPython v1.17) use [Version 0.2.7 (MicroPython v1.16)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.7) as backup. |
| [Version 0.3.0 (MicroPython v1.17)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.3.0) | Yes (tested) | If you experience problems with Version 0.3.x (MicroPython v1.17) use [Version 0.2.7 (MicroPython v1.16)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.7) as backup. |
| [Version 0.2.7 (MicroPython v1.16)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.7) | Yes (tested) | Everything functions correctly |
| [Version 0.2.6 (MicroPython v1.16)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.6) | Yes (tested) | Everything functions correctly |
| [Version 0.2.5 (MicroPython v1.16)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.5) | Yes (tested) | Everything functions correctly |
| [Version 0.2.4 (MicroPython v1.16)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.4) | Yes (tested) | Everything functions correctly |
| [Version 0.2.3 (MicroPython v1.16)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.3) | Yes (tested) | Everything functions correctly |
| [Version 0.2.2 (MicroPython v1.15)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.2) | Yes (tested) | Everything functions correctly |
| [Version 0.2.1 (MicroPython v1.15)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.1) | Yes (tested) | Everything functions correctly |
| [Version 0.2.0 (MicroPython v1.15)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.0) | Yes (tested) | Everything functions correctly |

## Requirements

### Hardware requirements

* [Pimoroni Pico Display Pack](https://shop.pimoroni.com/products/pico-display-pack) (or any other compatible display)
* [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) (or any other compatible board)
* USB data cable

### Software requirements

* [rshell](https://github.com/dhylands/rshell) ([can be installed through pip](https://pypi.org/project/rshell/))
* [mpy-cross](https://gitlab.com/alelec/mpy_cross) ([can be installed through pip](https://pypi.org/project/mpy-cross/))

## Installation

**This is a temporary solution until the PycOS client is complete.**

1. Connect the board to your computer and check that [rshell](https://github.com/dhylands/rshell) recognises the board

        rshell boards

1. Clone the repository

        git clone https://github.com/Coosta6915/PycOS.git

2. Change directory to `tools/{your_os}`

        cd PycOS/tools/windows

    or

        cd PycOS/tools/linux

3. Configure options in `config.py`

4. Run `py2mpy.py`

5. Run `py2mpy.cmd` or `py2mpy.sh` (will be created after `py2mpy.py` is run)

6. Run `cpbuild.py`

7. Run `cpbuild.cmd` or `cpbuild.sh` (will be created after `cpbuild.py` is run)

## Images

![PycOS running on a Raspberry Pi Pico](assets/boards.jpg)
