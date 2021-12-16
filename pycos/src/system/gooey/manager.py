import picodisplay as display
import time

from config import *


def clear():
    display.set_pen(BACKGROUND_COLOUR[0], BACKGROUND_COLOUR[1], BACKGROUND_COLOUR[2])
    display.clear()


def text(string: str, x: int, y: int, size: int = 2):
    display.set_pen(TEXT_COLOUR[0], TEXT_COLOUR[1], TEXT_COLOUR[2])
    display.text(string, x, y, (display.get_width() - x), size)


def separator():
    display.set_pen(SEPARATOR_COLOUR[0], SEPARATOR_COLOUR[1], SEPARATOR_COLOUR[2])
    display.circle(15, int(display.get_height() / 2), 1)
    display.rectangle(15, int((display.get_height() / 2) - 2), int(display.get_width() - 30), 4)
    display.circle(int(display.get_width() - 15), int(display.get_height() / 2), 1)


def refresh():
    display.update()
    time.sleep_ms(REFRESH_DELAY)
