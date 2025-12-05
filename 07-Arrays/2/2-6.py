zeroes = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

def zero_replace(zeroes):
    index = 0
    for row in zeroes:
        print(row)
        row[index] = 1
        index += 1
    print(zeroes)

zero_replace(zeroes)
