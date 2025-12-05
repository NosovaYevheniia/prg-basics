###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

questionNumber = len(test_results)
correct_answers = 0
incorrect_answers = 0
for answer in test_results:
    if answer == True:
        correct_answers += 1
    else:
        incorrect_answers += 1
correct_percentage = (correct_answers/questionNumber) * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', questionNumber)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Number of correct answers percentage:', correct_percentage,"%")