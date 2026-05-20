# Understanding Heaps & Priority Queues

> Not everyone waits their turn — the most important one always goes first.

---

## What is a Priority Queue?

Walk into a hospital emergency room. Three patients are sitting in the waiting area:

- A man with a small cut on his finger.
- A woman with a broken arm.
- A patient having a heart attack.

Whose name gets called first? Not the one who arrived first. The one with the **highest priority** — the heart attack. The cut and the broken arm wait.

That is a **priority queue**. A queue where you do not get out in the order you got in; you get out by priority. The most important element is always next.

Real systems use priority queues everywhere:

- Your phone's OS interleaves a Bilibili upload with a low-battery alert and a system update. The alert goes first.
- Douyin's recommender keeps the top-K candidate videos for you, updated as it scores more candidates.
- Baidu Maps runs Dijkstra's shortest-path algorithm — at every step it pops the closest unvisited intersection from a priority queue.

A priority queue is the **abstraction**. A **heap** is the data structure we use to implement it efficiently.

---

## The Heap Property

A **binary heap** is a **complete** binary tree with one extra rule.

### Min-heap

For every node `n`, **`n.value ≤ both children's values`**.

```
        1
       / \
      3   2
     / \ / \
    7  5 8  4
```

The smallest value lives at the root. Always.

### Max-heap

Mirror image: `n.value ≥ both children's values`. The largest value lives at the root.

```
        90
       /  \
      50   70
     / \   /
    10 30 60
```

Pick the variant that matches the question. "I want the cheapest first" → min-heap. "I want the highest-priority first" → max-heap (or min-heap with negated priorities).

### What "complete" means

Every level is full, except possibly the last — and on the last level, nodes are packed to the LEFT. No gaps in the middle.

This rule is more than aesthetic. It is what makes the array representation possible.

### ❌ Common confusion: a heap is NOT a BST

A BST has full left/right ordering — left subtree smaller than node smaller than right subtree. A heap only enforces parent vs children. There is no "left vs right" order at all.

```
        1
       / \
      3   2     ← OK in a min-heap. NOT OK in a BST (3 > 2 but in left).
```

If you walk a heap inorder you get garbage. If you want sorted output, the right tool is a BST — not a heap.

---

## The Array Trick

A complete binary tree has a tight structure: every position from index 0 up to n-1 is filled. So we can store it in a **plain list**, no left/right pointers, no Node class.

```
Tree                     Array
     1                   index: 0  1  2  3  4  5  6
    / \                  value: 1  3  2  7  5  8  4
   3   2
  / \ / \
 7  5 8  4
```

To navigate the tree, we use index arithmetic:

| Relationship | Formula |
|---|---|
| Parent of `i` | `(i - 1) // 2` |
| Left child of `i` | `2 * i + 1` |
| Right child of `i` | `2 * i + 2` |

### A worked example

Take index `5` in the array above (value 8). Apply the formulas:

- parent = (5 - 1) // 2 = **2** → value 2 in the array. ✓ (matches the tree)
- left child = 2 \* 5 + 1 = **11** → out of bounds, so no left child. ✓
- right child = 2 \* 5 + 2 = **12** → out of bounds. ✓

The array `[1, 3, 2, 7, 5, 8, 4]` and the tree above are the **same object**, written two different ways.

### Why this is a big deal

- **No pointers** = less memory and better cache behavior. The whole heap is one contiguous block in RAM.
- **O(1) random access** to any parent or child by index.
- **Trivial to copy or serialize** — it is just a list.

This is the trick that makes heaps faster than BSTs in practice for the operations a priority queue cares about.

---

## Push — Bubble Up

To add a value to a min-heap:

1. **Append at the end of the array** (the next available slot — fills the tree level-by-level, left-to-right by construction).
2. **Bubble up**: compare with parent. If smaller, swap. Repeat until the parent is ≤ the new value, or you reach index 0.

### Trace push(1) on `[2, 3, 5, 7, 4]`

```
[2, 3, 5, 7, 4]                    start
[2, 3, 5, 7, 4, 1]                 append 1 at index 5
  parent of 5 = 2, value 5. 1 < 5 → swap:
[2, 3, 1, 7, 4, 5]                 1 at index 2
  parent of 2 = 0, value 2. 1 < 2 → swap:
[1, 3, 2, 7, 4, 5]                 1 at index 0 → done
```

