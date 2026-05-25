# Understanding BST Deletion and Tree Shape

> Deleting is harder than inserting — and a lazy BST silently turns into a linked list.

---

## What Makes Deletion Hard?

Insertion in a BST always lands on <mark style="background: #FF5582A6;">the same kind of spot</mark>: a `None`. You walk down, you find an empty slot, you plant the new node. Done. Every insertion is fundamentally the same operation.

Deletion is not like that. When you remove a node, you have to **fill the hole** — and the way you fill it depends on how the node was connected.

- A **leaf** is easy. You unplug it and nothing else needs to move.
- A node with **one child** is also easy. The only child takes the parent's place — same as removing one wagon in the middle of a train: the cars on either side reconnect.
- A node with **two children** is the awkward one. Promoting the left child leaves the right subtree orphaned. Promoting the right child leaves the left subtree orphaned. Neither move keeps the tree intact.

The whole content of Class 08 is: how to fill that hole in the two-children case without breaking the BST property.

---

## The Three Cases in Detail

### Case 1 — leaf

```python
    5
   / \
  3   8
 /
1            ← delete(1): just disconnect it
```

The node has no children. Set the parent's pointer to `None`. The BST property cannot break — we removed a value, no remaining value moved.

### Case 2 — one child

```python
    5                       5
   / \                     / \
  3   8                   3   10
       \      → delete(8)  
        10
```

The node has exactly one child (left OR right, never both). Replace the node with its only child. The child "jumps up" one level — and because it was already in the correct half of the tree (every value in 8's right subtree is greater than 5; the survivor 10 is one of those values), the BST property still holds.

### Case 3 — two children

```python
        5
       / \
      3   8        ← delete(5): cannot pick a side
         / \
        6   10
```

Promoting 3 would orphan {6, 8, 10}. Promoting 8 would push 6 below 5 — wrong side. Either move breaks the tree.

The trick is to **NOT move a subtree at all**. Instead, find a value somewhere in the tree that can take 5's place without changing the structure — and copy that value into the node, leaving the connections untouched.

That value is the **inorder successor**.

---

## The Inorder Successor — Why It Works

The **inorder successor** of a node `n` is the **smallest value larger than `n.value`**. It is the next value you would print if you walked the tree in inorder.

In a BST, that successor always lives at one specific spot: the **leftmost node of `n`'s right subtree**. To find it, go right once (now you are in the "all-greater" half) and then keep going left until you can't (the leftmost is the smallest of that half).

Walk this on the lecture tree:

```python
        8
       / \
      3   10
         / \
        6   14
```

To find the inorder successor of 8: right → 10, left → 6. The successor is 6.

Why is 6 safe to copy into 8's position?
- 6 is **greater than every value in 8's left subtree** (because it lives in 8's right subtree, and the BST property at 8 already guaranteed that).
- 6 is **smaller than every value in 8's right subtree minus itself** (because 6 was the *smallest* value in that subtree).

So when we replace 8 with 6, every other value is still on the correct side of the new node 6. The property holds.

After the value copy, the OLD 6 is now a duplicate. We delete the original 6 from the right subtree. By construction, 6 was a **leftmost** node — so it has no left child. It is either case 1 (leaf) or case 2 (one right child). The recursive delete on it terminates cleanly.

### ❌ The wrong shortcut — promote one child

```python
        5
       / \
      3   8
         /
        6     ← if we delete 5 by promoting 8, what happens to 3?
```

You cannot just say `node = node.right`. The left subtree, 3, has nowhere to attach. You would have to re-insert 3 into the new tree (O(n) walk) or graft it as the leftmost descendant of 8. Both are messier than the inorder successor trick — and both can degenerate the tree shape.

### ✅ The clean fix — copy the inorder successor's value

```python
# At the node we want to delete:
successor = find_min(node.right)
node.value = successor.value
node.right = delete(node.right, successor.value)
```

Two things to notice:

1. We do **not** remove the original node from the tree. We just change its `.value`. Every pointer in the tree stays valid.
2. The recursive `delete(node.right, successor.value)` is guaranteed to terminate in case 1 or case 2 — the leftmost descendant cannot have a left child.

---

## Why Does It Matter?

Imagine a music app where each song is a node in a BST keyed on play count. Users add songs, remove songs, and re-rank in real time. A delete that mis-handles the two-children case could:

- **Lose songs** — orphaning the right subtree silently. Users complain that random tracks "disappear" from their library.
- **Break the BST property** — inserting future songs lands them in the wrong half of the tree, and subsequent searches return "not found" for songs that ARE in the tree. The most painful bug to debug: every search is "correct" individually, but the tree is structurally wrong.

The inorder-successor trick avoids both. The tree shape remains a valid BST after every delete, no matter which case fires.

---

## The Dark Side — Degenerate BSTs

Watch what happens when we insert sorted values into an empty BST:

```python
for v in [1, 2, 3, 4, 5, 6, 7]:
    root = bst_insert(root, v)
```

Each insert goes RIGHT (everything is larger than what we already have):

```
1 → 2 → 3 → 4 → 5 → 6 → 7
```

