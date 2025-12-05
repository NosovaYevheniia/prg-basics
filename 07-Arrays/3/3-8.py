arr = [2, 6, 4, 9, 7]

def star(n):
    stars = ""
    asteriks = "*"
    for i in n:
        stars += f"{i}: {i * asteriks} \n" 
    return stars

x = star(arr)
print(x)