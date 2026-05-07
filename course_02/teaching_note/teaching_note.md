# Understanding Linear Data Structures and the Walking Pattern

> Stacks and queues are the right shape for "ordered access" problems. Linked lists are not about storing data — they are about training the reflex you'll reuse on trees.

---

## What is a Linear Data Structure?

A **linear data structure** is one where each element has at most one predecessor and at most one successor. You can imagine the elements laid out on a single line: a queue at the bus stop, a tower of pancakes, a chain of paperclips. There is a beginning and an end, and you can walk from one to the other in a single direction.

This is in contrast to **branching** structures like trees and graphs, where one element can lead to many. We will meet those soon. The reason we spend a class on linear structures *first* is not that they are useful for the next month — it's that the **muscle memory** you build here (walking from one element to the next, doing something at each step) is the exact same muscle memory you'll use on trees.

In Python, you already use one linear structure constantly: the built-in `list`. What this lesson adds is **the four classical structures** — stack, queue, array (list), linked list — and the **trade-offs** between them.

```python
stack = []
stack.append("first task")   # push onto top
stack.append("second task")
print(stack.pop())           # → "second task"
```

The Pythonic stack is just a list where the **end** is the top.

---

## Stacks (LIFO) in Detail

### The analogy

Imagine a pile of plates at a canteen. When the dishwasher returns clean plates, they put them on top. When you take a plate, you take the one on top. You never pull from the bottom — that would risk crashing the whole pile.

This is **LIFO** — *Last In, First Out*. The last item added is the first one removed.

### The three operations

A stack offers three operations, each O(1):

| Operation | What it does |
|---|---|
| `push(v)` | Put `v` on top |
| `pop()` | Remove and return the top |
| `peek()` | Look at the top without removing |

### ❌ Without using the right end:

```python
class BadStack:
    def __init__(self):
        self._data = []

    def push(self, v):
        self._data.insert(0, v)   # adds at the FRONT

    def pop(self):
        return self._data.pop(0)  # removes from the FRONT
```

This works, but `list.insert(0, ...)` and `list.pop(0)` are both **O(n)** — Python has to shift every other element by one slot. Push 1000 items and you've done one million unnecessary moves.

### ✅ The Pythonic stack:

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, v):
        self._data.append(v)      # END = top, O(1)

    def pop(self):
        return self._data.pop()   # END = top, O(1)
```

The rule to remember: **when you build a stack on top of a Python list, the end of the list is the top of the stack.**

### Where stacks show up in real life

| Use case | What gets pushed | What gets popped |
|---|---|---|
| Browser **back button** | Each page you visit | The previous page |
| **Ctrl+Z** (undo) | Each action you perform | The last action |
| Python **call stack** | Each function call frame | The frame when the function returns |
| Matching **parentheses** | Each `(` `[` `{` | When `)` `]` `}` arrives |

That last one is so classical it shows up in compiler exercises, interview questions, and the BONUS section of this week's exercise. The pattern: push every opening bracket; on a closing bracket, pop and check that they match.

---

## Queues (FIFO) in Detail

### The analogy

A queue is a line at a canteen. The first person who arrives is the first person served. You never let someone jump the line.

This is **FIFO** — *First In, First Out*.

### Why not just use a list?

```python
# ❌ Using a list as a queue:
q = []
q.append("Alice")
q.append("Bob")
q.append("Charlie")
print(q.pop(0))      # → "Alice"  - works, but O(n)
```

Each `pop(0)` shifts every remaining element by one. A queue with one million items would do half a trillion shifts over its lifetime.

```python
# ✅ deque - the right tool:
from collections import deque

