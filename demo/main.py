# this file is only for demonstrating the look of the stock UI
# all it does is play a preset of the screen cycling through a few menus
# you can't actually interact or do anything with it

import machine
import picodisplay as screen
import uos as os
import utime as time

time.sleep_ms(5000)

screen.init(
    bytearray(screen.get_width() * screen.get_height() * 2)
)

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
    time.sleep_ms(250)


screen.set_backlight(1)

clear()
screen.set_pen(255, 225, 225)
screen.circle(0, int(screen.get_height() / 2), 100)
screen.set_pen(255, 0, 0)
screen.text("Pycos", 5, int(screen.get_height() / 2) - 10, (screen.get_width() - 5), 3)

text("Menu >", 170, 100)
refresh()

time.sleep_ms(2250)

clear()
text("< About", 10, 20)
text("< Back", 10, 100)
text("Options >", 140, 20)
text("Programs >", 120, 100)
separator()
refresh()

time.sleep_ms(500)

clear()
text("Pycos " + "0.0.1", 10, 10, 4)
text(os.uname()[0] + " - " + os.uname()[2], 10, 40)

text("< Back", 10, 100)
text("More info >", 120, 100)
refresh()

time.sleep_ms(1500)

clear()
text("Device: " + os.uname()[4], 10, 10)
text("MicroPython: " + os.uname()[3], 10, 50)

text("< Back", 10, 100)
text("Advanced >", 120, 100)
refresh()

time.sleep_ms(1500)

clear()
text("Pycos " + "0.0.1", 10, 10, 4)
text(os.uname()[0] + " - " + os.uname()[2], 10, 40)

text("< Back", 10, 100)
text("More info >", 120, 100)
refresh()

time.sleep_ms(500)

clear()
text("< About", 10, 20)
text("< Back", 10, 100)
text("Options >", 140, 20)
text("Programs >", 120, 100)
separator()
refresh()

time.sleep_ms(500)

clear()
text("< CPU Clock", 10, 20)
text("< Back", 10, 100)
text("Power >", 160, 20)
text("Bootloader >", 100, 100)
separator()
refresh()

time.sleep_ms(500)

clear()
text("< 133 MHz", 10, 20)
text("< Back", 10, 100)
text("125 Mhz > ", 150, 20)
text("100 MHz > ", 150, 100)
separator()
refresh()

time.sleep_ms(1250)

clear()
text("< CPU Clock", 10, 20)
text("< Back", 10, 100)
text("Power >", 160, 20)
text("Bootloader >", 100, 100)
separator()
refresh()

time.sleep_ms(500)

clear()
text("Bootloader", 10, 10, 3)
text("Please wait until the file finishes copying over", 10, 40)
refresh()
machine.bootloader()
