import os

with open("pycos-installer.sh", "at") as installer_file:
    for path, dirs, files in os.walk("..\\pycos\\src"):
        included_dirs = []
        for file in files:
            for dir in dirs:
                new_dir_path = os.path.join(path, dir).split("src")[1].replace("\\", "/")
                if new_dir_path in included_dirs:
                    continue

                else:
                    included_dirs.append(new_dir_path)
                    mkdir_command = f"rshell mkdir /pyboard/{new_dir_path}\n"
                    installer_file.write(mkdir_command)
        
            path_to_file = os.path.join(path, file).split("src")[1].replace("\\", "/")
            path_to_pyboard_file = f"/pyboard{path_to_file}"
            copy_command = f"rshell cp .{path_to_file} {path_to_pyboard_file}\n"
            installer_file.write(copy_command)
