# The price of the product on the price tag is given before and after the discount is applied. Write a program that allows you to enter the 
# product price and discount. Print the product price, discount, discounted product price, and the difference between the product price before 
# and after the discount. Print all prices with two decimal places. Sample result: 
# Enter price: 24.72
# Enter discount %: 15
# Price with discount: 21.01
# Reduction: 3.71

price = 24.72
discount = 15
price_discount = 21.01
reduction = 3.71
difference = price - price_discount
print(f"The product prise is {price}")
print(f"The discount is {discount}%")
print(f"The difference between the product price before and after the discount {difference}")