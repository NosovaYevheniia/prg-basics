def f(word:str):
    result = []
    word = word.lower()
    for i in range(len(word)):
        x = list(word)
        print(x)
        x[i] = x[i].upper()
        result.append("".join(x))
    return "-".join(result)

if __name__ == "__main__":
    print(f("water"))
    print(f("A"))
    print(f(""))