from numbers import Number


def merge_sort(numbers):
    if not numbers:
        return 'Nothing to sort.'

    for number in numbers:
        if not isinstance(number, Number):
            return 'Can only sort lists of just numbers.'

    if len(numbers) > 1:
        middle = len(numbers) // 2
        left_half = numbers[:middle]
        right_half = numbers[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                numbers[k] = left_half[i]
                i = i + 1
            else:
                numbers[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            numbers[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            numbers[k] = right_half[j]
            j = j + 1
            k = k + 1

    return numbers
