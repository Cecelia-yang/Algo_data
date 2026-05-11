# Understanding Recursion

> A function that calls a smaller version of itself, with a clear rule for when to stop.

---

## What is Recursion?

Imagine a stack of nested boxes. Each box might contain another box, which might contain another, until you reach a tiny box with a marble inside. To find the marble, you don't need a different procedure for each level — you just need one rule: *"if this box has a smaller box inside, open it; otherwise, give me what's there."* That single rule, applied over and over to smaller and smaller things, is recursion.

A **recursive function** is a function that calls itself on a *strictly smaller* input. To work, it needs two pieces:

- A **base case** — a condition where the function returns directly, without calling itself. This is what stops the recursion. Without it, you crash with `RecursionError`.
- A **recursive case** — a call to the same function on a smaller piece of the problem.

The simplest recursive function in Python is `factorial`. Mathematically, `n! = 1 × 2 × ... × n`, with the convention `0! = 1` (the neutral element of multiplication). For example, `4! = 24` and `5! = 120`. Because `n! = n × (n−1)!`, the function nearly writes itself:

```python
def factorial(n):
    if n == 0:
        return 1                    # base case: stops the recursion
    return n * factorial(n - 1)     # recursive case: shrinks toward 0
```

Every recursive function in this course follows this exact two-line shape. Memorize it now.

---

## The Call Stack in Detail

When `factorial(4)` runs, Python does **not** evaluate all four calls in parallel. It runs them one after another, and *remembers each one* on a structure called the **call stack**. The call stack is Python's pile of in-flight function calls — each call gets its own **frame**, with its own local variables, and the frame stays on the stack until that call returns.

Trace `factorial(4)` in your head:

```
factorial(4) calls factorial(3) and pauses.
factorial(3) calls factorial(2) and pauses.
factorial(2) calls factorial(1) and pauses.
factorial(1) calls factorial(0) and pauses.
factorial(0) hits the base case → returns 1.
factorial(1) wakes up: 1 * 1 = 1 → returns 1.
factorial(2) wakes up: 2 * 1 = 2 → returns 2.
factorial(3) wakes up: 3 * 2 = 6 → returns 6.
factorial(4) wakes up: 4 * 6 = 24 → final answer.
```

Two phases. **Going down**, each call stacks on top, paused, waiting for the smaller one. **Coming back up**, values bubble back, each level finishing its `*` or `+` and handing the result to the frame below.

A consequence: each frame keeps its **own** `n`. When `factorial(2)` runs the multiplication, its `n` is 2, regardless of what happens in the other frames. Python keeps them strictly separate. That separation is the entire reason recursion works.

A second consequence: the call stack has a hard ceiling. By default, Python allows about 1000 frames at once. If you forget the base case (or never reach it), you'll see `RecursionError: maximum recursion depth exceeded`. That isn't a Python bug — it's Python protecting your computer's memory.

That covers what recursion *is*. The next question is *how to write one that works*.

---

## The Skeleton — Three Questions

Every recursive function in this course collapses to the same three-line skeleton:

```python
def f(input):
    if <base case>:                                    # 1) when do we stop?
        return <neutral value>                         # 2) what do we return then?
    return <combine>(<current>, f(<smaller input>))   # 3) how do we shrink?
```

Three questions answer it:

1. **When do we stop?** For `factorial`: when `n == 0`. For walking a list: when the list is empty. For walking linked nodes: when `node is None`.
2. **What do we return at the bottom?** The *neutral element* of whatever you're combining. Multiplication → `1`. Addition → `0`. List building → `[]`.
3. **How do we shrink?** What is the smaller version of the input? `n - 1`, `lst[1:]`, `node.next`, or "the left half of the window" — pick what makes the input strictly smaller.

If you can answer those three questions in plain words, you have written the function. Always **write the base case first**, before the recursive call. That ordering is your safety net against bug #1.

---

## The Three Patterns

Recursion looks scary because it feels like one giant idea. It isn't. It's three small ideas. Once you recognize the pattern, the code writes itself.

