import picodisplay as screen

import machine
import os

from config import *
from system.sysdata import *
from system.gooey.manager import *


def display_home_screen():
    clear()
    screen.set_pen(255, 225, 225)
    screen.circle(0, int(screen.get_height() / 2), 100)
    screen.set_pen(255, 0, 0)
    screen.text("Pycos", 5, int(screen.get_height() / 2) - 10, (screen.get_width() - 5), 3)

    text("Menu >", 170, 100)
    refresh()


def display_main_menu():
    clear()
    text("< About", 10, 20)
    text("< Back", 10, 100)
    text("Options >", 140, 20)
    text("Programs >", 120, 100)
    separator()
    refresh()


def display_about_menu():
    clear()
    text("Pycos " + pycos_version, 10, 10, 4)
    text(os.uname()[0] + " - " + os.uname()[2], 10, 40)

    text("< Back", 10, 100)
    text("More info >", 120, 100)
    refresh()


def display_system_info_menu():
    clear()
    text("Device: " + os.uname()[4], 10, 10)
    text("MicroPython: " + os.uname()[3], 10, 50)

    text("< Back", 10, 100)
    text("Advanced >", 120, 100)
    refresh()


def display_advanced_menu():
    try:
        open("boot.py", "r").close()
        boot_file_present = True

    except OSError:
        boot_file_present = False

    clear()
    text("ID: " + str(machine.unique_id()), 10, 10)
    text("Reset: " + reset_causes[machine.reset_cause() - 1], 10, 30)
    text("CPU clock: " + str(int(machine.freq() / 1000000)) + " MHz", 10, 50)
    text("Boot file: " + str(boot_file_present), 10, 70)

    text("< Back", 10, 100)
    refresh()


def display_options_menu():
    clear()
    text("< Display", 10, 20)
    text("< Back", 10, 100)
    text("Power >", 160, 20)
    text("Bootloader >", 100, 100)
    separator()
    refresh()


def display_brightness_options_menu():
    clear()
    text("< Back", 10, 100)
    text("Increase >", 130, 20)
    text("Descrease >", 120, 100)
    separator()
    refresh()


def display_power_menu():
    clear()
    text("< CPU Clock", 10, 20)
    text("< Back", 10, 100)
    text("Sleep > ", 160, 20)
    text("Reset > ", 160, 100)
    separator()
    refresh()


def display_cpu_clock_menu():
    clear()
    text("< 133 MHz", 10, 20)
    text("< Back", 10, 100)
    text("125 Mhz > ", 150, 20)
    text("100 MHz > ", 150, 100)
    separator()
    refresh()


def display_sleep_menu():
    clear()
    text("< Back", 10, 100)
    text("Light sleep > ", 100, 20)
    text("Deep sleep > ", 110, 100)
    separator()
    refresh()


def display_reset_menu():
    clear()
    text("< Back", 10, 100)
    text("Soft reset > ", 110, 20)
    text("Hard reset > ", 110, 100)
    separator()
    refresh()
