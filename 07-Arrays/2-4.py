# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
    day = weekday(day_number)
    meal_value = meal_plan[day_number - 1]
    result = ",".join(meal_value)
    return f"{day}: {result}"

def all_meal_plans(meal_plan):
    result = ""
    for i in range(1, 8):
        day = weekday(i)
        meal_value = meal_plan[i - 1]
        result += day + ": " + ",".join(meal_value) + "\n"
    return result

# x = day_meal_plan(meal_plan, 4)
# print(x)
y = all_meal_plans(meal_plan)
print(y)



# Prints weekly meal plan
...
...
...