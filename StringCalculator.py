#import re

#def sum_of_numbers(input):
#    return sum(map(int, re.findall('\d+', input)))

def findSum(input):
    temp = "0"
    Sum = 0
    for ch in input:
        if (ch.isdigit()):
            temp += ch
        else:
            Sum += int(temp)
            temp = "0"
            
    return Sum + int(temp)
    
def add(input):
    findSum(input)
#    if (input == "0") or (input == ""):
#        return 0
#    else:
#        sum_of_numbers(input)
