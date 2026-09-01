# Config-Backup (OcNOS devices)

## What the project does?
The project performs back-up of the running configuration of the OcNOS devices. It logs in to each of the OcNOS devices listed in the inventory folder with devices.yml as the list

## How to run it?
In order to run it, log-in to the development server (ubnt-jumpserver) and change to the project folder. Activate the virtual environment #source conf-bak/bin/activate From there, run the python code by issuing the command: python3 src/main.py

## Inventory expectations:
The inventory is a list of OcNOS devices. They are marked with cisco_ios as device type because they operate as Cisco IOS

## Output behavior:
The project will create individual back-up files of each OcNOS device in the inventory. The back-up files will be stored in the output/backup folder from the main project folder.

