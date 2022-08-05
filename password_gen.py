# Coded_BY_SHA
#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

#for_letters

for x in range(1,nr_letters+1):
  random_letter=random.choice(letters)
  #print(random_letter)
  password+=random_letter 

#for_symblos
  
for y  in range(1,nr_symbols+1):
  random_symbol=random.choice(symbols)
  #print(random_symbol)
  password += random_symbol
  

#for_numbers

for z  in range(1,nr_numbers+1):
  random_numbers=random.choice(numbers)
  #print(random_numbers)
  password += random_numbers
  
new_pass = ''.join(random.sample(password,len(password)))


print(f'\nYour Password is: {new_pass}')