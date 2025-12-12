products_list = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
    }

total = 0
for product, number in products_list.items():
    print(f"{product} : {number}")
    total += number
print(f"The total number of products in the store is {total}")