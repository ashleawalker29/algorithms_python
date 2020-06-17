import unittest

from bst import BSTNode


class BinarySearchTreeTests(unittest.TestCase):

    def test_bst_attributes(self):
        tree = BSTNode(1)
        self.assertEqual(tree.root, 1)
        self.assertEqual(tree.left_branch, None)
        self.assertEqual(tree.right_branch, None)

