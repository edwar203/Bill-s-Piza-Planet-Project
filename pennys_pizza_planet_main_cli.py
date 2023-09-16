"""
"""
import pennys_pizza_planet_class as pizza

def get_pizza_size_input():
        #TODO get int for drinks sold
        pizza_size = str(input("What size pizza? ").lower)
        return pizza_size

def get_pizza_topping_input():
        #TODO get int for drinks sold
        pizza_topping = str(input("What pizza topping(Cheese, Pepperoni, or Supreme: ").lower)
        return pizza_topping

def display(pizza_size, pizza_topping):
#TODO: display total cost for customer
        pizza_size = pennys_pizza.get_pizza_size()
        pizza_topping = pennys_pizza.get_pizza_topping
        total_sale = pennys_pizza.get_total_sale(pizza_topping)
        print(f"The size of the pizza you ordered today is: {pizza_size}")
        print(f"The pizza topping you ordered today is {pizza_topping}")
        print(f"Your total today is ${total_sale:,.2f}")

pizza_size = get_pizza_size_input()
pizza_topping = get_pizza_topping_input()
pennys_pizza = pizza.pennyspizza()
display(pizza_size, pizza_topping)

