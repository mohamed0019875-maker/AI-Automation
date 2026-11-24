"""A simple customer manager that stores its data in customers.json.

Each customer is a dictionary like:
    {"name": "Alice Smith", "email": "alice@example.com", "status": "active"}
"""

import json

FILENAME = "customers.json"


def load_customers(filename=FILENAME):
    """Load the customer list from a JSON file.

    Returns:
        - a list of customers (empty if the file doesn't exist yet)
        - None if the file exists but can't be read safely
    """
    try:
        with open(filename, encoding="utf-8") as file:
            customers = json.load(file)
    except FileNotFoundError:
        print(f"Note: '{filename}' was not found. Starting with an empty list.")
        print("The file will be created when you add your first customer.")
        return []
    except json.JSONDecodeError as error:
        print(f"Error: '{filename}' is not valid JSON ({error}).")
        print("Please fix the file by hand. Nothing was changed, so your data is safe.")
        return None

    if not isinstance(customers, list):
        print(f"Error: '{filename}' should contain a list of customers.")
        print("Please fix the file by hand. Nothing was changed.")
        return None

    return customers


def save_customers(customers, filename=FILENAME):
    """Save the customer list to the JSON file. Returns True on success."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(customers, file, indent=4, ensure_ascii=False)
    except OSError as error:
        print(f"Error: could not save to '{filename}': {error}")
        return False
    return True


def add_customer(name, email, status="active", filename=FILENAME):
    """Add a customer, keeping all existing customers in the file."""
    customers = load_customers(filename)
    if customers is None:
        # The file is unreadable. Stop here so we never overwrite it.
        print("Customer was NOT added.")
        return

    customers.append({"name": name, "email": email, "status": status})

    if save_customers(customers, filename):
        print(f"Added customer: {name}")


def display_customers(customers):
    """Print all customers in a readable format."""
    if not customers:
        print("No customers to show.")
        return

    print(f"\n{'#':<4}{'Name':<25}{'Email':<30}{'Status':<10}")
    print("-" * 69)
    for number, customer in enumerate(customers, start=1):
        name = customer.get("name", "N/A")
        email = customer.get("email", "N/A")
        status = customer.get("status", "N/A")
        print(f"{number:<4}{name:<25}{email:<30}{status:<10}")
    print


def main():
    while True:
        print("1) Show customers")
        print("2) Add a customer")
        print("3) Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            customers = load_customers()
            if customers is not None:
                display_customers(customers)
        elif choice == "2":
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            status = input("Status (default: active): ").strip() or "active"
            if name and email:
                add_customer(name, email, status)
            else:
                print("Name and email are required.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()