requested_toppings = ['mushrooms','green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry, the green pepper are out of our storage")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza")


requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza")
else:
    print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pinapple','extra cheese']

requested_toppings = ['mushrooms','french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")

print("\nFinished making your pizza")