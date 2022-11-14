import random

while 1:
    try:
        pw_to_change = str(input("Which password do you want to change?\n")).upper()
    except ValueError:
        print("please enter a string")
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

with open('passwords.csv', 'r') as fp:
    lines = []
    for row in fp:
        current_row = row.strip('\n').split(",")
        if current_row == [] or current_row == '': continue

        lines.append(row)
        
        if current_row[0] == pw_to_change:
            lines.remove(row)
            current_row[1] = password
            print(f"Password for {pw_to_change} has been changed.")

            data = pw_to_change + ',' + password + '\n'
            lines.append(data)
fp.close()

with open('passwords.csv', 'w') as fp:
    for line in lines:
        fp.write(line)
fp.close()