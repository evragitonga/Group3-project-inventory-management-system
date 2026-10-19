class Supplier:
  _suppliers = {}
  _next_id = 1000

  def __init__(self, supplier_id, name, phone, email):
      pass

  def __repr__(self):
      pass

  @classmethod
  def create_supplier(cls, name, phone, email):
      pass

  @classmethod
  def get_supplier(cls, supplier_id):
      pass

  @classmethod
  def all_suppliers(cls):
      pass

  def update(self, name=None, phone=None, email=None):
      pass

  @classmethod
  def delete_supplier(cls, supplier_id):
      pass

  def to_dict(self):
      pass

  @classmethod
  def from_dict(cls, data):
      pass