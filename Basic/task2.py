import pwd
import grp
import sys

def user_exists(username):
    try:
        pwd.getpwnam(username)
        return True
    except KeyError:
        return False

def group_exists(groupname):
    try:
        grp.getgrnam(groupname)
        return True
    except KeyError:
        return False

def user_in_group(username, groupname):
    try:
        group = grp.getgrnam(groupname)
        return username in group.gr_mem
    except KeyError:
        return False

def main():
    user = "gde"
    group = "student"
    sudo_group = "sudo"

    if user_exists(user) and group_exists(group):
        if user_in_group(user, group) and user_in_group(user, sudo_group):
            print(f"User '{user}' exists and is part of the '{group}' and '{sudo_group}' groups.")
        else:
            print(f"User '{user}' exists and group '{group}' exists, but the user is not part of both '{group}' and '{sudo_group}' groups.")
            sys.exit(1)
    else:
        print(f"Either user '{user}' or group '{group}' does not exist.")
        sys.exit(1)

if __name__ == "__main__":
    main()