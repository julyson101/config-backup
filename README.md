#1. What the project does:
  The project performs back-up of the running configuration of the OcNOS devices.
#2. How to run it:
  In order to run it, log-in to the development server and go to the project folder. From the project folder, run the python code by issuing command: python3 src/main.py
#3. Inventory expectations:
  The inventory is a list of OcNOS devices. They are marked with cisco_ios as device type because they operate as Cisco IOS. 
#4. Output behavior:
  The project will create individual back-up files of each OcNOS device in the inventory. The back-up files will be stored in the output/backup folder from the main project folder.
