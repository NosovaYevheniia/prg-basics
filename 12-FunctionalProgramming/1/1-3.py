def ms_to_kmh(ms):
    km_per_h = ms * 3.6
    return km_per_h

if __name__ == "__main__":
    mets = int(input("Enetr meters per second: "))
    result  = ms_to_kmh(mets)
    print(f"{mets}m/s in km/h is equal to {result} km/h")