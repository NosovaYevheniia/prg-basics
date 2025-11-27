###
# Reads from file, line by line
#
counter = 0
with open('countries.txt', 'r') as file:
    for line in file:
        counter += 1
        print(counter, line, end="")