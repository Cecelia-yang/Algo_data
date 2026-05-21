# Understanding Binary Search Trees (Part 1)

> One rule, applied everywhere — and suddenly search becomes O(log n) instead of O(n).

---

## What is a BST?

Picture your WeChat contact list with **5,000 people**. Two ways to find someone called Wang Mei:

- An unsorted list of names — you scroll, you scan, you check every entry. Bad day: O(n).
- A sorted array — you binary search. ~13 comparisons for 5,000 names. Good day: O(log n).

The sorted array is fast to read but painful to update. Insert "Wang Xin" and you shift half the array right. Every keystroke in an auto-complete box becomes slow.

A **Binary Search Tree (BST)** is the structure that keeps the sorted order *without* the shifting. It is a binary tree — every node has at most two children — with one extra rule:

> For every node `n`: all values in the **left** subtree are **smaller** than `n.value`, all values in the **right** subtree are **greater**.

```python
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

Look at any node and the rule holds. At 8: left subtree {1, 3, 4, 6, 7} all smaller, right subtree {10, 13, 14} all greater. At 3: left {1} smaller, right {4, 6, 7} greater. Same check at every node.

This property is **recursive**. Every subtree of a BST is itself a BST. That single fact is what makes the recursive code so short.

---

## The BST Property in Detail

The common trap: checking only direct children. The rule is about the **entire subtree**, not the parent-child link alone.

### ❌ The local-only check (wrong):

```python
        8
       / \
      3   10
     / \
    1   12      ← 12 > 3 ✓ locally, but 12 > 8 and lives in 8's LEFT subtree.
```

If you only verify that every left child < parent and every right child > parent, this tree passes. It is **not** a BST. A search for 12 starting from 8 would go left (12 < 8 is false → wait, 12 > 8 → go right), end up at 14, then return "not found" — even though 12 sits in the tree.

### ✅ The recursive check (right):

```python
        8
       / \
      3   10
     / \    \
    1   6    14
```

Every value in the LEFT subtree of 8 (1, 3, 6) is < 8. Every value in the RIGHT subtree (10, 14) is > 8. Recurse the same check at every subtree. All pass. Valid BST.

The take-away: when you eyeball a tree, ask yourself the question at the **root** first — every value in my left subtree must be smaller than me, all the way down — and only then recurse into the children.

---

## Search in Detail

Search uses the property to eliminate half of the remaining tree at every step. At each node, compare the target with `node.value`:

- equal → found, return the node
- smaller → only the LEFT subtree can hold it; the right is impossible
- greater → only the RIGHT subtree can hold it; the left is impossible

Each step throws away an entire subtree. That is why search costs O(h) — the **height** of the tree — instead of O(n).

### Tracing `search(root, 7)` on the lecture tree

| Step | Current node | Compare | Decision |
|---|---|---|---|
| 1 | 8 | 7 < 8 | go LEFT — drop {10, 13, 14} |
| 2 | 3 | 7 > 3 | go RIGHT — drop {1} |
| 3 | 6 | 7 > 6 | go RIGHT — drop {4} |
| 4 | 7 | 7 = 7 | found |

Four comparisons in a tree of nine nodes. Every comparison kills a whole side.

### The relationship to binary search

You wrote `binary_search_iter(lst, target)` in Class 01 with three indices low / mid / high. The same pattern is back, but the "midpoint" is now decided by the **tree's shape**, not by arithmetic. The lecture tree happens to be roughly balanced, so the "midpoint" effectively halves the work — that is why we keep the O(log n) reading.

When the tree is balanced, h ≈ log₂(n) and you get binary-search speed. When the tree is degenerate (think: inserting `[1, 2, 3, 4, 5]` in order — see Class 08), h grows to n and you lose everything. The shape is the contract.

---

## Insert in Detail

Insert is **search that stops at `None`**. Walk down comparing as if you were looking for the value. When you fall off the tree — when the spot you want to follow is `None` — that empty slot is where the new node belongs.

The subtle part is the linking. In Python, the recursive call sees only its own subtree. It cannot reach back to the parent to say "please make me your new left child". So we use a small trick: every call **returns** its (possibly modified) subtree root, and the parent re-attaches.

### ❌ Without re-attaching — the silent bug

```python
def insert_broken(node, value):
    if node is None:
        node = Node(value)            # reassigning the LOCAL name only
        return
    if value < node.value:
        insert_broken(node.left, value)    # result discarded
    else:
        insert_broken(node.right, value)
