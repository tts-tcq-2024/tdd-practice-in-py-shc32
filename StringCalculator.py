def add(input):
    if input == "":
        return 0
    
    delimiter = ","
    if input.startswith("//"):
        delimiter_index = input.find("\n")
        delimiter = input[2:delimiter_index]
        input = input[delimiter_index+1:]

    numbers = parse_numbers(input, delimiter)
    negatives = identify_negative_elements(numbers)
    report_negative_elements(negatives)
    numbers = ignore_large_numbers(numbers)
    
    return sum(numbers)

def split_input_string(input, delimiter):
    segments = []
    for part in input.split('\n'):
        segments.extend(part.split(delimiter))
    return segments

def parse_numbers(input, delimiter):
    segments = split_input_string(input, delimiter)
    parsed_numbers = []
    for num in segments:
        if num != "":
            parsed_numbers.append(int(num))  # Convert valid segments to integers
    return parsed_numbers

def identify_negative_elements(numbers):
    negatives = []
    for num in numbers:
        if num < 0:
            negatives.append(num)
    return negatives

def report_negative_elements(negatives):
    if len(negatives) != 0:
        raise ValueError("negatives not allowed: " + ",".join(map(str, negatives)))

def ignore_large_numbers(numbers):
    numbers_less_than_1000 = []
    for num in numbers:
        if num <= 1000:
            numbers_less_than_1000.append(num)
    return numbers_less_than_1000


