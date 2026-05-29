# Notions to Know — Midterm Catch-up (Courses 01–09)

A fast review of everything the midterm can ask. Read this **after** the course notes — it is a catch-up, not a replacement. New words are in `glossary.md`.

> One reflex that covers half the exam: **count the loops** for Big-O, and **write the base case first** for recursion.

---

## 1 — Big-O (Course 01)

Big-O measures **how the work grows when the input gets big**. Not seconds.

| Notation | Name | Example |
|---|---|---|
| O(1) | constant | `lst[0]`, `d[k]`, heap `peek` |
| O(log n) | logarithmic | binary search, balanced BST search |
| O(n) | linear | one loop over a list |
| O(n²) | quadratic | two **nested** loops over the same data |

**Read it from code:**
- One loop over `n` → O(n).
- Two **nested** loops → O(n²).
- Two loops **one after another** (not nested) → still O(n).
- Work cut in half each step → O(log n).

On 1,000,000 items: O(1) ≈ 1 step, O(log n) ≈ 20 steps, O(n) ≈ 1,000,000 steps. That gap is why algorithm choice matters.

---

## 2 — Stack, Queue, Linked list (Course 02)

**Stack — LIFO** (Last In, First Out). Like a pile of plates.
- `push`, `pop`, `peek` are all **O(1)**.
- Build it on a Python list; the **end of the list is the top** (`append` / `pop()` are O(1); `pop(0)` is O(n)).
- Use for "do something in reverse order" (e.g. palindrome check, undo, browser back).

**Queue — FIFO** (First In, First Out). Like a line at the canteen.
- Use `from collections import deque`. `popleft()` is **O(1)**; a plain `list.pop(0)` is O(n).
- BFS uses a queue.

**Linked list** — a chain of nodes; each node has `data` and `.next`. The end is marked by `.next is None`.

**The walk** — the most reused pattern of the whole semester:
```python
cur = head
while cur is not None:
    # use cur.data
    cur = cur.next
```
On a tree this becomes two links (`left`, `right`) instead of one (`.next`).

---

## 3 — Hash tables / dict (Course 03)

A **dict** stores key → value. Lookup, insert, membership (`x in d`) are all **O(1) on average**.
- Inside: Python computes `hash(key)`, takes it modulo the array size → goes straight to that index. No scanning.

**The counting pattern** (write it 100 times):
```python
counts[w] = counts.get(w, 0) + 1
```
`d.get(w, 0)` returns the count if `w` is a key, else the default `0`. First time a word is seen → stores `1`.

**Two-sum — O(n²) → O(n):** instead of testing every pair, walk once and remember seen values in a dict. For each `x`, ask "have I seen `target - x` before?" — that lookup is O(1).
> Reflex: about to write nested loops? Ask if a dict can collapse them.

---

## 4 — Recursion (Course 04)

A recursive function calls itself. It needs **two parts**:
1. **Base case** — when to stop, returns directly. **Write it first.**
2. **Recursive case** — calls itself on a **smaller** input.

**The skeleton:**
```python
def f(x):
    if <base case>:
        return <neutral value>
    return <combine>(<current>, f(<smaller x>))
```

**Call stack** — the calls running right now, stacked one on top of another. Each call keeps its own variables. Python stops at ~1000 deep with `RecursionError`.

**Three patterns:** decrement (`n-1`), walk (`lst[1:]` or `node.next`), divide (binary search: keep one half).

**Four classic bugs:**
| Bug | Result |
|---|---|
| No base case | `RecursionError` |
| No `return` on the recursive call | returns `None` silently |
| Wrong direction (`n+1` instead of `n-1`) | `RecursionError` |
| Mutable default argument (`result=[]`) | shared state between calls |

---

## 5 — Trees: vocabulary + recursion (Course 05)

A **tree** branches downward from one **root**. A **binary tree** has **at most two children** per node (`left`, `right`).

| Word | Meaning |
|---|---|
| root | top node, no parent |
| parent / child | directly above / below |
| sibling | same parent |
| leaf | **no children** |
| subtree | a node + everything below it |
| **depth** | edges from root to a **node** (root = 0) |
| **height** | depth of the deepest leaf — a property of the **tree** |

