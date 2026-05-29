# M3 — top-K most-liked comments, using a heap.
#
# Instructions for today: INSTRUCTIONS/session_12.md
import heapq

# ─── Step 10 — flatten the tree into one list ─────────────────────────
#
# Same DFS preorder as display(), but append to `result` instead of
# printing. Append `comment`, recurse on each child, return `result`.


def collect_all_comments(comment, result):
    result.append(comment)
    for child in comment.children:
        collect_all_comments(child, result)
    return result


# ─── Step 11 — the K most-liked comments ──────────────────────────────
#
# heapq.nlargest(k, items, key=...) does the work. Rank by likes.


def top_k_comments(comments, k):
    return heapq.nlargest(k, comments, key=lambda comments: comments.likes)


# ─── Step 12 — pretty-print the leaderboard ───────────────────────────
#
# See the target look in session_12.md. f-string alignment helps:
#   f"{author:<12}"  left-align in 12 cols   f"{likes:>3}"  right-align in 3.


def print_leaderboard(top_comments):
    print("=" * 40)
    print("  🏆  TOP 5 HOT COMMENTS THIS WEEK 🏆  ")
    print("=" * 40)

    for rank, c in enumerate(top_comments, start=1):
        print(f' #{rank} {c.author}    {c.likes} ❤️     "{c.text}"')
