import subprocess
import sys

# Read the sshd_config file
with open('/etc/ssh/sshd_config', 'r') as f:
    config = f.read()

# Check if password authentication and root login are disabled
if 'PasswordAuthentication no' in config and 'PermitRootLogin no' in config:
    print("Password authentication and root login are disabled.")
else:
    print("Warning: Password authentication and/or root login are not disabled.")

# Initiate an SSH connection to the server
server = "gde-server"
try:
    subprocess.run(["ssh", server, "exit"], check=True)
except subprocess.CalledProcessError:
    print(f"Error: Failed to connect to {server}.")
    sys.exit(1)
print("SSH connection closed.")

