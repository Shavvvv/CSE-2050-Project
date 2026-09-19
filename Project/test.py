from store import Store
from product import Product
from customer import Customer



store = Store()
mouse = Product("P100", "Wireless Mouse", 29.99)
keyboard = Product("P101", "Keyboard", 59.99)
store.add_product(mouse)
store.add_product(keyboard)
customer = Customer("C100", "Alex")
store.add_customer(customer)
cart = customer.get_cart()
cart.add_product(mouse)
cart.add_product(keyboard)
print(cart.calculate_total())
print(cart.is_empty())

#  EDGE CASES TESTED

#Find a product or customer that does not exist → return None.
product_search=store.find_product("P109")
if product_search is not None:
   print( vars(product_search))
else: print(product_search)

#• Add a duplicate product ID or customer ID → return False and do not add a second object.

dup_customer=Customer("C101", "Matt")
ans=store.add_customer(dup_customer)
#print(ans)
#• Remove a product that is not in the cart → return False.

x=cart.remove_product("P100")
#print(x)
#• Remove a product that is in the cart → return True.
#• Empty cart → calculate_total() returns 0.0 and is_empty() returns True.