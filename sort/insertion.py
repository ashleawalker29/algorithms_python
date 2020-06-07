from numbers import Number


def insertion_sort(numbers):
    if not numbers:
        return 'Nothing to sort.'

    for number in numbers:
        if not isinstance(number, Number):
            return 'Can only sort lists of just numbers.'

    for i in range(1, len(numbers)):
        current_number = numbers[i]

        j = i - 1
        while j >= 0 and current_number < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = current_number

    return numbers
