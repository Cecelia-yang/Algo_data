# Understanding Big-O Notation

> Big-O is the language we use to talk about algorithm speed — not in seconds, but in **growth**.

---

## What is Big-O?

Imagine you're at the library looking for a specific book. You have two options:

1. Walk every shelf, pulling out books one by one until you find it.
2. Go to the catalogue, look up the call number, walk straight to it.

Both work. On a library of 10 books, the difference is invisible. On a library of 10 million books, one approach is your weekend, the other is 30 seconds.

**Big-O is the notation that captures this kind of difference.** It answers ONE question:

> *"As the input gets really, really big, how does the work grow?"*

Three things to keep in mind from the start:

- Big-O does **not** measure seconds. It measures the *shape* of growth.
- A laptop and a supercomputer running the same O(n) algorithm both slow down the same way when n doubles — the supercomputer is just faster at every step.
- We always think about the **worst case** unless told otherwise.

The smallest possible example:

```python
def first_user(users):
    return users[0]
# Whether `users` has 10 entries or 10 million,
# this is one read. That's O(1).
```

That's our starting point. Now let's meet the five Big-O classes you must know by heart this semester.

---

## The Five Classes

| Notation | Name | The intuition |
|---|---|---|
| **O(1)** | constant | The work doesn't depend on n |
| **O(log n)** | logarithmic | The work is **halved** each step |
| **O(n)** | linear | You touch every element once |
| **O(n log n)** | quasi-linear | The "smart" sorts (next phase) |
| **O(n²)** | quadratic | Two nested loops over the same data |

We'll walk each of them with a small example.

### O(1) in detail — constant time

The work is the same whether n is 5 or 5 billion. You go directly to the answer.

```python
users[42]                # direct index access
profile["name"]          # dict lookup
stack.append(comment)    # append to the end of a Python list
```

Mental image: you have an exact address, you go straight there. There is no walking around.

### O(n) in detail — linear time

You touch every element once. Double the input, double the work.

```python
def total_likes(comments):
    s = 0
    for c in comments:           # ← one loop over n elements
        s += c.likes
    return s
```

If `comments` has 1,000 entries → 1,000 reads. If it has 1,000,000 → 1,000,000 reads. Linear: the line on a graph is a straight line going up.

### ❌ Without binary search:
```python
def find_user(users, target_id):
    for i, u in enumerate(users):       # one loop over n
        if u.id == target_id:
            return i
    return -1
```
This works, but: on a list of 1,000,000 users, the worst case is 1,000,000 comparisons. That's O(n).

### ✅ With binary search (next section):
```python
def find_user(users, target_id):    # users sorted by id
    low, high = 0, len(users) - 1
    while low <= high:
        mid = (low + high) // 2
        if users[mid].id == target_id: return mid
        if target_id < users[mid].id:  high = mid - 1
        else:                          low  = mid + 1
    return -1
```
On the same 1,000,000 users, this finishes in **about 20 reads**. That's O(log n).

### O(log n) in detail — logarithmic time

The work is **halved at every step**. This is the most counter-intuitive class — and the most beautiful.

Imagine a paper dictionary with 1024 pages. You're looking for the word *"monkey"*:

1. Open the middle page (page 512). It says *"kangaroo"* → too early. **Throw away the left half.** 512 pages left.
2. Open the middle of what's left (page 768). *"platypus"* → too late. **Throw away the right.** 256 pages left.
3. Repeat.

After cut 1: 512 pages. After cut 2: 256. After cut 3: 128. After cut 10: **1 page left**.

You found a word in a 1024-page dictionary in 10 reads. That's the logarithm in action: log₂(1024) = 10. log₂(1,000,000) ≈ 20.

```python
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target: return mid
        if lst[mid] < target:  low  = mid + 1
        else:                  high = mid - 1
    return -1
```

The clue that an algorithm is O(log n): a loop where you **cut the work in half** at each step. The hard requirement: **the list must be sorted**. Without sorting, the "go left or go right" decision is meaningless — there's no guarantee the target is in the half you keep.

