import json

def number_of_rooms():
    with open("reservations.json", "r", encoding="utf-8") as file:
        content = json.load(file)
        res = content["reservations"]
        length = len(res)
    return length

def paid_reservations():
    paid_count = 0
    with open("reservations.json", "r", encoding="utf-8") as file:
        content = json.load(file)
        res = content["reservations"]
        for room in res:
            if room["paid"] == True:
                paid_count += 1
        return paid_count
    
def unpaid_reservations():
    unpaid_count = 0
    with open("reservations.json", "r", encoding="utf-8") as file:
        content = json.load(file)
        res = content["reservations"]
        for room in res:
            if room["paid"] == False:
                unpaid_count += 1
        return unpaid_count
    
def total_value_paid():
    total_value = 0
    with open("reservations.json", "r", encoding="utf-8") as file:
        content = json.load(file)
        res = content["reservations"]
        for room in res:
            if room["paid"] == True:
                total_value += room["price_per_night"]
        return total_value
    
def total_value_unpaid():
    total_value = 0
    with open("reservations.json", "r", encoding="utf-8") as file:
        content = json.load(file)
        res = content["reservations"]
        for room in res:
            if room["paid"] == False:
                total_value += room["price_per_night"]
        return total_value

if __name__ == "__main__":
    # print(number_of_rooms())
    # print(paid_reservations())
    # print(unpaid_reservations())
    print(total_value_paid())
    print(total_value_unpaid())