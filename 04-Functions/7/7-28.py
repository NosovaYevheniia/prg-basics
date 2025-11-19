# The sequence of digits contains the number of points rolled with a dice. Define a function f(dice) that returns a number 
# specifying the number of dice rolled the most times in a row. Sample result:
# f("5233165554211") returns 5
# f("2133") returns 3

def f(dice: str) -> int:
    biggest_amount_of_number = 0
    biggest_number = 0

    dice_number = "123456"
    for i in dice_number:
        current_dice_amount = dice.count(i)
        if current_dice_amount > biggest_amount_of_number:
            biggest_amount_of_number = current_dice_amount
            biggest_number = 1
    return biggest_number

if __name__ == "__main__":
    print(f("5233165554211"))