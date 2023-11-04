import os

# for Mac
clear = lambda: os.system('clear')

# for Windows
# clear = lambda: os.system('cls')
clear()

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
print("Your name is: " + name.capitalize())
print("Your age is: " + age)
print("Your city is: " + city.capitalize())

print(name)
print(city)

# name = 'string'
# print(dir(name))

# name = 'Alex'
# print(name.upper())

# print(10, 'Alex', True)

# print(dir(__builtins__))
