def add(input):
    if input == "":
        return 0
    
    delimiter = ","
    if input.startswith("//"):
        delimiter_index = input.find("\n")
        delimiter = input[2:delimiter_index]
        input = input[delimiter_index+1:]

    numbers = parse_numbers(input, delimiter)
    negatives = identify_negatives(numbers)
    report_negatives(negatives)
    numbers = ignore_large_numbers(numbers)
    
    return sum(numbers)

def split_input_string(input, delimiter):
    segments = []
    for part in input.split('\n'):
        segments.extend(part.split(delimiter))
    return segments

def parse_numbers(input, delimiter):
    segments = split_input_string(input, delimiter)
    return [int(num) for num in segments if num != ""]
    
def identify_negatives(numbers):
#    negatives = [num for num in numbers if num < 0]
    negatives = []
    for num in numbers:
        if num < 0:
            negatives.append(num)

    return negatives

def report_negatives(negatives):
    if len(negatives) != 0:
        raise ValueError("negatives not allowed: " + ",".join(map(str, negatives)))

def ignore_large_numbers(numbers):
    return [num for num in numbers if num <= 1000]


