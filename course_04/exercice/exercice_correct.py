# COURSE 04 EXERCISES — Recursion Deep Dive — CORRECTION


# ██████████████████████████████
# PART 1 — Warm-ups
# ██████████████████████████████


# --- Exo 1.1 : repeat(message, n) ---

def repeat(message, n):
    if n == 0:                       # base case: nothing left to print
        return
    print(message)
    repeat(message, n - 1)           # shrink by 1


print("=== Exo 1.1 ===")
repeat("hi", 3)
# Expected:
# hi
# hi
# hi



# --- Exo 1.2 : product_list(lst) ---

def product_list(lst):
    if not lst:                      # base case: empty list
        return 1                     # neutral of *
    return lst[0] * product_list(lst[1:])  # head * product of rest


print("\n=== Exo 1.2 ===")
print(product_list([]))           # Expected: 1
print(product_list([7]))          # Expected: 7
print(product_list([2, 3, 4]))    # Expected: 24
print(product_list([1, 5, 2, 3])) # Expected: 30



# --- Exo 1.3 : digits_sum(n) ---

def digits_sum(n):
    if n == 0:                       # base case: no digits left
        return 0
    return (n % 10) + digits_sum(n // 10)  # last digit + sum of rest


print("\n=== Exo 1.3 ===")
print(digits_sum(0))     # Expected: 0
print(digits_sum(7))     # Expected: 7
print(digits_sum(123))   # Expected: 6
print(digits_sum(98765)) # Expected: 35



# ██████████████████████████████
# PART 2 — Recursion on linked nodes
# ██████████████████████████████


class _Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def build_chain(values):
    head = None
    for v in reversed(values):
        head = _Node(v, head)
    return head



# --- Exo 2.1 : contains_in_chain(node, target) ---

def contains_in_chain(node, target):
    if node is None:                 # base case: chain exhausted
        return False
    if node.data == target:          # found at current node
        return True
    return contains_in_chain(node.next, target)  # try the rest


print("\n=== Exo 2.1 ===")
print(contains_in_chain(None, 5))                          # Expected: False
print(contains_in_chain(build_chain([10, 20, 30]), 20))    # Expected: True
print(contains_in_chain(build_chain([10, 20, 30]), 99))    # Expected: False
print(contains_in_chain(build_chain([42]), 42))            # Expected: True



# --- Exo 2.2 : max_in_chain(node) ---

def max_in_chain(node):
    if node.next is None:            # base case: last node
        return node.data
    return max(node.data, max_in_chain(node.next))  # current vs max of rest


print("\n=== Exo 2.2 ===")
print(max_in_chain(build_chain([42])))             # Expected: 42
print(max_in_chain(build_chain([10, 20, 30])))     # Expected: 30
print(max_in_chain(build_chain([5, 99, 12, 7])))   # Expected: 99
print(max_in_chain(build_chain([-3, -1, -10])))    # Expected: -1



# ██████████████████████████████
# PART 3 — ⭐ STRETCH
# ██████████████████████████████


# --- Exo 3 : count_nodes(node) ---

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# --- Exo 3.1 : integer_sqrt(n, low=None, high=None) ---

def integer_sqrt(n, low=None, high=None):
    if low is None:                                  # first call only
        low, high = 0, n
    if low > high:                                   # base case: window collapsed
        return high                                  # high is the floor
    mid = (low + high) // 2
    sq = mid * mid
    if sq == n:
        return mid                                   # perfect square
    if sq < n:
        return integer_sqrt(n, mid + 1, high)        # answer is in the right half
    return integer_sqrt(n, low, mid - 1)             # answer is in the left half


print("\n=== Exo 3.1 ===")
print(integer_sqrt(0))     # Expected: 0
print(integer_sqrt(1))     # Expected: 1
print(integer_sqrt(4))     # Expected: 2
print(integer_sqrt(9))     # Expected: 3
print(integer_sqrt(10))    # Expected: 3
print(integer_sqrt(99))    # Expected: 9
print(integer_sqrt(100))   # Expected: 10
