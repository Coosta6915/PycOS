import picodisplay as screen

import time

from config import *


def clear():
    screen.set_pen(255, 0, 0)
    screen.clear()


def text(string: str, x: int, y: int, size: int = 2):
    screen.set_pen(255, 255, 255)
    screen.text(string, x, y, (screen.get_width() - x), size)


def separator():
    screen.set_pen(255, 85, 85)
    screen.circle(15, int(screen.get_height() / 2), 1)
    screen.rectangle(15, int((screen.get_height() / 2) - 2), int(screen.get_width() - 30), 4)
    screen.circle(int(screen.get_width() - 15), int(screen.get_height() / 2), 1)


def refresh():
    screen.update()
    time.sleep_ms(REFRESH_DELAY)
