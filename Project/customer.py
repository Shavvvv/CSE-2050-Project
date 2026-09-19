#SG ADDED
from cart import ShoppingCart

#SG

class Customer:
    """Represents one customer of the store."""

    def __init__(self, customer_id: str, name: str):
        """Initialize a customer with an ID, name, and empty shopping cart."""
        self.customer_id = customer_id
        self.name = name
        self.cart =  ShoppingCart()
    

    def get_id(self) -> str:
        """Return the customer ID."""
        return self.customer_id
    
    def get_name(self) -> str:
        """Return the customer name."""
        return self.name
    
    def get_cart(self) -> ShoppingCart:
        """Return the customer's shopping cart.""" 
        return self.cart