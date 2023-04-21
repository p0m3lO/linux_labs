import os
import sys
import subprocess

def is_nfs_installed():
    try:
        output = subprocess.check_output(['apt', 'list', 'nfs-kernel-server'], text=True)
        return 'installed' in output
    except subprocess.CalledProcessError:
        return False

def is_nfs_configured():
    with open('/etc/exports', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if '/opt/nfs/shared' in line and 'no_root_squash' in line in line:
                return True
    return False

def is_nfs_v4_enabled():
    with open('/etc/default/nfs-kernel-server', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if '-N 2' in line and '-N 3' in line in line:
                return True
    return False

def is_nfs_service_running():
    try:
        output = subprocess.check_output(['systemctl', 'is-active', 'nfs-server'], text=True)
        return output.strip() == 'active'
    except subprocess.CalledProcessError:
        return False

def check_firewall():
    try:
        cmd = "iptables -L INPUT -nv | grep -qE '(^| )dpt:2049($| )'"
        subprocess.check_output(cmd, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == '__main__':
    if is_nfs_installed() and is_nfs_configured() and is_nfs_service_running() and check_firewall():
        print("Success: NFS server with NFSv4 is set up correctly.")
    else:
        print("Failed: NFS server with NFSv4 is not set up correctly.")
        sys.exit(1)