The "tree" is a chain. Height = 6 for 7 nodes. Search is O(n). Insert is O(n). Delete is O(n). Every BST advantage is gone — we built a singly-linked list with the wrong API.

### ❌ Without watching insertion order

```python
# Data arrives sorted from a file:
for line in open("scores_sorted.txt"):
    bst_insert(root, int(line))
# Result: a chain. Search degrades to O(n). On 1M scores, every lookup
# now scans up to 1M nodes — the dataset just became unusable.
```

### ✅ With awareness of the shape

```python
# Shuffle first, OR use a self-balancing BST (next slide):
import random
data = list(map(int, open("scores_sorted.txt")))
random.shuffle(data)
for x in data:
    bst_insert(root, x)
# Random insertion order → roughly balanced tree → O(log n) per op.
```

The shuffle works as a defensive measure, but it does not guarantee balance — bad luck can still produce a tall tree. For real systems, we use **self-balancing BSTs**.

---

## Self-Balancing BSTs (Concept Only)

A self-balancing BST automatically restructures itself after every insert and delete to keep its height close to log n. The two most common:

- **AVL tree** — strict height invariant (every node's two subtrees differ in height by at most 1). Rebalances aggressively. Used when reads dominate writes.
- **Red-Black tree** — looser invariant, faster writes. Used inside `java.util.TreeMap`, the Linux kernel scheduler, the C++ `std::map`, and Python's `sortedcontainers` library.

You will not implement either in this semester. The take-away is:

> A plain BST is a **teaching structure**. Real systems use self-balancing variants because the cost of a single degenerate operation can crash a service that depends on O(log n).

If you ever reach a real production system and you find yourself reaching for a plain BST, stop and ask: *what guarantees my data stays mixed enough to keep the tree shallow?* If you cannot answer, you want a self-balancing variant.

---

## Practical Examples

### Range-based queries that handle deletions

A taxi-dispatch system keeps drivers in a BST keyed by ID. Drivers log on and off constantly. A plain BST with insert+delete answers "give me the driver with this ID" in O(log n) — as long as logoffs are spread out enough to keep the tree balanced. If thousands of drivers log off in the same minute (shift change), the tree thins on one side; a self-balancing variant restores the shape automatically.

### A unique-prefix dictionary

Hospital records are stored by patient code, where codes are issued sequentially. If you build the index with a plain BST, every new record extends the right spine of the tree — and after a year of operation, the index is a chain. Either pre-shuffle the codes at insertion time, or use an AVL/Red-Black tree from the start.

### A scheduling system you remove tasks from

A task scheduler keeps pending jobs in a BST keyed on deadline. Jobs are added (insert) and removed when they complete (delete). If completions cluster in the leftmost part of the tree (early deadlines clear first), a plain BST goes lop-sided fast. A heap (next class!) is actually a better fit for this specific shape of workload.

---

## Common Pitfalls

### Pitfall 1: forgetting to re-attach the result of delete

```python
# ❌ The result is dropped — the node is never removed.
if value < node.value:
    bst_delete(node.left, value)
```

Same trap as `bst_insert` in Class 07. Capture the result back into the parent: `node.left = bst_delete(node.left, value)`.

### Pitfall 2: deleting the wrong node in the two-children case

```python
# ❌ Copy successor value but forget the second delete:
successor = find_min(node.right)
node.value = successor.value
# Tree now has TWO nodes with successor.value — the property is broken.
```

After the value copy, the original successor node is still in the right subtree as a duplicate. Recursively delete it: `node.right = bst_delete(node.right, successor.value)`. The recursive call hits case 1 or case 2 — never case 3 again — because a leftmost node cannot have a left child.

### Pitfall 3: assuming the successor exists

```python
# ❌ Crashes when node.right is None:
successor = find_min(node.right)
node.value = successor.value
```

If you reach this line in the two-children branch, you already know `node.right is not None` (that is what "two children" means). Still — if you ever consider re-using the successor strategy elsewhere, guard against `None`.

### Pitfall 4: trusting the tree to stay balanced on its own

```python
# ❌ Code that "works" in tests but breaks in production:
for x in user_input:        # user_input happens to be sorted
    root = bst_insert(root, x)
```

A plain BST is at the mercy of the insertion order. If your inputs are ever sorted, you build a chain. Either guarantee a mixed insertion order, or reach for a self-balancing structure.

---

## Summary

| Concept | What it does | When to use | Key rule |
|---------|--------------|-------------|----------|
| Case 1 — leaf | Return `None` from the recursive call | When the target has no children | Disconnect, nothing else moves |
| Case 2 — one child | Return the only child | When the target has exactly one child | Child jumps up to take the slot |
| Case 3 — two children | Copy inorder successor's value, then delete it from the right subtree | When the target has both children | Value moves, structure does not |
| Inorder successor | Smallest value in the right subtree | To fill the hole in case 3 | Go right once, then left until you can't |
| Degenerate BST | Chain-shaped tree from sorted inserts | Diagnose-only — never want it | Shape depends on insertion order |
| Self-balancing BST | Rebalances after every insert / delete | Production systems with frequent updates | AVL, Red-Black — built on top of the same recursion |
