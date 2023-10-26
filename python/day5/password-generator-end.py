# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# random letters
password = ""
random_letter = random.sample(letters, nr_letters)
for l in random_letter:
    password += l

# random_symbols
random_symbol = random.sample(symbols, nr_symbols)
for s in random_symbol:
    password += s

# random_numbers
random_number = random.sample(numbers, nr_numbers)
for n in random_number:
    password += n

print(f"Here is your password: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
shuffle = []
for p in password:
    shuffle += p

random.shuffle(shuffle)

shuffled_order = ""
for shuf in shuffle:
    shuffled_order += shuf

print(f"Here is your password: {shuffled_order}")

# Alternative solution
# Eazy Level
password2 = ""

for char in range(1, nr_letters + 1):
    password2 += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password2 += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password2 += random.choice(numbers)

print(f"Here is your password: {password2}")

# Hard Level
password2_list = []

for char in range(1, nr_letters + 1):
    password2_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password2_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password2_list.append(random.choice(numbers))

random.shuffle(password2_list)
password3 = ""
for char in password2_list:
    password3 += char

print(f"Here is your password: {password3}")
