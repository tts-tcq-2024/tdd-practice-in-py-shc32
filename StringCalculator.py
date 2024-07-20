#import re

def sum_of_numbers(input):
    numbers = input.split(',')
    return sum(int(num) for num in numbers)
#    return sum(map(int, re.findall('\d+', input)))
    
def add(input):
    if (input == "0") or (input == ""):
        return 0

    sum_of_numbers(input)
  
#    else:
#        sum_of_numbers(input)
