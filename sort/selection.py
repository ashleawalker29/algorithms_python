from numbers import Number


def selection_sort(numbers):
    if not numbers:
        return 'Nothing to sort.'

    for number in numbers:
        if not isinstance(number, Number):
            return 'Can only sort lists of just numbers.'

    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers
