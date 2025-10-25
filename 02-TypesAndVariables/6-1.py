###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Zhenia'   # replace Anna with your name
surname = 'Nosova' # replace May with your surname
full_name = "Zhenia Nosova"
characters_in_name = len(name)
characters_in_surname = len(surname)
full_name_characters = len(name) + len(surname)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {full_name} {full_name_characters} characters') # with a space between name and surname