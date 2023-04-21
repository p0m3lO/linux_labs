import os
import sys
import subprocess
import tempfile

def check_tar_demo_script(script_path, mode, archive_file_path, directory_path=None):
    try:
        if os.path.isfile(script_path) and os.access(script_path, os.X_OK):
            command = [script_path, mode, archive_file_path]
            if directory_path:
                command.append(directory_path)
            result = subprocess.run(command)
            if result.returncode == 0:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    user_home_dir = os.path.expanduser("~")
    script_path = os.path.join(user_home_dir, "tar_demo.sh")

    # Create a temporary directory with some files for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        for i in range(3):
            temp_file_path = os.path.join(temp_dir, f"testfile_{i}.txt")
            with open(temp_file_path, "w") as temp_file:
                temp_file.write(f"Test file {i}\n")

        archive_file_path = os.path.join(temp_dir, "archive.tar.gz")
        compression_result = check_tar_demo_script(script_path, "-c", archive_file_path, temp_dir)

        extraction_dir = os.path.join(temp_dir, "extracted_files")
        os.makedirs(extraction_dir)
        os.chdir(extraction_dir)
        extraction_result = check_tar_demo_script(script_path, "-x", archive_file_path)

    result = compression_result and extraction_result

    if result:
        print(f"The tar demo script '{script_path}' runs successfully.")
    else:
        print(f"The tar demo script '{script_path}' does NOT run successfully.")
        sys.exit(1)