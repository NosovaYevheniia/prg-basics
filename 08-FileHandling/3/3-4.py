###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file):
    for emails in email_file:
        email = email_file(email content)

# regular expression pattern
# for amounts
pattern = '....'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
length = len(amounts)
for amount in amounts:
   ...

# print result
print(...)