# COURSE 02 EXERCISES - CORRECTIONS
# Linear Data Structures
# "Push, pop, walk through nodes - the muscle memory you'll reuse on trees."


# ████████████████████████████████████████████████████
# PART 1 - Stack class
# ████████████████████████████████████████████████████


class Stack:
    def __init__(self):
        self._data = []

    def push(self, v):
        self._data.append(v)
    # append puts v at index -1 (the END), which is our TOP.
    # Both append and pop() are O(1) because the list never shifts.

    def pop(self):
        if not self._data:
            raise IndexError("empty stack")
        return self._data.pop()
    # list.pop() with no argument pops the LAST element - O(1).
    # Note: list.pop(0) would also work but it's O(n) - shifts everything.

    def peek(self):
        if not self._data:
            raise IndexError("empty stack")
        return self._data[-1]
    # Index -1 = last element = the top. Read-only, no mutation.

    def is_empty(self):
        return len(self._data) == 0
    # Equivalently: `return not self._data`. Pythonic, same result.

    def __len__(self):
        return len(self._data)
    # Letting len(stack) work makes the class feel native.


# --- Tests ---
s = Stack()
print(s.is_empty())     # Expected: True
print(len(s))           # Expected: 0

s.push("A")
s.push("B")
s.push("C")
print(len(s))           # Expected: 3
print(s.peek())         # Expected: C
print(s.pop())          # Expected: C
print(s.pop())          # Expected: B
print(s.is_empty())     # Expected: False
print(s.pop())          # Expected: A
print(s.is_empty())     # Expected: True



# ████████████████████████████████████████████████████
# PART 2 - is_palindrome using your Stack
# ████████████████████████████████████████████████████


def is_palindrome(s):
    stack = Stack()
    for c in s:
        stack.push(c)
    # Now stack holds the chars of s, with s[-1] on top.

    reversed_chars = []
    while not stack.is_empty():
        reversed_chars.append(stack.pop())
    # Popping from the top yields chars in reverse order.

    return s == "".join(reversed_chars)
# We never wrote any reversing logic. The LIFO property of the stack
# reversed the string for us, for free. That's the lesson of this exo.


# --- Tests ---
print(is_palindrome("racecar"))   # Expected: True
print(is_palindrome("level"))     # Expected: True
print(is_palindrome("madam"))     # Expected: True
print(is_palindrome("hello"))     # Expected: False
print(is_palindrome("python"))    # Expected: False
print(is_palindrome(""))          # Expected: True
print(is_palindrome("a"))         # Expected: True
print(is_palindrome("ab"))        # Expected: False



# ████████████████████████████████████████████████████
# PART 2.5 - Bakery queue (5 min, fun)
# ████████████████████████████████████████████████████


from collections import deque

def serve_all(regulars, vip):
    q = deque()
    for name in regulars:
        q.append(name)            # regulars line up at the back
    q.appendleft(vip)             # VIP skips straight to the front

    served = []
    while q:
        served.append(q.popleft())  # always serve the FRONT
    return served
# Every op here is O(1) — that's the whole point of deque.
# With a regular list, `pop(0)` and `insert(0, vip)` would each be
# O(n) because every other element gets shifted.


# --- Tests ---
print(serve_all(["Alice", "Bob", "Charlie"], "Diana"))
# Expected: ['Diana', 'Alice', 'Bob', 'Charlie']

print(serve_all([], "Solo"))
# Expected: ['Solo']

print(serve_all(["X", "Y"], "VIP"))
# Expected: ['VIP', 'X', 'Y']



# ████████████████████████████████████████████████████
# PART 3 - SinglyLinkedList: walk twice
# ████████████████████████████████████████████████████


class SinglyLinkedList:

    class _Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    # --- Exo 3.1 : add_tail ---
    def add_tail(self, v):
        new = self._Node(v)
        if self._head is None:
            # Empty list: the new node IS the head.
            self._head = new
        else:
            # Walk to the LAST node (its .next is None).
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = new
        self._size += 1
    # Note the loop condition: `cur.next is not None`.
    # We stop AT the last node, not after it - we need cur to attach to.

    # --- Exo 3.2 : find_max ---
    def find_max(self):
        if self._head is None:
            return None
        # Seed the running max with the first node, then walk the rest.
        current_max = self._head.data
        cur = self._head.next
        while cur is not None:
            if cur.data > current_max:
                current_max = cur.data
            cur = cur.next
        return current_max
    # Same skeleton as add_tail (walk while cur is not None) but doing
    # something different at each step. That's THE WALK pattern.

    def to_list(self):
        out = []
        cur = self._head
        while cur is not None:
            out.append(cur.data)
            cur = cur.next
        return out


