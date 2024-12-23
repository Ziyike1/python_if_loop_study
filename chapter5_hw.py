#5.1
friend = 'gav'
print(friend == 'roger')
print(friend == 'gav')
print(friend == 'GAV'.title())
print(friend == 'GAV'.lower())
print(friend == 'GAV'.upper())
friend = 'GAV'
print(friend == 'gav'.upper())
num_1 = 99
num_2 = 101
print(num_1 == num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)
print(num_1 != num_2)


#5.2
string_1 = 'adc'
string_2 = 'ADC'
print(string_1 == string_2)
print(string_1 == string_2.lower())

num_3 = -1
num_4 = 0
print(num_3 > num_4)
print(num_3 < num_4)

if num_3 < num_4 and string_1 == string_2.lower():
    print(True)


print(num_3 > num_4 or string_1 != string_2.lower())

my_list = [1,3,'ald',7,0,'hhh']
print(1 in my_list)
print(6 not in my_list)


#5.3
alien_color = 'green'

if alien_color == 'green':
    print("you gain 5 point")

if alien_color == 'red':
    print("you gain 10 point")


#5.4
alien_color = 'red'

if alien_color == 'green':
    point = 5
else:
    point = 10
print(f"\nyou gain {point} point.")


#5.5
alien_color = 'red'

if alien_color == 'green':
    point = 5
elif alien_color == 'yello':
    point = 10
else:
    point = 15
print(f"\nyou gain {point} point.")


#5.6
age = 15
if age < 2:
    print("baby")
elif age < 4:
    print("young child")
elif age < 13:
    print("child")
elif age < 18:
    print("youth")
elif age < 65:
    print("middle-age man")
else:
    print("old man")


#5.7
favorite_fruit = ['apple','pinapple','banana','peer']

if 'apple' in favorite_fruit:
    print("you really like apple")
if 'pinapple' in favorite_fruit:
    print("you really like pinapple")
if 'banana' in favorite_fruit:
    print("you really like banana")
if 'peer' in favorite_fruit:
    print("you really like peer")
if 'tomato' not in favorite_fruit:
    print("you really do not like tomato")


#5.8
user_list = []


#5.9
# user_list = ['admin','gav','frank','andy','ryan']

if user_list:
    for user in user_list:
        if user == 'admin':
            print("\nHello admin, would you like to see the status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users.\n")


#5.10
current_users = ['admin','Gav','Frank','andy','Ryan']
new_users = ['gav','frank','ANDREW','Leo','sara']
current_users_lower = []

for current_user in current_users:
    current_users_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("you need user another username")
    else:
        print("you can use this username")


#5.11
number_list = [1,2,3,4,5,6,7,8,9]
for number in number_list:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")