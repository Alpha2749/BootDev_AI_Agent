import os

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    full_path = None
    full_path = os.path.join(working_directory, file_path)
    full_path_abs = os.path.abspath(full_path)
    is_safe = full_path_abs.startswith(working_dir_abs)
    if not is_safe:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        with open(full_path_abs, "w") as f:
            f.write(content)
    except Exception as e:
        return "Error: some error occured"
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'