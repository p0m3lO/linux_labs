import os
import sys

def check_permanent_hostname(target_hostname):
    hostname_file = "/etc/hostname"
    hosts_file = "/etc/hosts"

    try:
        with open(hostname_file, 'r') as f:
            hostname = f.read().strip()

        if hostname != target_hostname:
            return False

        with open(hosts_file, 'r') as f:
            hosts = f.readlines()

        for line in hosts:
            if line.startswith('127.0.1.1'):
                parts = line.strip().split()
                if len(parts) > 1 and target_hostname in parts[1:]:
                    return True
                else:
                    return False

    except FileNotFoundError:
        print("Error: File not found. Make sure the script is run as root or with proper permissions.")
        return False

if __name__ == "__main__":
    target_hostname = "gde-lab"
    result = check_permanent_hostname(target_hostname)
    if result:
        print(f"The hostname is set permanently to '{target_hostname}'.")
    else:
        print(f"The hostname is NOT set permanently to '{target_hostname}'.")
        sys.exit(1)