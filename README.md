README.md
loader.py is a simple program which fetch latest file from server and updates the local version. It also updates the 'loader' itself for latest updates.

Following line is added to /etc/rc.local to make it run on system boot.
sudo python loader.py 

loader.py can also be used from command line or other programs to update other programs/file.