### O(n²) in detail — quadratic time

Two nested loops over the same data. For each element, you walk the whole thing again.

```python
def all_pairs(comments):
    pairs = []
    for a in comments:           # outer loop over n
        for b in comments:       # inner loop ALSO over n
            pairs.append((a, b))
    return pairs
```

Double n → 4× the work. Triple n → 9× the work. On 1,000,000 items: 10¹² operations, about **30 hours of compute** at one nanosecond per step.

This is the speed of bubble sort, of selection sort, of "compare every pair". **This is what we want to avoid on large data.**

### O(n log n) in detail — quasi-linear time

The speed of "smart" sorts: merge sort and quick sort. We'll meet them in Phase 4.

To put numbers on it, on a list of 1,000,000:
- O(n²) bubble sort: ~30 hours
- O(n log n) merge sort: ~20,000,000 steps → a fraction of a second

Much better than O(n²), almost as good as O(n). Don't worry about the maths now — we'll dig in when we cover divide-and-conquer.

---

## How to Read Big-O from Code

You don't compute Big-O with a formula. You **read** it. The trick is to look at the loops.

```python
def f(comments):                  # ONE loop over n
    for c in comments:
        print(c.text)
# → O(n)
```

```python
def f(comments):                  # NESTED loops over n
    for a in comments:
        for b in comments:
            print(a, b)
# → O(n²)
```

```python
def f(comments):                  # ONE loop, work cut in half
    low, high = 0, len(comments)-1
    while low <= high:
        mid = (low + high) // 2
        ...
# → O(log n)
```

```python
def f(comments):                  # NO loop, just direct access
    return comments[0]
# → O(1)
```

### ❌ Common trap: thinking "two loops" always means O(n²)

```python
def f(comments):
    for c in comments: print(c)            # loop A: O(n)
    for c in comments: print(c.replies)    # loop B: O(n)
```

Two loops, but they're **side-by-side**, not nested. Total: O(n) + O(n) = O(2n) = **O(n)**. Big-O drops constants — 2n grows the same shape as n.

### ✅ The simple rule:
- **Nested** loops over the same n → **multiply** (n × n = n²)
- **Side-by-side** loops over n → **add** (n + n = 2n, drop the constant → n)

When you read a function, count the loops, look at how they're stacked, and you have your Big-O 80% of the time.

---

## Why Big-O Matters — the speed gap is brutal

Imagine you're an engineer at ByteDance. You build a feature that finds a specific user in a list of 1,000,000 accounts. Two engineers write it differently:

- Engineer A uses naive search: O(n).
- Engineer B sorts the list once and uses binary search: O(log n).

Here's the same problem, on the same data, on the same machine:

| Operation | Complexity | Steps on 1,000,000 items | Wall-clock estimate |
|---|---|---|---|
| `lst[i]` direct access | O(1) | 1 | < 1 ns |
| Binary search | O(log n) | ~20 | < 1 µs |
| Naive search | O(n) | up to 1,000,000 | ~10 ms |
| Bubble sort | O(n²) | ~10¹² | ~30 hours |

**20 vs 1,000,000.** Same problem. Same data. **50,000× faster**, purely by choosing the right algorithm.

Engineer B's feature feels instant. Engineer A's feature times out under load. This is not optimisation theatre — this is the difference between *"the page loads"* and *"the user closes the tab"*. This is the daily reality at ByteDance, Alibaba, Tencent.

You're going to **see this gap live in your terminal** in today's exercise. You'll write binary search, count its steps, then run a naive search on the same data. The numbers will speak for themselves.

---

## Connecting Back to ALGO I

You've already met every one of these classes last semester. Let's locate them:

| ALGO I topic | Big-O |
|---|---|
| Naive search in a list | O(n) |
| Binary search in a sorted list | O(log n) |
| Bubble sort, selection sort | O(n²) |
| Dict lookup `d[k]` | O(1) on average |
| `lst.append(x)` | O(1) |

What's new in ALGO II is **not new complexities** — it's the same five, in new clothes:

