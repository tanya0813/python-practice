import random #used to choose random characters.
import string #provides predefined sets like ascii_letters, digits, and punctuation

def password_generator(length=12): #by default length=12
    character= string.ascii_letters +string.digits + string.punctuation #all letters (a-z, A-Z) + numbers (0-9) + special symbols.
    password= ''.join(random.choice(character)for _ in range(length))  #random.choice- to pick one random char from a sequence
    return password


length=input('Enter the length of password: ') #keep the input as a string first

if length.strip() == "":   # if empty input, then default value =12
    length = 12
else:
    length = int(length)   # if a number then convert to integer


password=password_generator(length)


print("Your Secure Random password is :", password)
