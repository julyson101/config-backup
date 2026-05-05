import yaml
from netmiko import ConnectHandler
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent

INVENTORY_FILE = ROOT_DIR / "inventory" / "devices.yml"
OUTPUT_DIR = BASE_DIR / "output" / "backups"

def load_inventory():
    with open(INVENTORY_FILE, "r") as f:
        return yaml.safe_load(f)["devices"]

def backup_device(device):
    print(f"Backing up {device['name']} ({device['host']})")

    conn = ConnectHandler(
        device_type=device["device_type"],
        host=device["host"],
        username=device["username"],
        password=device["password"],

    )

    config = conn.send_command("show run")
    conn.disconnect()

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{device['name']}_{timestamp}.cfg"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / filename, "w") as f:
        f.write(config)

def run_backups():
    devices = load_inventory()
    for device in devices:
        try:
            backup_device(device)
        except Exception as e:
            print(f"Failed to back up {device['name']}: {e}")

