import os
import sys
import stat

def check_directory_creation(directory_path, expected_permissions):
    try:
        if os.path.isdir(directory_path):
            actual_permissions = stat.S_IMODE(os.stat(directory_path).st_mode)
            if actual_permissions == expected_permissions:
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
    directory_path = os.path.join(user_home_dir, "test")
    expected_permissions = 0o755
    result = check_directory_creation(directory_path, expected_permissions)
    if result:
        print(f"The directory '{directory_path}' has the correct permissions '{oct(expected_permissions)}'.")
    else:
        print(f"The directory '{directory_path}' does NOT have the correct permissions '{oct(expected_permissions)}'.")
        sys.exit(1)