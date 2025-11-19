# Each month of a calendar year can be expressed by its name or by a number that indicates the position of the month in 
# year. In a separate module, define a function month(n) that returns a month name based on the month number (values from 
# 1 to 12). Then, write a program to print the name of the month 7. Import the module with the created function. Sample 
# result:
# Enter month number: 9
# The name of month 9 is September
print(__name__, 'is called')

def month(n: int) -> str:
    if n == 1:
        return "January"
    elif n == 2:
        return "February"
    elif n == 3:
        return "March"
    elif n == 4:
        return "April"
    elif n == 5:
        return "May"
    elif n == 6:
        return "June"
    elif n == 7:
        return "July"
    elif n == 8:
        return "August"
    elif n == 9:
        return "September"
    elif n == 10:
        return "October"
    elif n == 11:
        return "November"
    elif n == 12:
        return "December"
    else:
       return "Month number is incorrect"