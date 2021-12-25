import os

from platform import system
from sys import exit as sys_exit

from config import *

if SRC_DIR == BUILD_DIR:
    sys_exit("Source and build directories cannot be the same!")

if system() == "Windows":
    is_windows = True
    filetype = "cmd"

else:
    is_windows = False
    filetype = "sh"

with open(f"py2mpy.{filetype}", "wt") as f:
    f.write("")

with open(f"py2mpy.{filetype}", "at") as f:
    create_build_dir_cmd = f"mkdir {BUILD_DIR}\n"
    if is_windows:
        f.write("@echo off\n")
        f.write(create_build_dir_cmd.replace("/", "\\"))
    else:
        f.write(create_build_dir_cmd.replace("\\", "/"))

    for path, dirs, files in os.walk(SRC_DIR):
        for dir in dirs:
            create_req_dir_cmd = f"mkdir {os.path.join(path, dir).replace(SRC_DIR, BUILD_DIR)}\n"
            if is_windows:
                f.write(create_req_dir_cmd.replace("/", "\\"))
            else:
                f.write(create_req_dir_cmd.replace("\\", "/"))

        for file in files:
            conv_file_cmd = f"mpy-cross -o {os.path.join(path, file).replace(SRC_DIR, BUILD_DIR).replace('.py', '.mpy')} {os.path.join(path, file)}\n"
            if is_windows:
                f.write(conv_file_cmd.replace("/", "\\"))
            else:
                f.write(conv_file_cmd.replace("\\", "/"))

print("Finished")
input()
