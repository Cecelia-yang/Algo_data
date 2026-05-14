# COURSE 06 — Node and BinaryTree classes (given, do NOT modify)
#
# Same as course_05. Imported at the top of each exercise so you can
# copy a single exercise into the Python REPL on its own.


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
