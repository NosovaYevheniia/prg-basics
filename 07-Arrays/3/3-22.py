import random

def rand_elem(array:list):
    range_index = random.randint(0, len(array)-1)
    return array[range_index]

if __name__ == "__main__":
    x = rand_elem([1, 9, 5, 7, 3])
    print(x)