### Pattern 1 — Decrement

The input shrinks by one each call, heading down to 0. The simplest shape, used for purely numeric recursions:

```python
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
# count_digits(98765) → 5
```

`n // 10` is integer division — it chops the last digit. Each call works on a strictly smaller number, and after at most ~`log₁₀(n)` calls we hit a single digit. *Reflex sentence:* "I handle the current step, I pass a slightly smaller version to a smaller me."

### Pattern 2 — Walk

The input is a structure (a list, a chain of nodes, later a tree). Each call processes ONE element and recurses on the REST.

```python
# ❌ Without recursion (iterative version, fine but more lines):
def sum_list_iter(lst):
    total = 0
    for x in lst:
        total += x
    return total

# ✅ With recursion (the walk pattern):
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])
```

The same pattern works on linked nodes — replace `not lst` with `node is None` and `lst[1:]` with `node.next`:

```python
def length_recursive(node):
    if node is None:
        return 0
    return 1 + length_recursive(node.next)
```

**Same skeleton, two vehicles.** This is exactly why we drilled the linked-list walk in Class 02 — it's now a recursive walk. And next class, this same shape will work on trees, except we'll recurse on `node.left` *and* `node.right` instead of just `node.next`.

A small note on `lst[1:]`: in Python, slicing creates a new list. It is not a free operation. For huge lists, the iterative version is faster. The point of the recursive version today is the *shape*, which prepares you for trees, where iteration is much harder.

### Pattern 3 — Divide

At each step, you split the problem and keep going on only ONE half. The classic example is binary search on a sorted list:

```python
def binary_search_rec(lst, target, low=None, high=None):
    if low is None:
        low, high = 0, len(lst) - 1     # first call: full window
    if low > high:
        return -1                        # base case: empty window
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    if target < lst[mid]:
        return binary_search_rec(lst, target, low, mid - 1)
    return binary_search_rec(lst, target, mid + 1, high)
```

Each recursive call works on a window **half the size** of the previous one. After about `log₂(n)` calls, the window is empty. That's where the **O(log n)** comes from. We'll meet this exact pattern again on BSTs (Class 07) and merge sort / quick sort (Classes 15–16).

---

## A Note on Big-O — Drop the Constants

You'll often want to count exact recursive calls. For `factorial(n)`, there are `n+1` calls (from `n` down to `0`). For `sum_list` of a list of length `n`, there are `n+1` calls. Tempting answer: `O(n+1)`.

In Big-O, **we drop the constants and lower-order terms.** `O(n+1)` simplifies to `O(n)`. `O(2n + 5)` simplifies to `O(n)`. `O(n² + n)` simplifies to `O(n²)`. Big-O describes the *growth rate* as `n` becomes large, not the exact number of operations. Past a certain size, the constants are noise.

For recursive functions, always state **both** complexities:

- **Time** complexity = number of calls × work per call.
- **Space** complexity = the deepest the call stack gets. Each paused frame takes memory.

For `factorial(n)`: time is O(n), space is O(n) (because all `n` frames stack up before the first return). For `binary_search_rec`: time is O(log n), space is O(log n). Forget the space complexity and you'll be surprised on the exam.

---

## Why Does It Matter?

Recursion is the only natural way to express problems whose structure is recursive — and most interesting structures *are*. A file system contains files and folders, where each folder contains... files and folders. A comment thread is a comment plus a list of replies, where each reply is itself... a comment plus a list of replies. A binary tree has a root and two children, where each child is itself... a binary tree.

Try writing "count every file under this folder" iteratively. You end up reinventing a stack by hand and pushing folders onto it as you find them. Now write it recursively:

```python
def count_files(folder):
    if folder is None:
        return 0
    total = len(folder.files)
    for sub in folder.subfolders:
        total += count_files(sub)
    return total
```

Five short lines. The recursion *is* the structure. Your code mirrors the shape of the data.

That's the bet of the next 5 weeks: trees, BSTs, heaps, traversals — every meaningful operation will be recursive. The pattern you typed today on a chain (`length_recursive(node.next)`) becomes, almost letter-for-letter, the pattern on a tree (`count_nodes(node.left) + count_nodes(node.right)`).

