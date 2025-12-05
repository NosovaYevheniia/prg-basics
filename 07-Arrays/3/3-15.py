tuple1 = (10,20,30,40,50)

rev_tuple = tuple1[::-1]
print(f"Tuple: {tuple1}")
print(f"Reverse order: {rev_tuple}")
print("-----------------------------")

new_list = []
count = len(tuple1) - 1
while count >= 0:
    new_list.append(tuple1[count])
    count -= 1
print(f"Tuple: {tuple1}")
print(f"Reverse order: {new_list}")