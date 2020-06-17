import unittest

from bst import BSTNode


def is_BST(root):
    evaluated_nodes = []
    previous_node = None

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
