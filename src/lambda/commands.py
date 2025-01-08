import json
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("LAMBDA_API_KEY")
BASE_URL = "https://cloud.lambdalabs.com/api/v1"


def generate_ssh_key():
    """Generate SSH key and save to file."""
    url = f"{BASE_URL}/ssh-keys"
    auth = (API_KEY, "")
    open_file = "src/lambda/ssh-key/rick-private_key.pem"

    headers = {"Content-Type": "application/json"}
    data = {"name": "rick-public-key"}

    try:
        response = requests.post(url, auth=auth, headers=headers, json=data)
        response.raise_for_status()

        private_key = response.json()["data"]["private_key"]

        with open(open_file, "w") as f:
            f.write(private_key)

        os.chmod(open_file, 0o600)
        print("SSH key generated and saved to file. Check your Lambda Labs account!")

    except requests.exceptions.RequestException as e:
        print(f"Error generating SSH key: {e}")
        return None


def list_ssh_keys():
    """List all SSH keys associated with the account."""
    url = f"{BASE_URL}/ssh-keys"
    auth = (API_KEY, "")

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching SSH keys: {e}")
        return None


def list_intances():
    """List all instances."""

    url = f"{BASE_URL}/instances"
    auth = (API_KEY, "")

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching instances: {e}")
        return None


def list_instance_types():
    """List all available instance types from Lambda Labs."""

    url = f"{BASE_URL}/instance-types"
    auth = (API_KEY, "")

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching instance types: {e}")
        return None


def get_rick_vm_id():
    """Get the IP address of the Rick VM."""
    intances = list_intances()
    for instance in intances["data"]:
        if instance["name"] == "rick-finetune-instance":
            try:
                return instance["id"]
            except KeyError:
                print("Rick VM IP not found")
    return


def get_rick_vm_ip():
    """Get the IP address of the Rick VM."""
    intances = list_intances()
    for instance in intances["data"]:
        if instance["name"] == "rick-finetune-instance":
            try:
                print(f"Rick VM IP: {instance['ip']}")
            except KeyError:
                print("Rick VM IP not found")
    return


def launch_instance():
    """Launch a new Lambda Labs instance."""
    url = f"{BASE_URL}/instance-operations/launch"
    headers = {"Content-Type": "application/json"}
    auth = (API_KEY, "")

    try:
        with open("src/lambda/request.json", "r") as f:
            instance_config = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading config file: {e}")
        return None

    try:
        response = requests.post(url, auth=auth, headers=headers, json=instance_config)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error launching instance: {e}")
        return None


def terminate_instances():
    """Terminate the Rick VM."""
    url = f"{BASE_URL}/instance-operations/terminate"
    auth = (API_KEY, "")
    headers = {"Content-Type": "application/json"}

    instance_id = get_rick_vm_id()
    data = {"instance_ids": [instance_id]}

    try:
        response = requests.post(url, auth=auth, headers=headers, json=data)
        response.raise_for_status()
        print(f"Successfully terminated instances: {instance_id}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error terminating instances: {e}")
        return None


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python commands.py <command>")
        print("Available commands:")
        print("  generate-ssh-key - Generate a new SSH key")
        print("  list-ssh-keys   - List all SSH keys")
        print("  list-instances  - List all instances")
        print("  list-types     - List instance types")
        print("  get-ip         - Get Rick VM IP")
        print("  launch         - Launch instance")
        return

    command = sys.argv[1]

    commands = {
        "generate-ssh-key": generate_ssh_key,
        "list-ssh-keys": list_ssh_keys,
        "list-instances": list_intances,
        "list-types": list_instance_types,
        "get-ip": get_rick_vm_ip,
        "launch": launch_instance,
        "terminate": terminate_instances,
    }

    if command not in commands:
        print(f"Unknown command: {command}")
        return

    result = commands[command]()
    if isinstance(result, dict):
        print(json.dumps(result, indent=2))
    elif result is not None:
        print(result)


if __name__ == "__main__":
    main()
