import pytest
from RemovingConsecutiveDuplicatesFromAnArray import compress_numbers

data_testing_successful = [
    ([1, 2], [1, 2]),
    ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
    ([1, 2, 1], [1, 2, 1]),
    ([10.2, 10.2, 20.5, 20.5], [10.2, 20.5]),
    ([10.2, 20.5, 10.2, 20.5], [10.2, 20.5, 10.2, 20.5]),
    ([1, 1], [1]),
    ([1], [1])
]

error_message = "Входные данные должны быть списком чисел"

data_testing_failing = [
    ([], error_message),  
    ([1, 'a', 2], error_message)
]

# Тесты для функции compress_numbers, успешные случаи
@pytest.mark.parametrize("input_data, expected_output", data_testing_successful)

def test_compress_numbers(input_data, expected_output):
    assert compress_numbers(input_data) == expected_output

# Тесты для функции compress_numbers, случаи с ошибками
@pytest.mark.parametrize("input_data, expected_output", data_testing_failing)

def test_compress_numbers_errors(input_data, expected_output):
    assert compress_numbers(input_data) == expected_output