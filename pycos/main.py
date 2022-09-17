import picodisplay as screen

from system.fileh.jsonh import *
from system.sysdata import *
from system.gui.menu import *
from system.gui.manager import *

display_width = screen.get_width()
display_height = screen.get_height()

display_buffer = bytearray(display_width * display_height * 2)
screen.init(display_buffer)

sysconfig = load(sysconfig_path)

display_brightness = sysconfig["display"]["default_brightness"]
screen.set_backlight(display_brightness)

display_home_screen()
while True:
    if screen.is_pressed(screen.BUTTON_Y):
        main_menu()
        while True:
            if screen.is_pressed(screen.BUTTON_A): # about menu
                about_menu()
                while True:
                    if screen.is_pressed(screen.BUTTON_B): # back
                        break

                    if screen.is_pressed(screen.BUTTON_Y): # about details menu
                        about_details_menu()
                        while True:
                            if screen.is_pressed(screen.BUTTON_B):
                                break

                        about_menu()

                main_menu()

            if screen.is_pressed(screen.BUTTON_B): # back
                break

            if screen.is_pressed(screen.BUTTON_X): # options
                options_menu()
                while True:
                    if screen.is_pressed(screen.BUTTON_A): # brightness options menu
                        brightness_options_menu()
                        while True:
                            if screen.is_pressed(screen.BUTTON_A):
                                pass

                            if screen.is_pressed(screen.BUTTON_B):
                                break

                            if screen.is_pressed(screen.BUTTON_X):
                                display_brightness += 0.1
                                if display_brightness > 1.0:
                                    display_brightness = 1.0

                                screen.set_backlight(display_brightness)
                                time.sleep_ms(sysconfig["display"]["refresh_delay"])

                            if screen.is_pressed(screen.BUTTON_Y):
                                display_brightness -= 0.1
                                if display_brightness < 0.2: # 10% brightness is too dim
                                    display_brightness = 0.2
                                
                                screen.set_backlight(display_brightness)
                                time.sleep_ms(sysconfig["display"]["refresh_delay"])

                        options_menu()

                    if screen.is_pressed(screen.BUTTON_B): # back
                        break

                    if screen.is_pressed(screen.BUTTON_X): # power menu
                        power_menu()
                        while True:
                            if screen.is_pressed(screen.BUTTON_A): # cpu clock menu
                                cpu_clock_menu()
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

                                power_menu()

                            if screen.is_pressed(screen.BUTTON_B): # back
                                break

                            if screen.is_pressed(screen.BUTTON_X): # sleep menu
                                sleep_menu()
                                while True:
                                    if screen.is_pressed(screen.BUTTON_B):
                                        break

                                    if screen.is_pressed(screen.BUTTON_X):
                                        screen.set_backlight(0)
                                        machine.lightsleep()

                                    if screen.is_pressed(screen.BUTTON_Y):
                                        screen.set_backlight(0)
                                        machine.deepsleep()

                                power_menu()

                            if screen.is_pressed(screen.BUTTON_Y): # reset menu
                                reset_menu()
                                while True:
                                    if screen.is_pressed(screen.BUTTON_B):
                                        break

                                    if screen.is_pressed(screen.BUTTON_X):
                                        machine.soft_reset()

                                    if screen.is_pressed(screen.BUTTON_Y):
                                        machine.reset()

                                power_menu()

                        options_menu()

                    if screen.is_pressed(screen.BUTTON_Y): # bootloader
                        clear()
                        text("Bootloader", 10, 10, 3)
                        text("Please wait until the file finishes copying over", 10, 40)
                        refresh()
                        machine.bootloader()

                main_menu()

        display_home_screen()
