import random
import csv

def password_generator():
    #Set up the potential chars for a password
    lower_case = 'abcdefghijklmnopqrstuvwyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*?><;=+-_'

    valid_characters = lower_case + upper_case + numbers + symbols
    password_len = 12

    password = "".join(random.sample(valid_characters, password_len))
    return password

def changer():
    # get input from the user for which password to alter
    while 1:
        try:
            pw_to_change = str(input("\nWhich password do you want to change?\n")).upper()
        except ValueError:
            print("please enter a string")
            continue
        else:
            break

    password = password_generator()

    # read the file and change appropriate line
    with open('passwords.csv', 'r') as fp:
        lines = []
        for row in fp:
            current_row = row.strip('\n').split(",")
            if current_row == [] or current_row == '': continue

            lines.append(row)
            
            if current_row[0] == pw_to_change:
                lines.remove(row)
                current_row[1] = password
                print(f"\nPassword for {pw_to_change} has been changed.")

                data = pw_to_change + ',' + password + '\n'
                lines.append(data)
    fp.close()

    # re-write the files contents
    with open('passwords.csv', 'w') as fp:
        for line in lines:
            fp.write(line)
    fp.close()

def finder():
    while 1:
        try:
            wanted_pw = str(input("\nWhich password do you want?\n")).upper()
        except ValueError:
            print("please enter a string")
            continue
        else:
            break

    with open('passwords.csv', 'r') as fp:
        csv_reader = csv.reader(fp, delimiter=',')
        for row in csv_reader:
            if row[0] == wanted_pw:
                print(f'\nPassword for {wanted_pw}: {row[1]}')
                break
    fp.close()

def generator():
    # Get the user input
    while 1:
        try:
            name = str(input("\nWhat is the password for? ")).upper()
        except ValueError:
            print("Please enter a String")
            continue
        else:
            break

    password = password_generator()

    data = name + "," + password + '\n'

    # open the file to read, to make sure that there isn't already a password
    try:
        with open('passwords.csv', 'r') as fp:
            for row in fp:
                current_row = row.strip('\n').split(",")
                if current_row == [] or current_row == '': continue
                if current_row[0] == name:
                    print(f'password already exists for that item')
                    exit(0)    
            fp.close()
    except FileNotFoundError:
        print("you don't have a passwords file... we will create one for you...\npasswords.csv has been generated.\n please run the program and try again")
        f = open("passwords.csv", 'x')
        f.close()

    # Write the contents to the file
    fp = open('passwords.csv', 'a')
    fp.write(data)
    fp.close()

    print(f"\nPassword for {name} has successfully been generated")

def delete():
    # get the user input for which password to delete
    while 1:
        try:
            to_delete = str(input("\nWhich password do you want to delete?\n")).upper()
        except ValueError:
            print("please enter a string")
            continue
        else:
            break

    # remove the row from the arary of lines
    with open('passwords.csv', 'r') as fp:
        lines = []
        for row in fp:
            current_row = row.strip('\n').split(",")
            if row == [] or row == '': continue
            
            lines.append(row)
            
            if current_row[0] == to_delete:
                lines.remove(row)   
    fp.close()

    # re-write the file
    with open('passwords.csv', 'w') as fp:
        for line in lines:
            line = line.strip('\n').split(",")
            data = line[0] + ',' + line[1] + '\n'
            fp.write(data)
    fp.close()

    print(f"\nPassword for {to_delete} has successfully been removed")

def sort():

    lines = []

    # append each line of the file to an array
    with open('passwords.csv', 'r') as fp:
        for row in fp:
            current_row = row.strip('\n').split(",")
            lines.append(row)
    # sort the array
    lines.sort()
    fp.close()

    # re-write the file
    with open('passwords.csv', 'w') as fp:
        for line in lines:
            fp.write(line)
    fp.close()

    print("\npasswords have successfully been sorted!")

def main():
    while 1:
        try:
            reply = int(input("What would you like to do?\n1. Generate a password\n2. Change a password\n3. Delete a password\n4. Find a password\n5. Sort the passwords alphabetically\nYour Reply: "))
            if reply < 0 or reply > 5:
                print("please try a valid option")
                continue
        except ValueError:
            print("please enter a number")
            continue
        else:
            break

    if reply == 1:
        generator()
    elif reply == 2:
        changer()
    elif reply == 3:
        delete()
    elif reply == 4:
        finder()
    elif reply == 5:
        sort()

if __name__ == '__main__':
    main()