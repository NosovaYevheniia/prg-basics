###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    if number == 0:
        return number;

    posNumber = abs(number);
    strNumber = str(posNumber);
    total = 0;
    for i in strNumber:
        intNumber = int(i);
        total = total + intNumber;
    return total;

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is', result)

sum_digits(25)