q = deque()
q.append("Alice")
q.append("Bob")
q.append("Charlie")
print(q.popleft())   # → "Alice"  - O(1)
```

`collections.deque` is a doubly-linked queue under the hood. Both ends are O(1) for append and pop. **Always reach for `deque` when you need a queue in Python.**

### When you'll meet queues again

The first time queues become essential in this course is **Class 06 — Tree Traversals**. There, **BFS** (Breadth-First Search) explores a tree level by level using a queue: enqueue the root, then in a loop, dequeue a node, visit it, enqueue its children. Trees are different shapes, but the queue mechanic is identical to what you saw at the canteen.

---

## Linked Lists in Detail

### The analogy

A linked list is a **treasure hunt**. Each clue tells you where the next clue is. You can't jump to clue #5 directly — you have to follow #1 → #2 → #3 → #4 → #5. The list itself is just the reference to the **first clue** (the head).

```
 head
   ↓
 ┌─────────┐    ┌─────────┐    ┌─────────┐
 │ data: A │ →  │ data: B │ →  │ data: C │ → None
 │ next:●──┘    │ next:●──┘    │ next:●──┘
 └─────────┘    └─────────┘    └─────────┘
```

Each node holds a piece of data and a pointer (`.next`) to the next node. The last node's `.next` is `None`, which is how you know you've reached the end.

### The data classes

```python
class _Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
```

Two classes, twenty lines, and you have the foundation for everything you'll do in the next three weeks.

### Linked list vs Python list — the trade-offs

| Operation | Python `list` (array) | Linked list |
|---|---|---|
| `lst[i]` random access | **O(1)** | O(n) — must walk |
| Insert at end | **O(1)** amortized | O(n) without a tail pointer |
| Insert at start | O(n) | **O(1)** |
| Delete at start | O(n) | **O(1)** |
| Memory layout | Contiguous block | Scattered nodes + pointers |

**Honest take:** for 99% of your daily Python code, just use a regular `list`. It is faster, denser in memory, and supports indexing.

So why do we study linked lists? Because the way you walk through one — node by node, following `.next` — is **the exact pattern we'll use on trees, graphs, and recursive structures**. The shape of the data changes; the walking reflex stays the same.

---

## THE WALK — the pattern of the next three weeks

The whole point of this lesson is the four-line skeleton you should be able to type with your eyes closed:

```python
cur = self._head
while cur is not None:
    # do something with cur.data
    cur = cur.next
```

That's it. Everything else is "what do you do at each step?"

### Variation 1 — walk to the end and attach a new node

```python
def add_tail(self, v):
    new = self._Node(v)
    if self._head is None:
        self._head = new                 # empty list: new IS the head
    else:
        cur = self._head
        while cur.next is not None:      # walk to the LAST node
            cur = cur.next
        cur.next = new                   # attach
    self._size += 1
```

Notice the loop condition: `cur.next is not None`. We stop **at** the last node, not after it — we need `cur` to still exist so we can attach to it.

### Variation 2 — walk every node, track the maximum

```python
def find_max(self):
    if self._head is None:
        return None
    current_max = self._head.data
    cur = self._head.next
    while cur is not None:
        if cur.data > current_max:
            current_max = cur.data
        cur = cur.next
    return current_max
```

Here the loop condition is `cur is not None` — we *do* want to look at every node, including the last.

These two functions look different on the surface, but read them again. **Same skeleton both times**: start at `_head`, walk while a condition holds, do something at each step. The only thing that changes is the action.

---

## Why Does It Matter? — The Bridge to Trees

Look at THE WALK one more time. Now imagine each node has **two** pointers — `left` and `right` — instead of one `.next`. That's a binary tree.

```python
# Linked list walk:           Tree walk (preview):
cur = self._head              def visit(node):
while cur is not None:            if node is None: return
    look(cur.data)                look(node.data)
    cur = cur.next                visit(node.left)
                                  visit(node.right)
