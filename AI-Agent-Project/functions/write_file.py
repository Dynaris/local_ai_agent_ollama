import os

def write_file(working_directory, file_path, content):

    working_directory_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_abs, file_path))

    dir_list = [working_directory_abs, target_dir]

    valid_target_dir = os.path.commonpath(dir_list)

    parent_directory = os.path.dirname(target_dir)

    if valid_target_dir != working_directory_abs:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(target_dir):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    try:
        os.makedirs(parent_directory, exist_ok=True)
        with open(target_dir, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    