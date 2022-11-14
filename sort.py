lines = []

with open('passwords.csv', 'r') as fp:
    for row in fp:
        current_row = row.strip('\n').split(",")
        lines.append(row)

lines.sort()
fp.close()

with open('passwords.csv', 'w') as fp:
    for line in lines:
        fp.write(line)
fp.close()