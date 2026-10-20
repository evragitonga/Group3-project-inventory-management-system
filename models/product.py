class Product:
    def __init__(self, name, category, price, quantity):
        self.product_id = None
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    
    @classmethod
    def create_product(cls,name,category,price,quantity):
        return cls(name,category,price,quantity)
        
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
        product.product_id = data["product_id"]
        return  product
