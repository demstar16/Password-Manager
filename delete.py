# deletes a given names password

# get the user input for which password to delete
while 1:
    try:
        to_delete = str(input("Which password do you want to delete?\n")).upper()
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

print(f"Password for {to_delete} has successfully been removed")