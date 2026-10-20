from util.generate_id import generate_id
class Product:
    _next_id = 1000
    _products = {}
    def __init__(self,product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    @classmethod
    def _generate_id(cls):
        return generate_id(cls,"PDT",cls._products)
    
    @classmethod
    def create_product(cls,name,category,price,quantity):
        product_id = cls._generate_id()
        product = cls(product_id,name,category,price,quantity)
        cls._products[product_id] = product
        return product

    def __repr__(self):
        return f"""
        Product(
        id:{self.product_id}
        name:{self.name}
        category:{self.category}
        price:{self.price}
        quantity:{self.quantity}
        )"""
    
    def to_dict(self):
        return {
            "product_id":self.product_id,
            "name":self.name,
            "category":self.category,
            "price":self.price,
            "quantity":self.quantity
        }

    @classmethod
    def from_dict(cls, data):
        product = cls.__new__(cls)
        product.product_id = data["product_id"]
        product.name= data["name"]
        product.category = data["category"]
        product.price = data["price"]
        product.quantity = data["quantity"]
        return  product
