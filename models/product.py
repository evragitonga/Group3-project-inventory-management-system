class Product:
  _next_id = 1000

  def __init__(self, name, category, price, quantity):
      self.product_id = self._generate_id()
      self.name = name
      self.category = category
      self.price = price
      self.quantity = quantity

  @classmethod
  def _generate_id(cls):
    pass

  def __repr__(self):
      pass

  def update(self, name=None, category=None, price=None, quantity=None):
      pass

  def to_dict(self):
      pass

  @classmethod
  def from_dict(cls, data):
      pass