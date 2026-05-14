# Understanding Tree Traversals

> Four ways to visit every node of a tree. Three of them are the same function with one line moved. The fourth uses a queue.

---

## What is a Traversal?

You have a binary tree on screen. You want to do something to every node — print its value, save it to a file, render it on a UI, count something. To do that, you need a rule for **the order in which you visit the nodes**. That rule is a **traversal**.

A linked list has only one traversal: walk from head to tail. A tree has many. The order matters because different orders solve different problems. Reading a Binary Search Tree in **inorder** gives the values sorted. Computing a folder's size needs **postorder** (the children before the parent). Saving a tree to a file uses **preorder** (the parent before the children). Finding the shortest path uses **BFS** (level by level).

```python
def preorder(node):
    if node is None:
        return
    print(node.value)
    preorder(node.left)
    preorder(node.right)
```

That four-line skeleton is the foundation of three of the four traversals. The fourth, BFS, uses a queue and a loop instead.

---

## DFS — Depth-First, Three Twins

**Depth-first** means: when you reach a node, you go DEEP into one branch before looking at the others. You only come back up after a whole subtree is done. Recursion does this for free, because Python's call stack already behaves like a stack: the last call placed is the first call processed.

At each node, you do three things — **visit** (print, append, mutate), **recurse left**, **recurse right**. The DFS family is just three different orderings of those three actions.

### ❌ Visiting the wrong slot:

```python
def broken(node):
    if node is None:
        return
    broken(node.left)
    broken(node.right)
    print(node.value)               # accidentally postorder
# Author thought they wrote preorder. Output is reversed in surprising ways.
```

### ✅ Picking the slot deliberately:

```python
def preorder(node):
    if node is None: return
    print(node.value)               # visit BEFORE descending
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None: return
    inorder(node.left)
    print(node.value)               # visit BETWEEN the two recursions
    inorder(node.right)

def postorder(node):
    if node is None: return
    postorder(node.left)
    postorder(node.right)
    print(node.value)               # visit AFTER both recursions
```

The skeleton is identical. The two recursive calls are identical. **Only the position of the visit changes.** That single line decides whether the parent is processed before, between, or after its children.

### Tracing on the reference tree

For the rest of the note, we'll use this tree:

```
        1
       / \
      2   3
     / \
    4   5
```

| Traversal | Output | Mental model |
|---|---|---|
| Preorder | 1, 2, 4, 5, 3 | Print, then go left, then go right |
| Inorder | 4, 2, 5, 1, 3 | Go all the way left, print, go right |
| Postorder | 4, 5, 2, 3, 1 | Process the children first, parent last |

The five values come out in three different orders. Same tree, same recursion, different slot for `print`.

---

## BFS — Breadth-First, with a Queue

**Breadth-first** means: visit the tree level by level. Root first, then all its direct children, then all the grandchildren. On our reference tree → output: **1, 2, 3, 4, 5**.

DFS works naturally with recursion because the call stack IS a stack — perfect for "go deep, then come back". BFS needs the opposite behavior: process the **oldest** pending node first, not the newest. That's the definition of a **queue (FIFO — First In, First Out)**, and that's why we bring back the `deque` from Class 02.

### ❌ Trying BFS with recursion:

```python
def bfs_attempt(node):                # this won't work
    if node is None:
        return
    print(node.value)
    bfs_attempt(node.left)
    bfs_attempt(node.right)
# This is preorder, NOT BFS. Recursion is LIFO. We need FIFO.
```

### ✅ BFS with a deque:

```python
from collections import deque

def bfs(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()        # OLDEST waiting node
        print(node.value)
        if node.left is not None:
            queue.append(node.left)   # children go to the END
        if node.right is not None:
            queue.append(node.right)
```

Two operations make BFS work:
- `popleft()` — removes from the FRONT (the oldest waiting node).
- `append(child)` — adds to the END.

Both are O(1) on a `deque`. If you used a `list` and called `lst.pop(0)` instead, every pop would shift every remaining element — O(n) per pop, O(n²) total. The whole reason `deque` exists is to make this efficient.

### Tracing BFS step by step

Starting with `queue = deque([1])`:

1. Pop 1, print 1, enqueue children → `[2, 3]`
2. Pop 2, print 2, enqueue children → `[3, 4, 5]`
3. Pop 3, print 3, no children → `[4, 5]`
4. Pop 4, print 4, no children → `[5]`
5. Pop 5, print 5, no children → `[]`
6. Loop ends.

Output: 1, 2, 3, 4, 5. Exactly level by level. Notice that when a node is popped, its children are appended to the back — so they wait their turn while the rest of the current level is processed first. That's how the levels stay grouped.

---

## Why Does It Matter?

Suppose you're building a file explorer and want to display a folder tree. Each folder has sub-folders and files. The user clicks a node — what should you print first?

### ❌ Without choosing the right traversal:

