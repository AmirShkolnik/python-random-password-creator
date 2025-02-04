import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list("!#$%&()*+")

nr_letters = random.randint(1,5)
nr_numbers = random.randint(1,5)
nr_symbols = random.randint(1,5)

password_list = []

for letter in range(0, nr_letters):
    password_list += random.choice(letters)


