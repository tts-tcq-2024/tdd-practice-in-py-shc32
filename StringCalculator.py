import re

def add(numbers_string):
    if not numbers_string:
        return 0
    
    delimiter = ","
    
    # Check if custom delimiter is specified
    if numbers_string.startswith("//"):
        custom_delimiter_match = re.match(r"//(.+)\n", numbers_string)
        if custom_delimiter_match:
            delimiter = custom_delimiter_match.group(1)
            numbers_string = numbers_string[len(custom_delimiter_match.group(0)):]
    
    # Split numbers_string by delimiter and newline
    numbers = re.split(f"{delimiter}|\n", numbers_string)
    
    # Convert numbers to integers and filter out numbers > 1000
    numbers = [int(num) for num in numbers if int(num) <= 1000]
    
    # Raise exception for negative numbers
    negatives = [num for num in numbers if num < 0]
    if negatives:
        raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")
    
    # Return sum of filtered numbers
    return sum(numbers)







