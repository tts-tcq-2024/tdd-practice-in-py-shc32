import re

def sum_of_numbers(str):
    return sum(map(int, re.findall('\d+', str))) 
    
def add(input):
    if (input == "0") or (input == ""):
        return 0
        
    sum_of_numbers(input)
