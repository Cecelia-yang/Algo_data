# COURSE 05 — Example trees for testing
#
# Two ready-made integer trees so you can test your tree functions
# without rebuilding a tree by hand each time. Import at the top of
# any exercise:
#
#     from tree_exemple import small_tree, big_tree

from tree import Node, BinaryTree


# --- small_tree: 6 nodes ---
#
#       10
#      /  \
#     5    15
#    / \    \
#   3   7   20
#
# count_nodes = 6, find_max = 20, tree_height = 2, count_leaves = 3

small_tree = BinaryTree()
small_tree.root = Node(10)
_s5  = small_tree.add_left(small_tree.root, 5)
_s15 = small_tree.add_right(small_tree.root, 15)
small_tree.add_left(_s5, 3)
small_tree.add_right(_s5, 7)
small_tree.add_right(_s15, 20)


# --- big_tree: 15 nodes ---
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
# count_nodes = 15, find_max = 95, tree_height = 4, count_leaves = 7
# (subtree at 35: tree_height = 2, count_leaves = 2 → leaves 28 and 40)

big_tree = BinaryTree()
big_tree.root = Node(50)
_b25 = big_tree.add_left(big_tree.root, 25)
_b75 = big_tree.add_right(big_tree.root, 75)
_b10 = big_tree.add_left(_b25, 10)
_b35 = big_tree.add_right(_b25, 35)
_b60 = big_tree.add_left(_b75, 60)
_b90 = big_tree.add_right(_b75, 90)
big_tree.add_left(_b10, 5)
big_tree.add_right(_b10, 15)
_b30 = big_tree.add_left(_b35, 30)
big_tree.add_right(_b35, 40)
big_tree.add_right(_b60, 65)
big_tree.add_left(_b90, 80)
big_tree.add_right(_b90, 95)
big_tree.add_left(_b30, 28)
