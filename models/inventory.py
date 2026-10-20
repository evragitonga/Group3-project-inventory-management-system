from models.product import Product
from util.generate_id import generate_id
class Inventory:
    def __init__(self):
        self._inventory = {}


    def add_product(self, product):
        if product.product_id is None:
            product.product_id = self._generate_id()

        if product.product_id in self._inventory:
            print("Product already exists in inventory.")
            return None

        self._inventory[product.product_id] = product
        return product


    def _generate_id(self):
        return generate_id("PDT",self._inventory)

    def update_product(
        self, product_id, name=None, price=None, quantity=None, category=None
    ):
        product = self.get_product(product_id)

        if product is None:
            return False

        if name is not None:
            product.name = name
        if price is not None:
            product.price = price
        if quantity is not None:
            product.quantity = quantity
        if category is not None:
            product.category = category

        return True


    def remove_product(self, product_id):
        if product_id not in self._inventory:
            print("project not found")
        else:
            return self._inventory.pop(product_id)

    def get_product(self, product_id):
        return self._inventory.get(product_id)

    def all_products(self):
        return list(self._inventory.values())

    def search_product(self, search_term):
        search_term = search_term.lower()

        results = []

        for product in self._inventory.values():
            if search_term in product.product_id.lower() or search_term in product.name.lower():
                results.append(product)
        return results

    def reduce_stock(self, product_id, quantity):
        product = self.get_product(product_id)
        if product is None:
            print("Product not found.")
        else:
            product.quantity -= quantity

    def restock_product(self, product_id, quantity):
        product = self.get_product(product_id)
        if product == None:
            print("Product not found")
        else:
            product.quantity += quantity

    def low_stock_products(self,quantity):
        low_stock = []
        for product in self._inventory.values():
            if product.quantity < quantity:
                low_stock.append(product)
        return low_stock
    def total_stock_value(self):
        total_value = 0
        for product in self._inventory.values():
           total_value += (product.quantity * product.price)
        return total_value