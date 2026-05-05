# COURSE 01 EXERCISES - CORRECTIONS
# Big-O wake-up


# ████████████████████████████████████████████████████
# PART 1 - Iterative binary search
# ████████████████████████████████████████████████████


def binary_search_iter(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        if target < lst[mid]:
            high = mid - 1     # target is in the left half
        else:
            low = mid + 1      # target is in the right half
    return -1
# At each iteration the window [low, high] is divided in half.
# That's what makes this O(log n) instead of O(n).
# `mid + 1` and `mid - 1` are crucial — we already checked mid,
# so we exclude it. Skipping the +1/-1 is the classic infinite-loop bug.


# --- Tests ---
print(binary_search_iter([1, 3, 5, 7, 9, 11, 13], 7))    # Expected: 3
print(binary_search_iter([1, 3, 5, 7, 9, 11, 13], 4))    # Expected: -1
print(binary_search_iter([], 5))                          # Expected: -1
print(binary_search_iter([42], 42))                       # Expected: 0
print(binary_search_iter([1, 3, 5, 7, 9, 11, 13], 1))    # Expected: 0
print(binary_search_iter([1, 3, 5, 7, 9, 11, 13], 13))   # Expected: 6



# ████████████████████████████████████████████████████
# PART 2 - Counting the steps
# ████████████████████████████████████████████████████


def binary_search_count_steps(lst, target):
    low, high = 0, len(lst) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid, steps
        if target < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, steps
# Same logic as binary_search_iter, with `steps` bumped at the
# very top of each iteration so we count EVERY pass through the loop.


def naive_search_count_steps(lst, target):
    steps = 0
    for i, x in enumerate(lst):
        steps += 1
        if x == target:
            return i, steps
    return -1, steps


# --- Tests ---
arr = list(range(1_000_000))

idx, steps = binary_search_count_steps(arr, 198_308)
print(idx, "found in", steps, "steps  (binary search)")
# Expected: 198308 found in ~20 steps

idx, steps = naive_search_count_steps(arr, 198_308)
print(idx, "found in", steps, "steps  (naive search)")
# Expected: 198308 found in 198309 steps
#
# 20 vs 198,309. That's O(log n) vs O(n). ~10,000× faster on the same data.



# ████████████████████████████████████████████████████
# BONUS solutions
# ████████████████████████████████████████████████████


# B1) contains(lst, target) - True/False wrapper
def contains(lst, target):
    return binary_search_iter(lst, target) != -1
# Reuse the function you already wrote. -1 means "not found",
# anything else means "found at that index" → True.


print(contains([1, 3, 5, 7, 9], 5))     # Expected: True
print(contains([1, 3, 5, 7, 9], 4))     # Expected: False
print(contains([], 5))                   # Expected: False


# B2) Try with 10 million items
big = list(range(10_000_000))
idx, steps = binary_search_count_steps(big, 7_654_321)
print(idx, "found in", steps, "steps  (10M items)")
# Expected: ~24 steps. log₂(10_000_000) ≈ 23.25.
# 10× more data, just 4 more steps. THAT is what logarithmic means.


# B3) Watch binary stay flat as n grows
print()
print("size       binary steps")
for size in [1_000, 10_000, 100_000, 1_000_000]:
    a = list(range(size))
    target = size - 1                  # worst-ish case: end of the list
    _, b_steps = binary_search_count_steps(a, target)
    print(size, "       ", b_steps)
# n is multiplied by 10 each row. Binary steps grow by ~3 each time.
# That's the shape of log n: it barely moves while n explodes.
