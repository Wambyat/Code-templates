# This is explanation of *args and **kwargs
# @params: *topping ie *args: This takes the arguments as tuple
# @params: **details ie **kwargs: This takes the arguments as dictionary. Arguments must be sent as key value pairs

def pizza(name, *toppings, **details):
    print(f"Name: {name}")
    print(f"Toppings: {toppings}")
    print(f"Details: {details}")

pizza("Anirudha", "Mushrooms", "Onions", "Extra Cheese", size="Large", crust="Thin Crust")

# Output:
# Name: Anirudha
# Toppings: ('Mushrooms', 'Onions', 'Extra Cheese')
# Details: {'size': 'Large', 'crust': 'Thin Crust'}
# --------------------------------------------------------------------------------------------------------------



# This is an explaination of *<some iterable here>

ex_tuple = (1, 2, 3, 4, 5)
print(*ex_tuple)

# Output:
# 1 2 3 4 5