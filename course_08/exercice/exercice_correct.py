# COURSE 08 — Exercises (BST part 2) — CORRECTION


# ─── Exo 1 — bst_delete (cases 1 and 2) ──────────────────────────────

from bst import Node, build_bst, inorder_values

def bst_delete(node, value):
    if node is None:
        return None
    if value < node.value:
        node.left = bst_delete(node.left, value)
    elif value > node.value:
        node.right = bst_delete(node.right, value)
    else:
        # match — handle cases 1 and 2
        if node.left is None and node.right is None:
            return None                  # case 1: leaf
        if node.left is None:
            return node.right            # case 2: only right child
        if node.right is None:
            return node.left             # case 2: only left child
        # 2-children case: leave unchanged (handled in Exo 4)
    return node


print("=== Exo 1 ===")
t = build_bst([5, 3, 8, 1, 4])
t = bst_delete(t, 1)
print(inorder_values(t))
t = build_bst([5, 3, 8, 1, 10])
t = bst_delete(t, 8)
print(inorder_values(t))
t = build_bst([5, 3, 8, 1])
t = bst_delete(t, 3)
print(inorder_values(t))



# ─── Exo 2 — closest_value ───────────────────────────────────────────

from bst import Node
from tree_exemple import lecture_bst, balanced_bst

def closest_value(node, target):
    if node is None:
        return None
    best = node.value
    while node is not None:
        if abs(node.value - target) < abs(best - target):
            best = node.value
        if target < node.value:
            node = node.left
        elif target > node.value:
            node = node.right
        else:
            return node.value
    return best


print("\n=== Exo 2 ===")
print(closest_value(lecture_bst, 5))
print(closest_value(lecture_bst, 12))
print(closest_value(lecture_bst, 100))
print(closest_value(None, 0))



# ─── Exo 3 — successor ───────────────────────────────────────────────

from bst import Node
from tree_exemple import lecture_bst

def successor(node, value):
    best = None
    while node is not None:
        if value < node.value:
            best = node.value            # candidate — may find smaller
            node = node.left
        else:
            node = node.right            # too small, discard
    return best


print("\n=== Exo 3 ===")
print(successor(lecture_bst, 6))
print(successor(lecture_bst, 7))
print(successor(lecture_bst, 14))
print(successor(lecture_bst, 5))
print(successor(None, 0))



# ─── Exo 4 — bst_delete_full (with case 3) ───────────────────────────

from bst import Node, build_bst, inorder_values

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def bst_delete_full(node, value):
    if node is None:
        return None
    if value < node.value:
        node.left = bst_delete_full(node.left, value)
    elif value > node.value:
        node.right = bst_delete_full(node.right, value)
    else:
        if node.left is None and node.right is None:
            return None
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        # case 3: copy the inorder successor's value, delete it below
        succ = find_min(node.right)
        node.value = succ.value
        node.right = bst_delete_full(node.right, succ.value)
    return node


print("\n=== Exo 4 ===")
t = build_bst([8, 3, 10, 1, 6, 14, 4, 7, 13])
t = bst_delete_full(t, 6)
print(inorder_values(t))
t = build_bst([8, 3, 10, 1, 6, 14, 4, 7, 13])
t = bst_delete_full(t, 8)
print(t.value)
print(inorder_values(t))
t = build_bst([5, 3, 8, 1, 4, 7, 10])
for v in [3, 5, 8]:
    t = bst_delete_full(t, v)
print(inorder_values(t))



# ██████████████████████████████
# BONUS
# ██████████████████████████████


# ─── Bonus 1 — is_valid_bst ──────────────────────────────────────────

from bst import Node
from tree_exemple import lecture_bst, balanced_bst

def is_valid_bst(node, lo=float('-inf'), hi=float('inf')):
    if node is None:
        return True
    if node.value <= lo or node.value >= hi:
        return False
    return (is_valid_bst(node.left, lo, node.value)
            and is_valid_bst(node.right, node.value, hi))


print("\n=== Bonus 1 ===")
print(is_valid_bst(lecture_bst))
print(is_valid_bst(balanced_bst))
print(is_valid_bst(None))
bad = Node(8)
bad.left = Node(3); bad.right = Node(10)
bad.left.left = Node(1); bad.left.right = Node(12)
print(is_valid_bst(bad))



# ─── Bonus 2 — is_balanced ───────────────────────────────────────────

from bst import Node, tree_height
from tree_exemple import lecture_bst, balanced_bst, degenerate_bst

def is_balanced(node):
    if node is None:
        return True
    if abs(tree_height(node.left) - tree_height(node.right)) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)


print("\n=== Bonus 2 ===")
print(is_balanced(lecture_bst))
print(is_balanced(balanced_bst))
print(is_balanced(degenerate_bst))
print(is_balanced(None))
