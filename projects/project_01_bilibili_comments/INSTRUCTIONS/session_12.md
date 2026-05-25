# Session 12 — Milestone 3 + Bonus M4

*Today: heap-based leaderboard (mandatory). If you finish with time to spare, a knockout tournament between the top 8 (bonus). Final session of project 1.*

---

## Recap from session 11

You should have `count_total_replies`, `deepest_thread`, `delete_comment`. Fix them first if broken.

---

## What you do today

### Mandatory — M3

| Step | What | Where |
|------|------|-------|
| 10 | Collect all comments in a flat list | `src/leaderboard.py` |
| 11 | Top-K with `heapq` | `src/leaderboard.py` |
| 12 | Pretty-print the leaderboard | `src/leaderboard.py` |

### Bonus — M4 *(only if M3 done)*

| Step | What | Where |
|------|------|-------|
| 13 | Build a tournament bracket (binary tree) | `src/tournament.py` |
| 14 | Simulate matches (postorder) | `src/tournament.py` |
| 15 | Display the bracket | `src/tournament.py` |

> **M3 done = project complete. M4 = +10% (cannot go beyond 100%).**

---

## Step 10 — Flatten the tree

You need all comments in one flat list, so you can rank them.

`collect_all_comments(comment, result)`:
- append `comment` to `result`
- for each child → recurse with the same `result`
- return `result`

Same DFS preorder as `display()`, but appending to a list instead of printing.

---

## Step 11 — Top-K with `heapq`

You have ~25 comments and want the top K by likes. Write **`top_k_comments(comments, k)`** — it returns the K most-liked comments.

| Approach | Complexity | Tool |
|---|---|---|
| Sort all, slice | `O(n log n)` | `sorted(...)` |
| **Heap-based top-K** | `O(n log k)` | `heapq.nlargest(...)` |

`heapq.nlargest` does the work for you. Generic example:

```python
import heapq

words = ["hi", "hello", "hey", "wow", "amazing"]
top_3 = heapq.nlargest(3, words, key=len)
# → ['amazing', 'hello', 'hey']  (the 3 longest words)
```

The `key=` argument tells `heapq` which property to compare. You pass any function — `len`, or a `lambda`. Adapt this to rank comments by their `likes`.

For practice with the heap data structure (session 9), you can also do it manually: maintain a min-heap of size K, push when not full, replace `heap[0]` when a new item beats it.

---

## Step 12 — Pretty leaderboard

Write **`print_leaderboard(top_comments)`**. This is the exact ranking for `comments.json` (your formatting may differ — the order and the numbers won't):

```
========================================
   🏆  TOP 5 HOT COMMENTS THIS WEEK 🏆
========================================
 #1  Alice         98 ❤️  "Great video!"
 #2  Hua Mei       87 ❤️  "Best episode ever! The studio outdid themselves 🔥"
 #3  Wang Lei      54 ❤️  "Better than the last season, no cap"
 #4  Mei Lin       41 ❤️  "Who else is here after the trailer dropped?"
 #5  Lin Xiao      34 ❤️  "Right?? That fight scene 😭"
========================================
```

Python tip — f-string alignment:

```python
print(f"{'Hello':<10}|")   # → "Hello     |"   (left-align in 10 chars)
print(f"{42:>5}|")         # → "   42|"        (right-align in 5 chars)
```

---

## ✅ M3 complete

This is your minimum-viable project. Push:

```bash
git commit -m "M3: top-K hot comments leaderboard"
git push
```

If you're tired, stop here. Otherwise, keep going for the bonus.

---

# 🏆 BONUS — M4: Tournament Bracket

Take the top 8 from M3. Run a knockout: 8 → 4 → 2 → 1.

```
ROUND OF 8         SEMIS          FINAL         CHAMPION

#1 Alice    ─┐
             ├─→ ??? ─┐
#8 Yu Qing  ─┘        │
                      ├─→ ??? ─┐
#4 Mei Lin  ─┐        │        │
             ├─→ ??? ─┘        │
#5 Lin Xiao ─┘                 ├─→ 🏆
                               │
#2 Hua Mei  ─┐                 │
             ├─→ ??? ─┐        │
#7 Li Hua   ─┘        │        │
                      ├─→ ??? ─┘
#3 Wang Lei ─┐        │
             ├─→ ??? ─┘
#6 Su Yan   ─┘
```

The bracket is a **binary tree**: each match has 2 inputs (the players) and 1 output (the winner). To compute the champion, you must resolve children before parents → **postorder** (session 6).

---

## Step 13 — Build the bracket

`Match` class skeleton:

```python
class Match:
    def __init__(self, comment=None):
        ...
```

A `Match` holds:
- the comment that "won" this match (filled at leaves from the start, or assigned after the match is played)
- references to its two sub-matches (`None` for a leaf)

`build_bracket(top_8)`:
- start with 8 leaf matches, each holding one comment
- pair them up into 4 quarter-final matches
- pair those into 2 semis
- pair those into 1 final
- return the root (the final match)

---

## Step 14 — Simulate matches (postorder)

`play_tournament(match)`:
- **base case**: leaf (`match.comment is not None`) → return that comment
- **inductive case**:
  - `winner_left = play_tournament(match.left)`
  - `winner_right = play_tournament(match.right)`
  - decide the winner (higher likes wins, or add randomness for fun)
  - store winner in `match.comment` and return it

This is **postorder**: children first, then this node.

| Traversal | Order | Used in this project |
|---|---|---|
| **preorder** | this node → children | `display()`, `collect_all_comments()` |
| **postorder** | children → this node | `play_tournament()` |
| **BFS** | level by level | bracket display *(step 15)* |

For an upset chance, the `random` module gives you a float in `[0, 1)`:

```python
import random
if random.random() < 0.8:
    ...
```

---

## Step 15 — Display the bracket

Write **`print_bracket(final_match)`**. Example output (M4 is open-ended — your exact matchups depend on how you seed the bracket and whether you add randomness):

```
========================================
       🏆  COMMENT TOURNAMENT  🏆
========================================

ROUND OF 8:
  Alice (98)      vs Yu Qing (21)    → Alice wins!
  Mei Lin (41)    vs Lin Xiao (34)   → Mei Lin wins!
  Hua Mei (87)    vs Li Hua (22)     → Hua Mei wins!
  Wang Lei (54)   vs Su Yan (29)     → Wang Lei wins!

SEMIS:
  Alice (98)      vs Mei Lin (41)    → Alice wins!
  Hua Mei (87)    vs Wang Lei (54)   → Hua Mei wins!

FINAL:
  Alice (98)      vs Hua Mei (87)    → Alice wins!

🏆 CHAMPION: Alice — "Great video!" (98 ❤️)
```

Hint: BFS the tree level by level (session 6) and group matches by round.

---

## Final push 🚀

```bash
git commit -m "M3 done + M4 bonus: tournament bracket"
git push
```

**Submission deadline: saturday May 30, 11:59pm** Make sure:
- All code on your Gitee branch (e.g. <your_student_id>) in `projects/project_01_bilibili_comments/`
- `main.py` runs end-to-end
- A short `README.md` in your folder describing your work

---

## What you used in this project

- N-ary tree (custom class)
- Binary tree *(bonus)*
- Recursion (a lot of it)
- DFS preorder, postorder, BFS
- Heap (`heapq`)

Next class: mid-term exam.
