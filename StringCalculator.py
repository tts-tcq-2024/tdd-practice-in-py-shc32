import re

def parse_input(numbers_string):
    if not numbers_string:
        return ",", ""
    
    delimiter = ","
    if numbers_string.startswith("//"):
        custom_delimiter_match = re.match(r"//\[?(.+?)\]?\n", numbers_string)
        if custom_delimiter_match:
            delimiter = custom_delimiter_match.group(1)
            numbers_string = numbers_string[len(custom_delimiter_match.group(0)):]

    return delimiter, numbers_string

def parse_numbers(numbers_string, delimiter):
    return re.split(f"{delimiter}|\n", numbers_string)

def validate_numbers(numbers):
    negatives = [int(num) for num in numbers if int(num) < 0]
    if negatives:
        raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")

def filter_and_sum(numbers):
    numbers = [int(num) for num in numbers if 0 <= int(num) <= 1000]
    return sum(numbers)

def add(numbers_string):
    delimiter, numbers_string = parse_input(numbers_string)
    numbers = parse_numbers(numbers_string, delimiter)
    
    validate_numbers(numbers)
    
    return filter_and_sum(numbers)





