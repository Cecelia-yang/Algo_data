# M1 — the Comment class, build the tree, display it.
#
# Instructions for today: INSTRUCTIONS/session_10.md
#
# Fill in the bodies marked TODO. Do NOT rename the class, the functions
# or their parameters — main.py imports them by name.


class Comment:
    """One Bilibili comment. It can have any number of replies (children)."""

    def __init__(self, id, author, text, likes):
        pass    # TODO: store id, author, text, likes — and start children = []

    def add_reply(self, comment):
        pass    # TODO: append `comment` to this comment's children


# ─── Step 4 — build the tree from one JSON dict (recursive) ───────────
#
# Base case:      a dict whose "replies" is []  → just build the Comment.
# Inductive case: build the Comment, then for each reply dict, recursively
#                 build_tree(...) it and add_reply(...) the result.

def build_tree(comment_dict):

    pass    # TODO


# ─── Step 5 — display the tree (DFS preorder, 2-space indent) ─────────
#
# indent = "  " * depth   →   print THIS comment, then each child at depth + 1.
# Target line: "[#1] Alice (98 ❤️): Great video!"

def display(comment, depth=0):
    pass    # TODO


# ─── Step 6 (extra) — find a comment by id, or return None ────────────

def find_by_id(comment, target_id):
    pass    # TODO
