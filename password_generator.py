#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''

#order_letter = 0
for a in range(0, nr_letters):
    order_letter = random.randint(0, len(letters) - 1)
    #alternative option: order_letter=random.choice(lettes)
    password = password + letters[order_letter]

#order_number = 0
for b in range(0, nr_numbers):
    order_number = random.randint(0, len(numbers) - 1)
    password = password + numbers[order_number]

#order_symbol = 0
for c in range(0, nr_symbols):
    order_symbol = random.randint(0, len(symbols) - 1)
    password = password + symbols[order_symbol]

password_random = ''.join(random.sample(password, len(password)))
#Alternative option: make a list of the characters instead of a string, and then use random.shuffle() to shuffle the characters in the list

print(f'Password with orderly characters: {password}')
print(f'Password with randomized characters: {password_random}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# characters = [letters, numbers, symbols]
# #print(characters)
# nr_char = nr_letters + nr_numbers + nr_symbols

# password=''
# for char in range(0,nr_char):
#   if len(pass)<nr_char:
