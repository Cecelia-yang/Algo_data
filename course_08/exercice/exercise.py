# COURSE 08 — Exercises (Binary Search Trees, part 2)
#
# `bst.py` gives you all of C07's helpers + find_min + tree_height +
# inorder_values. `tree_exemple.py` provides lecture_bst, balanced_bst,
# degenerate_bst. Build a fresh tree with build_bst([...]) before any
# bst_delete test — globals get mutated.


# ─── Exo 1 — bst_delete (cases 1 and 2) ──────────────────────────────
# Remove `value` and return the (possibly modified) root. Handle a
# LEAF (return None) or a node with ONE child (return that child, it
# jumps up). 2-children case is Exo 4 — leave such nodes alone.
# Re-attach idiom: node.left = bst_delete(node.left, value)

from bst import Node, build_bst, inorder_values

def bst_delete(node, value): #ONLY CASES 1 AND 2 !
    pass    # TODO


print("=== Exo 1 ===")
# t = build_bst([5, 3, 8, 1, 4])
# t = bst_delete(t, 1)                     # case 1: leaf
# print(inorder_values(t))                 # [3, 4, 5, 8]
# t = build_bst([5, 3, 8, 1, 10])
# t = bst_delete(t, 8)                     # case 2: 8 has only right (10)
# print(inorder_values(t))                 # [1, 3, 5, 10]
# t = build_bst([5, 3, 8, 1])
# t = bst_delete(t, 3)                     # case 2: 3 has only left (1)
# print(inorder_values(t))                 # [1, 5, 8]



# ─── Exo 2 — closest_value ───────────────────────────────────────────
# Return the VALUE in the BST closest to `target`. The BST property
# means you walk down one side at a time, tracking the closest value
# seen so far. Empty tree → None. Ties: return either.

# Hint: not RECURSIVE — just walk down once, updating a `best` variable when you see a closer value.
# check the tree_exemple.py for some test trees to try out.

# use abs() -> absolute value function to compare distances between target and node value, and best and node value.

from tree_exemple import lecture_bst, balanced_bst

def closest_value(node, target):
    pass    # TODO


print("\n=== Exo 2 ===")
# print(closest_value(lecture_bst, 5))     # 4 or 6 — both distance 1
# print(closest_value(lecture_bst, 12))    # 13
# print(closest_value(lecture_bst, 100))   # 14
# print(closest_value(None, 0))            # None



# ─── Exo 3 — successor ───────────────────────────────────────────────
# Return the smallest value strictly greater than `value` (which need
# not be in the tree), or None. Walk down once, marking the current
# node as a candidate on every LEFT step, discarding it on RIGHT.

#Hint: not RECURSIVE — just walk down once, updating a `best` variable when you go left.
# When you go right, you know the current node can't be the successor.

from bst import Node
from tree_exemple import lecture_bst

def successor(node, value):
    pass    # TODO


print("\n=== Exo 3 ===")
# print(successor(lecture_bst, 6))     # 7
# print(successor(lecture_bst, 7))     # 8
# print(successor(lecture_bst, 14))    # None — 14 is the max
# print(successor(lecture_bst, 5))     # 6 — 5 is not in the tree
# print(successor(None, 0))            # None



# ─── Exo 4 — bst_delete_full (with case 3) ───────────────────────────
# Extend bst_delete to handle the 2-children case using the inorder
# successor trick from the lecture (slide 8):
#
# Idea: find the smallest value in the right subtree (use `find_min`
# defined just below — walk left from node.right until you can't).
# Copy that value into the current node. Recursively delete the
# successor from the right subtree — it has no left child, so it
# falls into case 1 or 2.
#
# Keep cases 1 and 2 from Exo 1.

from bst import Node, build_bst, inorder_values

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def bst_delete_full(node, value):
    pass    # TODO


print("\n=== Exo 4 ===")
# t = build_bst([8, 3, 10, 1, 6, 14, 4, 7, 13])      # lecture_bst shape
# t = bst_delete_full(t, 6)                          # case 3
# print(inorder_values(t))                # [1, 3, 4, 7, 8, 10, 13, 14]
# t = build_bst([8, 3, 10, 1, 6, 14, 4, 7, 13])
# t = bst_delete_full(t, 8)                          # case 3 on the root
# print(t.value)                          # 10
# print(inorder_values(t))                # [1, 3, 4, 6, 7, 10, 13, 14]
# t = build_bst([5, 3, 8, 1, 4, 7, 10])
# for v in [3, 5, 8]: t = bst_delete_full(t, v)      # mix of cases
# print(inorder_values(t))                # [1, 4, 7, 10]



# ██████████████████████████████
# BONUS
# ██████████████████████████████


# ─── Bonus 1 — is_valid_bst ──────────────────────────────────────────
# Return True if every left subtree value < node < every right subtree
# value, recursively, everywhere. Trap from C07: checking direct
# children is not enough. Thread a (lo, hi) window down the recursion.

from bst import Node
from tree_exemple import lecture_bst, balanced_bst

def is_valid_bst(node, lo=float('-inf'), hi=float('inf')):
    pass    # TODO


print("\n=== Bonus 1 ===")
# print(is_valid_bst(lecture_bst))     # True
# print(is_valid_bst(balanced_bst))    # True
# print(is_valid_bst(None))            # True
# # Build a broken tree: 12 is in 8's LEFT subtree but 12 > 8
# bad = Node(8)
# bad.left = Node(3); bad.right = Node(10)
# bad.left.left = Node(1); bad.left.right = Node(12)
# print(is_valid_bst(bad))             # False



# ─── Bonus 2 — is_balanced ───────────────────────────────────────────
# Return True if the tree is "balanced": for every subtree, the heights
# of the left and right children differ by at most 1. Empty tree → True.
#
# Why bother: this is the strict condition AVL trees enforce on every
# insert and delete — next-class teaser for self-balancing BSTs.
#
# tree_height(node) is given in bst.py: -1 on empty, else 1 + max(left, right).

from bst import Node, tree_height
from tree_exemple import lecture_bst, balanced_bst, degenerate_bst

def is_balanced(node):
    pass    # TODO


print("\n=== Bonus 2 ===")
# print(is_balanced(lecture_bst))         # False — node 10 left depth -1 vs right depth 1
# print(is_balanced(balanced_bst))        # True
# print(is_balanced(degenerate_bst))      # False — chain of height 6
# print(is_balanced(None))                # True
