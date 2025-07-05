import os, subprocess

def run_python_file(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    full_path = None
    full_path = os.path.join(working_directory, file_path)
    full_path_abs = os.path.abspath(full_path)
    is_safe = full_path_abs.startswith(working_dir_abs)

    if not is_safe:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path_abs):
        return f'Error: File "{file_path}" not found'
    if not full_path_abs.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(
            ['python', full_path_abs],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
            cwd=working_dir_abs,
            text=True
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        output = ""
        if stdout:
            output += "STDOUT:\n" + stdout
        if stderr:
            output += "\nSTDERR:\n" + stderr
        if result.returncode != 0:
            output += f"\nProcess exited with code {result.returncode}"
        if not stdout and not stderr:
            output = "No output produced."

        return output
    except Exception as e:
        return f"Error occurred: {str(e)}"