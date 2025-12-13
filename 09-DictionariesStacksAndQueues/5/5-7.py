hotels_in_Krakow = [
   {"name":"Sky", "price":320.00},
   {"name":"Metropol", "price":480.00},
   {"name":"New Port", "price":420.00},
   {"name":"Aparthotel", "price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

# krakow_aver = 0
# krakow_sum = 0
# krakow_length = len(hotels_in_Krakow)
# print(krakow_length)
# for names, prices in hotels_in_Krakow:
#     krakow_sum += prices
#     krakow_aver = krakow_sum/krakow_length
# print(f"Average hotel price in Krakow: {krakow_aver}")

def hotel_list(hotels):
    # print(hotels[1])
    names = []
    for h in hotels:
        names.append(h["name"])
    print(names)
    return names   

def avg_price(hotels):
    suma = 0
    for h in hotels:
        suma += h["price"]
        average =  suma/len(hotels)
    return average




if __name__ == "__main__":
    krakow = hotel_list(hotels_in_Krakow)
    sopot = hotel_list(hotels_in_Sopot)
    print("Hotels in Krakow: ", krakow)
    print("Hotels in Sopot: ", sopot)
    x = avg_price(hotels_in_Krakow)
    y = avg_price(hotels_in_Sopot)
    print("Average hotel prices in Krakow: ", x)
    print("Average hotel price in Sopot:", y)
    if x > y:
        print("Cheaper hotels in: Sopot")
    else:
        print("Cheaper hotels in: Krakow")