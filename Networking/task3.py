import os
import subprocess
from bs4 import BeautifulSoup

def check_nginx_installed():
    try:
        result = subprocess.run(['nginx', '-v'], stderr=subprocess.PIPE, text=True)
        return "nginx" in result.stderr
    except FileNotFoundError:
        return False

def check_custom_welcome_page():
    custom_page_path = "/usr/share/nginx/html/index.html"
    if not os.path.exists(custom_page_path):
        return False

    with open(custom_page_path, "r") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    h1_elements = soup.find_all("h1")

    if len(h1_elements) == 1 and h1_elements[0].text == "Welcome to My GDE lab test Site!":
        return True
    else:
        return False

def check_nginx_running():
    result = subprocess.run(['systemctl', 'is-active', 'nginx'], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip() == 'active'

def main():
    if not check_nginx_installed():
        print("Nginx is not installed.")
        sys.exit(1)

    if not check_custom_welcome_page():
        print("The custom welcome page is not configured correctly.")
        sys.exit(1)

    if not check_nginx_running():
        print("Nginx is not running.")
        sys.exit(1)

    print("Everything is set up correctly!")

if __name__ == "__main__":
    main()
