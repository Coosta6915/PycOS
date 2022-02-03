import os

from platform import system as get_os
from sys import exit as sys_exit

from config import *

if get_os() != "Windows":
    print("This is the Windows build, it will genrate a batch file!")
    input()

if BUILD_DIR == "":
    print("Build directory not specified!")
    input()
    sys_exit()

with open(f"cpbuild.cmd", "wt") as f:
    f.write("")

with open("cpbuild.cmd", "at") as f:
    f.write("@echo off\n")
    for path, dirs, files in os.walk(BUILD_DIR):
        for dir in dirs:
            create_pyboard_dir = f"rshell mkdir {os.path.join(path, dir).replace(BUILD_DIR, '/pyboard')}\n"
            f.write(create_pyboard_dir.replace("\\", "/"))

            print(f"Directory:     {dir}")

        for file in files:
            local_file_path = os.path.join(path, file).replace("\\", "/").replace("/", "\\\\")
            pyboard_file_path = os.path.join(path, file).replace(BUILD_DIR, '/pyboard').replace("\\", "/")
            copy_file_cmd = f"rshell cp {local_file_path} {pyboard_file_path}\n"
            f.write(copy_file_cmd)

            print(f"File:          {file}")

    f.write("echo.\n")
    f.write("echo Finished\n")
    f.write("pause > nul\n")

print()
print("Finished")
input()
