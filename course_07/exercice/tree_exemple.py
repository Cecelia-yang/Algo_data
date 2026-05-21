# COURSE 07 — Example BSTs for testing
#
# Three BSTs built by hand (raw Node objects, no insert needed). That
# way you can test `bst_search` BEFORE you finish `bst_insert`. Import
# at the top of any exercise:
#
#     from tree_exemple import lecture_bst, small_bst, degenerate_bst

from bst import Node


# --- lecture_bst (9 nodes) — the exact tree from the slides ---
#
#         8
#        / \
#       3   10
#      / \    \
#     1   6    14
#        / \   /
#       4   7 13
#

lecture_bst = Node(8)
lecture_bst.left = Node(3)
lecture_bst.right = Node(10)
lecture_bst.left.left = Node(1)
lecture_bst.left.right = Node(6)
lecture_bst.left.right.left = Node(4)
lecture_bst.left.right.right = Node(7)
lecture_bst.right.right = Node(14)
lecture_bst.right.right.left = Node(13)


# --- small_bst (5 nodes) ---
#
#       5
#      / \
#     3   8
#    / \
#   1   4
#

small_bst = Node(5)
small_bst.left = Node(3)
small_bst.right = Node(8)
small_bst.left.left = Node(1)
small_bst.left.right = Node(4)


# --- degenerate_bst (4 nodes) — what you get from inserting [1, 2, 3, 4] ---
#
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#

degenerate_bst = Node(1)
degenerate_bst.right = Node(2)
degenerate_bst.right.right = Node(3)
degenerate_bst.right.right.right = Node(4)
