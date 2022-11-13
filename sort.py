lines = []

with open('passwords.csv', 'r') as fp:
    for row in fp:
        current_row = row.strip('\n').split(",")
        lines.append(current_row)

lines.sort()
fp.close()

with open('passwords.csv', 'w') as fp:
    for line in lines:
        data = line[0] + ',' + line[1] + '\n'
        fp.write(data)
fp.close()