import module_month

if __name__ == "__main__":
    m = int(input("Enter month number: "))
    result = module_month.month(m)
    print(f"The name of month {m} is {result}")