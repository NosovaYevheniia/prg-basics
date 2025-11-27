###
# Writes Seven Wonders of the World to a file
#
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
sorted_data = sorted(file_name)

# Write data to the file
with open(file_name, 'w') as file:
    for item in file:
        file.write(f"The World Wander: {seven_wonders}")

print("The seven wonders of the world")