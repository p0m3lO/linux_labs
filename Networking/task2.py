import os
import sys
import subprocess

def check_ping_monitor_script(script_path, ip_address):
    try:
        if os.path.isfile(script_path) and os.access(script_path, os.X_OK):
            result = subprocess.run([script_path, ip_address], capture_output=True)
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
    script_path = os.path.join(user_home_dir, "monitor.sh")
    test_ip_address = "1.1.1.1"
    result = check_ping_monitor_script(script_path, test_ip_address)
    if result:
        print(f"The monitoring script '{script_path}' runs successfully.")
    else:
        print(f"The monitoring script '{script_path}' does NOT run successfully.")
        sys.exit(1)