# Understanding Binary Trees

> A tree is a linked list with two pointers per node — and from that one tweak, a whole new world of recursion opens up.

---

## What is a Tree?

Think of the folder structure on your laptop. `~/` contains `Documents/`, which contains `school/`, which contains `algo_ii/`, which contains today's homework file. To go from the home folder to the file, you go down — never sideways, never up. Every folder can hold many sub-folders. A folder with no sub-folders is "the bottom".

That's a **tree**: a hierarchical data structure where every element (a "node") has exactly one parent, and can have any number of children. The single node with no parent is the **root** of the tree. The nodes with no children are called **leaves**.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# A two-node tree:
root = Node("A")
root.left = Node("B")
print(root.value, root.left.value)   # → A B
```

A **binary tree** is the special case where every node has at most two children — `left` and `right`. That's the only kind of tree we use today.

The key contrast with a linked list (which we wrote in Class 02) is shape. A linked list is a chain: each node has one successor, and the whole structure is a straight line. A binary tree branches: each node has up to two successors, and the structure spreads downward into a fan.

---

## The Vocabulary

A handful of words. Memorize them — every exam, every project description will use them.

- **Root**: the top node. The only node with no parent.
- **Parent**: the node directly above another.
- **Child**: the node directly below another.
- **Siblings**: two nodes that share the same parent.
- **Leaf**: a node with no children.
- **Subtree**: a node together with all its descendants. The "subtree rooted at B" means B plus everything below B.
- **Depth (of a node)**: the number of edges from the root down to that node. The root has depth 0.
- **Height (of a tree)**: the depth of the deepest leaf. A single-node tree has height 0; an empty tree has height -1 (our convention).

Two traps to internalize:

- **Depth is a property of a node. Height is a property of a tree** (or of a subtree). They are not interchangeable.
- The root has depth **0**, not 1. Some textbooks start from 1 — we always start from 0, because that lines up with how we count edges and how recursion bases out.

That covers the words. Now let's see why we care.

---

## The Node Class — One Extra Pointer

A binary tree node is a linked list node with one structural change: where the linked list had `self.next`, the tree has both `self.left` and `self.right`.

### ❌ Without the extra pointer (linked list, from Class 02):

```python
class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None       # exactly ONE successor
```

This works perfectly for a chain. But every node points to the next one in line, never to a sibling. There's no way to model a folder with two sub-folders, or a person with two children.

### ✅ With the extra pointer (binary tree, this class):

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None      # was 'next'
        self.right = None      # NEW
```

Now each node can spawn up to two paths. That single change is enough to model anything tree-shaped: file systems, comment threads, decision trees, family trees.

The `BinaryTree` class on top is a thin wrapper. It holds the root and gives us two helpers — `add_left(parent, value)` and `add_right(parent, value)` — so we can build a tree without manually wiring `parent.left = Node(...)` ten times. Each helper returns the newly created node, so we can chain attachments:

```python
tree = BinaryTree()
tree.root = Node("A")
b = tree.add_left(tree.root, "B")    # save b — we'll attach more to it
tree.add_right(tree.root, "C")       # leaf, don't bother saving
tree.add_left(b, "D")
tree.add_right(b, "E")
```

That's the lecture tree, built in five lines. The structure on screen mirrors the diagram on paper.

---

## Recursion on a Tree — Same Skeleton, Two Branches

Yesterday (Class 04), the recursion skeleton was:

> Base case → return a neutral value. Recursive case → combine the current node with `f(smaller)`.

On a linked list, "smaller" meant `node.next`. On a binary tree, "smaller" means `node.left` AND `node.right`. **One recursive call becomes two.** That is the entire jump from yesterday to today.

### ❌ Walking only one side:

```python
def count_only_left(node):
    if node is None:
        return 0
    return 1 + count_only_left(node.left)
```

This counts the leftmost spine of the tree and ignores everything on the right. On a tree with 100 nodes, this might return 3.

### ✅ Walking both sides:

```python
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
```

Now we visit every node. The base case (`node is None`) is hit at the bottom of every branch. We add 1 for the current node, then sum the two subtree counts. The function ends when all branches have bottomed out.

### Tracing it on a small tree

Take this five-node tree:

```
      A
     / \
    B   C
   / \
  D   E
```

`count_nodes(A)` expands like this:

1. `count_nodes(A)` → `1 + count_nodes(B) + count_nodes(C)`
2. `count_nodes(B)` → `1 + count_nodes(D) + count_nodes(E)` → `1 + 1 + 1 = 3`
3. `count_nodes(C)` → `1 + 0 + 0 = 1`
4. Back to A: `1 + 3 + 1 = 5` ✓

The call stack does the same dance as `factorial(4)` from Class 04: frames go down, hit the base case, return, frames unwind back up combining results. The shape is identical — you just have two branches under each frame instead of one.

That covers the count case. The same skeleton, with a different action at each step, gives us every other tree function.

---

## find_max_value — Same Skeleton, Different Action

When you walk every node and want the biggest value, the skeleton is unchanged — only the action and the neutral element differ.

```python
def find_max_value(node):
    if node is None:
        return float('-inf')
    return max(node.value,
               find_max_value(node.left),
               find_max_value(node.right))
```

Three values are in play at every node: my own value, the max of my left subtree, the max of my right subtree. `max(...)` picks the biggest. The empty subtree returns `float('-inf')` so it always loses.

