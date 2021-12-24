import picodisplay as screen

import time

display_width = screen.get_width()
display_height = screen.get_height()

display_buffer = bytearray(display_width * display_height * 2)
screen.init(display_buffer)

screen.set_pen(0, 0, 0)
screen.clear()

screen.text("Running system file check", 0, 0, display_width, 2)
screen.update()

time.sleep(2)

required_files = []

for required_file in required_files:
    try:
        with open(required_file, "rb") as f:
            f.read()

    except OSError as e:
        screen.set_pen(255, 255, 255)
        screen.text(str(e), 0, 0, display_width, 2)
        screen.update()