# The new Node is created and immediately garbage-collected. The tree
# is unchanged. No error is raised. Worst kind of bug — silent.
```

### ✅ With re-attaching — the working idiom

The fix is to write `node.left = insert(node.left, value)` (and the same for the right side). The recursive call returns whatever the modified subtree should look like, and the parent stitches it back in.

Whether the child was `None` (a brand-new Node comes back) or already a real subtree (the same root comes back, with the new value placed somewhere inside it), the line `node.left = ...` works the same. The pattern handles both cases with one line.

Always return `node` at the end of `insert`, so the caller above you can stitch *you* in too. The pattern flows all the way up to the root.

### A worked trace — inserting 7 into the lecture tree

Starting from:

```python
        8
       / \
      3   10
     / \    \
    1   6    14
              /
             13
```

`insert(root, 7)`:

1. At 8: 7 < 8 → recurse on `node.left` (the subtree rooted at 3).
2. At 3: 7 > 3 → recurse on `node.right` (the subtree rooted at 6).
3. At 6: 7 > 6 → recurse on `node.right` (None — empty spot).
4. Base case: return `Node(7)`.
5. Back at 6: `node.right = Node(7)`. Return node 6.
6. Back at 3: `node.right = node 6` (unchanged root, but its subtree has grown). Return node 3.
7. Back at 8: `node.left = node 3`. Return node 8 — the root.

Each level on the way back up does one re-assignment. Most of them are no-ops (the same child as before), but the one at the bottom plants the new node. The "return on the way up" is what lets the planting reach the parent.

###  But why "return and re-attach" the current node ?

A natural question after seeing the worked trace: *why don't we just check if `node.left is None` and create the new node right there, instead of going down into the empty spot and returning it back up?* This "look-ahead" idea is smart — and it does work for most cases. But the standard `node.left = bst_insert(node.left, value)` pattern is preferred for three concrete reasons.

#### 1. The completely empty tree

If the very first root is `None`, you cannot check `node.left` at all — `None.left` raises `AttributeError`. The look-ahead approach needs a special case at the very top just for "the tree is empty". The re-attach approach handles "empty tree" and "empty bottom branch" with the *same* base case — `if node is None: return Node(value)` — and that base case fires whether we are at depth 0 or depth 10.

#### 2. The creation logic stays in one place

With look-ahead, you have to write the `Node(value)` line twice — once for each branch:

```python
# ❌ Look-ahead — creation logic repeated
if value < node.value:
    if node.left is None:
        node.left = Node(value)        # written once
    else:
        # recurse left
        ...
elif value > node.value:
    if node.right is None:
        node.right = Node(value)       # written twice
    else:
        # recurse right
        ...
```

```python
# ✅ Re-attach — creation logic written once
if node is None:
    return Node(value)                 # written ONLY once, at the top
if value < node.value:
    node.left = bst_insert(node.left, value)
elif value > node.value:
    node.right = bst_insert(node.right, value)
return node
```

The re-attach version factors the creation into one spot — the base case — and everything else is the same walk in both branches. Less code, fewer places for a typo to hide.

#### 3. It is the same pattern self-balancing trees need

In this class and the next, we mention AVL and Red-Black trees — BSTs that automatically rebalance after every insert by performing a *rotation* on the affected subtree. After a rotation, the **root of the subtree changes** — the parent that called the function suddenly needs to point at a different node.

The re-attach pattern handles this for free. The recursive call already returns "the new root of this subtree, whatever it now is", and the parent already re-attaches it with `node.left = ...`. Whether the call returned the same root or a rotated one, the parent line does not change.

The look-ahead pattern cannot express this — it never asks the child "what is your new root?", so a rotation has no way to tell the parent to re-link. To support balancing later, you would have to rewrite every insert in the re-attach style anyway. Better to learn the future-proof pattern from the start.

---


## Why Does It Matter?

Imagine you are building the auto-complete box for a Chinese dictionary app. The dictionary has **100,000 words**. Every keystroke triggers a lookup; the user is typing fast, so each lookup must finish in well under a millisecond.

### ❌ Without a BST — sorted array with `bisect.insort`:

```python
words = []              # kept sorted

def add_word(w):
    bisect.insort(words, w)   # O(n) per insert — shifts elements

