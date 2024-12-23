age = 17
if age >= 18:
    print("Your are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote")
    print("Please registered to vote as soon as you turn 18!")

age = 12
if age < 4:
    print("0$, free to enter")
elif age < 18:
    print("you need to pay 25$ to enter")
else:
    print("you need to pay 40$ to enter")

age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age > 65:
    price = 20
# else:
#     price = 20
print(f"You need pay {price} to enter.\n")

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("extra cheese")
print("Finshed making your pizza.")


