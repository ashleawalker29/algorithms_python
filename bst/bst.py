from numbers import Number


class BSTNode():
    def __init__(self, root):
        self.root = root
        self.left_branch = None
        self.right_branch = None


def array_to_bst(numbers):
    for number in numbers:
        if not isinstance(number, Number):
            return 'Can only convert lists of just numbers.'

    numbers = sorted(numbers)

    if not numbers:
        return None

    middle = len(numbers) // 2

    tree = BSTNode(numbers[middle])
    tree.left_branch = array_to_bst(numbers[:middle])
    tree.right_branch = array_to_bst(numbers[middle + 1:])

    return tree
