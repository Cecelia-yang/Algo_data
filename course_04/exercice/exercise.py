# COURSE 04 EXERCISES — Recursion Deep Dive

# Reflex for every function in this file:
#   1) Write the BASE CASE first.
#   2) Make the recursive call on a STRICTLY SMALLER input.
#   3) RETURN every recursive result — silent `None` is bug #2.


# ██████████████████████████████
# PART 1 — Warm-ups (3 short functions to drill the reflex)
# ██████████████████████████████


# --- Exo 1.1 : repeat(message, n) ---
# Print `message` n times — each on its own line. Returns nothing.
# n is a non-negative int. repeat(msg, 0) prints nothing.
# Your job: one base case, one print, one recursive call.

def repeat(message, n):
    # TODO
    pass


print("=== Exo 1.1 ===")
repeat("hi", 3)
# Expected:
# hi
# hi
# hi



# --- Exo 1.2 : product_list(lst) ---
# Return the product of all integers in `lst`, recursively.
# NO `math.prod()`, NO loops. Empty list returns 1 (neutral of *).
#
# Hint: walk one element at a time. The "rest" of the list is
# `lst[1:]` — a new list without the first element. For example,
# if lst is [10, 20, 30], then lst[1:] is [20, 30]. The "head" is `lst[0]`. Pick the right neutral for the empty case.

def product_list(lst):
    # TODO
    pass


print("\n=== Exo 1.2 ===")
print(product_list([]))           # Expected: 1
print(product_list([7]))          # Expected: 7
print(product_list([2, 3, 4]))    # Expected: 24
print(product_list([1, 5, 2, 3])) # Expected: 30



# --- Exo 1.3 : digits_sum(n) ---
# Return the sum of the digits of a non-negative int n, recursively.
# NO str(n). digits_sum(0) is 0. digits_sum(7) is 7.
# digits_sum(123) is 1 + 2 + 3 = 6.
#
# Hint: `n % 10` is the last digit. `n // 10` chops it off and gives
# you the rest of the number. Stop when there is nothing left to
# chop — what value of n means "no digits left"?

def digits_sum(n):
    # TODO
    pass


print("\n=== Exo 1.3 ===")
print(digits_sum(0))     # Expected: 0
print(digits_sum(7))     # Expected: 7
print(digits_sum(123))   # Expected: 6
print(digits_sum(98765)) # Expected: 35



# ██████████████████████████████
# PART 2 — Recursion on linked nodes
# ██████████████████████████████
# This is the WALK pattern on a chain of nodes. Different vehicle
# from PART 1's Python lists: the structure is _Node objects, the
# shrink is `node.next`, the base case is `node is None`. Whatever
# you write here you will reuse on TREES next class with `node.left`
# and `node.right`.

# _Node class — given. DO NOT modify. You wrote this kind of class in Class 02.
class _Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Helper that builds a chain from a Python list — given. Useful for tests.
def build_chain(values):
    head = None
    for v in reversed(values):
        head = _Node(v, head)
    return head



# --- Exo 2.1 : contains_in_chain(node, target) ---
# Return True if any node in the chain starting at `node` has its
# `data` equal to `target`. Return False otherwise. An empty chain
# (node is None) returns False.
#
# Hint: walk one node at a time. There are two short-circuits where
# you can answer immediately without recursing — think about which.
# In every other case, the answer is whatever the rest of the chain
# reports.

def contains_in_chain(node, target):
    # TODO
    pass


print("\n=== Exo 2.1 ===")
print(contains_in_chain(None, 5))                          # Expected: False
print(contains_in_chain(build_chain([10, 20, 30]), 20))    # Expected: True
print(contains_in_chain(build_chain([10, 20, 30]), 99))    # Expected: False
print(contains_in_chain(build_chain([42]), 42))            # Expected: True



# --- Exo 2.2 : max_in_chain(node) ---
# Return the maximum `data` value in the chain. Assume the chain
# has at least one node — you do not need to handle the empty case.
#
# Hint: since the chain is non-empty, the base case is the simplest
# possible chain — what makes a chain "as small as it gets"? Once
# you have that, the recursive case combines the current node's
# data with the answer for the rest. Tool: `max(a, b)` returns the
# larger of two values.

def max_in_chain(node):
    # TODO
    pass


print("\n=== Exo 2.2 ===")
print(max_in_chain(build_chain([42])))             # Expected: 42
print(max_in_chain(build_chain([10, 20, 30])))     # Expected: 30
print(max_in_chain(build_chain([5, 99, 12, 7])))   # Expected: 99
print(max_in_chain(build_chain([-3, -1, -10])))    # Expected: -1




# ██████████████████████████████
# PART 3 — ⭐ STRETCH (Bonus — only after Core 1 + Core 2)
# ██████████████████████████████
# Skip this if you have not finished PART 1 and PART 2 cleanly.


# --- Exo 3.0 : count_nodes(node) ----
#let's start easy, count every node in recursive.

class _TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



def count_nodes(node):
    pass

# --- Tests Exo 9 ---
print("\n=== Exo 9 ===")
# Tree :         1
#              /   \
#             2     3
#            / \
#           4   5
tree = _TreeNode(1,
                 _TreeNode(2, _TreeNode(4), _TreeNode(5)),
                 _TreeNode(3))
print(count_nodes(tree))   # Expected: 5
print(count_nodes(None))   # Expected: 0



# This is the DIVIDE pattern. We'll meet it again with BST search (Class 07)
# and merge sort / quick sort (Classes 15-16). Pattern matters more than code.

# --- Exo 3.1 : integer_sqrt(n, low=None, high=None) ---
# Return floor(sqrt(n)) for a non-negative int n, recursively. Examples:
#   integer_sqrt(0)  → 0
#   integer_sqrt(9)  → 3   (perfect square)
#   integer_sqrt(10) → 3   (floor — 3 < sqrt(10) < 4)
#
# This is class 01's iterative binary search reborn as a recursion,
# applied to a NEW domain: the answer lives somewhere in [0, n], and
# you binary-search the answer range until you converge on the floor.
#
# Strategy: at each call, take the middle of `[low, high]` and compare
# `mid * mid` to n. If equal, you've found a perfect square — return
# `mid`. If too small, the answer is in the right half. If too big, in
# the left half. Stop when the window has collapsed (`low > high`) —
# at that point, `high` is the floor.
#
# Beware: `low=None, high=None` is the safer Python default — set the
# actual window (`0`, `n`) inside the function on the first call.
#
# Forbidden: `math.sqrt`, `n ** 0.5`, any module. The whole point is
# the divide pattern.

def integer_sqrt(n, low=None, high=None):
    # TODO
    pass


print("\n=== Exo 3.1 ===")
print(integer_sqrt(0))     # Expected: 0
print(integer_sqrt(1))     # Expected: 1
print(integer_sqrt(4))     # Expected: 2
print(integer_sqrt(9))     # Expected: 3
print(integer_sqrt(10))    # Expected: 3
print(integer_sqrt(99))    # Expected: 9
print(integer_sqrt(100))   # Expected: 10
