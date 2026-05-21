# COURSE 07 — Exercises (Binary Search Trees, part 1)
#
# `bst.py` defines Node. `tree_exemple.py` gives you three ready-made
# BSTs (lecture_bst, small_bst, degenerate_bst) so you can test the
# search exercises BEFORE writing insert. Each exercise re-imports
# what it needs so you can copy a single one into the Python REPL.


# ─── Exo 1 — bst_search ──────────────────────────────────────────────
# Return the Node holding `target`, or None. Recursive, no loop.

from bst import Node
from tree_exemple import lecture_bst, small_bst

def bst_search(node, target):
    pass    # TODO


print("=== Exo 1 ===")
# print(bst_search(lecture_bst, 7))     # Node(7)
# print(bst_search(lecture_bst, 99))    # None
# print(bst_search(None, 42))           # None



# ─── Exo 2 — bst_insert ──────────────────────────────────────────────
# Insert `value`, return the (possibly new) subtree root.
# Duplicates: do nothing. Re-attach idiom:
#     node.left = bst_insert(node.left, value)

from bst import Node

def bst_insert(node, value):
    pass    # TODO


print("\n=== Exo 2 ===")
# root = None
# for v in [10, 5, 15, 2, 7, 20]:
#     root = bst_insert(root, v)
# print(root.value, root.left.value, root.right.value)      # 10 5 15
# print(root.left.left.value, root.left.right.value)        # 2 7



# ─── Exo 3 — bst_min / bst_max ───────────────────────────────────────
# Return the smallest / largest VALUE. The BST property tells you which
# side to walk — iterative is fine. Empty tree → None.

from bst import Node
from tree_exemple import lecture_bst, small_bst

def bst_min(node):
    pass    # TODO


def bst_max(node):
    pass    # TODO


print("\n=== Exo 3 ===")
# print(bst_min(lecture_bst), bst_max(lecture_bst))     # 1 14
# print(bst_min(small_bst), bst_max(small_bst))         # 1 8
# print(bst_min(None))                                  # None



# ─── Exo 4 — inorder_values ──────────────────────────────────────────
# Return ALL values in INORDER (left, node, right). On a BST the
# result is sorted — try it on lecture_bst and check for yourself.

from bst import Node
from tree_exemple import lecture_bst, small_bst

def inorder_values(node):
    pass    # TODO


print("\n=== Exo 4 ===")
# print(inorder_values(lecture_bst))    # [1, 3, 4, 6, 7, 8, 10, 13, 14]
# print(inorder_values(small_bst))      # [1, 3, 4, 5, 8]
# print(inorder_values(None))           # []



# ██████████████████████████████
# BONUS
# ██████████████████████████████


# ─── Bonus 1 — range_values ──────────────────────────────────────────
# Return the sorted list of values v with lo <= v <= hi.
#
# Naive way: filter inorder_values. Works, but visits every node.
# Smart way (do this one): use the BST order to PRUNE.
#   - node.value < lo  →  no match in the LEFT subtree, skip it
#   - node.value > hi  →  no match in the RIGHT subtree, skip it
# Whole subtrees never get visited.

from bst import Node
from tree_exemple import lecture_bst

def range_values(node, lo, hi):
    pass    # TODO


print("\n=== Bonus 1 ===")
# print(range_values(lecture_bst, 4, 10))      # [4, 6, 7, 8, 10]
# print(range_values(lecture_bst, 0, 3))       # [1, 3]
# print(range_values(lecture_bst, 20, 30))     # []
# print(range_values(None, 0, 100))            # []



# ─── Bonus 2 — build_balanced ────────────────────────────────────────
# Given a SORTED list of distinct values, build a BALANCED BST and
# return its root.
#
# Idea: the MIDDLE element becomes the root, the left half becomes the
# left subtree (recurse), the right half becomes the right subtree
# (recurse). Empty list → None.
#
# Why bother: insert [1, 2, 3, 4, 5] one-by-one with bst_insert and
# you get a degenerate chain — height n, search O(n). This trick gives
# you height ≈ log n. Same values, very different speeds.

from bst import Node

def build_balanced(sorted_values):
    pass    # TODO


print("\n=== Bonus 2 ===")
# t = build_balanced([1, 2, 3, 4, 5, 6, 7])
# print(t.value)                            # 4
# print(t.left.value, t.right.value)        # 2 6
# print(inorder_values(t))                  # [1, 2, 3, 4, 5, 6, 7]
# print(build_balanced([]))                 # None
