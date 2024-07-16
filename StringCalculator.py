class StringCalculator:

    @staticmethod
    def add(numbers_string):
        if not numbers_string:
            return 0
        
        delimiter = ","
        if numbers_string.startswith("//"):
            custom_delimiter_match = re.match(r"//(\[?.+?\]?)\n", numbers_string)
            if custom_delimiter_match:
                delimiter = custom_delimiter_match.group(1)
                numbers_string = numbers_string[len(custom_delimiter_match.group(0)):]

        numbers = re.split(f"{delimiter}|\n", numbers_string)
        
        negatives = [int(num) for num in numbers if int(num) < 0]
        if negatives:
            raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")
        
        filtered_numbers = [int(num) for num in numbers if 0 <= int(num) <= 1000]
        
        return sum(filtered_numbers)






