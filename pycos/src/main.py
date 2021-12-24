import picodisplay as screen

from config import *
from system.gooey.menus import *
from system.gooey.manager import *

display_width = screen.get_width()
display_height = screen.get_height()

display_buffer = bytearray(display_width * display_height * 2)
screen.init(display_buffer)

brightness = DEFAULT_DISPLAY_BRIGHTNESS
screen.set_backlight(brightness)

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
                    if screen.is_pressed(screen.BUTTON_A): # brightness options menu
                        display_brightness_options_menu()
                        while True:
                            if screen.is_pressed(screen.BUTTON_A):
                                pass

                            if screen.is_pressed(screen.BUTTON_B):
                                break

                            if screen.is_pressed(screen.BUTTON_X):
                                brightness += 0.1
                                if brightness > 1.0:
                                    brightness = 1.0

                                screen.set_backlight(brightness)
                                time.sleep_ms(250)

                            if screen.is_pressed(screen.BUTTON_Y):
                                brightness -= 0.1
                                if brightness < 0.2: # 10% brightness is too dim
                                    brightness = 0.2
                                
                                screen.set_backlight(brightness)
                                time.sleep_ms(250)

                        display_options_menu()

                    if screen.is_pressed(screen.BUTTON_B): # back
                        break

                    if screen.is_pressed(screen.BUTTON_X): # power menu
                        display_power_menu()
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

                                display_power_menu()

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
