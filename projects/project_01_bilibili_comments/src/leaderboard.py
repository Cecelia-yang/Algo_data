# M3 — top-K most-liked comments, using a heap.
#
# Instructions for today: INSTRUCTIONS/session_12.md

import heapq


# ─── Step 10 — flatten the tree into one list ─────────────────────────
#
# Same DFS preorder as display(), but append to `result` instead of
# printing. Append `comment`, recurse on each child, return `result`.

def collect_all_comments(comment, result):
    pass    # TODO


# ─── Step 11 — the K most-liked comments ──────────────────────────────
#
# heapq.nlargest(k, items, key=...) does the work. Rank by likes.

def top_k_comments(comments, k):
    pass    # TODO


# ─── Step 12 — pretty-print the leaderboard ───────────────────────────
#
# See the target look in session_12.md. f-string alignment helps:
#   f"{author:<12}"  left-align in 12 cols   f"{likes:>3}"  right-align in 3.

def print_leaderboard(top_comments):
    pass    # TODO
