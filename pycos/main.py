import machine
import picodisplay as screen
import uos as os
import utime as time

from config import *

pycos_version = "0.0.1"
reset_causes = ["PWRON_RESET", "HARD_RESET", "WDT_RESET", "DEEPSLEEP_RESET", "SOFT_RESET"]

screen.init(
    bytearray(screen.get_width() * screen.get_height() * 2)
)


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
    text("< CPU Clock", 10, 20)
    text("< Back", 10, 100)
    text("Power >", 160, 20)
    text("Bootloader >", 100, 100)
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


def display_power_menu():
    clear()
    text("< Back", 10, 100)
    text("Sleep > ", 160, 20)
    text("Reset > ", 160, 100)
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


screen.set_backlight(DEFAULT_DISPLAY_BRIGHTNESS)

display_home_screen()
while True:
    if screen.is_pressed(screen.BUTTON_Y):
        display_main_menu()
        while True:
            if screen.is_pressed(screen.BUTTON_A): # about menu
                display_about_menu()
                while True:
                    if screen.is_pressed(screen.BUTTON_B): # back
                        break

                    if screen.is_pressed(screen.BUTTON_Y): # system info menu
                        display_system_info_menu()
                        while True:
                            if screen.is_pressed(screen.BUTTON_B):
                                break

                            if screen.is_pressed(screen.BUTTON_Y): # advanced menu
                                display_advanced_menu()
                                while True:
                                    if screen.is_pressed(screen.BUTTON_B):
                                        break

                                display_system_info_menu()

                        display_about_menu()

                display_main_menu()

            if screen.is_pressed(screen.BUTTON_B): # back
                break

            if screen.is_pressed(screen.BUTTON_X): # options
                display_options_menu()
                while True:
                    if screen.is_pressed(screen.BUTTON_A): # cpu clock menu
                        display_cpu_clock_menu()
                        while True:
                            if screen.is_pressed(screen.BUTTON_A):
                                machine.freq(133000000)
                                break

                            if screen.is_pressed(screen.BUTTON_B):
                                break

                            if screen.is_pressed(screen.BUTTON_X):
                                machine.freq(125000000)
                                break

                            if screen.is_pressed(screen.BUTTON_Y):
                                machine.freq(100000000)
                                break

                        display_options_menu()

                    if screen.is_pressed(screen.BUTTON_B): # back
                        break

                    if screen.is_pressed(screen.BUTTON_X): # power menu
                        display_power_menu()
                        while True:
                            if screen.is_pressed(screen.BUTTON_A):
                                pass

                            if screen.is_pressed(screen.BUTTON_B): # back
                                break

                            if screen.is_pressed(screen.BUTTON_X): # sleep menu
                                display_sleep_menu()
                                while True:
                                    if screen.is_pressed(screen.BUTTON_B):
                                        break

                                    if screen.is_pressed(screen.BUTTON_X):
                                        screen.set_backlight(0)
                                        machine.lightsleep()

                                    if screen.is_pressed(screen.BUTTON_Y):
                                        screen.set_backlight(0)
                                        machine.deepsleep()

                                display_power_menu()

                            if screen.is_pressed(screen.BUTTON_Y): # reset menu
                                display_reset_menu()
                                while True:
                                    if screen.is_pressed(screen.BUTTON_B):
                                        break

                                    if screen.is_pressed(screen.BUTTON_X):
                                        machine.soft_reset()

                                    if screen.is_pressed(screen.BUTTON_Y):
                                        machine.reset()

                                display_power_menu()

                        display_options_menu()

                    if screen.is_pressed(screen.BUTTON_Y): # bootloader
                        clear()
                        text("Bootloader", 10, 10, 3)
                        text("Please wait until the file finishes copying over", 10, 40)
                        refresh()
                        machine.bootloader()

                display_main_menu()

            if screen.is_pressed(screen.BUTTON_Y): # programs

                programs = []

                try:
                    for file in os.listdir():
                        if file[0:3] == "Pp_":
                            programs.append(file)

                except FileNotFoundError:
                    break

                if len(programs) > 3:
                    break

                clear()
                try:
                    text("< " + programs[0].split(".")[0][3:], 10, 20)
                    text(programs[1].split(".")[0][3:] + " >", 100, 20)
                    text(programs[2].split(".")[0][3:] + " >", 100, 100)
                except IndexError:
                    pass
    
                text("< Back", 10, 100)
                separator()
                refresh()
                while True:
                    if screen.is_pressed(screen.BUTTON_A):
                        program_import = programs[0].split(".")[0]
                        program = __import__(program_import)
                        program.main()

                    if screen.is_pressed(screen.BUTTON_B):
                        break

                display_main_menu()

        display_home_screen()
