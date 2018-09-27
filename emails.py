
output = open("duplicate-free-email-list.txt", "w")

uniq_lines = []

with open("emails.txt",'r') as file_object:
    lines = file_object.readlines()
    for line in lines:
        if line not in uniq_lines:
            uniq_lines.append(line)

for line in uniq_lines:
    output.write(line)

output.close()