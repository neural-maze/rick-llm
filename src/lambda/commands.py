import json
import os

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
