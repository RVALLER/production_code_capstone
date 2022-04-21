# production_code_capstone
Capstone assignment


DESCRIPTION: Production code that takes a shopping cart of products of type item and calculates total based on state and state tax rates

INSTALL INSTRUCTIONS: 

Simply Run the required project main.py, enter your state abreviation of choice and you'll be given your total
If you want to add a new item to be included in the total use the following format:
your_item = item(yourname, price, qty, category) # Note that category must be cast as a string of either 'wic' 'clothing' or 'other'
Subsequently, you must append it to the shopping cart:
shopping_cart.append(your_item) 
and then simply rerun main.

NOT INCLUDED: Projected future changes: Auto loop to restart the software and choose new state & maybe add a feature to let user add new item to shopping cart from the main loop.
