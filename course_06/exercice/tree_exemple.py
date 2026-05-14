# COURSE 06 — Example trees for testing traversals
#
# Three integer trees of increasing size, all usable as ready-made
# inputs for preorder / inorder / postorder / bfs. Import at the top
# of any exercise:
#
#     from tree_exemple import small_tree, medium_tree, big_tree

from tree import Node, BinaryTree


# --- small_tree: 5 nodes ---
#
#       1
#      / \
#     2   3
#    / \
#   4   5
#

small_tree = BinaryTree()
small_tree.root = Node(1)
_s2 = small_tree.add_left(small_tree.root, 2)
small_tree.add_right(small_tree.root, 3)
small_tree.add_left(_s2, 4)
small_tree.add_right(_s2, 5)


# --- medium_tree: 8 nodes ---
#
#           10
#         /    \
#       20      30
#      /  \    /  \
#     40  50  60  70
#         /
#        80
#

medium_tree = BinaryTree()
medium_tree.root = Node(10)
_m20 = medium_tree.add_left(medium_tree.root, 20)
_m30 = medium_tree.add_right(medium_tree.root, 30)
medium_tree.add_left(_m20, 40)
_m50 = medium_tree.add_right(_m20, 50)
medium_tree.add_left(_m30, 60)
medium_tree.add_right(_m30, 70)
medium_tree.add_left(_m50, 80)


# --- big_tree: 12 nodes ---
#
#                    1
#                  /  \
#                /     \
#               2       3
#              / \     / \
#             4   5   6   7
#            /   / \       \
#           8   9  10      11
#                  /  
#                 12  
#

big_tree = BinaryTree()
big_tree.root = Node(1)
_b2 = big_tree.add_left(big_tree.root, 2)
_b3 = big_tree.add_right(big_tree.root, 3)
_b4 = big_tree.add_left(_b2, 4)
_b5 = big_tree.add_right(_b2, 5)
_b6 = big_tree.add_left(_b3, 6)
_b7 = big_tree.add_right(_b3, 7)
big_tree.add_left(_b4, 8)
big_tree.add_left(_b5, 9)
_b10 = big_tree.add_right(_b5, 10)
big_tree.add_right(_b7, 11)
big_tree.add_left(_b10, 12)
