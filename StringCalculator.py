import re

def parse_delimiter(numbers_string):
    delimiter = ","
    if numbers_string.startswith("//"):
        custom_delimiter_match = re.match(r"//(\[?.+?\]?)\n", numbers_string)
        if custom_delimiter_match:
            delimiter = custom_delimiter_match.group(1)
            numbers_string = numbers_string[len(custom_delimiter_match.group(0)):]
    return delimiter, numbers_string

def parse_numbers(numbers_string, delimiter):
    return re.split(f"{delimiter}|\n", numbers_string)

def check_negatives(numbers):
    negatives = [int(num) for num in numbers if int(num) < 0]
    if negatives:
        raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")

def filter_numbers(numbers):
    return [int(num) for num in numbers if 0 <= int(num) <= 1000]

def add(numbers_string):
    if not numbers_string:
        return 0
    
    delimiter, numbers_string = parse_delimiter(numbers_string)
    numbers = parse_numbers(numbers_string, delimiter)
    
    check_negatives(numbers)
    
    return sum(filter_numbers(numbers))









