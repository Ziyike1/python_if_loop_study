cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = "bmw"
car2 = "Bmw"
print(car == car2)
print(car == car2.lower())

requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("This is not the correct answer!")
if answer < 42:
    print("This is a lower answer")

age_0 = 22
age_1 = 18
print((age_0 >= 21) and (age_1 >= 21))
print((age_0 >= 21) and (age_1 <= 21))

print((age_0 >= 21) or (age_1 >= 21))
print((age_0 >= 23) or (age_1 <= 15))

#检测特定的值是否在列表中使用判断词"in" / "not in"
requested_topping = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_topping)
print('pepperoni' in requested_topping)

banned_user = ['andrew','carolina','david']
user = 'marie'
if user not in banned_user:
    print(f"{user.title()}, you can post anything if you want.")