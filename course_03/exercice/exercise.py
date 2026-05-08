# COURSE 03 EXERCISES - Hash tables + a taste of recursion
# "From O(n²) to O(n) for free — and the first real recursive function."


# ██████████████████████████████
# PART 1 - Your first recursive function
# ██████████████████████████████

# A recursive function calls itself. It needs a BASE CASE (returns
# directly, no recursion) and a RECURSIVE CASE (calls itself on a
# smaller input). Reflex: write the base case first.
#
# factorial(n) = n × (n-1) × ... × 2 × 1.   factorial(0) = 1.


def factorial(n):
    # TODO
    pass


# --- Tests for Part 1 ---
print(factorial(0))         # Expected: 1
print(factorial(1))         # Expected: 1
print(factorial(5))         # Expected: 120
print(factorial(10))        # Expected: 3628800



# ██████████████████████████████
# PART 2 - Counting with a dict (word_count)
# ██████████████████████████████

# Walk the words once and count occurrences in a dict.
# Tools: `text.split()`, `dict.get(key, default)`.


def word_count(text):
    # TODO: return a dict {word: count}
    pass


# --- Tests for Part 2 ---
print(word_count(""))                                                              # Expected: {}
# print(sorted(word_count("hello hello hello").items()))                           ← UNCOMMENT after implementing word_count
# # Expected: [('hello', 3)]
# text = "the quick brown fox the lazy dog the quick brown fox"                   ← UNCOMMENT after implementing word_count
# print(sorted(word_count(text).items()))                                          ← UNCOMMENT after implementing word_count
# # Expected: [('brown', 2), ('dog', 1), ('fox', 2), ('lazy', 1), ('quick', 2), ('the', 3)]



# ██████████████████████████████
# PART 3 - The two-sum wow moment (O(n²) → O(n))
# ██████████████████████████████

# Given nums and target, find i < j such that
# nums[i] + nums[j] == target. Return (i, j), or None.
#
# Constraint: ONE pass through the list, using a dict.
# As you walk through nums, ask yourself: "have I already seen
# the value that, added to x, gives target?"
#
# Tools: `enumerate(nums)`, a dict mapping value → index.
# Beware: an element must not pair with itself.


def two_sum(nums, target):
    # TODO
    pass


# --- Tests for Part 3 ---
print(two_sum([2, 7, 11, 15], 9))    # Expected: (0, 1)   (2 + 7 = 9)
print(two_sum([3, 2, 4], 6))          # Expected: (1, 2)   (2 + 4 = 6)
print(two_sum([3, 3], 6))             # Expected: (0, 1)
print(two_sum([1, 2, 3], 10))         # Expected: None
print(two_sum([], 5))                  # Expected: None



# ██████████████████████████████
# BONUS - if you finish early
# ██████████████████████████████

# B1) char_count(s)
#     Same as word_count but counts CHARACTERS instead of words.
#     Example: char_count("banana") -> {'b': 1, 'a': 3, 'n': 2}
#     (Same pattern as word_count, just iterate over s instead of
#      s.split().)
#
# B2) most_frequent(text)
#     Return the word that appears the most often in `text`. If
#     several are tied, return any one of them.
#     Hint: call word_count first. Then walk d.items() with a
#     small for-loop tracking the best word seen so far.
#     Example: most_frequent("the cat the dog the fox") -> "the"
#
# B3) Watch the speed gap.
#     Add a step counter to BOTH two_sum (the dict version above) and
#     two_sum_naive (the nested-loops version). Run both on a list
#     of 10_000 numbers and print the step counts.
#     You should see ~10_000 vs ~50_000_000. Same WOW as Class 01.
