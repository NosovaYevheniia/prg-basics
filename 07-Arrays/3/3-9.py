

def compare(array1:list, array2:list):
    if array1 == array2:
        return True
    else:
        return False
    

if __name__ == "__main__":
    array1 = ["water","book","sky"]
    array2 = ["water","book","sky"]
    x = compare(array1, array2)
    print("Array1: " + " ".join(array1))
    print("Array2: " + " ".join(array2))
    if (x):
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are not the same")