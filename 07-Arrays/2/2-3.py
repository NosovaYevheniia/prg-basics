# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
total = 0
week1 = 0
week2 = 0
week3 = 0
week4 = 0
food = 0
transport = 0
utilities = 0
for row in monthly_expenses:
    row_index = monthly_expenses.index(row)
    if row_index == 0:
        week1 = sum(row)
    elif row_index == 1:
        week2 = sum(row)
    elif row_index == 2:
        week3 = sum(row)
    elif row_index == 3:
        week4 = sum(row)
    for i in row:
        value_index = row.index(i)
        if value_index == 0:
            food += i
        elif value_index == 1:
            transport += i
        elif value_index == 2:
            utilities += i


        total += i

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',week1)
print('Week 2:',week2)
print('Week 3:',week3)
print('Week 4:',week4)
print('---------------')
print('TOTAL:', total)