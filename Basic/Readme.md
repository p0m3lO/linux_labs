# Basic lab for linux

## 1. Task

 Create a directory named `gde` and put a file called `gde.txt` into it with content: `"This is a test"`

## 2. Task

Create a user `gde` create a new group `student` and add gde user to the new `student` group and also to the `sudo` group

## 3. Task

Change the server hostname permanently to `gde-lab`

## 4. Task
SSH configuration:

1. generate an `ssh-key` and set key-based authentication on `gde-server`
2. Create an `ssh configuration` file with a stanza (section). The host should named `gde-server` and configure to use the generated key
3. Test the connection eg.: `$ ssh gde-server`
4. Configure the local ssh daemon: disable `root login`, disable `password authentication`

