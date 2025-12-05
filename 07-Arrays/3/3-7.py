names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

def longest_name(names):
    maximum_length = 0
    max_valie_index = 0
    for i in names:
        name_length = len(i)
        index = names.index(i)
        if name_length > maximum_length:
            maximum_length = name_length
            max_valie_index = index
    print(index)
    return names[max_valie_index]

x = longest_name(names)
print(x)
        