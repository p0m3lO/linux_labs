import subprocess
import sys

def check_package_installed(package_name):
    try:
        subprocess.run(["which", package_name], check=True, stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    package_name = "htop"
    result = check_package_installed(package_name)
    if result:
        print(f"The package '{package_name}' is installed.")
    else:
        print(f"The package '{package_name}' is NOT installed.")
        sys.exit(1)