# PRACTICE MIDTERM — Exercises (Courses 01–09 review) — SOLUTIONS
#
# Run end-to-end:  python3 exercice_correct.py
# Every printed line matches its trailing # expected comment.


# ─── SETUP — shared fixtures ─────────────────────────────────────────
class Node:                       # binary tree / BST node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2          # middle of the current window
        if lst[mid] == target:
            return mid
        if lst[mid] < target:
            low = mid + 1                # drop the left half
        else:
            high = mid - 1               # drop the right half
    return -1


print("=== Exo 1 ===")
print(binary_search([1, 3, 5, 7, 9, 11], 7))   # 3
print(binary_search([1, 3, 5, 7, 9, 11], 4))   # -1
print(binary_search([], 5))                     # -1


# ─── Exo 2 — word_count ──────────────────────────────────────────────
def word_count(text):
    counts = {}
    for w in text.split():
        counts[w] = counts.get(w, 0) + 1
    return counts


print("\n=== Exo 2 ===")
print(word_count("the cat the dog the"))   # {'the': 3, 'cat': 1, 'dog': 1}


# ─── Exo 3 — two_sum ─────────────────────────────────────────────────
def two_sum(nums, target):
    seen = {}                            # value -> index
    for i, x in enumerate(nums):
        if target - x in seen:           # check FIRST (O(1) lookup)
            return (seen[target - x], i)
        seen[x] = i                      # record AFTER
    return None


print("\n=== Exo 3 ===")
print(two_sum([2, 7, 11, 15], 9))   # (0, 1)
print(two_sum([8, 2, 5, 11], 7))    # (1, 2)
print(two_sum([1, 2, 3], 100))      # None


# ─── Exo 4 — factorial ───────────────────────────────────────────────
def factorial(n):
    if n == 0:                           # base case first
        return 1
    return n * factorial(n - 1)


print("\n=== Exo 4 ===")
print(factorial(0))   # 1
print(factorial(5))   # 120


# ─── Exo 5 — count_nodes / find_max_value ────────────────────────────
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def find_max_value(node):
    if node is None:
        return float('-inf')             # neutral value for max
    return max(node.value,
               find_max_value(node.left),
               find_max_value(node.right))


print("\n=== Exo 5 ===")
print(count_nodes(sample_tree))      # 6
print(count_nodes(None))             # 0
print(find_max_value(sample_tree))   # 8


# ─── Exo 6 — inorder ─────────────────────────────────────────────────
def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


print("\n=== Exo 6 ===")
print(inorder(sample_tree))   # [1, 4, 7, 6, 8, 3]
print(inorder(sample_bst))    # [20, 30, 40, 50, 70, 90]  (sorted!)


# ─── Exo 7 — bfs ─────────────────────────────────────────────────────
from collections import deque

def bfs(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()           # oldest waiting node first (FIFO)
        result.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result


print("\n=== Exo 7 ===")
print(bfs(sample_tree))   # [6, 4, 8, 1, 7, 3]
print(bfs(None))          # []


# ─── Exo 8 — bst_search ──────────────────────────────────────────────
def bst_search(node, target):
    if node is None:
        return None
    if node.value == target:
        return node
    if target < node.value:
        return bst_search(node.left, target)
    return bst_search(node.right, target)


print("\n=== Exo 8 ===")
found = bst_search(sample_bst, 40)
print(found.value if found else None)         # 40
print(bst_search(sample_bst, 55))             # None


# ─── Exo 9 — bst_insert ──────────────────────────────────────────────
def bst_insert(node, value):
    if node is None:
        return Node(value)               # empty spot → new node
    if value < node.value:
        node.left = bst_insert(node.left, value)    # re-attach
    elif value > node.value:
        node.right = bst_insert(node.right, value)
    return node                          # duplicates fall through unchanged


print("\n=== Exo 9 ===")
root = None
for v in [5, 3, 8, 1, 4, 7]:
    root = bst_insert(root, v)
print(root.value, root.left.value, root.right.value)   # 5 3 8
print(root.left.left.value, root.left.right.value)     # 1 4
print(root.right.left.value)                            # 7


# ─── Exo 10 — heap indexes / is_min_heap ─────────────────────────────
def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def is_min_heap(arr):
    n = len(arr)
    for i in range(n):
        l, r = left(i), right(i)
        if l < n and arr[i] > arr[l]:
            return False
        if r < n and arr[i] > arr[r]:
            return False
    return True


print("\n=== Exo 10 ===")
print(parent(3), left(3), right(3))           # 1 7 8
print(is_min_heap([2, 4, 3, 8, 5, 9, 7]))     # True
print(is_min_heap([1, 5, 2, 7, 4]))           # False
