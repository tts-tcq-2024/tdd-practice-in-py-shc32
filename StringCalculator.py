def add(self, input_string):
    if input_string == "":
        return 0
    
    delimiter = ","
    if input_string.startswith("//"):
        delimiter_index = input_string.find("\n")
        delimiter = input_string[2:delimiter_index]
        input_string = input_string[delimiter_index+1:]
    
    # Split by delimiter, commas, or new lines
    numbers = []
    for part in input_string.split('\n'):
        numbers.extend(part.split(delimiter))
    
    # Filter out empty strings and convert to integers
    numbers = [int(num) for num in numbers if num != ""]
    
    # Check for negatives
    negatives = [num for num in numbers if num < 0]
    if negatives:
        raise ValueError("negatives not allowed: " + ",".join(map(str, negatives)))
    
    # Ignore numbers larger than 1000
    numbers = [num for num in numbers if num <= 1000]
    
    return sum(numbers)

