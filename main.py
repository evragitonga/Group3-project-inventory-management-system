from models.product import Product
from models.inventory import Inventory
from models.suppliers import Supplier
from data.savedata import load_data, save_data, load_suppliers, save_suppliers

LOW_STOCK_LIMIT = 5


def load_inventory():
    inventory = Inventory()
    saved_products = load_data()
    if saved_products:
        for item in saved_products:
            inventory.add_product(Product.from_dict(item))
    return inventory


def save_inventory(inventory):
    data = []
    for product in inventory.all_products():
        data.append(product.to_dict())
    save_data(data)


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
    print("ID".ljust(10) + "Name".ljust(20) + "Category".ljust(15) + "Price".ljust(10) + "Qty".ljust(6) + "Status")
    print("-" * 70)
    for p in products:
        if p.quantity < LOW_STOCK_LIMIT:
            status = "LOW STOCK"
        else:
            status = "OK"
        print(str(p.product_id).ljust(10) + p.name.ljust(20) + p.category.ljust(15) + str(p.price).ljust(10) + str(p.quantity).ljust(6) + status)


def get_low_stock(inventory):
    low_stock = []
    for p in inventory.all_products():
        if p.quantity < LOW_STOCK_LIMIT:
            low_stock.append(p)
    return low_stock


def add_product(inventory):
    print("\n--- Add Product ---")
    name = get_text("Enter product name: ")
    category = get_text("Enter category: ")
    price = get_float("Enter price: ")
    quantity = get_int("Enter quantity: ")

    new_product = Product.create_product(name, category, price, quantity)
    inventory.add_product(new_product)
    save_inventory(inventory)
    print("Product added with ID", new_product.product_id)


def view_products(inventory):
    print("\n--- All Products ---")
    show_products(inventory.all_products())


def search_products(inventory):
    print("\n--- Search Products ---")
    term = get_text("Enter product ID or name: ")
    results = inventory.search_product(term)
    show_products(results)


def update_product(inventory):
    print("\n--- Update Product ---")
    product_id = get_text("Enter ID of product to update: ")
    product = inventory.get_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Current name:", product.name)
    print("Current category:", product.category)
    print("Current price:", product.price)
    print("Current quantity:", product.quantity)
    print("What do you want to update?")
    print("1. Name")
    print("2. Category")
    print("3. Price")
    print("4. Quantity")
    choice = input("Enter choice: ")

    if choice == "1":
        new_name = get_text("Enter new name: ")
        inventory.update_product(product_id, name=new_name)
    elif choice == "2":
        new_category = get_text("Enter new category: ")
        inventory.update_product(product_id, category=new_category)
    elif choice == "3":
        new_price = get_float("Enter new price: ")
        inventory.update_product(product_id, price=new_price)
    elif choice == "4":
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
    show_products(inventory.all_products())

    print("\n--- Products That Need Restocking ---")
    show_products(get_low_stock(inventory))


def restock_product(inventory):
    print("\n--- Restock Product ---")
    product_id = get_text("Enter product ID: ")
    product = inventory.get_product(product_id)

    if product is None:
        print("Product not found.")
        return

    amount = get_int("How many units were added? ")
    inventory.restock_product(product_id, amount)
    save_inventory(inventory)
    print(product.name, "now has", product.quantity, "in stock.")


def reduce_stock(inventory):
    print("\n--- Reduce Stock ---")
    product_id = get_text("Enter product ID: ")
    product = inventory.get_product(product_id)

    if product is None:
        print("Product not found.")
        return

    amount = get_int("How many units were taken out? ")
    if amount > product.quantity:
        print("Not enough stock. Only", product.quantity, "available.")
        return

    inventory.reduce_stock(product_id, amount)
    save_inventory(inventory)
    print(product.name, "now has", product.quantity, "in stock.")


def show_total_value(inventory):
    print("\n--- Total Stock Value ---")
    print("Total value of all stock:", inventory.total_stock_value())


def load_supplier_data():
    saved_suppliers = load_suppliers()
    if saved_suppliers:
        for item in saved_suppliers:
            Supplier.from_dict(item)


def save_supplier_data():
    data = []
    for supplier in Supplier.all_suppliers():
        data.append(supplier.to_dict())
    save_suppliers(data)


def show_suppliers(suppliers):
    if len(suppliers) == 0:
        print("No suppliers to show.")
        return

    print("")
    print("ID".ljust(10) + "Name".ljust(22) + "Phone".ljust(16) + "Email")
    print("-" * 70)
    for s in suppliers:
        print(s.supplier_id.ljust(10) + s.name.ljust(22) + s.phone.ljust(16) + s.email)


def add_supplier():
    print("\n--- Add Supplier ---")
    name = get_text("Enter supplier name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    new_supplier = Supplier.create_supplier(name, phone, email)
    save_supplier_data()
    print("Supplier added with ID", new_supplier.supplier_id)


def view_suppliers():
    print("\n--- All Suppliers ---")
    show_suppliers(Supplier.all_suppliers())


def update_supplier():
    print("\n--- Update Supplier ---")
    supplier_id = get_text("Enter ID of supplier to update: ")
    supplier = Supplier.get_supplier(supplier_id)

    if supplier is None:
        print("Supplier not found.")
        return

    print("Current name:", supplier.name)
    print("Current phone:", supplier.phone)
    print("Current email:", supplier.email)
    print("What do you want to update?")
    print("1. Name")
    print("2. Phone")
    print("3. Email")
    choice = input("Enter choice: ")

    if choice == "1":
        new_name = get_text("Enter new name: ")
        supplier.update(name=new_name)
    elif choice == "2":
        new_phone = input("Enter new phone: ")
        supplier.update(phone=new_phone)
    elif choice == "3":
        new_email = input("Enter new email: ")
        supplier.update(email=new_email)
    else:
        print("Invalid choice.")
        return

    save_supplier_data()
    print("Supplier updated.")


def delete_supplier():
    print("\n--- Delete Supplier ---")
    supplier_id = get_text("Enter ID of supplier to delete: ")
    supplier = Supplier.get_supplier(supplier_id)

    if supplier is None:
        print("Supplier not found.")
        return

    sure = input("Delete " + supplier.name + "? (y/n): ").lower()
    if sure == "y":
        Supplier.delete_supplier(supplier_id)
        save_supplier_data()
        print("Supplier deleted.")
    else:
        print("Cancelled.")


def supplier_menu():
    back = False

    while not back:
        print("\n------ SUPPLIERS ------")
        print("1. Add supplier")
        print("2. View all suppliers")
        print("3. Update a supplier")
        print("4. Delete a supplier")
        print("0. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_supplier()
        elif choice == "2":
            view_suppliers()
        elif choice == "3":
            update_supplier()
        elif choice == "4":
            delete_supplier()
        elif choice == "0":
            back = True
        else:
            print("Invalid choice, please try again.")


def main():
    inventory = load_inventory()
    load_supplier_data()
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
        print("7. Restock a product")
        print("8. Reduce stock")
        print("9. Total stock value")
        print("10. Suppliers")
        print("0. Exit")

        low_count = len(get_low_stock(inventory))
        if low_count > 0:
            print("** " + str(low_count) + " product(s) need restocking **")

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
        elif choice == "7":
            restock_product(inventory)
        elif choice == "8":
            reduce_stock(inventory)
        elif choice == "9":
            show_total_value(inventory)
        elif choice == "10":
            supplier_menu()
        elif choice == "0":
            save_inventory(inventory)
            save_supplier_data()
            print("Goodbye!")
            running = False
        else:
            print("Invalid choice, please try again.")


main()
