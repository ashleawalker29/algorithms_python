from numbers import Number


def linear_search(numbers, value):
    if not numbers:
        return 'Nothing to search through.'

    if not value and value != 0:
        return 'Nothing to search for.'

    if not isinstance(value, Number):
        return 'Can only search for numbers.'

    for number in numbers:
        if not isinstance(number, Number):
            return 'Can only search through lists of just numbers.'

        if number == value:
            return 'Value was found within the list.'
    return 'Value was not found within the list.'
