import os

import picodisplay as display


def raise_boot_exception(error: str = "unknown?", info: str = "unknown?"):
    boot_exception_message = "boot.py failed to recognise the presense of required files and has therefore interupted the startup process."

    try:
        import system.recovery

        system.recovery.main(error, info)

    except ImportError:
        boot_exception_message += " Attempting to start recovery was unsuccessful."

    except Exception:
        boot_exception_message += " Recovery successfully started but has now closed."

    import machine
    import sys

    display.set_pen(0, 0, 0)
    display.clear()

    display.set_pen(255, 255, 255)

    display.text("Boot exception raised", 0, 0, display_width, 2)
    display.text(boot_exception_message, 0, 20, display_width, 1)
    display.text(error, 0, 50, display_width, 1)
    display.text(info, 0, 60, display_width, 1)

    display.text(str(sys.version), 0, 70, display_width, 1)
    display.text(str(sys.implementation), 0, 80, display_width, 1)
    # display.text(str(sys.modules), 0, 90, display_width, 1) # can cause overflow issues and cascading
    display.text(str(os.uname()), 0, 100, display_width, 1)

    display.update()

    exit()


# required files for startup
required_files = ["system/recovery.py"]

# initialise display
display_width = display.get_width()
display_height = display.get_height()

display_buffer = bytearray(display_width * display_height * 2)
display.init(display_buffer)

# system file check
for file in required_files:
    try:
        with open(file, "rt") as f:
            f.read()

    except FileNotFoundError as e:
        raise_boot_exception(str(e), str(file))

    except Exception as e:
        raise_boot_exception(str(e))

# user initiated recovery
if display.is_pressed(display.BUTTON_X):
    raise_boot_exception("User initiated recovery", "System file check completed successfully")
