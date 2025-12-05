array = [2, 3, 2, 5, 8, 1, 9, 8]

unique_elements = []
for i in array:
    if array.count(i) == 1:
        unique_elements.append(i)

if __name__ == "__main__":
    space_array = " ".join(map(str, array))
    space_unique = " ".join(map(str, unique_elements))
    print(f"Array: {space_array}")
    print(f"Unique elements: {space_unique}")

