# Basic networking lab for linux

## 1. Task

### SSH configuration:

1. generate an ***ssh-key*** and set key-based authentication on ***gde-server***
2. Create an ***ssh configuration*** file with a stanza (section). The host should named ***gde-server*** and configure to use the generated key
3. Test the connection eg.: ***$ ssh gde-server***
4. Configure the local ssh daemon: disable ***root login***, disable ***password authentication***


## 2. Task

### Create a monitor script 

Create a ***Bash script*** named ***monitor.sh*** in the ***home directory*** that pings a server using the IP address provided as the first positional parameter. The script should be executable.


## 3. Task

### Create a Web server

- ***Install*** Nginx web server
- ***Create*** a custom HTML welcome page with the text ***"Welcome to My GDE lab test Site!"*** in an `<h1>` element
- ***Configure*** Nginx to serve the custom welcome page as the default page
- ***Restart*** the Nginx service to apply the changes

## 4. Task

### Basic file creation Task

Create an ***NFS server*** that only supports NFSv4 protocol and exports a shared directory to clients in

- Install the necessary NFS server packages.
- Create a shared directory, ***/opt/nfs/shared***
- Configure the NFS server to export the shared directory and allow only NFSv4 protocol
- Start and enable the NFS server service
- Configure the firewall to allow NFSv4 traffic