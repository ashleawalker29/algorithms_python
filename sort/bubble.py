from numbers import Number


def bubble_sort(numbers):
    if not numbers:
        return 'Nothing to sort.'

    for number in numbers:
        if not isinstance(number, Number):
            return 'Can only sort lists of just numbers.'

    for i in range(len(numbers) - 1):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers
