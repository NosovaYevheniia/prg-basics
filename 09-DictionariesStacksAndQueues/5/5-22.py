import json

def product(product_name, product_price, product_paid):
    file_name = "product.json"
    product = {}
    product["name"] = product_name
    product["price"] = product_price
    product["paid"] = product_paid
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(product, file)

if __name__ == "__main__":
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_paid = bool(input("Enter yes if product is payed, no if not: "))
    product(product_name, product_price, product_paid)