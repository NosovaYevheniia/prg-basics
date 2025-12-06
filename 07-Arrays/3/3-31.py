arr = [[-38, 19], [5,40], [-7,11], [29,16]]

maximum_number = [0][0]
minimum_number = [0][0]
max_col = 0
min_row = 0
max_col = 0
max_row = 0
for row in arr:
    for i in row:
        if i < minimum_number:
            minimum_number = i
            min_row = arr.index(row)
            min_col = row.index(i)
        if i > maximum_number:
            maximum_number = i
            max_row = arr.index(row)
            max_col = row.index(i)

print(f"The smallest number is {minimum_number} in row {min_row} and {min_col}")
print(f"The largest number is {maximum_number} in row {max_row} and {max_col}")