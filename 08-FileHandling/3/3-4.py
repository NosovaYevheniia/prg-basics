###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, "r", encoding="utf-8") as file:
    email = file.read()

# regular expression pattern
# for amounts
pattern = '€(\d+)'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)
print(amounts)

# calculate the total purchases
total = 0.0
for amount in amounts:
    total += float(amount)

# print result
print(f"The total amount of money spent is: {total}")