import os

from platform import system as get_os
from sys import exit as sys_exit

from config import *

if get_os() != "Linux":
    print("This is the Linux build, it will genrate a shell script!")
    input()

if SRC_DIR == "" or BUILD_DIR == "":
    print("Source and/or build directory not specified!")
    input()
    sys_exit()

if SRC_DIR == BUILD_DIR:
    print("Source and build directories cannot be the same!")
    input()
    sys_exit()

with open(f"py2mpy.sh", "wt") as f:
    f.write("")

with open(f"py2mpy.sh", "at") as f:
    rem_prev_build_dir_cmd = f"rm -rf {BUILD_DIR}\n"
    create_build_dir_cmd = f"mkdir {BUILD_DIR}\n"
    f.write(rem_prev_build_dir_cmd.replace('\\', '/'))
    f.write(create_build_dir_cmd.replace("\\", "/"))

    for path, dirs, files in os.walk(SRC_DIR):
        for dir in dirs:
            create_req_dir_cmd = f"mkdir {os.path.join(path, dir).replace(SRC_DIR, BUILD_DIR)}\n"
            f.write(create_req_dir_cmd.replace("\\", "/"))

            print(f"Directory:     {dir}")

        for file in files:
            if file in EXCLUDE_FILES:
                handle_file_cmd = f"cp {os.path.join(path, file)} {os.path.join(path.replace(SRC_DIR, BUILD_DIR), file)}\n"
            else:
                handle_file_cmd = f"python3 -m mpy_cross -o {os.path.join(path, file).replace(SRC_DIR, BUILD_DIR).replace('.py', '.mpy')} -s {file} -march={ARCH} -X emit={EMITTER} {os.path.join(path, file)}\n"

            f.write(handle_file_cmd.replace("\\", "/"))

            print(f"File:          {file}")
    
    f.write("echo Finished\n")  

print()
print("Finished")
input()
