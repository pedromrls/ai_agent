import os


def write_file(working_directory, file_path, content):
    abs_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_dir):
        try:
            os.makedirs(abs_dir)
        except Exception as e:
            return f'Error reading file "{file_path}": {e}'
    try:
        with open(target_file, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error writing to file: {file_path}: {e}"