- **O(log n)** comes back on **trees** (BST search, heap operations).
- **O(n log n)** is the speed of **merge sort and quick sort** (Phase 4).
- We'll meet algorithms that fall from O(2ⁿ) (catastrophic) to O(n) (sane) using **memoization** — the most magical moment of the semester.

Recognise the same five, in new structures. That's all.

---

## Common Pitfalls

### Pitfall 1: Confusing Big-O with seconds

```python
# ❌ Wrong reasoning:
"My function takes 2 seconds, so it's O(2)."
```

Big-O has nothing to do with seconds. O(2) is not even a Big-O class. Big-O describes **how the work grows when n grows** — independent of your machine's speed.

```python
# ✅ The right question:
"If I double the input, does the work stay the same (O(1)),
 double (O(n)), barely change (O(log n)), or quadruple (O(n²))?"
```

### Pitfall 2: Binary search on an unsorted list

```python
# ❌ This will return wrong answers:
users = [User(id=42), User(id=7), User(id=99), User(id=3)]   # unsorted
binary_search(users, target_id=7)
```

Binary search works **only because the list is sorted**. On an unsorted list, "go left or go right" is a coin flip — the target may not be in the half you keep.

```python
# ✅ Three correct options:
# 1. Sort once (O(n log n)), then binary search (O(log n)) every time
# 2. Use naive search (O(n) every lookup, no sorting)
# 3. Put the data in a dict (O(1) per lookup, if you can key by id)
```

### Pitfall 3: Two loops ≠ O(n²)

```python
# ❌ Looking at this and concluding "O(n²)":
for c in comments: print(c.text)
for c in comments: print(c.replies)
```

These loops are **side-by-side**, not nested. Total: O(n) + O(n) = O(n). Read carefully: **nested vs sequential** is the distinction that matters.

### Pitfall 4: Off-by-one in binary search

```python
# ❌ A version that infinite-loops:
low, high = 0, len(lst)
while low < high:
    mid = (low + high) // 2
    if lst[mid] == target: return mid
    if lst[mid] < target: low = mid       # ← bug: should be mid + 1
    else: high = mid
```

When `lst[mid] < target` and you set `low = mid` (not `mid + 1`), the window doesn't shrink — `mid` stays the same, you re-check the same element forever.

```python
# ✅ The two correct moves:
low  = mid + 1   # we already checked mid, exclude it
high = mid - 1   # same — mid is no longer a candidate
```

The general rule: after checking `lst[mid]`, **exclude it from the next window**. That's how the window keeps shrinking.

---

## Summary

| Class | Name | What it means | Typical example | Steps on 1M items |
|---|---|---|---|---|
| **O(1)** | constant | Work doesn't depend on n | `lst[i]`, `d[k]` | 1 |
| **O(log n)** | logarithmic | Work cut in half each step | Binary search, BST search | ~20 |
| **O(n)** | linear | Touch every element once | Naive search, sum of list | 1,000,000 |
| **O(n log n)** | quasi-linear | Smart sorts | Merge sort, quick sort | ~20,000,000 |
| **O(n²)** | quadratic | Nested loops over same n | Bubble sort, all pairs | 10¹² (30 h) |

**The reading reflex** — when you read code, count the loops:

- One loop over n → **O(n)**
- Nested loops over n → **O(n²)**
- One loop, work halved each step → **O(log n)**
- No loop, direct access → **O(1)**
- Two loops side-by-side → still **O(n)** — drop the constant

**The binary search skeleton** — memorise the shape, you'll reuse it on BSTs in three weeks:

```python
low, high = 0, len(lst) - 1
while low <= high:
    mid = (low + high) // 2
    if lst[mid] == target: return mid
    if target < lst[mid]:  high = mid - 1     # search left
    else:                  low  = mid + 1     # search right
return -1
```

Today's exercise will make all of this concrete. You'll write iterative binary search by hand, then add a step counter and watch your terminal print **~20 vs ~200,000** for the same problem. That number is Big-O made visible.
