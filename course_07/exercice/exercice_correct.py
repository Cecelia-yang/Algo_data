# COURSE 07 — Exercises (BST part 1) — CORRECTION


# ─── Exo 1 — bst_search ──────────────────────────────────────────────

from bst import Node
from tree_exemple import lecture_bst, small_bst

def bst_search(node, target):
    if node is None:
        return None
    if node.value == target:
        return node
    if target < node.value:
        return bst_search(node.left, target)
    return bst_search(node.right, target)


print("=== Exo 1 ===")
print(bst_search(lecture_bst, 7))
print(bst_search(lecture_bst, 99))
print(bst_search(None, 42))



# ─── Exo 2 — bst_insert ──────────────────────────────────────────────

from bst import Node

def bst_insert(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = bst_insert(node.left, value)
    elif value > node.value:
        node.right = bst_insert(node.right, value)
    return node

# Note — if you wrote the "look-ahead" version (check `if node.left is None`
# and create the new Node there, without returning it back up):
# it works, but (1) it crashes on an empty root, (2) it repeats the
# Node(value) creation in both branches instead of factoring it into one
# base case, and (3) it cannot support the rotations that AVL / Red-Black
# trees do in Class 08 — those need the parent to re-attach a possibly-
# different subtree root, which is exactly what `node.left = bst_insert(...)`
# is built for. See the teaching note FAQ for the full version.


print("\n=== Exo 2 ===")
root = None
for v in [10, 5, 15, 2, 7, 20]:
    root = bst_insert(root, v)
print(root.value, root.left.value, root.right.value)
print(root.left.left.value, root.left.right.value)



# ─── Exo 3 — bst_min / bst_max ───────────────────────────────────────

from bst import Node
from tree_exemple import lecture_bst, small_bst

def bst_min(node):
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node.value


def bst_max(node):
    if node is None:
        return None
    while node.right is not None:
        node = node.right
    return node.value


print("\n=== Exo 3 ===")
print(bst_min(lecture_bst), bst_max(lecture_bst))
print(bst_min(small_bst), bst_max(small_bst))
print(bst_min(None))



# ─── Exo 4 — inorder_values ──────────────────────────────────────────

from bst import Node
from tree_exemple import lecture_bst, small_bst

def inorder_values(node):
    if node is None:
        return []
    return inorder_values(node.left) + [node.value] + inorder_values(node.right)


print("\n=== Exo 4 ===")
print(inorder_values(lecture_bst))
print(inorder_values(small_bst))
print(inorder_values(None))



# ██████████████████████████████
# BONUS
# ██████████████████████████████


# ─── Bonus 1 — range_values ──────────────────────────────────────────

from bst import Node
from tree_exemple import lecture_bst

def range_values(node, lo, hi):
    if node is None:
        return []
    result = []
    if node.value > lo:                       # left subtree may contain matches
        result += range_values(node.left, lo, hi)
    if lo <= node.value <= hi:
        result.append(node.value)
    if node.value < hi:                       # right subtree may contain matches
        result += range_values(node.right, lo, hi)
    return result


print("\n=== Bonus 1 ===")
print(range_values(lecture_bst, 4, 10))
print(range_values(lecture_bst, 0, 3))
print(range_values(lecture_bst, 20, 30))
print(range_values(None, 0, 100))



# ─── Bonus 2 — build_balanced ────────────────────────────────────────

from bst import Node

def build_balanced(sorted_values):
    if not sorted_values:
        return None
    mid = len(sorted_values) // 2
    root = Node(sorted_values[mid])
    root.left = build_balanced(sorted_values[:mid])
    root.right = build_balanced(sorted_values[mid+1:])
    return root


print("\n=== Bonus 2 ===")
t = build_balanced([1, 2, 3, 4, 5, 6, 7])
print(t.value)
print(t.left.value, t.right.value)
print(inorder_values(t))
print(build_balanced([]))
