#In easy level the order of symbols is fixed which is not ideal.

import random

print("Welcome to Password Generator")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
specialSymbols = ['!','@','#','$','%','^','&','*','(',')','=','+']

password_list = []
input_letters_list = int(input("How many letters you want in the password?\n"))
input_numbers_list = int(input("How many numbers you want in the password?\n"))
input_special_list = int(input("How many special symbols you want in the password?\n"))

for pwd in range(1, input_letters_list+1):
    password_list += random.choice(letters)
for pwd in range(1, input_numbers_list+1):
    password_list += random.choice(numbers)
for pwd in range(1, input_special_list+1):
    password_list += random.choice(specialSymbols)


random.shuffle(password_list) 
#shuffles the order of pwd generated
password = ""
for pwd in password_list:
 password += pwd

print(f"Your password is: {password}")



