
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("inventory.json")

def load_data():
    """Load product data from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_data(data):
    """Save product data to the JSON file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

SUPPLIERS_FILE = Path(__file__).with_name("suppliers.json")


def load_suppliers():
    """Load supplier records from the JSON file."""
    if not SUPPLIERS_FILE.exists():
        return []

    try:
        with SUPPLIERS_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_suppliers(suppliers):
    """Save supplier records to the JSON file."""
    with SUPPLIERS_FILE.open("w", encoding="utf-8") as file:
        json.dump(suppliers, file, indent=4)
