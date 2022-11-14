# sort the texxt file by alphabetical order

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