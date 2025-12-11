mean = lambda ms: ms * 3.6
mets = int(input("Enetr meters per second: "))

result  = mean(mets)
print(f"{mets}m/s in km/h is equal to {result} km/h")