**Why `-inf`?** It is the **neutral element** for `max`, in the same way `0` is the neutral element for `+` and `1` is the neutral element for `*`. A neutral element is a value that, when combined with any real value, returns the real value:

- `max(real_value, -inf, -inf) = real_value`
- `0 + real_value = real_value`
- `1 * real_value = real_value`

Picking the right neutral element is the trick that lets recursion handle the empty case without a special branch. It is also the most common bug source: people use `0` for max, then their function returns `0` on a tree of negative numbers. Our Bonus 3.2 forces you to live this mistake on purpose.

---

## Why Does It Matter?

Suppose you're building a tool that counts replies in a Bilibili comment thread. Every comment can have multiple replies; each reply can have replies of its own; replies can be 12 levels deep.

### ❌ Without recursion on a tree:

```python
total = 1                                 # the top comment itself
for reply_lvl_1 in comment.replies:
    total += 1
    for reply_lvl_2 in reply_lvl_1.replies:
        total += 1
        for reply_lvl_3 in reply_lvl_2.replies:
            total += 1
            # ...how deep does this go?
```

This breaks the moment a thread is one level deeper than your code expects. You can't write a loop for "any depth", so you end up writing dozens of nested loops and still missing the deepest replies.

### ✅ With recursion on a tree:

```python
def count_replies(comment):
    if comment is None:
        return 0
    total = 1                              # this comment counts
    for reply in comment.replies:
        total += count_replies(reply)
    return total
```

Six lines. Works for any depth, forever. This is exactly what Project 1 in Week 10 will ask you to write — `count_replies()`, `deepest_chain()`, `add_reply()`. The recursive shape you learn today is the shape you'll ship in five weeks.

---

## Practical Examples

### Counting files in a folder

A file-system tree where each directory has children (sub-directories or files). `count_files` is `count_nodes` minus 1 for non-file root.

```python
def count_items(folder_node):
    if folder_node is None:
        return 0
    total = 1
    for child in folder_node.children:
        total += count_items(child)
    return total
```

### Highest grade in a tournament bracket

A bracket is a binary tree where each internal node holds the winner of two sub-matches and each leaf holds a player's final score. `find_max_value` answers "who scored highest overall".

### Deepest reply in a comment thread

Replace `count_nodes` with the height pattern. Convention: empty tree has height -1, a single comment (no replies) has height 0, and the recursive case is `1 + max(height(left), height(right))`. The deepest reply is `tree_height(root)`.

---

## Common Pitfalls

### Pitfall 1: Forgetting one of the two branches

```python
# ❌ What people try (still thinking in linked-list mode):
def count_nodes_buggy(node):
    if node is None:
        return 0
    return 1 + count_nodes_buggy(node.left)
# Symptom: returns the length of the leftmost spine, not the node count.
```

```python
# ✅ Correct: both branches.
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
```

The trap is muscle memory from Class 04. Yesterday there was only `node.next`, so people write `node.left` and stop. The whole point of today is that "smaller" has two halves, not one.

### Pitfall 2: Wrong neutral element for `max`

```python
# ❌ What people try:
def find_max_buggy(node):
    if node is None:
        return 0                  # ← wrong neutral
    return max(node.value,
               find_max_buggy(node.left),
               find_max_buggy(node.right))
# Symptom: on a tree of all negative values, returns 0.
```

```python
# ✅ Correct: use a value smaller than anything real.
def find_max_value(node):
    if node is None:
        return float('-inf')
    return max(node.value, ...)
```

The neutral element rule: for `+`, use 0. For `*`, use 1. For `max`, use `-inf`. For `min`, use `+inf`. Pick the value that "loses" when combined with a real value.

### Pitfall 3: Mixing up depth and height

People say "the depth of the tree" or "the height of node D" and confuse the two. Lock the convention now:

- **Depth is for a NODE.** Counted from the root, downward. Root has depth 0.
- **Height is for a TREE** (or a subtree). It is the depth of the deepest leaf. A single-node tree has height 0; an empty tree has height -1.

If a question asks "the depth of the tree", read it as "the height of the tree" — the questioner is using sloppy language but means the deepest depth.

### Pitfall 4: Mutating `tree.root` without using `BinaryTree`

```python
# ❌ What people try:
tree = BinaryTree()
tree.add_left(tree.root, "B")   # crashes — tree.root is None
```

`add_left` expects an existing parent node. The empty tree has no root, so you must set `tree.root = Node(...)` yourself before attaching anything. The helpers only attach children; they don't create the root.

---

## Summary

| Concept | What it does | When to use | Key rule |
|---------|--------------|-------------|----------|
| Binary tree node | A linked list node with two pointers (`left`, `right`) | Any hierarchical data with at most two branches per element | One extra pointer is the whole structural change |
| Vocabulary (root/leaf/depth/height) | Names every part of the tree | Reading exercises, exam questions, project specs | Depth is for a node, height is for a tree. Root has depth 0 |
| `count_nodes` | Counts every node in a subtree | Sizing a tree, validating builds | Same as `length_recursive`, with two recursive calls |
| `find_max_value` | Returns the biggest value in the tree | Searching a tree for an extreme | Use `float('-inf')` as the neutral element for `max` |
| Recursion skeleton | Base case + combine current with `f(left)` and `f(right)` | Every tree function in this course | One call becomes two — that's the whole jump from Class 04 |