def lookup(w):
    i = bisect.bisect_left(words, w)
    return i < len(words) and words[i] == w   # O(log n)
```

Lookups are fast — `bisect_left` does the binary search — but every `add_word` becomes painful as the dictionary grows. A dictionary of 100,000 words means **shifting up to 100,000 elements per insertion**. Updating the dictionary in the background freezes the UI.

### ✅ With a BST:

```python
class Dictionary:
    def __init__(self):
        self.root = None
    def add_word(self, w):
        self.root = bst_insert(self.root, w)   # O(log n) on a balanced BST
    def lookup(self, w):
        return bst_search(self.root, w) is not None   # O(log n)
```

Both operations are O(log n) on a balanced BST — about 17 comparisons for 100,000 words, no shifting, no blocking. The user types, the dictionary grows, nothing slows down.

The catch (and the topic of Class 08): the BST must stay balanced. We will see what happens when it does not.

---

## Practical Examples

### Range queries — "all users between ages 18 and 25"

A BST keyed on age lets you walk in-order between two bounds and collect everything in the range. The cost is O(log n + k) where k is the number of matching users. A hash table cannot do this — hashing loses the order.

### A leaderboard with constant updates

Players' scores rise and fall during a match. You want the top-K and you want fast inserts. A BST keyed on score updates a single player's record in O(log n) and reads the K highest by walking the right spine — without re-sorting the full leaderboard.

### Building a sorted list from a stream

Insert each incoming value into a BST. When you need the sorted output, run an inorder traversal. The first value you read is the smallest. No need to call `sorted()` ever — sorting happens incrementally as you insert.

---

## Common Pitfalls

### Pitfall 1: forgetting the re-attach in insert

```python
# ❌ The result is dropped — the tree never grows.
if value < node.value:
    bst_insert(node.left, value)
```

The recursive call returns the new subtree root, but you ignored it. The original `node.left` still points where it pointed before. The new Node is created and garbage-collected. No exception is raised — the test "did insert work?" simply fails next time you search.

```python
# ✅ Capture the result back into the parent.
if value < node.value:
    node.left = bst_insert(node.left, value)
```

### Pitfall 2: forgetting the equality check in search

The "not found" base case (`node is None`) is easy to remember. The "found" base case (`node.value == target`) is the one that gets skipped — students jump straight to the comparison and the recursion. Without it, a search for a value sitting at a node will keep descending past it, eventually fall off the tree, and return `None` for a value that is actually present.

The rule to lock in muscle memory: **two base cases first, comparison after.** Empty subtree → return None. Match → return the node. Only then do you compare and pick a side.

### Pitfall 3: inserting duplicates without a policy

Real data has duplicates. The lecture version does nothing — `value == node.value` returns the unchanged node. Pick one of three policies *before* writing the code:

- Drop duplicates silently — the simplest. Use it unless you have a reason not to.
- Allow duplicates by routing them all to the right (or all to the left). The tree gains a tilt, but the recursive code still works.
- Reject duplicates with an exception. Useful when "I tried to add a key that already exists" is a bug.

No policy is wrong. Picking one is the rule.

### Pitfall 4: inserting in sorted order produces a degenerate tree

```python
# Insert [1, 2, 3, 4, 5] into an empty BST →
1
 \
  2
   \
    3
     \
      4
       \
        5
```

The tree is technically a valid BST, but every node has exactly one child. The "height" is 4 for 5 nodes. Search is O(n). You lost the entire point of the data structure.

The cause: insertion order. If your input is already sorted (or reverse sorted), you build a chain. Class 08 covers the fix — self-balancing BSTs that rotate the tree back into shape after every insert.

---

## Summary

| Concept | What it does | When to use | Key rule |
|---------|--------------|-------------|----------|
| BST property | Left subtree < node < right subtree, recursively | Whenever you need sorted lookup + fast inserts | Holds for every subtree, not just direct children |
| Recursive search | Compare target, go left or right | Find a value in a BST | Two base cases, then ONE comparison |
| Recursive insert | Search until a `None` spot, plant the new node | Add a value to a BST | Always `node.left = insert(node.left, v)` and return node |
| Complexity O(h) | Cost depends on tree height | Estimating performance | Balanced → O(log n); degenerate → O(n) |
| Inorder = sorted | Inorder walk on a BST yields sorted values | Reading the tree in order | Direct consequence of the BST property |
