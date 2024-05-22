from time import sleep
from random import choice, shuffle
import string

def line(n):
    print("-" * len(n))
    print(n)
    print("-" * len(n))

line("Welcome to your password generator")
print("First select the characteristics of your password")
line("""#1 - Password Length
     #2 - Number of special characters
     #3 - Number of digits""")

while True:
    length = int(input("How many characters will your password need? "))
    special = int(input("Of those, how many are special characters? "))
    numbers = int(input("Of those, how many are numbers? "))
    if special > length:
        print("It's impossible, there are more special characters than total characters.")
    elif numbers > length:
        print("It's impossible, there are more numbers than total characters.")
    elif special + numbers > length:
        print("It's impossible, the sum of special characters and numbers exceeds the total characters.")
    else:
        print("Generating")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        break

# Character pools
letters = string.ascii_letters
special_chars = "!@#$%^&?"
digits = string.digits

# Generate password components
password_chars = []
password_chars.extend(choice(special_chars) for _ in range(special))
password_chars.extend(choice(digits) for _ in range(numbers))
password_chars.extend(choice(letters) for _ in range(length - special - numbers))

# Shuffle to mix the characters
shuffle(password_chars)

# Join to form the final password
password = ''.join(password_chars)

# Display the generated password
print("Your generated password is:")
print(password)