```python
def show_anything(folder):
    if folder is None:
        return
    show_anything(folder.left)
    print(folder.name)
    show_anything(folder.right)
# That's inorder. It works for a BST, but for a folder tree it
# scrambles the layout: parent in the middle, sub-folders on either
# side. The UI looks like nothing the user expects.
```

### ✅ With the right traversal for the job:

```python
def show_folder_tree(folder, depth=0):
    if folder is None:
        return
    print("  " * depth + folder.name)         # parent first
    for child in folder.children:
        show_folder_tree(child, depth + 1)
# Preorder — parent before children. Indents line up. The user sees
# the layout they expect: home/, then home/Documents/, then files inside.
```

For computing the **size** of every folder (`du`-style), you'd reach for **postorder** instead — you can't sum the parent's size until you know the children's sizes:

```python
def folder_size(folder):
    total = folder.own_size
    for child in folder.children:
        total += folder_size(child)           # children FIRST (postorder)
    return total
```

The choice of traversal isn't cosmetic. It determines whether the algorithm can even run.

---

## Practical Examples

### Saving a tree to a file (preorder)

A serialization format like JSON natively writes parent before children. Preorder visits in exactly that order. You can rebuild the tree from the file by reading top-down.

### Reading a Binary Search Tree in sorted order (inorder)

A BST has the property `left < parent < right` at every node. Inorder visits left, then parent, then right — exactly the sorted order. Class 07 makes this click; for now, just keep the hook in mind.

### Computing folder sizes (`du`-style — postorder)

Each parent's size = sum of its own files + sizes of its sub-folders. You cannot compute the parent's size before knowing the children's. Postorder is the only DFS order that gives you the children first.

### Shortest path in an unweighted graph (BFS)

BFS visits by **distance** from the start. The first time you reach a node, you reached it via the shortest path (in edges). Used by every web crawler, every navigation app, and every "minimum number of steps" puzzle.

---

## Common Pitfalls

### Pitfall 1: Wrong slot for the visit

```python
# ❌ Meant to write preorder, accidentally wrote postorder:
def f(node):
    if node is None: return
    f(node.left)
    f(node.right)
    print(node.value)
# Symptom: output looks "almost right" but reversed at every level.
# Easy to miss in code review.

# ✅ Decide first WHERE the visit happens, then write it:
def preorder(node):
    if node is None: return
    print(node.value)              # decided: BEFORE descending
    preorder(node.left)
    preorder(node.right)
```

The trap is that all three traversals "compile and run". The bug is silent. Always say the order out loud BEFORE typing — "root first, then left, then right" — then put the print in the matching slot.

### Pitfall 2: Using a `list` as a queue

```python
# ❌ Looks fine, silently O(n²):
queue = [root]
while queue:
    node = queue.pop(0)            # O(n) each call
    ...
    queue.append(node.left)
# On a tree with 10000 nodes, this gets noticeably slow.

# ✅ deque is the right tool:
from collections import deque
queue = deque([root])
while queue:
    node = queue.popleft()         # O(1)
    ...
```

`list.pop(0)` shifts every remaining element down by one. `deque.popleft()` is O(1) by construction. The interface is almost identical; the cost is not.

### Pitfall 3: Forgetting the empty tree

```python
# ❌ Crashes on bfs(None):
def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value)          # AttributeError: NoneType has no .value
        ...

# ✅ Handle empty tree first:
def bfs(root):
    if root is None:
        return
    queue = deque([root])
    ...
```

The recursive DFS traversals already handle `node is None` in their base case, so they don't crash on empty trees. BFS doesn't have that base case for free — you have to add the guard yourself, before the loop starts.

### Pitfall 4: Appending None children to the queue

```python
# ❌ Appends Nones, then crashes when popping them:
while queue:
    node = queue.popleft()
    print(node.value)
    queue.append(node.left)        # might be None
    queue.append(node.right)
# Next iteration: node = None, then None.value → crash.

# ✅ Filter at append time:
while queue:
    node = queue.popleft()
    print(node.value)
    if node.left is not None:
        queue.append(node.left)
    if node.right is not None:
        queue.append(node.right)
```

Some textbooks do the check at pop time instead (`if node is not None: print(...); queue.append(...)`). Both work. Pick one and stick to it. Mixing them is how you double-check or never-check.

---

## Summary

| Concept | What it does | When to use | Key rule |
|---------|--------------|-------------|----------|
| Preorder | Visit BEFORE recursing left and right | Save / serialize a tree, top-down exploration | Print first, then recurse |
| Inorder | Visit BETWEEN left and right | Read a BST in sorted order (Class 07) | Recurse left, print, recurse right |
| Postorder | Visit AFTER both recursions | Folder size, tree height, free memory | Children first, parent last |
| BFS | Visit level by level using a `deque` | Shortest path, level rendering, web crawl | `popleft` + `append` = FIFO |
| The DFS reveal | All three DFS twins share one skeleton | Once you write one, you wrote all three | Only the visit line moves |
