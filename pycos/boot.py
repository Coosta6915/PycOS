import picodisplay as screen

import time

display_width = screen.get_width()
display_height = screen.get_height()

display_buffer = bytearray(display_width * display_height * 2)
screen.init(display_buffer)

screen.set_pen(0, 0, 0)
screen.clear()
screen.set_pen(255, 255, 255)

required_files = ["boot.py", "main.py"]

try:
    for required_file in required_files:
        with open(required_file, "rb") as f:
            f.read()

except Exception as e:
    screen.set_led(100, 0, 0)
    screen.text(str(e), 10, 10, display_width, 2)
    screen.update()
    time.sleep(5)
