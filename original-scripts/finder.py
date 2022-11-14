import csv

while 1:
    try:
        wanted_pw = str(input("Which password do you want?\n")).upper()
    except ValueError:
        print("please enter a string")
        continue
    else:
        break


with open('passwords.csv', 'r') as fp:
    csv_reader = csv.reader(fp, delimiter=',')
    for row in csv_reader:
        if row[0] == wanted_pw:
            print(f'Password for {wanted_pw}: {row[1]}')
            break

fp.close()
