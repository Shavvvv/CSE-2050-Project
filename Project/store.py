# access is needed to store product and customer data 
from product import Product
from customer import Customer

class Store():
    """main platform for Store database that has cus"""

    def __init__(self):
        """initializes the instance, with lists to store product """
        self.products=[]
        self.customers=[]

        #PRODUCTS
    def add_product(self, product:Product):
            """Adds a new product to the Product Database"""
            product_added=False
            if not self.products:
                 self.products.append(product)
                 product_added=True
            else: 
             for product_check in self.products:       
                    id=product_check.get_id() 
                    if(id==product.get_id()):
                        print("product with id already exitst")
                    else: product_added=True               
            return product_added

    def find_product(self,product_id: str):
        """Looks for a product based on user given id"""
        product_found=None
        for product in self.products: 
            id=product.get_id()       
            if(id==product_id):
                product_found=product
        return product_found

            
    # CUSTOMERS
    def add_customer(self, customer:Customer):
        """Adds a new customer to the Customer Database"""
        customer_added=False
        if not self.customers:
             self.customers.append(customer)
             customer_added=True
        else: 
         for customer_check in self.customers:       
                id=customer_check.get_id() 
                if(id==customer.get_id()):
                    print("customer with id already exitst")
                else: customer_added=True               
        return customer_added
    
    
    def find_customer(self,customer_id: str):
            """searches for customer based on user given id"""
            customer_found=None
            for customer in self.customers: 
                id=customer.get_id()              
                if(id==customer_id):
                    customer_found=customer               
            return customer_found

