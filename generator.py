# Generates a password if one doesn't already exist

import random
from csv import writer

# Get the user input
while 1:
    try:
        name = str(input("What is the password for?\n")).upper()
    except ValueError:
        print("Please enter a String")
        continue
    else:
        break

#Set up the potential chars for a password
lower_case = 'abcdefghijklmnopqrstuvwyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*?><;=+-_'

valid_characters = lower_case + upper_case + numbers + symbols
password_len = 12

password = "".join(random.sample(valid_characters, password_len))

print(f'Password is: {password}')

data = []

# open the file to read, to make sure that there isn't already a password
try:
    with open('passwords.csv', 'r') as fp:
        current_values = fp.read()
        if 3 == 5:
            # Implement for when there is a duplicate name
            pass

        data.append(name)
        data.append(password)    
        fp.close()
except FileNotFoundError:
    print("you don't have a passwords file... we will create one for you...\npasswords.csv has been generated.\n please run the program and try again")
    f = open("passwords.csv", 'x')
    f.close()

# Write the contents to the file
fp = open('passwords.csv', 'a')
writer_object = writer(fp)
writer_object.writerow(data)
fp.close()