```

The tree version walks recursively (we'll explain recursion next class) and it walks **two** branches at each step, but the spirit is identical: **at each node, look at the data, then keep going.**

Today's `find_max` will come back as `find_max_value(node)` on a tree. The logic is identical — walk every node, keep track of the max — except the tree version walks left AND right at each node. **Get the pattern in your fingers today, and trees will feel natural.**

---

## Practical Examples

### Example 1 — Browser history is a stack

When you click "back" in a browser, the page that pops is the one you most recently visited. Each new URL is **pushed**; each "back" click **pops**. Forward history is a separate stack: as pages pop from the back-stack, they are pushed onto a forward-stack. Click forward, and they are pushed back onto the main stack.

This isn't a metaphor. The Chromium source code literally calls these classes `BackForwardList` and uses two stacks under the hood.

### Example 2 — A printer queue is a queue

A shared office printer receives jobs in the order people send them. The job that started printing first finishes first; the next job in line goes second. Adding new jobs to the back; printing pulls from the front. **FIFO**, every time.

In Python you'd model it with a `deque`. Adding `q.append(job)` when a user prints; the printer thread runs `job = q.popleft()` in a loop.

### Example 3 — Friends-of-friends in a social network is a linked walk

Imagine each user is a node, and each user has a `.next_friend` pointer to one specific person they recommended. To find "the most influential person in this chain of recommendations", you walk from the seed user, follow `.next_friend` until it's `None`, and at each step compare the influence score against the running max.

That's literally `find_max` from the exercise, with `data` renamed to `influence`. The walk doesn't care.

### Example 4 — The Python call stack IS a stack

When you call a function, Python pushes a **frame** onto its internal call stack: the function's local variables, the line number it'll return to, the arguments. When the function returns, Python pops the frame. When you see `RecursionError: maximum recursion depth exceeded`, you've **pushed too many frames** without ever popping. Every recursive function you write rides on top of this LIFO machinery.

---

## Common Pitfalls

### Pitfall 1: Off-by-one when walking the linked list

```python
# ❌ Stops one step too early - misses the last node:
cur = self._head
while cur.next is not None:
    visit(cur.data)
    cur = cur.next

# ✅ Visits every node, including the last:
cur = self._head
while cur is not None:
    visit(cur.data)
    cur = cur.next
```

The trap is reading `while cur.next is not None` as *"while there's more"*. There isn't — when `cur` is the last node, `cur.next` is `None`, but `cur` itself still has data we want to visit.

The exception is `add_tail`, where you specifically want to **stop at** the last node so you can attach to it. There the right condition is `cur.next is not None`. Read each loop carefully and ask: *"do I want to visit the last node, or do I want to land on it?"*

### Pitfall 2: Using `list.pop(0)` for a queue

```python
# ❌ Looks fine, silently O(n) per operation:
q = []
q.append("Alice")
first = q.pop(0)
```

Single-character difference, two-orders-of-magnitude slowdown on large queues. **Reflex:** the moment you write `pop(0)`, ask yourself if you should be using `deque.popleft()` instead.

### Pitfall 3: Forgetting to update `self._size`

```python
# ❌ size lies after you call add_tail:
def add_tail(self, v):
    new = self._Node(v)
    cur = self._head
    while cur.next is not None:
        cur = cur.next
    cur.next = new
    # forgot self._size += 1

# ✅ Update on every mutation:
def add_tail(self, v):
    ...
    cur.next = new
    self._size += 1
```

If `__len__` returns `self._size` and you don't update `_size` on every insert/remove, `len(ll)` will quietly disagree with the actual list. The fix is discipline: every method that mutates the list ends with a `self._size += 1` or `-= 1`.

### Pitfall 4: Empty-stack and empty-list edge cases

```python
# ❌ Crashes with IndexError on empty:
def pop(self):
    return self._data.pop()

# ✅ Raise a clearer error:
def pop(self):
    if not self._data:
        raise IndexError("empty stack")
    return self._data.pop()
```

The bare version *does* raise `IndexError`, but the message is `pop from empty list` — leaking the implementation. Wrapping it lets you tell the caller in your own words, which is also good practice for `peek()`, `find_max()` (which returns `None` on empty), and `add_tail()` on empty lists.

---

## Summary

| Concept | What it does | When to use | Key rule |
|---------|--------------|-------------|----------|
| **Stack (LIFO)** | Last in, first out — push/pop/peek | "Reverse the order", undo, brackets, recursion | Build on a Python list; the END is the top |
| **Queue (FIFO)** | First in, first out — append/popleft | Job processing, BFS traversal, fair scheduling | Use `collections.deque`, never `list.pop(0)` |
| **Python list (array)** | Contiguous, indexed storage | Default container for almost everything | O(1) access by index, O(1) append at end |
| **Linked list** | Chain of nodes with `.next` | Training the WALK pattern; rare in real Python | Walk with `while cur is not None: cur = cur.next` |
| **THE WALK** | Visit every node by following `.next` | Read, find max, count, attach, modify | Same skeleton on linked lists, trees, graphs |
