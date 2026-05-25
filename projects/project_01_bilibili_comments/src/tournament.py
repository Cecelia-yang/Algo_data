# M4 (BONUS) — a knockout tournament between the top 8 comments.
#
# Instructions: INSTRUCTIONS/session_12.md (the BONUS section at the bottom).
#
# The bracket is a BINARY tree: each Match has 2 inputs (its sub-matches)
# and 1 output (the winner). You resolve children before parents → postorder.


class Match:
    """A node in the bracket: a winner comment + two sub-matches."""

    def __init__(self, comment=None):
        pass    # TODO: comment, plus left = None and right = None


# ─── Step 13 — build the bracket: 8 leaves → 4 → 2 → 1 ────────────────
#
# Start with 8 leaf matches (each holding one comment), pair them up into
# 4 matches, then 2, then 1. Return the root (the final match).

def build_bracket(top_8):
    pass    # TODO


# ─── Step 14 — play the tournament (postorder) ────────────────────────
#
# Base case: a leaf (match.comment is not None) → return that comment.
# Else: resolve left and right, the higher-liked comment wins, store it in
#       match.comment and return it.

def play_tournament(match):
    pass    # TODO


# ─── Step 15 — display the bracket ────────────────────────────────────
#
# BFS the tree level by level and print each round (see session_12.md).

def print_bracket(final_match):
    pass    # TODO
