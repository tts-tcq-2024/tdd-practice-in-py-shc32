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
    numbers = []
    for part in input.split('\n'):
        numbers.extend(part.split(delimiter))
    return [int(num) for num in numbers if num != ""]

def handle_negatives(numbers):
    negatives = [num for num in numbers if num < 0]
#    if negatives:
#        raise ValueError("negatives not allowed: " + ",".join(map(str, negatives)))

def ignore_large_numbers(numbers):
    return [num for num in numbers if num <= 1000]


