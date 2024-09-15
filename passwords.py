import string
import random

def main():
    print('Welcome to Random Password Generator.')
    length = int(input('Enter the length of the password: '))
    include_uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
    include_special = input('Include special characters? (y/n): ').lower() == 'y'
    include_numbers = input('Include numbers? (y/n): ').lower() == 'y'

    password = generate_password(length,include_uppercase,include_numbers,include_special)
    print(password)

def generate_password(length,include_uppercase=True,include_numbers=True,include_special=True):

    characters = string.ascii_lowercase

    if include_uppercase:
        characters += string.ascii_uppercase

    if include_numbers:
        characters += string.digits

    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range (length))
    return password

main()