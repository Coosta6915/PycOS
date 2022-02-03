import picodisplay as screen

import machine
import os

from system.gooey.manager import *
from system.sysdata import *


def display_home_screen():
    clear()
    screen.set_pen(255, 225, 225)
    screen.circle(0, int(screen.get_height() / 2), 100)
    screen.set_pen(255, 0, 0)
    screen.text("PycOS", 5, int(screen.get_height() / 2) - 10, (screen.get_width() - 5), 3)
    text("Menu >", 170, 100)
    refresh()


def main_menu():
    clear()
    text("< About", 10, 20)
    text("< Back", 10, 100)
    text("Options >", 140, 20)
    text("Programs >", 120, 100)
    separator()
    refresh()


def about_menu():
    clear()
    text("PycOS " + pycos_version, 10, 10, 4)
    text(os.uname()[0] + " - " + os.uname()[2], 10, 40)
    text("< Back", 10, 100)
    text("Details >", 140, 100)
    refresh()


def about_details_menu():
    clear()
    text("Device: " + os.uname()[4], 10, 10)
    text("MicroPython: " + os.uname()[3], 10, 50)
    text("< Back", 10, 100)
    refresh()


def advanced_menu():
    clear()
    text("ID: " + str(machine.unique_id()), 10, 10)
    text("Reset: " + str(machine.reset_cause()) + " (" + reset_causes[machine.reset_cause() - 1] + ")", 10, 30)
    text("CPU clock: " + str(int(machine.freq() / 1000000)) + " MHz", 10, 50)
    text("< Back", 10, 100)
    refresh()


def options_menu():
    clear()
    text("< Display", 10, 20)
    text("< Back", 10, 100)
    text("Power >", 160, 20)
    text("Bootloader >", 100, 100)
    separator()
    refresh()


def brightness_options_menu():
    clear()
    text("< Back", 10, 100)
    text("Increase >", 130, 20)
    text("Descrease >", 120, 100)
    separator()
    refresh()


def power_menu():
    clear()
    text("< CPU Clock", 10, 20)
    text("< Back", 10, 100)
    text("Sleep > ", 160, 20)
    text("Reset > ", 160, 100)
    separator()
    refresh()


def cpu_clock_menu():
    clear()
    text("< 133 MHz", 10, 20)
    text("< Back", 10, 100)
    text("125 Mhz > ", 150, 20)
    text("100 MHz > ", 150, 100)
    separator()
    refresh()


def sleep_menu():
    clear()
    text("< Back", 10, 100)
    text("Light sleep > ", 100, 20)
    text("Deep sleep > ", 110, 100)
    separator()
    refresh()


def reset_menu():
    clear()
    text("< Back", 10, 100)
    text("Soft reset > ", 110, 20)
    text("Hard reset > ", 110, 100)
    separator()
    refresh()
