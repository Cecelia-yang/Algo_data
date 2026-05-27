"""Project 1 — Bilibili Comment Tree.

main.py only IMPORTS and ORCHESTRATES. The real work lives in src/.
Build it up session by session, uncommenting each block as you go:

    Session 10 (M1) → src/comment.py
    Session 11 (M2) → src/explorer.py
    Session 12 (M3) → src/leaderboard.py   (+ bonus M4 → src/tournament.py)

Run it from THIS folder:   python3 main.py
"""

import os
import json

from src.comment import Comment, build_tree, display, find_by_id
from src.explorer import count_total_replies, deepest_thread, delete_comment
from src.leaderboard import collect_all_comments, top_k_comments, print_leaderboard
from src.tournament import Match, build_bracket, play_tournament, print_bracket

# Path to the dataset — works no matter which folder you launch python from.
HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(HERE, "data", "comments.json")


# ══════════════════════════════════════════════════════════════════════
# M1 — build the tree and display it   (Session 10)
# ══════════════════════════════════════════════════════════════════════
print("----- step 1: load data -----")    
# TODO: open DATA_PATH, json.load it, keep the list of top-level dicts.

# load the JSON file into a Python dict "data"
with open(DATA_PATH, "r", encoding = "utf-8") as f:
    data = json.load(f)
raw_comments = data["comments"]
print(f"loaded {len(raw_comments)} top-level comments")
# raw_comments = data["comments"]
# print(f"Loaded {len(raw_comments)} top-level comments")

print("\n----- steps 4-5: build + display the trees -----")
# TODO: build one tree per top-level dict, then display each root.
# roots = [build_tree(c) for c in raw_comments]
# for root in roots:
#     display(root)
roots = [build_tree(c) for c in raw_comments]
for root in roots:
    display(root)

# ══════════════════════════════════════════════════════════════════════
# M2 — explore the tree   (Session 11)
# ══════════════════════════════════════════════════════════════════════
# print("\n----- step 7: count_total_replies -----")
# print(count_total_replies(roots[0]), "replies under comment #1")
#
# print("\n----- step 8: deepest_thread -----")
# print(deepest_thread(roots[0]), "levels deep under comment #1")
#
# print("\n----- step 9: delete_comment (#5) -----")
# delete_comment(roots[0], 5)
# display(roots[0])


# ══════════════════════════════════════════════════════════════════════
# M3 — leaderboard   (Session 12)
# ══════════════════════════════════════════════════════════════════════
# print("\n----- steps 10-12: leaderboard -----")
# all_comments = []
# for root in roots:
#     collect_all_comments(root, all_comments)
# top5 = top_k_comments(all_comments, 5)
# print_leaderboard(top5)


# ══════════════════════════════════════════════════════════════════════
# M4 (BONUS) — tournament   (Session 12)
# ══════════════════════════════════════════════════════════════════════
# print("\n----- steps 13-15: tournament -----")
# top8 = top_k_comments(all_comments, 8)
# final = build_bracket(top8)
# play_tournament(final)
# print_bracket(final)


print("\n✅ Imports OK. Start with Session 10 (M1) in src/comment.py.")
