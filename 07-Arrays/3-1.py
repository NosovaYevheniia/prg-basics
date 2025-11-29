arr = [34,7,19,4,21,8]
# result = [i for i in arr if i%2 == 0]
# print(result)

length = len(arr)
index = 0
even_numbers_list = []
while (length > 0):
    if arr[index]%2 == 0:
        even_numbers_list.append(arr[index])
    index += 1
    length -= 1
new_list_lenght = len(even_numbers_list)
print(even_numbers_list)
print(new_list_lenght)




