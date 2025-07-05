import os

def get_files_info(working_directory, directory=None):
    working_dir_abs = os.path.abspath(working_directory)
    full_path = None
    if directory != "." and directory != None:
        full_path = os.path.join(working_directory, directory)
    else:
        full_path = working_directory
    full_path_abs = os.path.abspath(full_path)
    is_safe = full_path_abs.startswith(working_dir_abs)
    if not is_safe:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path_abs):
        return f'Error: "{directory}" is not a directory'


    if directory == ".":
        directory = "current"
    dir_contents = f"Results for '{directory}' directory:"
    for item in os.listdir(full_path_abs):
        item_fp = os.path.join(full_path_abs, item)
        item_size = os.path.getsize(item_fp)
        is_dir = not os.path.isfile(item_fp)
        dir_contents += f"\n - {item}: file_size={item_size} bytes, is_dir={is_dir}"
    return dir_contents

