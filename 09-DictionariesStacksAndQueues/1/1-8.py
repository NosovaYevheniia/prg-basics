price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print(price_list)
print("------------------------------")

total_before = 0
for product, price in price_list.items():
    total_before += price
print(f"The total price before discount: {int(total_before)}")
print("------------------------------")

for product, price in price_list.items():
    discount_prices = price - (price * 0.1)
    print(f"Prices before discount: {product}: {int(discount_prices)}")
print("------------------------------")

total_after = 0
for product, price in price_list.items():
    total_after += discount_prices
    print(f"Price after discount: {product}: {total_after}")
print("------------------------------")

