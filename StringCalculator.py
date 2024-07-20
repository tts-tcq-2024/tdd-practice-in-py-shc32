def add(input):
    if input == "":
        return 0
    
    delimiter = ","
    if input.startswith("//"):
        delimiter_index = input.find("\n")
        delimiter = input[2:delimiter_index]
        input = input[delimiter_index+1:]
    
    # Split by delimiter, commas, or new lines
    numbers = []
    for part in input.split('\n'):
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

