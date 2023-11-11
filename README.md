# linux_labs

## Requirements

1. Vagrant
2. Virtualbox

## Good to know

It is recommended to synchronize the labs every time you start working with it. 


## Usage

1. ***Provision the virtual lab machines***

    To use the virtual lab machine navigate to the ***lab_vm*** or the ***server_vm*** directory and provision the virtual machine:

    ```
    $ vagrant up
    ```
    
    After the virtual machine started you can access the ***web interface*** through the host browser at http://localhost:5000

2. ***Connect to the virtual lab machine***

    From the ***lab_vm/*** directory run:

    ```
    $ vagrant ssh
    ```

3. ***Start / stop the virtual lab web interface on demand***

    After connected to the virtual lab machine run:

    ```
    $ lab --start
    $ lab --stop
    ```
4. ***Synchronize the labs and start / stop the virtual lab terminal interface***
    
   After connected to the virtual lab machine run:

    ```
    $ lab --resync
    $ lab
    ```

5. ***Stop the virtual lab machine***

    From the ***lab_vm/*** directory run:

    ```
    $ vagrant halt
    ```

6. ***Reload the virtual lab machine configuration after changes made to the vagrantfile***

    ```
    $ vagrant reload
    ```

## Issues

### Windows

1. If vagrant cannot provision the VM and it stucks you may need to disable WSL and restart:

```
bcdedit /set hypervisorlaunchtype off
```

2. If ssh not working via vagrant ssh (permission denied public key):

```
Delete the default openssh which is preinstalled with Win10: settings => apps => apps and features => Optional features" => filter out ssh and delete openssh
```
