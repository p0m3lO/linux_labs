import os
import sys
import subprocess
import tempfile

def check_redirection_demo_script(script_path, input_file_path, output_file_path):
    try:
        if os.path.isfile(script_path) and os.access(script_path, os.X_OK):
            result = subprocess.run([script_path, input_file_path, output_file_path])
            if result.returncode == 0:
                with open(output_file_path, "r") as output_file:
                    content = output_file.read()
                    if content.isupper():
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
    script_path = os.path.join(user_home_dir, "redirection.sh")

    # Create a temporary input file with some content for testing
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as input_temp_file:
        input_temp_file.write("This is a test file.\n")
        input_temp_file.write("It contains some lines with mixed case characters.\n")

    # Create a temporary output file to store the result
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as output_temp_file:
        pass

    result = check_redirection_demo_script(script_path, input_temp_file.name, output_temp_file.name)
    os.remove(input_temp_file.name)  # Clean up the temporary input file
    os.remove(output_temp_file.name)  # Clean up the temporary output file

    if result:
        print(f"The redirection demo script '{script_path}' runs successfully.")
    else:
        print(f"The redirection demo script '{script_path}' does NOT run successfully.")
        sys.exit(1)
