from numbers import Number


def binary_search(numbers, value, start=0, end=None):
    if not numbers:
        return 'Nothing to search through.'

    if not value and value != 0:
        return 'Nothing to search for.'

    if not isinstance(value, Number):
        return 'Can only search for numbers.'

    for number in numbers:
        if not isinstance(number, Number):
            return 'Can only search through lists of just numbers.'

    numbers = sorted(numbers)

    if end is None:
        end = len(numbers)

    if start == end:
        return 'Value was not found within the list.'

    position = (end - start) // 2 + start

    if value == numbers[position]:
        return 'Value was found within the list.'
    elif value < numbers[position]:
        return binary_search(numbers, value, start=start, end=position)
    elif value > numbers[position]:
        return binary_search(numbers, value, start=position + 1, end=end)
