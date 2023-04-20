import os
import sys
import subprocess
import tempfile

def check_grep_search_script(script_path, file_path, pattern):
    try:
        if os.path.isfile(script_path) and os.access(script_path, os.X_OK):
            result = subprocess.run([script_path, file_path, pattern], capture_output=True)
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
    script_path = os.path.join(user_home_dir, "search.sh")

    # Create a temporary file with some content for testing
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write("This is a test file.\n")
        temp_file.write("It contains some lines with the word 'test'.\n")
        temp_file.write("This line does not contain the keyword.\n")
        temp_file.write("Another line with 'test' in it.\n")

    test_pattern = "test"
    result = check_grep_search_script(script_path, temp_file.name, test_pattern)
    os.remove(temp_file.name)  # Clean up the temporary file

    if result:
        print(f"The grep search script '{script_path}' runs successfully.")
    else:
        print(f"The grep search script '{script_path}' does NOT run successfully.")
        sys.exit(1)