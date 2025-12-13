paragraph = "cat dog mouse cat rat cat mouse"

count = {}
arr = paragraph.split()
print(arr)
for word in arr:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)
