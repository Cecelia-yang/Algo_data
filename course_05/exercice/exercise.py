# COURSE 05 EXERCISES — Trees: vocabulary + Binary Tree class

# Same recursion skeleton as Class 04, just with TWO recursive calls
# (one on node.left, one on node.right) instead of one on node.next.
#
# The Node and BinaryTree classes live in tree.py, and ready-made test
# trees (small_tree, big_tree) live in tree_exemple.py. Each exercise
# below starts with its own imports so you can copy a single exercise
# into the Python REPL on its own.
#
# REPL setup (one-time): open the `exercice/` folder as your VS Code
# workspace, OR `cd` into it before launching `python3`. That way the
# imports `from tree import ...` and `from tree_exemple import ...`
# resolve correctly without any path hack.


# ██████████████████████████████
# PART 1 — Build a tree by hand
# ██████████████████████████████


# --- Exo 1.1 : build the lecture tree ---
from tree import Node, BinaryTree

# Build the EXACT tree from the lecture, save it in `tree_1_1` using the imported classes ↑↑:
#
#         A
#        / \
#       B   C
#      / \
#     D   E
#
# A is the root. B and C are A's children (B left, C right).
# D and E are B's children (D left, E right).
#
# Hint: each add_* RETURNS the new node, so you can keep a handle on B
# to attach D and E to it. You set tree.root yourself; the helpers only
# attach children.

tree_1_1 = None    # TODO
#tree_root = ...
#b = ....add_...(..., "B")

# Quick checks (you can comment out once you have the tree built):
# use control + "/" to comment out or uncomment lines

#print(tree_1_1.root.value)              # Expected: A
#print(tree_1_1.root.left.value)         # Expected: B
#print(tree_1_1.root.right.value)        # Expected: C
#print(tree_1_1.root.left.left.value)    # Expected: D
#print(tree_1_1.root.left.right.value)   # Expected: E



# --- Exo 1.2 : vocabulary check ---

# Look at the tree from Exo 1.1 and fill in the answers below.
#
# Reminder:
#   - leaf      = node with no children
#   - depth(n)  = number of edges from root to n  (root has depth 0)
#   - height(t) = depth of the deepest leaf

#! /!| this is not code, just a place to write your answers.

answer_1_2_root_value     = None    # the value at the root
answer_1_2_leaf_values    = None    # set of leaf values, e.g. {"X", "Y"}
answer_1_2_depth_of_D     = None    # an integer
answer_1_2_height_of_tree = None    # an integer




# ██████████████████████████████
# PART 2 — count_nodes (recursion, two branches)
# ██████████████████████████████
# Same skeleton as Class 04's `length_recursive(node)`, but the "smaller"
# input is no longer just node.next — it's BOTH node.left and node.right.
# Combine: 1 (for the current node) + f(left) + f(right). Base case:
# `node is None` returns 0 (an empty subtree has zero nodes).


# --- Exo 2.1 : count_nodes ---
from tree import Node, BinaryTree
from tree_exemple import small_tree

# Return the total number of nodes in the subtree rooted at `node`.

def count_nodes(node):
    pass    # TODO

## Uncomment once count_nodes is implemented and tree_1_1 is built:
print(count_nodes(tree_1_1.root))      # Expected: 5
print(count_nodes(small_tree.root))    # Expected: 6
print(count_nodes(None))               # Expected: 0



# --- Exo 2.2 : count_nodes on a different tree ---
from tree import Node, BinaryTree

# Build the 3-node tree below in `tree_2_2`, then verify count_nodes
# returns 3.
#
#       X
#      / \
#     Y   Z

tree_2_2 = None    # TODO

print() #do your own print to count your little tree #TODO



# ██████████████████████████████
# PART 3 — find_max_value (recursion, three values)
# ██████████████████████████████


# --- Exo 3.1 : find_max_value ---
from tree import Node, BinaryTree
from tree_exemple import small_tree

# Return the biggest value in the subtree rooted at `node`.
#
# Hint: at each node, three values are in play — your own value, the max
# of the left subtree, the max of the right subtree. Take the biggest of
# the three with `max(a, b, c)`.
# The empty subtree must return a value smaller than ANY real value, so
# it loses every comparison. `float('-inf')` is the neutral element for
# max, just like 0 is for + and 1 is for *.

def find_max_value(node):
    pass    # TODO


# Build the integer tree below:
#
#         5
#        / \
#       9   2
#      / \
#     3   12

tree_3_1 = None    # TODO

## Uncomment once tree_3_1 is built and find_max_value is implemented:
# print(find_max_value(tree_3_1.root))      # Expected: 12
# print(find_max_value(small_tree.root))    # Expected: 20
# print(find_max_value(None))               # Expected: -inf



# --- Exo 3.2 : same idea, your own tree ---
from tree import Node, BinaryTree
from tree_exemple import big_tree

# Build the small tree of negative numbers below in `tree_3_2`, then run
# find_max_value on it. This forces you to confirm that 0 would have
# been the WRONG neutral value for max.
#
#       -7
#      /  \
#    -3   -10

tree_3_2 = None    # TODO

## Uncomment once tree_3_2 is built and find_max_value is implemented:
# print(find_max_value(tree_3_2.root))    # Expected: -3
# print(find_max_value(big_tree.root))    # Expected: 95



# ██████████████████████████████
# PART 4 — BONUS: tree_height + count_leaves
# ██████████████████████████████
# Same notion as PARTs 2–3: recursion on a tree with two branches.
# Only the action at each step changes.

# big_tree (15 nodes) is defined in tree_exemple.py — see the ASCII
# diagram there. We reuse it for both 4.1 and 4.2.


# --- Bonus 4.1 : tree_height ---
from tree import Node, BinaryTree
from tree_exemple import big_tree

# Return the height of the subtree rooted at `node`.
# Conventions in this course:
#   - height of an empty tree (node is None) is -1
#   - height of a tree with one node (a single leaf) is 0
#
# Hint: this is "two recursions + max + 1" — the same shape as
# count_nodes, but with `max` instead of `+`. The empty tree returns -1
# so a single leaf returns 1 + max(-1, -1) = 0.

def tree_height(node):
    pass    # TODO


## Uncomment once tree_height is implemented:
# print(tree_height(None))                          # Expected: -1
# print(tree_height(Node("only")))                  # Expected: 0
# print(tree_height(big_tree.root))                 # Expected: 4
# print(tree_height(big_tree.root.left.right))      # Expected: 2  (subtree rooted at 35)




# --- Bonus 4.2 : count_leaves ---
from tree import Node, BinaryTree
from tree_exemple import big_tree

# Return the number of leaves in the subtree rooted at `node`.
#
# Hint: only leaves should contribute to the total — internal nodes do
# not. So you'll need a SECOND base case besides `node is None`. How do
# you spot a leaf from inside a recursive call? Look at its left and
# right pointers.

def count_leaves(node):
    pass    # TODO


## Uncomment once count_leaves is implemented:
# print(count_leaves(big_tree.root))                 # Expected: 7
# print(count_leaves(big_tree.root.left.right))      # Expected: 2  (subtree rooted at 35)
# print(count_leaves(None))                          # Expected: 0
