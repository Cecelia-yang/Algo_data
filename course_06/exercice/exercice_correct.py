# COURSE 06 EXERCISES — CORRECTION
# Tree Traversals
#
# Node and BinaryTree live in tree.py. Example trees (small_tree 5 nodes,
# medium_tree 8 nodes, big_tree 12 nodes) live in tree_exemple.py. Each
# exercise re-imports what it needs so you can copy a single exercise
# into the Python REPL on its own.
#
# REPL setup (one-time): open the `exercice/` folder as your VS Code
# workspace, OR `cd` into it before launching `python3`. The imports
# resolve correctly without any path hack.


# ████████████████████████████████████████████████████
# PART 1 — DFS + BFS implementations
# ████████████████████████████████████████████████████
# (Reference trees drawn at the END of PART 1, scroll down.)


# --- Exo 1.1 : preorder (given) ---
from tree import Node, BinaryTree
from tree_exemple import small_tree, medium_tree, big_tree

def preorder(node):
    if node is None:
        return
    print(node.value)              # 1) visit BEFORE descending
    preorder(node.left)
    preorder(node.right)


print("=== preorder (small_tree) ===")
preorder(small_tree.root)
# Expected (one per line): 1, 2, 4, 5, 3

print("\n=== preorder (medium_tree) ===")
preorder(medium_tree.root)
# Expected (one per line): 10, 20, 40, 50, 80, 30, 60, 70



# --- Exo 1.2 : inorder ---
from tree import Node, BinaryTree
from tree_exemple import small_tree, medium_tree, big_tree

def inorder(node):
    if node is None:
        return
    inorder(node.left)             # left first
    print(node.value)              # 2) visit BETWEEN the two recursions
    inorder(node.right)
    # The visit slot moved to the middle. Same skeleton, one line moved.


print("\n=== inorder (small_tree) ===")
inorder(small_tree.root)
# Expected (one per line): 4, 2, 5, 1, 3

print("\n=== inorder (medium_tree) ===")
inorder(medium_tree.root)
# Expected (one per line): 40, 20, 80, 50, 10, 60, 30, 70



# --- Exo 1.3 : postorder ---
from tree import Node, BinaryTree
from tree_exemple import small_tree, medium_tree, big_tree

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)              # 3) visit AFTER both recursions
    # Children first, parent last. Useful when the parent's result
    # depends on the children (folder size, tree height, free memory).


print("\n=== postorder (small_tree) ===")
postorder(small_tree.root)
# Expected (one per line): 4, 5, 2, 3, 1

print("\n=== postorder (big_tree) ===")
postorder(big_tree.root)
# Expected (one per line): 8, 4, 9, 12, 10, 5, 2, 6, 11, 7, 3, 1



# --- Exo 1.4 : bfs ---
from collections import deque
from tree import Node, BinaryTree
from tree_exemple import small_tree, medium_tree, big_tree

def bfs(root):
    if root is None:
        return                                # empty tree: nothing to print
    queue = deque([root])                     # start with root in the queue
    while queue:
        node = queue.popleft()                # OLDEST first (FIFO)
        print(node.value)                     # visit
        if node.left is not None:
            queue.append(node.left)           # add children to the END
        if node.right is not None:
            queue.append(node.right)
    # popleft + append = FIFO. That's the whole BFS discipline.


print("\n=== bfs (small_tree) ===")
bfs(small_tree.root)
# Expected (one per line): 1, 2, 3, 4, 5

print("\n=== bfs (big_tree) ===")
bfs(big_tree.root)
# Expected (one per line): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

print("\n=== bfs (None — empty tree) ===")
bfs(None)
# Expected: nothing printed (no crash)


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



# ████████████████████████████████████████████████████
# PART 2 — Mental trace exercises (answers)
# ████████████████████████████████████████████████████


# --- Exo 2.1 : simple tree (5 nodes) ---
#
#       A
#      / \
#     B   C
#        / \
#       D   E

trace_2_1_preorder  = "ABCDE"
trace_2_1_inorder   = "BADCE"
trace_2_1_postorder = "BDECA"
trace_2_1_bfs       = "ABCDE"

print("\n=== trace 2.1 ===")
print("preorder :", trace_2_1_preorder)     # Expected: ABCDE
print("inorder  :", trace_2_1_inorder)      # Expected: BADCE
print("postorder:", trace_2_1_postorder)    # Expected: BDECA
print("bfs      :", trace_2_1_bfs)          # Expected: ABCDE



# --- Exo 2.2 : medium tree (7 nodes) ---
#
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#       /
#      7

trace_2_2_preorder  = "1245736"
trace_2_2_inorder   = "4275136"
trace_2_2_postorder = "4752631"
trace_2_2_bfs       = "1234567"

print("\n=== trace 2.2 ===")
print("preorder :", trace_2_2_preorder)     # Expected: 1245736
print("inorder  :", trace_2_2_inorder)      # Expected: 4275136
print("postorder:", trace_2_2_postorder)    # Expected: 4752631
print("bfs      :", trace_2_2_bfs)          # Expected: 1234567



# --- Exo 2.3 : complex tree (9 nodes, asymmetric) ---
#
#          A
#         / \
#        B   C
#       /   / \
#      D   E   F
#     / \      /
#    G   H    I

trace_2_3_preorder  = "ABDGHCEFI"
trace_2_3_inorder   = "GDHBAECIF"
trace_2_3_postorder = "GHDBEIFCA"
trace_2_3_bfs       = "ABCDEFGHI"

print("\n=== trace 2.3 ===")
print("preorder :", trace_2_3_preorder)     # Expected: ABDGHCEFI
print("inorder  :", trace_2_3_inorder)      # Expected: GDHBAECIF
print("postorder:", trace_2_3_postorder)    # Expected: GHDBEIFCA
print("bfs      :", trace_2_3_bfs)          # Expected: ABCDEFGHI



# ████████████████████████████████████████████████████
# PART 3 — STRETCH: return a list
# ████████████████████████████████████████████████████


# --- Stretch 3.1 : preorder_list ---
from tree import Node, BinaryTree
from tree_exemple import small_tree, big_tree

def preorder_list(node):
    result = []
    def walk(n):
        if n is None:
            return
        result.append(n.value)                # same skeleton as preorder,
        walk(n.left)                          # `print` swapped for `append`
        walk(n.right)
    walk(node)
    return result
    # The closure `walk` shares `result` with the outer function.
    # We return result at the end. Empty tree → empty list.


print("\n=== preorder_list ===")
print(preorder_list(small_tree.root))    # Expected: [1, 2, 4, 5, 3]
print(preorder_list(big_tree.root))      # Expected: [1, 2, 4, 8, 5, 9, 10, 12, 3, 6, 7, 11]
print(preorder_list(None))               # Expected: []



# --- Stretch 3.2 : bfs_list ---
from collections import deque
from tree import Node, BinaryTree
from tree_exemple import small_tree, big_tree

def bfs_list(root):
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result
    # Same loop as bfs. Just append to result instead of printing.


print("\n=== bfs_list ===")
print(bfs_list(small_tree.root))     # Expected: [1, 2, 3, 4, 5]
print(bfs_list(big_tree.root))       # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(bfs_list(None))                # Expected: []
