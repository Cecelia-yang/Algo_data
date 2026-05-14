# COURSE 06 EXERCISES — Tree Traversals

# Four ways to visit every node: preorder, inorder, postorder (DFS twins,
# all recursive) and BFS (queue-based, iterative).
#
# Node and BinaryTree live in tree.py. Example trees (small_tree 5 nodes,
# medium_tree 8 nodes, big_tree 12 nodes) live in tree_exemple.py. Each
# exercise re-imports what it needs so you can copy a single exercise
# into the Python REPL on its own.
#
# REPL setup (one-time): open the `exercice/` folder as your VS Code
# workspace, OR `cd` into it before launching `python3`. That way the
# imports `from tree import ...` and `from tree_exemple import ...`
# resolve correctly without any path hack.


# ██████████████████████████████
# PART 1 — DFS + BFS implementations
# ██████████████████████████████
# DFS (preorder, inorder, postorder) share the SAME 4-line skeleton —
# only the line where you "visit" MOVES. BFS uses a queue instead.
#
#   def traversal(node):
#       if node is None:
#           return
#       # ← preorder visits HERE   (root before children)
#       traversal(node.left)
#       # ← inorder  visits HERE   (root between children)
#       traversal(node.right)
#       # ← postorder visits HERE  (root after children)
#
# (The 3 reference trees used by all PART 1 tests are drawn at the END
#  of PART 1 — scroll down to the "Reference trees" block.)


# --- Exo 1.1 : preorder (GIVEN — read it carefully) ---
from tree import Node, BinaryTree
from tree_exemple import small_tree, medium_tree, big_tree

# Preorder visits BEFORE descending. Order: root → left → right.
# This one is filled in for you. Read it. Run it. Match the output
# with what you traced by hand.

def preorder(node):
    if node is None:
        return
    print(node.value)              # 1) VISIT current
    preorder(node.left)            # 2) recurse LEFT
    preorder(node.right)           # 3) recurse RIGHT


print("=== preorder (small_tree) ===")
preorder(small_tree.root)
# Expected (one per line): 1, 2, 4, 5, 3

print("\n=== preorder (medium_tree) ===")
preorder(medium_tree.root)
# Expected (one per line): 10, 20, 40, 50, 80, 30, 60, 70



# --- Exo 1.2 : inorder ---
from tree import Node, BinaryTree
from tree_exemple import small_tree, medium_tree, big_tree

# Order: left → root → right.
# Adapt preorder by MOVING the print line. Skeleton stays the same; the
# two recursive calls stay the same. Only the position of `print` changes.

def inorder(node):
    pass    # TODO


print("\n=== inorder (small_tree) ===")
## Uncomment once inorder is implemented:
# inorder(small_tree.root)
## Expected (one per line): 4, 2, 5, 1, 3

print("\n=== inorder (medium_tree) ===")
## Uncomment once inorder is implemented:
# inorder(medium_tree.root)
## Expected (one per line): 40, 20, 80, 50, 10, 60, 30, 70



# --- Exo 1.3 : postorder ---
from tree import Node, BinaryTree
from tree_exemple import small_tree, medium_tree, big_tree

# Order: left → right → root.
# Same idea — move the print line, this time AFTER both recursive calls.
# Children first, parent last.

def postorder(node):
    pass    # TODO


print("\n=== postorder (small_tree) ===")
## Uncomment once postorder is implemented:
# postorder(small_tree.root)
## Expected (one per line): 4, 5, 2, 3, 1

print("\n=== postorder (big_tree) ===")
## Uncomment once postorder is implemented:
# postorder(big_tree.root)
## Expected (one per line): 8, 4, 9, 12, 10, 5, 2, 6, 11, 7, 3, 1



# --- Exo 1.4 : bfs ---
from collections import deque
from tree import Node, BinaryTree
from tree_exemple import small_tree, medium_tree, big_tree

# Print every value LEVEL BY LEVEL, starting from the root.
#
# Hint: you already know `deque`, `popleft`, `append` from Class 02.
# Start the queue with the root inside, loop while the queue is not
# empty, and at each step: pop the front, print its value, and append
# the existing children to the back.
#
# Edge case: a None root → print nothing, don't crash.

