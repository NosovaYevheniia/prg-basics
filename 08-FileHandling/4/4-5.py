import re
import email

def email_sender(content):
    return re.search("^[j][m]$", content) #jan.kowalski@example.com

def email_recipient(content):
    return re.search("", content) #mail.example.com

def email_subject(content):
    return re.search("", content) #Report request

def email_body(content):
    return re.search("", content) #

file_name = "email.txt"
with open(file_name, "r") as file:
    content = file.read()

print("Sender email adress: ", email_sender(content))

