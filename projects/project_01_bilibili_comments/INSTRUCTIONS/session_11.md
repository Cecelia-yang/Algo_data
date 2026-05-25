# Session 11 — Milestone 2: Explore the tree

*Today: write three recursive functions to explore the tree. All three are short. All three follow the same recursion pattern.*

---

## Recap from session 10

You should have:
- `Comment` class
- `build_tree(comment_dict)` — recursive
- `display(comment, depth=0)`

Fix M1 first if broken.

---

## What you do today

| Step | What | Where |
|------|------|-------|
| 6 | `find_by_id` *(if not done last time)* | `src/comment.py` |
| 7 | `count_total_replies(comment)` | `src/explorer.py` |
| 8 | `deepest_thread(comment)` | `src/explorer.py` |
| 9 | `delete_comment(parent, target_id)` | `src/explorer.py` |

> **If steps 7, 8, 9 work, you are done. Push it.**

All three go in a new file: `src/explorer.py`.

---

## Step 7 — `count_total_replies(comment)`

Count **all** replies under a comment — direct, indirect, all the way down. The comment itself does NOT count.

Expected results (on the session 10 example tree):

| Call | Result |
|------|--------|
| `count_total_replies(Alice)` | 6 |
| `count_total_replies(Bob)` | 1 |
| `count_total_replies(Charlie)` | 0 |

Recursion structure:
- **Base case**: no children → return 0
- **Inductive case**: for each child, add `1 + count_total_replies(child)`

---

## Step 8 — `deepest_thread(comment)`

Maximum depth of any thread under a comment. A leaf is depth 0. A comment with one direct reply is depth 1.

| Call | Result |
|------|--------|
| `deepest_thread(Alice)` | 2 |
| `deepest_thread(Bob)` | 1 |
| `deepest_thread(Charlie)` | 0 |

Recursion structure:
- **Base case**: no children → return 0
- **Inductive case**: one more than the **deepest** of its children — i.e. `1 +` the largest `deepest_thread(child)` among them. (The `max(... for ...)` tip just below is exactly the tool for this.)

Python tip — `max()` works with a generator. Example:

```python
max(len(word) for word in ["hi", "hello", "hey"])   # → 5
```

Same idiom: `max(f(x) for x in collection)`.

---

## Step 9 — `delete_comment(parent, target_id)`

Remove the comment with `target_id` from the tree. The whole sub-thread goes with it (replies of a deleted comment have no meaning).

| Operation | BST delete | N-ary subtree delete |
|---|---|---|
| Cases to handle | 3 (leaf / 1 child / 2 children) | 1 |
| Successor lookup needed | Yes | No |
| Reconnect children | Yes | No |
| Tree structure after | Restored, possibly rebalanced | Subtree removed |

Python tip — two ways to remove from a list:

```python
my_list.remove(item)   # remove the first occurrence of `item`
my_list.pop(i)         # remove and return the element at index `i`
```

Algorithm:
- Walk the tree looking for a child of `parent` whose `id` matches.
- When found → remove it from `parent.children`.
- If not at this level → recurse into each child.

Hint: have the function return a boolean (`True` if deleted, `False` if not) so you can stop searching once found.

---

## Debug pattern

```
-----step 7: count_total_replies-----
Alice's thread: 6 replies

-----step 8: deepest_thread-----
Alice: 2 levels

-----step 9: delete_comment-----
Tree after deleting #5:
[indented tree, comment #5 gone]
```

---

## The recursion pattern

All three functions share the same shape:

```
function f(node):
    if node has no children:
        return base_value
    combine results of f(child) for each child
```

Trust the recursion. Don't think about depth manually.

---

## Done for today ✅

```bash
git commit -m "M2: count_total_replies, deepest_thread, delete_comment"
git push
```

Next session: heap-based leaderboard. Optional: tournament bracket.
