import os
import hashlib
import sys

def check_directory_exists(directory):
    return os.path.exists(directory) and os.path.isdir(directory)

def check_file_exists(file_path):
    return os.path.exists(file_path) and os.path.isfile(file_path)

def sha256sum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while (chunk := file.read(8192)):
            sha256.update(chunk)
    return sha256.hexdigest()

def check_file_content_sha256(file_path, expected_sha256s):
    file_sha256 = sha256sum(file_path)
    return any(file_sha256 == expected_sha256 for expected_sha256 in expected_sha256s)

def main():
    home_directory = os.path.expanduser("~")
    directory = os.path.join(home_directory, "gde")
    file_name = "gde.txt"
    file_path = os.path.join(directory, file_name)
    expected_content_without_newline = "This is a test"
    expected_content_with_newline = expected_content_without_newline + "\n"
    expected_sha256s = [
        hashlib.sha256(expected_content_without_newline.encode()).hexdigest(),
        hashlib.sha256(expected_content_with_newline.encode()).hexdigest(),
    ]

    if not check_directory_exists(directory):
        print(f"Directory '{directory}' does not exist.")
        sys.exit(1)

    if not check_file_exists(file_path):
        print(f"File '{file_name}' does not exist in the directory '{directory}'.")
        sys.exit(1)

    if not check_file_content_sha256(file_path, expected_sha256s):
        print(f"The content of '{file_name}' is incorrect.")
        sys.exit(1)

    print("Directory, file, and content checks passed.")

if __name__ == "__main__":
    main()