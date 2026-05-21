# COURSE 08 — Example BSTs for testing deletion
#
# Built with build_bst from bst.py — so the shape is exactly what you
# get from the insert sequence shown. Import what you need:
#
#     from tree_exemple import lecture_bst, balanced_bst, degenerate_bst

from bst import build_bst


# --- lecture_bst (9 nodes) — same tree as Class 07's lecture ---
#
#         8
#        / \
#       3   10
#      / \    \
#     1   6    14
#        / \   /
#       4   7 13
#
# Built by hand-picked insertion order to reproduce that exact shape.

lecture_bst = build_bst([8, 3, 10, 1, 6, 14, 4, 7, 13])


# --- balanced_bst (7 nodes, height 2) — perfectly balanced ---
#
#         4
#        / \
#       2   6
#      / \ / \
#     1  3 5  7
#

balanced_bst = build_bst([4, 2, 6, 1, 3, 5, 7])


# --- degenerate_bst (7 nodes, height 6) — a chain to the right ---
#
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6
#              \
#               7
#
# Same VALUES as balanced_bst — only the insertion order changes.

degenerate_bst = build_bst([1, 2, 3, 4, 5, 6, 7])
