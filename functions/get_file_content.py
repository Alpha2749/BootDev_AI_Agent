import os
MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    full_path = None
    full_path = os.path.join(working_directory, file_path)
    full_path_abs = os.path.abspath(full_path)
    is_safe = full_path_abs.startswith(working_dir_abs)
    if not is_safe:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(full_path_abs, "r") as f:
        file_content_string = f.read(MAX_CHARS)
    if len(file_content_string) == MAX_CHARS:
        file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
    return file_content_string