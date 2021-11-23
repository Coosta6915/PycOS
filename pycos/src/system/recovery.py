import machine
import os
import sys
import time

import picodisplay as display


def clear():
    display.set_pen(255, 0, 0)
    display.clear()


def text(string: str, x: int, y: int, size: int = 2):
    display.set_pen(255, 255, 255)
    display.text(string, x, y, (display.get_width() - x), size)


def separator():
    display.set_pen(255, 85, 85)
    display.circle(15, int(display.get_height() / 2), 1)
    display.rectangle(15, int((display.get_height() / 2) - 2), int(display.get_width() - 30), 4)
    display.circle(int(display.get_width() - 15), int(display.get_height() / 2), 1)


def refresh():
    display.update()
    time.sleep_ms(250)


def main_menu(error_message_to_display: str, info_message_to_display: str):
    clear()
    text("Recovery", 10, 10, 3)
    text(error_message_to_display, 10, 35, 1)
    text(info_message_to_display, 10, 45, 1)

    text("< More info", 10, 100)
    text("Options >", 140, 100)
    refresh()


def more_info_menu():
    clear()
    text(str(sys.version), 10, 10, 1)
    text(str(sys.implementation), 10, 20, 1)
    text(str(sys.modules), 10, 30, 1)
    text(str(os.uname()), 10, 60, 1)

    text("Close >", 160, 100)
    refresh()


def options_menu():
    clear()
    text("< Exit", 10, 20)
    text("< Back", 10, 100)
    text("Reset >", 160, 20)
    text("Bootloader >", 100, 100)
    separator()
    refresh()


def main(error_message: str, info_message: str):
    display_width = display.get_width()
    display_height = display.get_height()

    display_buffer = bytearray(display_width * display_height * 2)
    display.init(display_buffer)

    main_menu(error_message, info_message)
    while True:
        if display.is_pressed(display.BUTTON_B):
            more_info_menu()
            while True:
                if display.is_pressed(display.BUTTON_Y):
                    break

            main_menu(error_message, info_message)

        if display.is_pressed(display.BUTTON_Y):
            options_menu()
            while True:
                if display.is_pressed(display.BUTTON_A):
                    exit()

                if display.is_pressed(display.BUTTON_B):
                    break

                if display.is_pressed(display.BUTTON_X):
                    machine.reset()

                if display.is_pressed(display.BUTTON_Y):
                    machine.bootloader()

            main_menu(error_message, info_message)