# --- Tests ---
ll = SinglyLinkedList()
print(len(ll))               # Expected: 0
print(ll.find_max())         # Expected: None

ll.add_tail(7)
print(ll.to_list())          # Expected: [7]
print(ll.find_max())         # Expected: 7
print(len(ll))               # Expected: 1

ll.add_tail(3)
ll.add_tail(11)
ll.add_tail(5)
print(ll.to_list())          # Expected: [7, 3, 11, 5]
print(ll.find_max())         # Expected: 11
print(len(ll))               # Expected: 4

ll.add_tail(11)
ll.add_tail(2)
print(ll.find_max())         # Expected: 11



# ████████████████████████████████████████████████████
# BONUS - reverse() in place (30-min challenge)
# ████████████████████████████████████████████████████

# Goal: reverse a SinglyLinkedList IN PLACE.
#   - O(n) time, O(1) extra memory.
#   - No new _Node objects, no list slicing, no reversed().
#   - We rewire .next pointers on the existing nodes.
#
# The trick is THE WALK extended with three references that move
# in lockstep:
#
#       prev    cur     nxt
#         |      |       |
#         v      v       v
#       None     A   ->  B  ->  C  -> None
#
# At each step:
#   1. nxt = cur.next      (remember the node after cur BEFORE we
#                            overwrite cur.next — otherwise we lose
#                            the rest of the chain)
#   2. cur.next = prev     (flip the arrow backward)
#   3. prev = cur          (slide prev forward)
#   4. cur = nxt           (slide cur forward)
#
# When cur becomes None, prev is sitting on what used to be the
# last node — that's the new head.


def reverse(self):
    prev = None
    cur = self._head
    while cur is not None:
        nxt = cur.next         # 1. remember where we were going
        cur.next = prev        # 2. flip the arrow backward
        prev = cur             # 3. slide prev forward
        cur = nxt              # 4. slide cur forward
    self._head = prev          # prev is now the new head
    # self._size is untouched on purpose — same nodes, same count.

SinglyLinkedList.reverse = reverse
# Why the order matters: if we did `cur.next = prev` BEFORE saving
# `nxt = cur.next`, we'd overwrite the only pointer to the rest of
# the chain. Save first, flip second.
#
# Why the empty-list case "just works": cur starts as None, the
# while loop never runs, prev stays None, _head is set to None.
# Same for single node: one iteration, cur.next was None so the
# node's next becomes None (was already None), prev becomes that
# node, _head ends up pointing at it. No special cases needed —
# the invariants of the loop carry every shape of input.


# --- Tests for the bonus ---

# Empty list -> still empty
ll_b = SinglyLinkedList()
ll_b.reverse()
print(ll_b.to_list())          # Expected: []
print(len(ll_b))               # Expected: 0

# Single node -> unchanged
ll_b.add_tail(42)
ll_b.reverse()
print(ll_b.to_list())          # Expected: [42]
print(len(ll_b))               # Expected: 1

# Two nodes
ll_b2 = SinglyLinkedList()
ll_b2.add_tail("A")
ll_b2.add_tail("B")
ll_b2.reverse()
print(ll_b2.to_list())         # Expected: ['B', 'A']

# Longer chain
ll_b3 = SinglyLinkedList()
for v in [1, 2, 3, 4, 5]:
    ll_b3.add_tail(v)
ll_b3.reverse()
print(ll_b3.to_list())         # Expected: [5, 4, 3, 2, 1]
print(len(ll_b3))              # Expected: 5

# Property test: reverse twice == identity
ll_b3.reverse()
print(ll_b3.to_list())         # Expected: [1, 2, 3, 4, 5]

# add_tail still works after reversing (proves _head is correctly rewired)
ll_b3.reverse()                # list is now [5, 4, 3, 2, 1]
ll_b3.add_tail(0)
print(ll_b3.to_list())         # Expected: [5, 4, 3, 2, 1, 0]
print(ll_b3.find_max())        # Expected: 5
