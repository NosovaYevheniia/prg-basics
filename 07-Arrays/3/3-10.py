arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

def compare(arr1:list, arr2:list) -> int:
    for i in arr1:
        if i not in arr2:
            print(i)

if __name__ == "__main__":
    compare(arr1, arr2)