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
    changed = False

    # read the file and change appropriate line
    with open('passwords.csv', 'r') as fp:
        lines = []
        for row in fp:
            current_row = row.strip('\n').split(",")
            if current_row == [] or current_row == '': continue

            lines.append(row)
            
            if current_row[0] == pw_to_change:
                lines.remove(row)
                changed = True
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

    if changed == True:
        print(f"\nPassword for {pw_to_change} has successfully changed")
    else:
        print(f"\nThere is no password for {pw_to_change}, try to generate one.")

def finder():
    while 1:
        try:
            wanted_pw = str(input("\nWhich password do you want?\n")).upper()
        except ValueError:
            print("\nplease enter a string\n")
            continue
        else:
            break

    found = False

    with open('passwords.csv', 'r') as fp:
        for row in fp:
            current_row = row.strip('\n').split(",")
            if current_row[0] == wanted_pw:
                found = True
                print(f'\nPassword for {wanted_pw}: {current_row[1]}')
                break
    fp.close()

    if found == False:
        print(f"\nthere is no password for {wanted_pw}")

def generator():
    # Get the user input
    while 1:
        try:
            name = str(input("\nWhat is the password for? ")).upper()
        except ValueError:
            print("\nPlease enter a String\n")
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
                    print(f'\npassword already exists for that item')
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
            print("\nplease enter a string\n")
            continue
        else:
            break

    deleted = False
    
    # remove the row from the arary of lines
    with open('passwords.csv', 'r') as fp:
        lines = []
        for row in fp:
            current_row = row.strip('\n').split(",")
            if row == [] or row == '': continue
            
            lines.append(row)
            
            if current_row[0] == to_delete:
                lines.remove(row)
                deleted = True   
    fp.close()

    # re-write the file
    with open('passwords.csv', 'w') as fp:
        for line in lines:
            fp.write(line)
    fp.close()
    if deleted == True:
        print(f"\nPassword for {to_delete} has successfully been removed")
    else:
        print(f"\nThere is no password for {to_delete}")

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

    print("\npasswords have successfully been sorted!\n")

def main():
    while 1:
        try:
            reply = int(input("What would you like to do?\n1. Generate a password\n2. Change a password\n3. Delete a password\n4. Find a password\n5. Sort the passwords alphabetically\nYour Reply: "))
            if reply < 0 or reply > 5:
                print("\nplease try a valid option\n")
                continue
        except ValueError:
            print("\nplease enter a number\n")
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