---

## Practical Examples

A real-world example — pricing a customer's order with bundled items:

```python
def total_price(item):
    if not item.children:
        return item.price                # base case: leaf item
    return item.price + sum(total_price(c) for c in item.children)
```

A bundle is an item containing children. Children may themselves be bundles. The recursive case naturally handles any nesting depth — a gift basket containing a gift basket containing two pens.

Another — flattening a nested comment thread for display:

```python
def flatten(comment, depth=0):
    rows = [(depth, comment.text)]
    for reply in comment.replies:
        rows.extend(flatten(reply, depth + 1))
    return rows
```

The `depth` parameter is how recursion can carry context downward without globals — each frame has its own `depth`, exactly like each `factorial` frame had its own `n`.

---

## Common Pitfalls

### Pitfall 1: Missing base case

```python
# ❌ What people try:
def factorial(n):
    return n * factorial(n - 1)

# Symptom: RecursionError: maximum recursion depth exceeded
```

The function never stops. Even for `factorial(0)`, it tries `factorial(-1)`, `factorial(-2)`, and so on until Python's limit. **Fix:** write the base case `if n == 0: return 1` *before* the recursive call. Always.

### Pitfall 2: Missing `return`

```python
# ❌ What people try:
def factorial(n):
    if n == 0:
        return 1
    n * factorial(n - 1)            # ← result is computed then thrown away

# Symptom: factorial(5) returns None. No error message.
```

The recursive call did its job — the multiplication happened — but the result wasn't sent back. The whole point of a `return` value is to bubble back up the stack. **Fix:** add `return` in front of the recursive call.

### Pitfall 3: Wrong direction

```python
# ❌ What people try:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n + 1)     # ← growing instead of shrinking

# Symptom: RecursionError again, because n never reaches 0.
```

The base case exists, but the input moves *away* from it. The reflex check: *"What shrinks at each call?"* If nothing shrinks, you're racing toward infinity. **Fix:** verify that every recursive call is on a strictly smaller (or strictly closer-to-base) input.

### Pitfall 4: Mutating a shared default

```python
# ❌ What people try:
def collect_evens(lst, result=[]):
    if not lst:
        return result
    if lst[0] % 2 == 0:
        result.append(lst[0])
    return collect_evens(lst[1:], result)

# Symptom: the FIRST call works. The SECOND call returns the leftovers from the first.
```

The default `result=[]` is built **once**, when the function is defined, and shared by every call that doesn't pass an explicit `result`. So `collect_evens([2, 4])` then `collect_evens([1, 3])` returns `[2, 4]` instead of `[]`. **Fix:** use `result=None`, then inside the function `if result is None: result = []`. Same idea is used in `binary_search_rec` with `low=None, high=None`.

---

## Summary

| Concept | What it does | When to use | Key rule |
|---|---|---|---|
| Base case | Stops the recursion by returning directly | First line of every recursive function | Write it FIRST, before the recursive call |
| Recursive case | Calls the function on a strictly smaller input | After the base case, on the way back up | Must `return` the result |
| Call stack | Python's pile of paused calls, one frame each | Always — implicit | Limited to ~1000 frames; space complexity = max depth |
| Decrement pattern | Shrinks input by one numerically | `factorial`, `count_digits`, `count_down` | Stop when input hits 0 (or single-digit) |
| Walk pattern | Processes one element + recurses on the rest | Lists, linked nodes, trees (next class) | Base = empty / `None`; combine current with rest |
| Divide pattern | Splits the problem, keeps one half | Binary search, BST search, merge/quick sort | Base = empty window; recurse on one half only |
| Big-O simplification | `O(n+1) → O(n)`, `O(2n+5) → O(n)`, `O(n²+n) → O(n²)` | Whenever you state complexity | Drop constants, keep the dominant term |
| Time vs space | Time = #calls × work; space = max stack depth | Always state both for recursion | Forgetting space complexity is the classic exam trap |
