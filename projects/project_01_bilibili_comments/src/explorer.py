# M2 — explore the tree. Three short recursive functions.
#
# Instructions for today: INSTRUCTIONS/session_11.md
#
# They all share the same shape: base case on a leaf, then combine the
# results of the children. Trust the recursion.


# ─── Step 7 — count every reply under `comment` (direct + indirect) ───
#
# The comment itself does NOT count.
# Base case: no children → 0.
# Inductive: for each child, add 1 + count_total_replies(child).


def count_total_replies(comment):
    total = 0
    for child in comment.children:
        total += 1 + count_total_replies(child)

    return total


# ─── Step 8 — deepest level under `comment` ───────────────────────────
#
# A leaf is depth 0. One direct reply is depth 1.
# Base case: no children → 0.
# Inductive: 1 + max(deepest_thread(c) for c in children).


def deepest_thread(comment):
    if not comment.children:
        return 0
    return 1 + max(deepest_thread(child) for child in comment.children)


# ─── Step 9 — delete the comment with `target_id` (whole sub-thread) ──
#
# Walk `parent.children`: if one matches target_id → remove it.
# Otherwise recurse into each child.
# Return True if something was deleted, False otherwise.


def delete_comment(parent, target_id):
    pass  # TODO
