# PycOS

An open source operating system (mostly just a GUI) designed primarily for the Raspberry Pi Pico, written entirely in MicroPython.

## Overview

**Currently in [alpha](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha), with a lot of incomplete features.**

"PycOS" is an combination of the words Python, Pico and OS.

### Features

* Overclocking/underclocking support
* Quick bootloader access
* Editable configuration file

### Future plans

* User interface improvements
* More customisation options
* Hardware specific features/versions

## Requirements

### Hardware requirements

* [Compatible display](#Compatibility)
* [Compatible board](#Compatibility)
* Data cable

### Software requirements

* [rshell](https://pypi.org/project/rshell/)
* [mpy-cross](https://pypi.org/project/mpy-cross/)

## Compatibility

| Displays | Compatible? | Notes |
|---|---|---|
| [Pimoroni Pico Display Pack](https://shop.pimoroni.com/products/pico-display-pack) | Yes (tested) | |
| [Pimoroni Pico Display Pack 2.0](https://shop.pimoroni.com/products/pico-display-pack-2-0) | No | ~~Requires a different display driver to work~~ [Pull request #327](https://github.com/pimoroni/pimoroni-pico/pull/327) fixes this issue, but code still requires rewriting |

| Boards | Compatible? | Notes |
|---|---|---|
| [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) | Yes (tested) | |
| [Raspberry Pi Pico H](https://www.raspberrypi.com/products/raspberry-pi-pico/) | Yes | Similar to the original variant, so most likely works |
| [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) | Yes | Similar to the original variant, so most likely works |
| [Pimoroni Pico LiPo (4MB)](https://shop.pimoroni.com/products/pimoroni-pico-lipo?variant=39386149093459) | Yes | Similar to the 16MB variant, so most likely works |
| [Pimoroni Pico LiPo (16MB)](https://shop.pimoroni.com/products/pimoroni-pico-lipo?variant=39335427080275) | Yes (tested) | |

| Firmware (Excluding pre-releases) | Compatible? | Notes |
|---|---|---|
| [Version 1.19.x](https://github.com/pimoroni/pimoroni-pico/releases/tag/v1.19.6) | No | [Display driver code refactor](https://github.com/pimoroni/pimoroni-pico/pull/327) |
| [Version 1.18.x](https://github.com/pimoroni/pimoroni-pico/releases/tag/v1.18.7) | Yes (tested) | |
| **Legacy** | | |
| [Version 0.3.x (MicroPython v1.17)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.3.3) | Yes (tested) | |
| [Version 0.2.x (MicroPython v1.15/v1.16)](https://github.com/pimoroni/pimoroni-pico/releases/tag/v0.2.7) | Yes (tested) | |

## Installation

Ensure your board is running compatible firmware and is detected by `rshell`.

1. Clone the repository

        git clone https://github.com/Coosta6915/PycOS.git

2. Change directory into `pycos/`

        cd PycOS/pycos/

3. Use `rshell` to synchronise the board with the currect directory

        rshell rsync --mirror . /pyboard

## Images

![PycOS running on a Raspberry Pi Pico](assets/boards.jpg)
