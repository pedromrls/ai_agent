def get_file_content(working_directory, file_path):
    abs_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, filepath))
    if not target_file.startwith(abs_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

