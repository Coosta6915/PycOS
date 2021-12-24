import picodisplay as screen

import time

from config import *
from themes.raspberry import *


def clear():
    screen.set_pen(BACKGROUND_COLOUR[0], BACKGROUND_COLOUR[1], BACKGROUND_COLOUR[2])
    screen.clear()


def text(string: str, x: int, y: int, size: int = 2):
    screen.set_pen(TEXT_COLOUR[0], TEXT_COLOUR[1], TEXT_COLOUR[2])
    screen.text(string, x, y, (screen.get_width() - x), size)


def separator():
    screen.set_pen(SEPARATOR_COLOUR[0], SEPARATOR_COLOUR[1], SEPARATOR_COLOUR[2])
    screen.circle(15, int(screen.get_height() / 2), 1)
    screen.rectangle(15, int((screen.get_height() / 2) - 2), int(screen.get_width() - 30), 4)
    screen.circle(int(screen.get_width() - 15), int(screen.get_height() / 2), 1)


def refresh():
    screen.update()
    time.sleep_ms(REFRESH_DELAY)