def bfs(root):
    pass    # TODO


print("\n=== bfs (small_tree) ===")
## Uncomment once bfs is implemented:
# bfs(small_tree.root)
## Expected (one per line): 1, 2, 3, 4, 5

print("\n=== bfs (big_tree) ===")
## Uncomment once bfs is implemented:
# bfs(big_tree.root)
## Expected (one per line): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

print("\n=== bfs (None — empty tree) ===")
## Uncomment once bfs is implemented:
# bfs(None)
## Expected: nothing printed (no crash)


# ──────────────────────────────────────────────────────────────────────
# Reference trees used by all PART 1 tests (defined in tree_exemple.py):
# ──────────────────────────────────────────────────────────────────────
#
# small_tree (5)        medium_tree (8)              big_tree (12)
#
#     1                       10                              1
#    / \                    /    \                          /  \
#   2   3                 20      30                      /     \
#  / \                   /  \    /  \                    2       3
# 4   5                 40  50  60  70                  / \     / \
#                           /                          4   5   6   7
#                          80                         /   / \       \
#                                                    8   9  10      11
#                                                            /
#                                                           12



# ██████████████████████████████
# PART 2 — Mental trace exercises (NO CODE TO WRITE)
# ██████████████████████████████
# Look at each tree below WITHOUT running any code. Mentally walk through
# the 4 traversals and fill in the strings as concatenated values, e.g.
# "ABCDE" for preorder on a 5-node tree with letter values.
# Simple → medium → complex. Don't peek at the correction file.


# --- Exo 2.1 : simple tree (5 nodes) ---
#
#       A
#      / \
#     B   C
#        / \
#       D   E

trace_2_1_preorder  = ""    # TODO
trace_2_1_inorder   = ""    # TODO
trace_2_1_postorder = ""    # TODO
trace_2_1_bfs       = ""    # TODO



# --- Exo 2.2 : medium tree (7 nodes) ---
#
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#       /
#      7

trace_2_2_preorder  = ""    # TODO
trace_2_2_inorder   = ""    # TODO
trace_2_2_postorder = ""    # TODO
trace_2_2_bfs       = ""    # TODO



# --- Exo 2.3 : complex tree (9 nodes, asymmetric) ---
#
#          A
#         / \
#        B   C
#       /   / \
#      D   E   F
#     / \      /
#    G   H    I

trace_2_3_preorder  = ""    # TODO
trace_2_3_inorder   = ""    # TODO
trace_2_3_postorder = ""    # TODO
trace_2_3_bfs       = ""    # TODO



# ██████████████████████████████
# PART 3 — STRETCH: return a list instead of printing
# ██████████████████████████████
# Same notion as PART 1. Just change the action: instead of printing,
# append to a list and return it. More testable, and what you'll actually
# want in projects.


# --- Stretch 3.1 : preorder_list ---
from tree import Node, BinaryTree
from tree_exemple import small_tree, big_tree

# Same as preorder, but build and return a list of values in preorder.
# Empty tree → return [].
#
# Hint: a tiny inner function (closure) that grows a shared list as it
# walks. Wrap it so the public function returns the finished list.

def preorder_list(node):
    pass    # TODO


## Uncomment once preorder_list is implemented:
# print(preorder_list(small_tree.root))    # Expected: [1, 2, 4, 5, 3]
# print(preorder_list(big_tree.root))      # Expected: [1, 2, 4, 8, 5, 9, 10, 12, 3, 6, 7, 11]
# print(preorder_list(None))               # Expected: []



# --- Stretch 3.2 : bfs_list ---
from collections import deque
from tree import Node, BinaryTree
from tree_exemple import small_tree, big_tree

# Same idea for BFS. Returns a list of values in BFS order.
# Empty tree → return [].

def bfs_list(root):
    pass    # TODO


## Uncomment once bfs_list is implemented:
# print(bfs_list(small_tree.root))     # Expected: [1, 2, 3, 4, 5]
# print(bfs_list(big_tree.root))       # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(bfs_list(None))                # Expected: []
