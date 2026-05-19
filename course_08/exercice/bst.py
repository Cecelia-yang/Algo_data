# COURSE 08 — Node + BST toolbox (given, do NOT modify)
#
# Everything you built in Class 07 is already wired up here:
#   - Node                  the same value/left/right node
#   - bst_insert(node, v)   recursive insert with the re-attach idiom
#   - bst_search(node, v)   recursive search returning the Node or None
#   - build_bst(values)     insert every value of a list into an empty tree
#   - find_min(node)        return the leftmost NODE (smallest value), or None
#   - tree_height(node)     -1 for an empty tree, 0 for a single leaf, else
#                           1 + max(left height, right height)
#
# Your job in exercise.py is to add ONE more function: `bst_delete`.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


def bst_insert(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = bst_insert(node.left, value)
    elif value > node.value:
        node.right = bst_insert(node.right, value)
    return node


def bst_search(node, target):
    if node is None:
        return None
    if node.value == target:
        return node
    if target < node.value:
        return bst_search(node.left, target)
    return bst_search(node.right, target)


def build_bst(values):
    root = None
    for v in values:
        root = bst_insert(root, v)
    return root


def find_min(node):
    """Return the leftmost NODE of the subtree (the one holding the
    smallest value). Returns None on an empty subtree."""
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node


def tree_height(node):
    """-1 on empty tree, 0 on a single leaf, else 1 + max(left, right)."""
    if node is None:
        return -1
    return 1 + max(tree_height(node.left), tree_height(node.right))


def inorder_values(node):
    """Inorder walk → sorted list of values. Useful to check that a BST
    is still a BST after a delete."""
    result = []
    def walk(n):
        if n is None:
            return
        walk(n.left)
        result.append(n.value)
        walk(n.right)
    walk(node)
    return result
