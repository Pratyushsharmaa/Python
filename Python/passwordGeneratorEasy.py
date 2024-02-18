import random

print("Welcome to Password Generator")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
specialSymbols = ['!','@','#','$','%','^','&','*','(',')','=','+']
input_letters = int(input("How many letters you want in the password?\n"))
input_numbers = int(input("How many numbers you want in the password?\n"))
input_special_symbols = int(input("How many special symbols you want in the password?\n"))
password = ""
for pwd in range(1, input_letters+1):
    password += random.choice(letters)
for pwd in range(1, input_numbers+1):
    password += random.choice(numbers)
for pwd in range(1, input_special_symbols+1):
    password += random.choice(specialSymbols)

print(password)
