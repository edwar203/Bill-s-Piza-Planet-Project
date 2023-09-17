"""
  Name: pizza_planet.py
  Author: Bill Edwards
  Created 09/17/2023
  Purpose: To create working program to begin with and then to build from there instead of jumping ahead of myself
"""

#TODO: Create contants
SMALL_COST = 5.00
MEDIUM_COST = 10.00
LARGE_COST = 15.00
CHEESE = 0.50
PEPPERONI = 1.00
SUPREME = 2.00

#TODO: Get user input for pizza size and toppings
pizza_size = input("What size pizza would you like to order(Small, Meduim, or Large): ").upper
pizza_topping = input("What kind of topping would you like on your pizza(Cheese, Pepperoni, or Supreme): ").upper

#TODO: Apply user order to cost
if pizza_size == "SMALL":
  pizza_price = SMALL_COST
elif pizza_size == "MEDIUM":
  pizza_price = MEDIUM_COST
elif pizza_size == "LARGE":
  pizza_price = LARGE_COST
else:
  print("Please choose either SMALL, MEDIUM, or LARGE for your pizza size!")
  continue

if pizza_topping == "CHEESE":
  topping_price = CHEESE
elif pizza_topping == "PEPPERONI":
  topping_price = PEPPERONI
elif pizza_topping == "SUPREME":
  topping_price = SUPREME
else:
  print("Please choose either CHEESE, PEPPERONI, or SUPREME for your pizza topping!")


#TODO: Calculate cost of order
total_cost = pizza_price + topping_price

#TODO: Display order to user
print(f"You ordered a {pizza_size} pizza with {pizza_topping} for your topping")
print(f"The cost of a {pizza_size} pizza is ${pizza_price:.2f}.")
print(f"The cost of {pizza_topping} is ${topping_price:.2f}.")
print(f"The total for your pizza is ${total_cost:.2f}")


#TODO: Ask user if they would like to order again
