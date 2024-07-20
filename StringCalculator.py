def add(input):
    if input == "":
        return 0
    
    delimiter = ","
    if input.startswith("//"):
        delimiter_index = input.find("\n")
        delimiter = input[2:delimiter_index]
        input = input[delimiter_index+1:]
    
    numbers = parse_numbers(input, delimiter)
    handle_negatives(numbers)
    numbers = ignore_large_numbers(numbers)
    
    return sum(numbers)

def parse_numbers(input, delimiter):
    parts = input.split('\n')
    split_parts = [part.split(delimiter) for part in parts]
    flattened_numbers = [int(num) for sublist in split_parts for num in sublist if num != ""]
    return flattened_numbers

def handle_negatives(numbers):
    negatives = [num for num in numbers if num < 0]
#    if negatives:
#        raise ValueError("negatives not allowed: " + ",".join(map(str, negatives)))

def ignore_large_numbers(numbers):
    return [num for num in numbers if num <= 1000]


