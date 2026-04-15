from itertools import groupby

def compress_numbers(numbers):
    if not numbers or not all(isinstance(x, (int, float)) for x in numbers):
        return "Входные данные должны быть списком чисел"
    elif len(numbers) == 1:
        return numbers
    return [key for key, _ in groupby(numbers)]
    