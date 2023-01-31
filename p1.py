# name = input('what is your name? ')
# fav_color = input('what is ur fav color? ')
# print(name + ' likes ' + fav_color)


# birth_year = input('birth_year: ')
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(age)
# print(type(age))

# weight_pounds = input('what is ur weight(in pounds)? ')
# weight_kg = int(weight_pounds) * 0.45
# print(weight_kg)

# fname = 'anamika'
# lname = 'bhatt'
# msg = f'{fname} [{lname}] is a coder'
# print(msg)

# name = input('enter ur name: ')
# name_len = len(name)
# if (name_len < 3):
#     print('name must be at least 3 characters')
# elif (name_len > 50):
#     print('name can be a max of 50 characters')
# else:
#     print('name looks good!')


print('Need help!!')
print('start - to start the car')
print('stop - to stop the car')
print('quit - to exit')

s = 'start'
st = 'stop'

choice = input('enter any choice[start/stop/quit]')
while (choice != quit):
    if (choice == s):
     print('car is started')
    elif(choice == st):
     print('car is stopped')
    else:
        print("i can't understand")
break

    






