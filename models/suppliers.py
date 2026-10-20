from util.generate_id import generate_id


class Supplier:
    """Represent a supplier in the inventory system."""

    _suppliers = {}
    _next_id = 1000

    def __init__(self, supplier_id, name, phone, email):
        """Initialize a supplier with its details."""
        if not name.strip():
            raise ValueError("Supplier name cannot be empty.")

        self.supplier_id = supplier_id
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email.strip()

    def __repr__(self):
        """Return a readable representation of the supplier."""
        return (
            f"Supplier(ID={self.supplier_id}, "
            f"Name={self.name!r}, "
            f"Phone={self.phone!r}, "
            f"Email={self.email!r})"
        )

    @classmethod
    def create_supplier(cls, name, phone, email):
        """Create and register a supplier with a unique ID."""
        supplier_id = generate_id(cls, "SUP", cls._suppliers)
        supplier = cls(supplier_id, name, phone, email)
        cls._suppliers[supplier_id] = supplier
        return supplier

    @classmethod
    def get_supplier(cls, supplier_id):
        """Find a supplier by ID."""
        return cls._suppliers.get(supplier_id)

    @classmethod
    def all_suppliers(cls):
        """Return all registered suppliers."""
        return list(cls._suppliers.values())

    def update(self, name=None, phone=None, email=None):
        """Update the supplied details without changing other fields."""
        if name is not None:
            if not name.strip():
                raise ValueError("Supplier name cannot be empty.")
            self.name = name.strip()

        if phone is not None:
            self.phone = phone.strip()

        if email is not None:
            self.email = email.strip()

        return self

    @classmethod
    def delete_supplier(cls, supplier_id):
        """Delete a supplier by ID."""
        return cls._suppliers.pop(supplier_id, None) is not None

    def to_dict(self):
        """Convert supplier details into a dictionary for JSON storage."""
        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data):
        """Rebuild a supplier from a dictionary."""
        supplier = cls(
            data["supplier_id"],
            data["name"],
            data["phone"],
            data["email"],
        )
        cls._suppliers[supplier.supplier_id] = supplier
        return supplier