> Trap: **depth is for a node, height is for a tree.**

Tree recursion = the Class 04 skeleton with **two** recursive calls:
```python
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
```
`find_max_value` returns `float('-inf')` for the empty case (neutral value for `max`), then takes the max of the node and both subtrees.

---

## 6 — Tree traversals (Course 06)

A **traversal** visits every node in a chosen order. The three DFS traversals share **one skeleton** — only the line that visits the node moves.

| Traversal | Order | Output on the tree below |
|---|---|---|
| **preorder** | root → left → right | 7, 3, 8, 2, 9 |
| **inorder** | left → root → right | 8, 3, 2, 7, 9 |
| **postorder** | left → right → root | 8, 2, 3, 9, 7 |
| **BFS** (level-order) | level by level | 7, 3, 9, 8, 2 |

```
        7
       / \
      3   9
     / \
    8   2
```

- **inorder on a BST → values in sorted order.**
- **BFS** uses a **queue** (`deque`, `append` + `popleft`) because it serves the **oldest** waiting node first.

---

## 7 — Binary Search Trees (Courses 07 & 08)

**BST property:** for every node, all values in the **left** subtree are smaller, all in the **right** are greater. Applied everywhere.

**Search** — compare at each node, go left or right. Each comparison throws away one whole subtree (about half). Cost = **O(h)**: O(log n) if balanced, O(n) if degenerate.

**Insert** — search until you hit a `None` spot; put the new node there. Always **return the node** so the parent can re-attach: `node.left = insert(node.left, v)`. Duplicates: do nothing.

> Inserting **sorted** values in order (`1, 2, 3, …`) makes a **degenerate** chain (height n) → search O(n). A plain BST does **not** auto-balance.

**Delete — three cases:**
1. **Leaf** → just remove it.
2. **One child** → the child takes its place.
3. **Two children** → copy the **inorder successor** (smallest value in the right subtree) into the node, then delete that successor.

**Self-balancing trees** (AVL, red-black) re-fix the shape automatically to keep height ≈ log n. You only need the concept, not the code.

| Operation | Balanced | Degenerate |
|---|---|---|
| search / insert / delete | O(log n) | O(n) |

---

## 8 — Heaps & priority queues (Course 09)

A **priority queue** returns the most important item first, not the oldest. A **heap** makes it fast.

A **binary heap** is a **complete** binary tree with the **heap property**:
- **min-heap** → parent ≤ children → smallest at the root.
- **max-heap** → parent ≥ children → largest at the root.
- **Not a BST** — there is no left/right ordering, only parent vs children.

**Stored in an array.** For index `i`:
| | Formula |
|---|---|
| parent | `(i - 1) // 2` |
| left child | `2 * i + 1` |
| right child | `2 * i + 2` |

- **push** = add at the end + **bubble up**. O(log n).
- **pop** = return root, move last item to root + **bubble down**. O(log n).
- **peek** (read the min at index 0) = **O(1)**.

Python's `heapq` is a **min-heap**. For a **max-heap**, store **negative** values (the smallest negative is the largest real value). Top-K: `heapq.nlargest(k, lst)` → O(n log k).

| | Heap | BST |
|---|---|---|
| find min | O(1) | O(h) |
| find any value | O(n) | O(h) |
| storage | array | nodes + pointers |

---

## Exam reflexes (quick checklist)

- **Big-O:** count loops. Nested = O(n²). Halving = O(log n).
- **LIFO = stack, FIFO = queue.** Singly linked list ends at `.next is None`.
- **`d.get(k, 0) + 1`** is the counting pattern; first time stores `1`.
- **Recursion** needs a base case; growing input or no base case → `RecursionError`.
- **count_nodes(None) = 0**; count every node = `1 + left + right`.
- **Traversal outputs:** preorder root-first, inorder left-root-right (sorted on a BST), postorder root-last, BFS level by level.
- **BST search path:** at each node go left if target is smaller, right if greater.
- **Sorted inserts → degenerate chain → O(n).**
- **Delete:** 3 cases; two children → inorder successor.
- **Heap:** parent `(i-1)//2`; root is min (min-heap); max-heap via negatives.
