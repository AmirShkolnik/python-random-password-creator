import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list("!#$%&()*+?€/")

password_length = 11

nr_letters = random.randint(1,5)
nr_numbers = random.randint(1,5)
nr_symbols = random.randint(1,5)

password_list = []

for letter in range(0, nr_letters):
    password_list += random.choice(letters)

for number in range(0, nr_numbers):
    password_list += random.choice(numbers)

for symbol in range(0, nr_symbols):
    password_list += random.choice(symbols)

password = ""

for char in password_list:
    password += char

print(password)