# COURSE 05 — Node and BinaryTree classes (given, do NOT modify)
#
# A binary tree node = a linked-list node with one extra pointer:
# `left` replaces `next`, and `right` is brand new.
#
# This file is imported at the top of each exercise so you can copy
# a single exercise block into the Python REPL without running the
# whole exercise file.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None              # the tree starts empty

    def add_left(self, parent, value):
        """Attach a new node as the LEFT child of `parent`. Returns it."""
        new = Node(value)
        parent.left = new
        return new

    def add_right(self, parent, value):
        """Attach a new node as the RIGHT child of `parent`. Returns it."""
        new = Node(value)
        parent.right = new
        return new
