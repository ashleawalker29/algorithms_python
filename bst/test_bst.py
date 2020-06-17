import unittest

from bst import BSTNode


class BinarySearchTreeTests(unittest.TestCase):

    def test_bst_attributes(self):
        tree = BSTNode(1)
        self.assertEqual(tree.root, 1)
        self.assertEqual(tree.left_branch, None)
        self.assertEqual(tree.right_branch, None)

    def test_is_bst(self):
        tree = BSTNode(2)
        tree.left_branch = BSTNode(1)
        tree.right_branch = BSTNode(2)

        self.assertTrue(is_BST(tree))

    def test_is_not_bst(self):
        tree = BSTNode(3)
        tree.left_branch = BSTNode(2)
        tree.right_branch = BSTNode(1)

        self.assertFalse(is_BST(tree))
