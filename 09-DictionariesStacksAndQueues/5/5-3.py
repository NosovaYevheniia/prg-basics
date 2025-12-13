translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}


inp = input("Enter a word to translate: ")
value = translations[inp]
print(f"The word {inp} translates to {value} in polish")