def avg_speed(distance,hours,minutes):
    total_time = hours + (minutes/60)
    speed = distance / total_time
    return speed

if __name__ == "__main__":
    minutes = int(input("Enter number of minutes travelled: "))
    hours = int(input("Enter number of thours travelled: "))
    distance = int(input("Enter the distance travelled: "))
    result = avg_speed(distance,hours,minutes)
    print(f"Average speed is {result} km/h")