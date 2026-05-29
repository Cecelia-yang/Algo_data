# PRACTICE MIDTERM — Exercises (Courses 01–09 review)
#
# Small, independent exercises. Fill each `# TODO`, then remove the `# `
# in front of the test prints below it and run:  python3 exercise.py
# The SETUP block gives you a Node class and two ready-made trees.
# If you copy one exercise into a REPL, run the SETUP block first.


# ─── SETUP — shared fixtures (run this first) ────────────────────────
class Node:                       # binary tree / BST node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# A small binary tree (used by the traversal exercises):
#         6
#        / \
#       4   8
#      / \   \
#     1   7   3
sample_tree = Node(6)
sample_tree.left = Node(4)
sample_tree.right = Node(8)
sample_tree.left.left = Node(1)
sample_tree.left.right = Node(7)
sample_tree.right.right = Node(3)

# A valid BST (used by the BST exercises):
#         50
#        /  \
#       30   70
#      / \     \
#     20  40    90
sample_bst = Node(50)
sample_bst.left = Node(30)
sample_bst.right = Node(70)
sample_bst.left.left = Node(20)
sample_bst.left.right = Node(40)
sample_bst.right.right = Node(90)


# ─── Exo 1 — binary_search ───────────────────────────────────────────
# Course 01. The list is SORTED. Return the index of `target`, or -1.
# Cut the search space in half each step — do NOT scan from the start.

def binary_search(lst, target):
    pass    # TODO


print("=== Exo 1 ===")
# print(binary_search([1, 3, 5, 7, 9, 11], 7))   # 3
# print(binary_search([1, 3, 5, 7, 9, 11], 4))   # -1
# print(binary_search([], 5))                     # -1


# ─── Exo 2 — word_count ──────────────────────────────────────────────
# Course 03. Return a dict mapping each word to how many times it appears.
# Split on spaces with text.split(). Use the d.get(w, 0) + 1 pattern.

def word_count(text):
    pass    # TODO


print("\n=== Exo 2 ===")
# print(word_count("the cat the dog the"))   # {'the': 3, 'cat': 1, 'dog': 1}


# ─── Exo 3 — two_sum ─────────────────────────────────────────────────
# Course 03. Return (i, j) with nums[i] + nums[j] == target, i < j, else None.
# ONE pass. As you walk, ask: "have I already seen target - x?"
# Beware: an element must not pair with itself. enumerate gives (i, x).

def two_sum(nums, target):
    pass    # TODO


print("\n=== Exo 3 ===")
# print(two_sum([2, 7, 11, 15], 9))   # (0, 1)
# print(two_sum([8, 2, 5, 11], 7))    # (1, 2)
# print(two_sum([1, 2, 3], 100))      # None


# ─── Exo 4 — factorial ───────────────────────────────────────────────
# Course 03/04. Recursive. factorial(0) = 1. Write the BASE CASE first.

def factorial(n):
    pass    # TODO


print("\n=== Exo 4 ===")
# print(factorial(0))   # 1
# print(factorial(5))   # 120


# ─── Exo 5 — count_nodes / find_max_value ────────────────────────────
# Course 05. Recursion on a binary tree: same skeleton as a linked-list
# walk, but TWO recursive calls (left AND right). Empty tree (None):
# count_nodes → 0, find_max_value → float('-inf').

def count_nodes(node):
    pass    # TODO


def find_max_value(node):
    pass    # TODO


print("\n=== Exo 5 ===")
# print(count_nodes(sample_tree))      # 6
# print(count_nodes(None))             # 0
# print(find_max_value(sample_tree))   # 8


# ─── Exo 6 — inorder ─────────────────────────────────────────────────
# Course 06. RETURN a list of values in inorder (left → node → right).
# On a BST, inorder comes out sorted — check it on sample_bst.

def inorder(node):
    pass    # TODO


print("\n=== Exo 6 ===")
# print(inorder(sample_tree))   # [1, 4, 7, 6, 8, 3]
# print(inorder(sample_bst))    # [20, 30, 40, 50, 70, 90]  (sorted!)


# ─── Exo 7 — bfs ─────────────────────────────────────────────────────
# Course 06. RETURN the values level by level (breadth-first).
# A queue serves the oldest waiting node first. deque: .append, .popleft.

def bfs(root):
    pass    # TODO


print("\n=== Exo 7 ===")
# print(bfs(sample_tree))   # [6, 4, 8, 1, 7, 3]
# print(bfs(None))          # []


# ─── Exo 8 — bst_search ──────────────────────────────────────────────
# Course 07. Return the Node holding `target`, or None. Recursive.
# Compare with node.value, then go left or right (do not search both).

def bst_search(node, target):
    pass    # TODO


print("\n=== Exo 8 ===")
# found = bst_search(sample_bst, 40)
# print(found.value if found else None)         # 40
# print(bst_search(sample_bst, 55))             # None


# ─── Exo 9 — bst_insert ──────────────────────────────────────────────
# Course 07. Insert `value`, return the (possibly new) subtree root.
# Duplicates: do nothing. Re-attach idiom:
#     node.left = bst_insert(node.left, value)

def bst_insert(node, value):
    pass    # TODO


print("\n=== Exo 9 ===")
# root = None
# for v in [5, 3, 8, 1, 4, 7]:
#     root = bst_insert(root, v)
# print(root.value, root.left.value, root.right.value)          # 5 3 8
# print(root.left.left.value, root.left.right.value)            # 1 4
# print(root.right.left.value)                                   # 7


# ─── Exo 10 — heap indexes / is_min_heap ─────────────────────────────
# Course 09. A heap lives in an array. For index i:
#   parent = (i - 1) // 2,  left = 2*i + 1,  right = 2*i + 2.
# Write the three index helpers, then is_min_heap(arr): True if every
# parent is <= its children.

def parent(i):
    pass    # TODO


def left(i):
    pass    # TODO


def right(i):
    pass    # TODO


def is_min_heap(arr):
    pass    # TODO


print("\n=== Exo 10 ===")
# print(parent(3), left(3), right(3))           # 1 7 8
# print(is_min_heap([2, 4, 3, 8, 5, 9, 7]))     # True
# print(is_min_heap([1, 5, 2, 7, 4]))           # False
