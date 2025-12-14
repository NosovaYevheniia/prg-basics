###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input("Enter a username (at least 6 characters): ")
password = input("Enter a password (at least 8 charaters): ")

# pattern (criteria) for username and password
username_pattern = "^[a-z]{6,}$"
password_pattern = "^[A-Za-z0-9_]{8,}$"

# check if username and password are ok
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# print results
if username_match:
   print("The username is correct")
else:
   print("Username is incorrect")

if password_match:
   print("The password is correct")
else:
   print("Password is incorrect")