import unittest

from bst import BSTNode, array_to_bst


def is_BST(root):
    if not isinstance(root, BSTNode):
        return False

    evaluated_nodes = []
    previous_node = None

    if root.root != 0 and not (root.left_branch or root.right_branch or evaluated_nodes):
        return False

    while root or evaluated_nodes:
        while root:
            evaluated_nodes.append(root)
            root = root.left_branch
        root = evaluated_nodes.pop()
        if previous_node and root.root <= previous_node.root:
            return False
        previous_node = root
        root = root.right_branch
    return True


class BinarySearchTreeTests(unittest.TestCase):

    def test_bst_attributes(self):
        tree = BSTNode(1)
        self.assertEqual(tree.root, 1)
        self.assertEqual(tree.left_branch, None)
        self.assertEqual(tree.right_branch, None)

    def test_is_bst(self):
        tree = BSTNode(2)
        tree.left_branch = BSTNode(1)
        tree.right_branch = BSTNode(3)

        self.assertTrue(is_BST(tree))

    def test_is_not_bst(self):
        tree = BSTNode(3)
        tree.left_branch = BSTNode(2)
        tree.right_branch = BSTNode(1)

        self.assertFalse(is_BST(tree))

    def test_string_is_not_bst(self):
        tree = 'This is an example.'

        self.assertFalse(is_BST(tree))

    def test_is_bst_none(self):
        tree = BSTNode(None)

        self.assertFalse(is_BST(tree))

    def test_is_bst_single_value(self):
        tree = BSTNode(0)

        self.assertTrue(is_BST(tree))

    def test_array_to_bst_not_nums(self):
        partially_numerical = [1, 2, 'a', 4, 5]
        self.assertEqual(array_to_bst(partially_numerical), 'Can only convert lists of just numbers.')
        self.assertFalse(is_BST(array_to_bst(partially_numerical)))

        non_numerical = ['a', 'b', 'c']
        self.assertEqual(array_to_bst(non_numerical), 'Can only convert lists of just numbers.')
        self.assertFalse(is_BST(array_to_bst(partially_numerical)))

    def test_sorted_array_to_bst(self):
        numbers = [1, 2, 3, 4, 5]

        self.assertTrue(
            is_BST(array_to_bst(numbers)))

    def test_unsorted_array_to_bst(self):
        numbers = [1, 3, 5, 2, 4]

        self.assertTrue(
            is_BST(array_to_bst(numbers)))
