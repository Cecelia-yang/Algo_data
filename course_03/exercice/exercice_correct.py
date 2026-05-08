# COURSE 03 EXERCISES - CORRECTIONS
# Hash tables + a taste of recursion


# ████████████████████████████████████████████████████
# PART 1 - factorial (recursion)
# ████████████████████████████████████████████████████


def factorial(n):
    if n == 0:                          # base case — STOP recursing
        return 1
    return n * factorial(n - 1)         # recursive case — smaller problem
# Reading order matters: the base case is what STOPS the recursion.
# Without it, Python keeps calling factorial(-1), factorial(-2), ...
# until it crashes with RecursionError.


# --- Tests ---
print(factorial(0))         # Expected: 1
print(factorial(1))         # Expected: 1
print(factorial(5))         # Expected: 120
print(factorial(10))        # Expected: 3628800



# ████████████████████████████████████████████████████
# PART 2 - word_count (dict counting pattern)
# ████████████████████████████████████████████████████


def word_count(text):
    d = {}
    for w in text.split():
        d[w] = d.get(w, 0) + 1
    return d
# `d.get(w, 0)` returns 0 when w is not yet a key, so the first
# occurrence becomes 0 + 1 = 1. Without .get(), you'd need an
# `if w in d: ... else: ...` branch — same logic, twice the lines.


# --- Tests ---
print(word_count(""))                                            # Expected: {}
print(sorted(word_count("hello hello hello").items()))           # Expected: [('hello', 3)]

text = "the quick brown fox the lazy dog the quick brown fox"
print(sorted(word_count(text).items()))
# Expected: [('brown', 2), ('dog', 1), ('fox', 2), ('lazy', 1), ('quick', 2), ('the', 3)]



# ████████████████████████████████████████████████████
# PART 3 - two_sum (the wow moment: O(n²) → O(n))
# ████████████████████████████████████████████████████


def two_sum(nums, target):
    seen = {}                              # value → index
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:             # O(1) dict lookup
            return (seen[complement], i)
        seen[x] = i                        # record AFTER checking
    return None
# Why "check first, record after": if x equals target/2 exactly and
# we recorded x first, the complement (also x) would already be in
# seen — we'd return (i, i), pairing x with itself. Wrong.


# --- Tests ---
print(two_sum([2, 7, 11, 15], 9))    # Expected: (0, 1)   (2 + 7 = 9)
print(two_sum([3, 2, 4], 6))          # Expected: (1, 2)   (2 + 4 = 6)
print(two_sum([3, 3], 6))             # Expected: (0, 1)
print(two_sum([1, 2, 3], 10))         # Expected: None
print(two_sum([], 5))                  # Expected: None



# ████████████████████████████████████████████████████
# BONUS solutions
# ████████████████████████████████████████████████████


# B1) char_count - same pattern, on characters
def char_count(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
# Identical structure to word_count. The only change: iterate over `s`
# directly instead of `s.split()`. That's why we call this pattern
# "memorise it once, reuse it forever".


print(sorted(char_count("banana").items()))   # Expected: [('a', 3), ('b', 1), ('n', 2)]
print(char_count(""))                          # Expected: {}


# B2) most_frequent - compose word_count + a max-tracking walk
def most_frequent(text):
    counts = word_count(text)
    if not counts:
        return None
    best_word = None
    best_count = 0
    for w, c in counts.items():
        if c > best_count:
            best_word = w
            best_count = c
    return best_word
# Same "track the best so far" pattern as find_max from course 02 —
# just on dict items instead of linked-list nodes. Same walk, new shape.


print(most_frequent("the cat the dog the fox"))    # Expected: the
print(most_frequent("a b c"))                       # Expected: a (or b or c — all tied at 1)
print(most_frequent(""))                            # Expected: None


# B3) Watch the speed gap — same wow as Class 01
def two_sum_count_steps(nums, target):
    seen = {}
    steps = 0
    for i, x in enumerate(nums):
        steps += 1
        complement = target - x
        if complement in seen:
            return (seen[complement], i), steps
        seen[x] = i
    return None, steps


def two_sum_naive_count_steps(nums, target):
    steps = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            steps += 1
            if nums[i] + nums[j] == target:
                return (i, j), steps
    return None, steps


# Build a list of 10_000 numbers where the answer sits at the END
# (worst case): first 9_998 are zeros, last two add up to target.
nums = [0] * 9_998 + [3, 7]
target = 10
_, dict_steps = two_sum_count_steps(nums, target)
_, naive_steps = two_sum_naive_count_steps(nums, target)
print()
print(f"dict  version : {dict_steps:>12} steps")
print(f"naive version : {naive_steps:>12} steps")
# Expected (worst case): 10_000 vs ~50 million.
# That's the difference O(n) vs O(n²) makes on real-size data.
