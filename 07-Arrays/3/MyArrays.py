import sys

def sec_maximum(array:list):
    maximum = maximum(array)
    sec_max_num = 0
    for number in array:
        if number != maximum:
            if number > sec_max_num:
                sec_max_num = number
    return sec_max_num

def maximum(array):
    maximum = 0
    for number in array:
        if number > maximum:
            maximum = number
    return maximum

def minimum(array):
    minimum = sys.maxsize
    for number in array:
        if number < minimum:
            minimum = number
    return minimum

def maximum_minimum(array:list):
    maximum = maximum(array)
    minimum = minimum(array)
    diff = maximum - minimum
    return diff


def median(array:list):
    length = len(array)
    median_index = length/2
    if length%2 != 0:
        return array[median_index]
    else:
        return (array[median_index - 1] + array[median_index]) / 2
    
def smallest_largest(array):
    smallest = minimum(array)
    largest = maximum(array)
    return [smallest, largest]

def string_number(array:list):
    return "-".join(map(str, array))