# COURSE 05 EXERCISES — CORRECTION
# Trees: vocabulary + Binary Tree class
#
# The Node and BinaryTree classes live in tree.py, and the example
# trees (small_tree, big_tree) in tree_exemple.py. Each exercise below
# re-imports what it needs so you can copy a single exercise into the
# Python REPL on its own.
#
# REPL setup (one-time): open the `exercice/` folder as your VS Code
# workspace, OR `cd` into it before launching `python3`. That way the
# imports resolve correctly without any path hack.


# ████████████████████████████████████████████████████
# PART 1 — Build a tree by hand
# ████████████████████████████████████████████████████


# --- Exo 1.1 : build the lecture tree ---
from tree import Node, BinaryTree

tree_1_1 = BinaryTree()
tree_1_1.root = Node("A")
b = tree_1_1.add_left(tree_1_1.root, "B")    # save b — we attach D and E to it next
tree_1_1.add_right(tree_1_1.root, "C")        # leaf, no need to save
tree_1_1.add_left(b, "D")
tree_1_1.add_right(b, "E")
# Each add_* returns the new node. We only keep `b` because we need it
# again to attach D and E. C is a leaf so we don't bother naming it.

print(tree_1_1.root.value)              # Expected: A
print(tree_1_1.root.left.value)         # Expected: B
print(tree_1_1.root.right.value)        # Expected: C
print(tree_1_1.root.left.left.value)    # Expected: D
print(tree_1_1.root.left.right.value)   # Expected: E



# --- Exo 1.2 : vocabulary check ---
from tree import Node, BinaryTree

answer_1_2_root_value     = "A"
answer_1_2_leaf_values    = {"C", "D", "E"}    # the three nodes with no children
answer_1_2_depth_of_D     = 2                  # A → B → D = 2 edges
answer_1_2_height_of_tree = 2                  # the deepest leaf (D or E) has depth 2

print(answer_1_2_root_value)      # Expected: A
print(answer_1_2_leaf_values)     # Expected: {'C', 'D', 'E'}
print(answer_1_2_depth_of_D)      # Expected: 2
print(answer_1_2_height_of_tree)  # Expected: 2



# ████████████████████████████████████████████████████
# PART 2 — count_nodes
# ████████████████████████████████████████████████████


# --- Exo 2.1 : count_nodes ---
from tree import Node, BinaryTree
from tree_exemple import small_tree

def count_nodes(node):
    if node is None:
        return 0                               # base case: empty subtree has 0 nodes
    return 1 + count_nodes(node.left) + count_nodes(node.right)
    # +1 for the current node, plus the count of each subtree


print(count_nodes(tree_1_1.root))      # Expected: 5
print(count_nodes(small_tree.root))    # Expected: 6
print(count_nodes(None))               # Expected: 0



# --- Exo 2.2 : count_nodes on a different tree ---
from tree import Node, BinaryTree

tree_2_2 = BinaryTree()
tree_2_2.root = Node("X")
tree_2_2.add_left(tree_2_2.root, "Y")
tree_2_2.add_right(tree_2_2.root, "Z")

print(count_nodes(tree_2_2.root))    # Expected: 3



# ████████████████████████████████████████████████████
# PART 3 — find_max_value
# ████████████████████████████████████████████████████


# --- Exo 3.1 : find_max_value ---
from tree import Node, BinaryTree
from tree_exemple import small_tree

def find_max_value(node):
    if node is None:
        return float('-inf')                   # neutral element for max
    return max(node.value,
               find_max_value(node.left),
               find_max_value(node.right))
    # Three values: my own + max of left subtree + max of right subtree.


tree_3_1 = BinaryTree()
tree_3_1.root = Node(5)
nine = tree_3_1.add_left(tree_3_1.root, 9)
tree_3_1.add_right(tree_3_1.root, 2)
tree_3_1.add_left(nine, 3)
tree_3_1.add_right(nine, 12)

print(find_max_value(tree_3_1.root))      # Expected: 12
print(find_max_value(small_tree.root))    # Expected: 20
print(find_max_value(None))               # Expected: -inf



# --- Exo 3.2 : same idea, your own tree ---
from tree import Node, BinaryTree
from tree_exemple import big_tree

tree_3_2 = BinaryTree()
tree_3_2.root = Node(-7)
tree_3_2.add_left(tree_3_2.root, -3)
tree_3_2.add_right(tree_3_2.root, -10)

print(find_max_value(tree_3_2.root))    # Expected: -3
# If we had used 0 as the neutral element, this would have returned 0
# instead of -3. -inf is the only safe choice for max.
print(find_max_value(big_tree.root))    # Expected: 95



# ████████████████████████████████████████████████████
# PART 4 — BONUS
# ████████████████████████████████████████████████████
# big_tree (15 nodes, defined in tree_exemple.py) is deeper and slightly
# unbalanced — heavier stress for the recursion than tree_1_1 ever could:
#
#                 50
#              /      \
#            25        75
#           /  \      /  \
#         10    35   60   90
#        /  \  /  \    \  / \
#       5   15 30  40  65 80 95
#              /
#             28
#
# 15 nodes total, height 4 (50→25→35→30→28), leaves = {5, 15, 28, 40, 65, 80, 95} → 7 leaves.
# Note: 30 is NOT a leaf — it still has one child (28), even though its
# right pointer is None. A node is a leaf only when BOTH children are None.


# --- Bonus 4.1 : tree_height ---
from tree import Node, BinaryTree
from tree_exemple import big_tree

def tree_height(node):
    if node is None:
        return -1                              # so a single leaf returns 0
    return 1 + max(tree_height(node.left), tree_height(node.right))
    # height = 1 + bigger subtree height. Same shape as count_nodes,
    # max instead of +, and -1 as the neutral element.


print(tree_height(None))                          # Expected: -1
print(tree_height(Node("only")))                  # Expected: 0
print(tree_height(big_tree.root))                 # Expected: 4
print(tree_height(big_tree.root.left.right))      # Expected: 2
# Calling tree_height on a SUBTREE (here big_tree.root.left.right = the
# subtree rooted at 35) returns the height of that subtree only — 35 has
# children 30 (with one child 28) and 40, so its height is 2.



# --- Bonus 4.2 : count_leaves ---
from tree import Node, BinaryTree
from tree_exemple import big_tree

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1                               # this node IS a leaf
    return count_leaves(node.left) + count_leaves(node.right)
    # Two base cases instead of one. Note: no +1 in the recursive case —
    # internal nodes don't count as leaves, only their leaf descendants do.


print(count_leaves(big_tree.root))                 # Expected: 7
print(count_leaves(big_tree.root.left.right))      # Expected: 2
print(count_leaves(None))                          # Expected: 0
# big_tree has 7 leaves: 5, 15, 28, 40, 65, 80, 95.
# The subtree at 35 counts only 2 leaves (28 and 40) because we recurse
# into 35's subtree only — everything above 35 is invisible from this call.