The new value walked from the leaf up to the root, two swaps. The number of swaps is bounded by the tree height — `log₂(n)`. So push is **O(log n)**.

### ❌ A common bug — forgetting the comparison direction

```python
# Min-heap bubble-up that uses > instead of < :
if self.data[i] > self.data[parent]:
    swap...                # the BIG value bubbles up instead of the small one
```

The heap silently becomes a max-heap, or — worse — neither. Always state the invariant out loud before writing the code: *"the new value bubbles up while it is smaller than its parent"*.

---

## Pop — Bubble Down

To extract the minimum (the root):

1. **Save the root** — that is what `pop` returns.
2. **Move the last element of the array to position 0** (the root spot). The tree is now "complete" again, but the new root is probably wrong.
3. **Bubble down**: compare with the **smaller** of the two children. If the node is bigger, swap. Repeat until the node has no children, or it is ≤ both children.

### Trace pop on `[1, 3, 2, 7, 4, 5]`

```
[1, 3, 2, 7, 4, 5]                 save root: 1 (return value)
[5, 3, 2, 7, 4]                    move last (5) to position 0
  children of 0: 1 (value 3), 2 (value 2). Min = 2. 5 > 2 → swap:
[2, 3, 5, 7, 4]                    5 at index 2
  children of 2: 5, 6 → out of bounds. Done.
returned: 1
```

Two swaps, height-bounded. Pop is **O(log n)**.

### ❌ A common bug — swapping with the WRONG child

```python
# Bubble-down that always picks the left child:
if self.data[i] > self.data[left]:
    swap with left
```

If the right child is smaller, the heap property breaks on the right side. Always compute `min_child = left if data[left] < data[right] else right` first (with the right-out-of-bounds guard), then compare against `min_child`.

---

## Python's heapq

You will not write the bubble-up / bubble-down code in production — Python's standard library does it for you. The `heapq` module operates **on a plain list** (no class, no wrapper), and treats it as a **min-heap**.

```python
import heapq

nums = [5, 3, 8, 1, 9, 2]
heapq.heapify(nums)             # turn the list into a heap, in place, O(n)
heapq.heappush(nums, 0)         # push, O(log n)
smallest = heapq.heappop(nums)  # pop the min, O(log n)
```

Three things to remember:

1. **heapq mutates the list in place.** No copy is returned. If you need the original, pass `nums[:]` or `list(nums)`.
2. **The root is always `nums[0]`.** Peeking the smallest is O(1) — just `nums[0]`, no function call.
3. **`heapq` is min-only.** Want a max-heap? Negate every value: push `-x`, pop `-x`. The smallest negative is the largest original.

### Top-K shortcuts

For the very common "give me the K smallest / largest of n values" question, `heapq` has dedicated helpers:

```python
heapq.nlargest(3, nums)         # 3 largest, in descending order
heapq.nsmallest(3, nums)        # 3 smallest, in ascending order
```

Both run in **O(n log k)**. When `k << n`, this beats `sorted(nums)[:k]` which is O(n log n) — you avoid sorting the values you do not care about.

---

## Heap vs BST — Which One Do I Use?

Both are tree-based, both support insertion. They serve different jobs.

| Operation | Heap | BST |
|---|---|---|
| Find min | **O(1)** | O(h) |
| Find arbitrary value | O(n) | O(h) |
| Insert | O(log n) | O(h) |
| Sorted iteration | NO — heap order ≠ sorted | YES — inorder gives sorted |
| Storage | Array (compact) | Nodes + pointers |

The rule of practice:

- "I want the most important element, fast, and I don't care about the rest" → **heap**.
- "I want to search by key, get values in sorted order, do range queries" → **BST**.

Trying to use a heap to find a specific (non-root) value is painful — you walk the whole array. Trying to use a BST for top-K is wasteful — every search is O(log n) instead of O(1) for the min.

---

## Why Does It Matter?

Imagine a recommender service for a video platform. It has scored 1,000,000 candidate videos for a user and must return the top 50 to display.

### ❌ Without a heap — full sort

```python
def top_50_via_sort(scored_videos):
    scored_videos.sort(key=lambda v: -v.score)    # O(n log n)
    return scored_videos[:50]
# Sorts ALL 1M videos to keep only 50. Wasted work on the bottom
# 999,950.
```

