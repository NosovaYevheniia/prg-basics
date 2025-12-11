mean = lambda distance,hours,minutes: distance / (hours + (minutes/60))

minutes = int(input("Enter number of minutes travelled: "))
hours = int(input("Enter number of thours travelled: "))
distance = int(input("Enter the distance travelled: "))

result = mean(distance,hours,minutes)
print(f"Average speed is {result} km/h")