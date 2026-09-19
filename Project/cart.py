#Necessary import to allow for the cart's intended purposes
from product import Product

class ShoppingCart:

    
    def __init__(self):
       """Initializes the list that will record products in users' carts"""
       self.items=[]
       
    def add_product(self,product: Product):
        """Adds an item to the cart"""
        self.items.append(product)
        
        


    def remove_product(self,product_id:str):
        """removes product in user's cart based on given id """
        index=0
        product_removed=True
        for product in self.items:           
            id=product.get_id()
            if(product_id == id):
                self.items.pop(index)
                product_removed=True
                break
            else: 
                product_removed=False
        index+=1 
        return product_removed


    def get_items(self):
        """returns all items in cart"""
        return self.items

    def calculate_total(self):
        """Computes the total price of items in the cart"""
        total=0.0
        for product in self.items:   
            total+=product.price 
        return total

    def is_empty(self):
        """Checks to see whether cart is empty or not."""
        if not self.items:
            print("List is empty")
            return True
        else:
            print("List is not empty")
            return False