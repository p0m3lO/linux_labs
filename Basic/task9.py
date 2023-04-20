import os
import sys
import subprocess
import tempfile

def check_find_files_script(script_path, directory_path, name_pattern):
    try:
        if os.path.isfile(script_path) and os.access(script_path, os.X_OK):
            result = subprocess.run([script_path, directory_path, name_pattern], capture_output=True)
            if result.returncode == 0:
                output = result.stdout.decode("utf-8").strip().split("\n")
                if len(output) > 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    user_home_dir = os.path.expanduser("~")
    script_path = os.path.join(user_home_dir, "find_files.sh")

    # Create a temporary directory with some files for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        for i in range(3):
            temp_file_path = os.path.join(temp_dir, f"testfile_{i}.txt")
            with open(temp_file_path, "w") as temp_file:
                temp_file.write(f"Test file {i}\n")

        test_name_pattern = "testfile_*.txt"
        result = check_find_files_script(script_path, temp_dir, test_name_pattern)

    if result:
        print(f"The find files script '{script_path}' runs successfully.")
    else:
        print(f"The find files script '{script_path}' does NOT run successfully.")
        sys.exit(1)
