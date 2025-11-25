###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#1, 4, 7
#
def weekday(n):
    weekday = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday[n - 1]

print(weekday(1))
print(weekday(4))
print(weekday(7))