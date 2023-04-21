import os
import sys

def check_symbolic_link(link_path, target_path):
    try:
        if os.path.islink(link_path):
            actual_target_path = os.path.realpath(link_path)
            if actual_target_path == target_path:
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
    link_path = os.path.join(user_home_dir, "gde_link")
    target_path = "/tmp/testdir"
    result = check_symbolic_link(link_path, target_path)
    if result:
        print(f"The symbolic link '{link_path}' points to the correct target '{target_path}'.")
    else:
        print(f"The symbolic link '{link_path}' does NOT point to the correct target '{target_path}'.")
        sys.exit(1)