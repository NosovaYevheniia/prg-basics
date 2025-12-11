temperatures = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
fimoz = list(filter(lambda x: temperatures[x] > 0, temperatures))
print(f"Cities with positive temperatures: {fimoz}")