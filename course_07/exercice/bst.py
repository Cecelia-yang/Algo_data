# COURSE 07 — Node class for BSTs (given, do NOT modify)
#
# Same shape as the Node class in courses 05 and 06: a value, a left
# child, a right child. The BST property lives in HOW you arrange the
# nodes — not in the class itself.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"
