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

**Guided skeleton — `count_total_replies`**

```python
def count_total_replies(comment):

    # ① A running total for everything under THIS comment.
    total = ???

    # ② Each child counts as 1, PLUS everything under that child.
    #    (this line is the whole trick)
    for ??? in comment.???:
        total += 1 + ????

    return ???
```

🔍 **The recursive line, explained**
- `1` is the child itself; `count_total_replies(child)` is all of *its* replies. Add both for every child and you've counted the entire sub-tree. A leaf has an empty `children` list → the loop never runs → `total` stays `0`. No `if` needed.

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

**Guided skeleton — `deepest_thread`**

```python
def deepest_thread(comment):

    # ① Base case: a leaf has no children → depth 0.
    if not comment.???:
        return ???

    # ② Otherwise: 1 level (these children) + the deepest child below.
    #    Reuse the max(... for ...) idiom from just above.
    return 1 + max(??? for child in comment.???)
```

🔍 **The recursive line, explained**
- The `???` inside `max(...)` is the recursive call on each child; `max(...)` keeps the deepest; `1 +` adds the step from `comment` down to it. The `(... for ...)` is a *generator* — `max` reads the values one by one, no list built.

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

**Guided skeleton — `delete_comment`** (the hardest of the three — two phases)

```python
def delete_comment(parent, target_id):

    # ── Phase 1: is the target a DIRECT child of parent? ──
    # enumerate gives the position i AND the child, so you can pop(i).
    for i, child in enumerate(parent.children):
        if child.??? == ???:
            parent.children.pop(i)
            return ???

    # ── Phase 2: not here → look INSIDE each child (recurse). ──
    for child in parent.children:
        if delete_comment(child, target_id):
            return ???

    # ── Searched the whole sub-tree, never found it. ──
    return ???
```

🔍 **Why two phases**
- **Phase 1** scans `parent`'s *own* children, because you can only remove a node from the list that holds it. `enumerate` gives the index so `pop(i)` removes exactly that one — its whole sub-thread goes with it.
- **Phase 2**: if it wasn't a direct child, the target is deeper → recurse. The inner call returns `True` if it deleted something below; pass that result straight up. The very last `return` means *"not in this sub-tree"* (so: `False`).

🪜 **Trace** — `delete_comment(Alice, 5)`  (#5 = Eve, a child of David):

```
Alice → Phase 1: kids [Bob, David, Grace], no #5 → Phase 2: recurse
   David → Phase 1: kids [Eve#5, Frank] → match! pop → True
   → True bubbles up to Alice → True
```

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
