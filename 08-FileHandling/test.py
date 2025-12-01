try:
    with open("pets.txt") as file:
        print(file)
      
        for line in file:
            print(line)
except FileNotFoundError:
   pass

