"""
 Filename: bills_drink_shack3.py
 Author: Bill Edwards
 Created: 09/03/2023
 Purpose: POS program OOP
"""

#cost of drinks for the customer
COST_SMALL = 5.00
COST_MEDIUM = 7.50
COST_LARGE = 10.00
COST_SUPREME = 2.00
COST_PEPPERONI = 1.00
COST_CHEESE = 0

class pennyspizza:
    def __init__(self):
        pass
        
    def get_pizza_size(pizza_size):
        #validation
        if pizza_size == "Small".lower:
            pizza_size = COST_SMALL
            return pizza_size
        elif pizza_size == "Medium".lower:
            pizza_size = COST_MEDIUM
            return pizza_size
        elif pizza_size == "Large".lower:
            pizza_size = COST_LARGE
            return pizza_size
        
    def get_pizza_topping(pizza_topping):
        if pizza_topping == "Small".lower:
            pizza_topping = COST_SMALL
            return pizza_topping
        elif pizza_topping == "Medium".lower:
            pizza_topping = COST_MEDIUM
            return pizza_topping
        elif pizza_topping == "Large".lower:
            pizza_topping = COST_LARGE
            return pizza_topping

    def get_total_sale(pizza_size, pizza_topping):
        total_sale = pizza_size + pizza_topping
        return total_sale
