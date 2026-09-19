
class Product:
    """Represents one product sold by the store."""

    def __init__(self, product_id: str, name: str, price: float):
        """Initialize a product with an ID, name, and price."""
        self.product_id = product_id
        self.name = name
        self.price = price
      
    def get_id(self) -> str:
        """Return the product ID."""
        return self.product_id
    
    def get_name(self) -> str:
        """Return the product name."""
        return self.name
    
    def get_price(self) -> float:
        """Return the product price."""
        return self.price
