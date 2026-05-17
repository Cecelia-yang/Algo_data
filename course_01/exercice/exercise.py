# COURSE 01 EXERCISES - Big-O wake-up
# "Same problem, same input, different complexity. Feel the gap."


# ██████████████████████████████
# PART 1 - Iterative binary search
# ██████████████████████████████

# Tools:     `//` (integer division), comparisons, while-loop, indexing
# Forbidden: lst.index(), `target in lst`, bisect, any module
# Return:    the index of target, or -1 if not found
#
# Strategy:  the list is SORTED. Don't scan left to right —
#            cut the search space in HALF every step.
#
# Hints:
#   - keep two pointers `low` and `high` bounding the search range
#   - each step, look at the MIDDLE element (use `//` for integer division)
#   - depending on how middle compares to target, eliminate one half
#   - stop when low and high cross — target isn't there


def binary_search_iter(lst, target):
    low, high = 0, len(lst) - 1 
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1
    return -1

# --- Tests for Part 1 ---
print(binary_search_iter([1, 3, 5, 7, 9, 11, 13], 7))    # Expected: 3
print(binary_search_iter([1, 3, 5, 7, 9, 11, 13], 4))    # Expected: -1
print(binary_search_iter([], 5))                          # Expected: -1
print(binary_search_iter([42], 42))                       # Expected: 0
print(binary_search_iter([1, 3, 5, 7, 9, 11, 13], 1))    # Expected: 0
print(binary_search_iter([1, 3, 5, 7, 9, 11, 13], 13))   # Expected: 6



# ██████████████████████████████
# PART 2 - Counting the steps
# ██████████████████████████████

# Same logic as binary_search_iter, but with a step counter.
# Increment `steps` ONCE per while-loop iteration.
# Return a tuple (index, steps) — index is -1 if not found.
#
# Goal: feel O(log n) vs O(n) live in your terminal.


def binary_search_count_steps(lst, target):
    low, high = 0, len(lst)-1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid, steps
        if target < lst[mid]:
            high = mid -1
        else:
            low = mid + 1
    return -1, steps


# Already done for you — naive linear search with a step counter.
def naive_search_count_steps(lst, target):
    steps = 0
    for i, x in enumerate(lst):
        steps += 1
        if x == target:
            return i, steps
    return -1, steps


# --- Tests for Part 2 ---
arr = list(range(1_000_000))                # [0, 1, 2, ..., 999_999]

idx, steps = binary_search_count_steps(arr, 198_308)            
print(idx, "found in", steps, "steps  (binary search)")         
# # Expected: 198308 found in around 20 steps

idx, steps = naive_search_count_steps(arr, 198_308)
print(idx, "found in", steps, "steps  (naive search)")
# Expected: 198308 found in 198309 steps
#
# Once both are implemented you'll see ~20 vs ~198,309.
# Same problem, same input — that's O(log n) vs O(n).



# ██████████████████████████████
# BONUS - if you finish early
# ██████████████████████████████

# B1) contains(lst, target)
#     A True/False wrapper around your binary_search_iter.
#     Example: contains([1, 3, 5, 7], 3) -> True
#              contains([1, 3, 5, 7], 4) -> False
def contains(lst, target):
    return binary_search_iter(lst, target)  != -1

print(contains([1, 3, 5, 7], 3))
print(contains([1, 3, 5, 7], 4))

#
# B2) Try a BIGGER list.
#     Build a list of 10_000_000 items and call binary_search_count_steps
#     on it. How many steps now?
#     (Spoiler: only ~24 — just 4 more steps for 10× more data.)

big = list(range(10_000_000))
idx, steps = binary_search_count_steps(big, 7_654_321)
print(idx, "found in", steps, "steps  (10M items)")

# B3) Watch binary stay flat as n grows.
#     For each size in [1_000, 10_000, 100_000, 1_000_000]:
#       - call binary_search_count_steps on list(range(size))
#       - print the size and the step count.
#     You should see something like 10, 14, 17, 20.

for size in [100, 1000, 10000, 100000]:
    lst = list(range(size))
    target = size - 1 
    idx, steps = binary_search_count_steps(lst, target)
    print(idx, "found in", steps, "steps  (10M items)")
