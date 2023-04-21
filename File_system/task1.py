import os
import sys
import subprocess

def check_lvm_setup(disk1, disk2, vg_name, lv_name, mount_point, fs_type):
    try:
        # Check if the physical volumes exist
        pv_check = subprocess.run(["pvs", disk1, disk2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if pv_check.returncode != 0:
            return False

        # Check if the volume group exists and contains the specified physical volumes
        vg_check = subprocess.run(["vgs", vg_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if vg_check.returncode != 0:
            return False

        # Check if the logical volume exists
        lv_check = subprocess.run(["lvs", f"{vg_name}/{lv_name}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if lv_check.returncode != 0:
            return False

        # Check if the filesystem type is correct
        fs_check = subprocess.run(["blkid", "-o", "value", "-s", "TYPE", f"/dev/{vg_name}/{lv_name}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if fs_check.stdout.decode("utf-8").strip() != fs_type:
            return False

        # Check if the filesystem is mounted at the specified mount point
        mount_check = subprocess.run(["findmnt", "-rn", "-S", f"/dev/{vg_name}/{lv_name}", "-T", mount_point], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if mount_check.returncode != 0:
            return False

        # Check for the fstab entry
        with open('/etc/fstab', 'r') as fstab:
            fstab_entry = f"/dev/mapper/{vg_name}-{lv_name}\s+{mount_point}\s+{fs_type}"
            if not any(re.search(fstab_entry, line) for line in fstab):
                return False

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    import re

    disk1 = "/dev/sda"
    disk2 = "/dev/sdb"
    vg_name = "gde_group"
    lv_name = "gde_volume"
    mount_point = "/mnt/lvm"
    fs_type = "ext4"

    result = check_lvm_setup(disk1, disk2, vg_name, lv_name, mount_point, fs_type)

    if result:
        print(f"The LVM setup is configured correctly.")
    else:
        print(f"The LVM setup is NOT configured correctly.")
        sys.exit(1)