For 1,000,000 videos, full sort takes ~10x the work that is strictly needed. If this runs for every user request, the server burns through CPU.

### ✅ With a heap — top-K only

```python
def top_50_via_heap(scored_videos):
    return heapq.nlargest(50, scored_videos, key=lambda v: v.score)
# Keeps a heap of size 50 as it scans. O(n log 50) = O(n × 6).
```

Same answer, ~10x less CPU per request. At Bilibili scale, that is the difference between a service that costs ¥X per day and ¥10X per day.

The general lesson: **if you do not need the full sorted order, do not pay for it.** A heap is the data structure for partial-order problems.

---

## Practical Examples

### A request scheduler

A web service handles requests with different priorities — paying customers above free users, admin tasks above paying customers. Each incoming request goes into a max-heap keyed on priority. The worker pool pops from the heap to pick the next job. O(log n) per push and pop — scales to thousands of pending requests per server.

### Dijkstra's shortest path

The algorithm needs to repeatedly pop the unvisited node with the smallest current distance. A min-heap of `(distance, node)` tuples handles this in O(log n) per step. Without the heap, every step scans the unvisited set — O(n²) total. With the heap, O((n + edges) × log n).

### Streaming median

Keep two heaps: a max-heap of the lower half of values seen so far, a min-heap of the upper half. As new values arrive, push into the right heap and rebalance. The median is one peek away — never re-sort the stream.

### Heapsort

Build a heap from a list (O(n)), then pop n times (O(log n) each) collecting the values. Total: O(n log n) sort, in place. The same algorithm `heapq` runs is the engine of `heapsort` — a non-recursive O(n log n) sort that uses no extra memory.

---

## Common Pitfalls

### Pitfall 1: using a heap as if it were a BST

```python
# ❌ "Is x in the heap?" — O(n) scan, no shortcut.
if x in nums:
    ...
```

The heap property tells you nothing about non-root values. If you need fast lookup AND fast pop-min, you need a hybrid (heap + hash) or a self-balancing BST. A bare heap is not a search structure.

### Pitfall 2: forgetting that heapq is min-only

```python
# ❌ Trying to get the max:
nums = [5, 3, 8, 1]
heapq.heapify(nums)
print(nums[0])               # prints 1 — the MIN, not the max
```

Negate the values, push `-x`, peek `-nums[0]`. Or use `heapq.nlargest(1, nums)[0]` for a one-shot max.

### Pitfall 3: mutating a list that something else is reading

```python
# ❌ heapify mutates in place — the caller's list is now reordered.
def kth_smallest(nums, k):
    heapq.heapify(nums)
    for _ in range(k - 1):
        heapq.heappop(nums)
    return nums[0]
# The caller's `nums` is now a heap — and shorter by k-1 elements.
```

If the caller expects `nums` to stay unchanged, take a copy at the top: `heap = list(nums)`. Then mutate `heap`, not `nums`.

### Pitfall 4: tuples with non-orderable second elements

```python
# ❌ heapq breaks when two priorities tie and the second elements
#    are not comparable:
queue = [(1, customer_obj_1), (1, customer_obj_2)]
heapq.heapify(queue)         # TypeError: '<' not supported between
                             # instances of 'Customer' and 'Customer'
```

When ties are possible, add a tiebreaker as the second element: a counter, an arrival timestamp, anything ordered. Pattern: `(priority, counter, payload)`.

---

## Summary

| Concept | What it does | When to use | Key rule |
|---------|--------------|-------------|----------|
| Priority queue | Returns the highest-priority element next | Schedulers, top-K, Dijkstra, ER triage | Order is by priority, not by arrival |
| Min-heap | Complete tree, parent ≤ children | When you need the smallest fast | Root is the min, O(1) to peek |
| Max-heap | Complete tree, parent ≥ children | When you need the largest fast | Same shape, opposite rule |
| Array storage | Indexes encode parent/child relations | Always — no pointers needed | parent (i-1)//2, children 2i+1 and 2i+2 |
| Push / Pop | Bubble up / bubble down | Add or remove from the heap | Both O(log n), height-bounded |
| `heapq` module | Min-heap on plain lists | Almost every time in Python | Use negatives for a max-heap |
| Top-K | `nlargest` / `nsmallest` | When K is small relative to n | O(n log k) instead of O(n log n) |
