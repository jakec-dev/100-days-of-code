import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', "#", "$", "%", "&", "*", "(", ")"]

print("Welcome to the PyPassword Generator!")

number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))
number_of_numbers = int(input("How many numbers would you like?\n"))

pw_char_list = []
for i in range(1,number_of_letters+1):
   pw_char_list.append(random.choice(letters))
for i in range(1,number_of_numbers+1):
   pw_char_list.append(random.choice(numbers))
for i in range(1,number_of_symbols+1):
   pw_char_list.append(random.choice(symbols))
random.shuffle(pw_char_list)

password = ""
for i in pw_char_list:
    password += i

print(password)