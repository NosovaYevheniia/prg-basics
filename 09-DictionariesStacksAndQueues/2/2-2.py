emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]
unique_emails = set(emails) # Removes duplicates
print(type(unique_emails))

l = list(unique_emails)

print(unique_emails)
list1 = ["j"]
list1.extend(unique_emails)
print(type(list1))
print(list1)