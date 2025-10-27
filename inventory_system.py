import json
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item and quantity to the inventory."""
    if logs is None:
        logs = []
    if not isinstance(item, str):
        raise ValueError("Item name must be a string")
    if not isinstance(qty, int):
        raise ValueError("Quantity must be an integer")
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(item, qty):
    """Remove a quantity of an item from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        logging.info("Removed %d of %s", qty, item)
    except KeyError:
        logging.warning("Item '%s' not found in stock.", item)
    except ValueError as e:
        logging.error("Invalid value for '%s': %s", item, e)
    except (TypeError, OSError) as e:
        logging.error("Error removing item '%s': %s", item, e)


def get_qty(item):
    """Return quantity of an item."""
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """Load inventory data from file."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
            stock_data.clear()
            stock_data.update(data)
        logging.info("Inventory data loaded successfully.")
    except FileNotFoundError:
        logging.warning("File %s not found. Starting with empty inventory.", file_name)
        stock_data.clear()
    except json.JSONDecodeError:
        logging.error("Invalid JSON in %s.", file_name)
        stock_data.clear()


def save_data(file_name="inventory.json"):
    """Save inventory data to file."""
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4)
        logging.info("Inventory data saved successfully.")
    except OSError as e:
        logging.error("File write error: %s", e)


def print_data():
    """Display all items and quantities."""
    logging.info("Items Report:")
    if not stock_data:
        logging.info("No items in inventory.")
        return
    for item, qty in stock_data.items():
        logging.info("%s -> %d", item, qty)


def check_low_items(threshold=5):
    """Return list of items below threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function for testing inventory operations."""
    try:
        add_item("apple", 10)
        add_item("banana", -2)
        remove_item("apple", 3)
        remove_item("orange", 1)
        logging.info("Apple stock: %d", get_qty("apple"))
        logging.info("Low items: %s", check_low_items())
        save_data()
        load_data()
        print_data()
        logging.info("All operations completed successfully.")
    except ValueError as e:
        logging.error("Value error: %s", e)
    except (RuntimeError, OSError) as e:
        logging.error("Runtime or OS error: %s", e)


if __name__ == "__main__":
    main()
