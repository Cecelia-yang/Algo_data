# Understanding Hash Tables (and a Taste of Recursion)

> Two ideas. The big one: a hash table turns *"scan the rest"* into *"ask once"* — O(n²) becomes O(n) for free. The small one: a function can call itself.

---

## What Is a Hash Table?

Imagine you walk into a hotel reception and ask whether a guest named "Adnan" is staying tonight.

The slow way: the receptionist walks the registry line by line until they find your name. With 1,000 guests, worst case is 1,000 reads.

The fast way: the receptionist has a board of letter slots. Names starting with "A" go in slot A, "B" in slot B, and so on. They look at slot A, check the few names there, and answer in **constant time** — no matter how big the hotel.

That's a **hash table**: a data structure that gives you the value associated with a key in **O(1) on average**. In Python, you've used one all year — it's called `dict`.

```python
d = {}
d["apple"] = 1
d["banana"] = 2
print(d["apple"])      # → 1, in O(1)
print("apple" in d)    # → True, in O(1)
del d["banana"]        # → O(1)
```

Insert, lookup, membership, delete — all O(1) on average. **That is the magic.**

### How does it work, in 30 seconds?

Internally, a dict is just an array. When you say `d["apple"] = 1`:

1. Python computes `hash("apple")` — a function that turns the string into a number.
2. It takes that number modulo the size of the array → an **index**.
3. It puts the pair `("apple", 1)` at `array[index]`.

When you later read `d["apple"]`, Python redoes the same math and goes **directly** to the index. No scanning.

The "average" disclaimer: two different keys can land on the same index — a **collision**. The dict handles collisions internally, but in pathological cases lookup can degrade. With Python's built-in dict on regular keys, you can trust O(1).

| Operation | List | Dict |
|---|---|---|
| `x in container` | O(n) | O(1) |
| Get value for key | — | O(1) |
| Insert | O(1) at end | O(1) |

That table is the whole reason dicts exist. Anywhere a list would force you to scan, a dict gives you a direct hit.

---

## The Counting Pattern

The most common use of a dict in real code: **counting things**. How many times each word appears in an article. How many requests came from each IP address. How many of each item is in a shopping cart.

The pattern fits in three lines:

```python
def word_count(text):
    d = {}
    for w in text.split():
        d[w] = d.get(w, 0) + 1
    return d
```

Read the third line carefully:

- `d.get(w, 0)` → returns `d[w]` if `w` is already a key; otherwise returns `0`.
- `+ 1` → we just saw `w` once more.
- `d[w] = ...` → store the new count.

**Memorise this pattern.** You will write it 100 times this year.

### ❌ Without `.get()`:

```python
def word_count(text):
    d = {}
    for w in text.split():
        if w in d:
            d[w] = d[w] + 1
        else:
            d[w] = 1
    return d
```

This works, but: 5 lines instead of 3, and you have to write the "first time vs already seen" branch yourself.

### ✅ With `.get()`:

```python
d[w] = d.get(w, 0) + 1
```

Same logic, one line. The `0` is the default when the key is missing. The branching is hidden inside `.get()`.

**Why is this O(n)?** The loop runs n times (one per word). Every dict operation inside is O(1). Total: O(n). Doing the same with a list (scanning to count) would be O(n²).

---

## The Two-Sum Wow Moment — O(n²) → O(n)

Here's a classic problem. Given a list `nums` and a number `target`, find two indices `i < j` such that `nums[i] + nums[j] == target`.

```
nums = [2, 7, 11, 15], target = 9
→ 2 + 7 = 9 → return (0, 1)
```

### ❌ The naive way — O(n²)

The first reflex: try every pair. Two nested loops.

```python
def two_sum_naive(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None
```

Works. But on **100,000** numbers → about **5 billion** operations. Too slow for any real product.

### ✅ The hash table way — O(n)

ONE pass through the list. As we walk, we ask one question per element:

> *"Have I already seen `target - x` somewhere before?"*

If yes, we found the pair. If no, we remember `x` for the future.

To answer that question in O(1), we keep a dict `seen` mapping every value already encountered to its index.

```python
def two_sum(nums, target):
    seen = {}                              # value → index
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:             # O(1) lookup
            return (seen[complement], i)
        seen[x] = i                        # remember x for the future
    return None
```

100,000 numbers → 100,000 operations. **About 50,000× faster than the naive version**, on the same input.

This is the same kind of leap as binary search vs naive search from Class 01: replace *"scan the rest"* with *"check a dict in O(1)"* and watch O(n²) collapse into O(n). Different problem, same idea.

### When to reach for a dict — the reflex to build

> *"I'm about to write a nested loop. Wait — could I use a dict to remember things, and turn this into a single loop?"*

Often the answer is yes. Hash tables are not just storage. They're an **algorithmic weapon**.

---

## A Taste of Recursion

Now we change subject. The next class is the proper recursion deep dive — call stack, three patterns, classic bugs. Today is just one tiny function so the syntax feels familiar when we go deep.

