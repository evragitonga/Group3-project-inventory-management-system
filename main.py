from product import Product
from storage import load_inventory, save_inventory

LOW_STOCK_LIMIT = 5


def get_text(message):
    text = input(message).strip()
    while text == "":
        print("This cannot be empty.")
        text = input(message).strip()
    return text


def get_float(message):
    while True:
        try:
            number = float(input(message))
            if number < 0:
                print("Cannot be negative.")
            else:
                return number
        except ValueError:
            print("Please enter a number.")


def get_int(message):
    while True:
        try:
            number = int(input(message))
            if number < 0:
                print("Cannot be negative.")
            else:
                return number
        except ValueError:
            print("Please enter a whole number.")


def show_products(products):
    if len(products) == 0:
        print("No products to show.")
        return

    print("")
    print("ID".ljust(10) + "Name".ljust(20) + "Price".ljust(10) + "Qty".ljust(6) + "Status")
    print("-" * 55)
    for p in products:
        if p.quantity <= LOW_STOCK_LIMIT:
            status = "LOW STOCK"
        else:
            status = "OK"
        print(str(p.product_id).ljust(10) + p.name.ljust(20) + str(p.price).ljust(10) + str(p.quantity).ljust(6) + status)


def add_product(inventory):
    print("\n--- Add Product ---")
    product_id = get_text("Enter product ID: ")

    if inventory.get_product(product_id) is not None:
        print("A product with that ID already exists.")
        return

    name = get_text("Enter product name: ")
    price = get_float("Enter price: ")
    quantity = get_int("Enter quantity: ")

    new_product = Product(product_id, name, price, quantity)
    inventory.add_product(new_product)
    save_inventory(inventory)
    print("Product added.")


def view_products(inventory):
    print("\n--- All Products ---")
    show_products(inventory.get_all())


def search_products(inventory):
    print("\n--- Search Products ---")
    term = get_text("Enter product ID or name: ")
    results = inventory.search(term)
    show_products(results)


def update_product(inventory):
    print("\n--- Update Product ---")
    product_id = get_text("Enter ID of product to update: ")
    product = inventory.get_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Current name:", product.name)
    print("Current price:", product.price)
    print("Current quantity:", product.quantity)
    print("What do you want to update?")
    print("1. Name")
    print("2. Price")
    print("3. Quantity")
    choice = input("Enter choice: ")

    if choice == "1":
        new_name = get_text("Enter new name: ")
        inventory.update_product(product_id, name=new_name)
    elif choice == "2":
        new_price = get_float("Enter new price: ")
        inventory.update_product(product_id, price=new_price)
    elif choice == "3":
        new_quantity = get_int("Enter new quantity: ")
        inventory.update_product(product_id, quantity=new_quantity)
    else:
        print("Invalid choice.")
        return

    save_inventory(inventory)
    print("Product updated.")


def remove_product(inventory):
    print("\n--- Remove Product ---")
    product_id = get_text("Enter ID of product to remove: ")
    product = inventory.get_product(product_id)

    if product is None:
        print("Product not found.")
        return

    sure = input("Remove " + product.name + "? (y/n): ").lower()
    if sure == "y":
        inventory.remove_product(product_id)
        save_inventory(inventory)
        print("Product removed.")
    else:
        print("Cancelled.")


def check_stock(inventory):
    print("\n--- Stock Levels ---")
    show_products(inventory.get_all())

    low_stock = inventory.get_low_stock(LOW_STOCK_LIMIT)
    print("\n--- Products That Need Restocking ---")
    show_products(low_stock)


def main():
    inventory = load_inventory()
    running = True

    while running:
        print("\n==============================")
        print("  INVENTORY MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add product")
        print("2. View all products")
        print("3. Search for a product")
        print("4. Update a product")
        print("5. Remove a product")
        print("6. Check stock levels")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            view_products(inventory)
        elif choice == "3":
            search_products(inventory)
        elif choice == "4":
            update_product(inventory)
        elif choice == "5":
            remove_product(inventory)
        elif choice == "6":
            check_stock(inventory)
        elif choice == "0":
            save_inventory(inventory)
            print("Goodbye!")
            running = False
        else:
            print("Invalid choice, please try again.")


main()