### What is a recursive function?

A **recursive function** is a function that calls itself. To work, it needs two pieces:

1. A **base case** — a condition under which the function returns directly, without recursing. **Without it, the function runs forever and Python crashes.**
2. A **recursive case** — a smaller version of the same problem, calling the function again on simpler input.

### The classic example: factorial

`factorial(n) = n × (n-1) × ... × 2 × 1`. By convention, `factorial(0) = 1`.

The trick: notice that `factorial(n) = n × factorial(n-1)`. If you can compute the smaller one, you only need ONE multiplication for the bigger one.

```python
def factorial(n):
    if n == 0:                       # ← base case
        return 1
    return n * factorial(n - 1)      # ← recursive case
```

### Tracing it on `factorial(4)`:

```
factorial(4)
  → 4 * factorial(3)
         → 3 * factorial(2)
                → 2 * factorial(1)
                       → 1 * factorial(0)
                              → 1               ← base case hits!
                       → 1 * 1 = 1
                → 2 * 1 = 2
         → 3 * 2 = 6
  → 4 * 6 = 24
```

Each call **waits** for the next one to finish. Python keeps track of all the pending calls — that's called the **call stack**. We'll visualise it properly next class.

### Forgetting the base case = infinite recursion

```python
# ❌ No base case:
def factorial(n):
    return n * factorial(n - 1)
```

Python keeps calling: `factorial(0)`, `factorial(-1)`, `factorial(-2)`... until it hits the recursion limit and crashes:

```
RecursionError: maximum recursion depth exceeded
```

```python
# ✅ Base case first:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

**Reflex to build today**: when you write a recursive function, **write the base case FIRST**, before the recursive call.

### Don't try to fully understand recursion right now

If recursion still feels weird at the end of this class, that's **normal and expected**. Next class is fully dedicated to it — call stack visualised, three patterns, classical bugs. Today the only goal is: you've **typed** a recursive function once. The fingers know the shape. The deep understanding comes next.

---

## Common Pitfalls

### Pitfall 1: Reading `d[k]` when `k` is missing

```python
# ❌ KeyError on the first occurrence:
counts = {}
counts["fox"] = counts["fox"] + 1     # crash: KeyError: 'fox'
```

The first time you see "fox", `d["fox"]` doesn't exist — Python raises `KeyError`. This is exactly why the `.get()` pattern exists.

```python
# ✅ Default to 0 if the key is missing:
counts["fox"] = counts.get("fox", 0) + 1
```

### Pitfall 2: Forgetting the base case in recursion

```python
# ❌ No base case — infinite recursion:
def factorial(n):
    return n * factorial(n - 1)
```

Python crashes with `RecursionError: maximum recursion depth exceeded`. The function never stops calling itself.

```python
# ✅ Base case first:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

The reflex: when you start writing a recursive function, write `if <stop condition>: return <answer>` **first**. Then write the recursive call.

### Pitfall 3: Writing nested loops when a dict would do

```python
# ❌ O(n²) — scan the rest of the list at every step:
def two_sum_naive(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None
```

Two nested loops over n. On 100k items, about 5 billion operations.

```python
# ✅ O(n) — replace "scan" with "ask the dict":
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return (seen[target - x], i)
        seen[x] = i
    return None
```

The trigger: when you catch yourself writing a nested loop, ask if a dict could remember things and collapse the inner one.

### Pitfall 4: Forgetting the order in two-sum

```python
# ❌ Adding x to seen BEFORE checking the complement:
seen[x] = i                          # ← too early
if target - x in seen:               # x might match itself
    return (seen[target - x], i)
```

If you record `x` before checking, then for an input like `nums = [3, 4]`, `target = 6`, when `x = 3` you'd record it, then check if `6 - 3 = 3` is in `seen` — yes, the same 3 you just recorded! You'd return `(0, 0)` — same index twice. Wrong.

```python
# ✅ Check FIRST, record AFTER:
if target - x in seen:
    return (seen[target - x], i)
seen[x] = i
```

The current `x` should never see itself. Check before you record.

---

## Summary

| Concept | What it does | Complexity | When to use |
|---|---|---|---|
| Dict insert / lookup / membership | Map keys to values, hashed direct access | O(1) avg | Anywhere you'd otherwise "scan" or "remember" |
| `d[k] = d.get(k, 0) + 1` | Increment a counter, default 0 first time | O(1) per step | Counting occurrences of anything |
| Two-sum with a dict | Remember each value as you walk; check the complement | O(n) | When the naive solution is two nested loops |
| Recursive function | Function calls itself with simpler input | depends | When the problem has a self-similar shape |
| Base case | Condition that ends the recursion | O(1) | Always — write it FIRST |

The two reflexes to leave with:

- **"Nested loop? Could a dict collapse it?"** Most of the time, yes — and you save a factor of n.
- **"Recursive function? Write the base case FIRST."** Without it, Python crashes. With it, recursion feels almost magical.

Today you typed your first recursive function. Next class — the deep dive.
