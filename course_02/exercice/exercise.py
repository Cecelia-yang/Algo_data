# COURSE 02 EXERCISES - Linear Data Structures
# "Push, pop, walk through nodes - the muscle memory you'll reuse on trees."


# ██████████████████████████████
# PART 1 - Stack class
# ██████████████████████████████

# Tools:   Python list, list.append, list.pop, list.pop(0)
# Rule:    The END of the list is the TOP of the stack
#          (because list.append() and list.pop() are O(1) — but
#          list.pop(0) is O(n), avoid it).
#
# Five methods to implement:
#   push(v)    - put v on top                   - O(1)
#   pop()      - remove and return the top      - O(1)
#   peek()     - look at the top, no remove     - O(1)
#   is_empty() - True if no items               - O(1)
#   __len__()  - so len(stack) works            - O(1)
#
# Hints:
#   - the storage is already given as `self._data = []`
#   - "the top" = the LAST element — pick the right list method
#   - for pop()/peek() on an empty stack: `raise IndexError("empty stack")`

class Stack:
    def __init__(self):
        self._data = []

    def push(self, v):
        # TODO
        pass

    def pop(self):
        # TODO
        pass

    def peek(self):
        # TODO
        pass

    def is_empty(self):
        # TODO
        pass

    def __len__(self):
        # TODO
        pass


# --- Tests for Part 1 ---
s = Stack()
print(s.is_empty())     # Expected: True
# print(len(s))         # Expected: 0   ← UNCOMMENT after implementing __len__
s.push("A")
s.push("B")
s.push("C")
# print(len(s))         # Expected: 3   ← UNCOMMENT after implementing __len__
print(s.peek())         # Expected: C
print(s.pop())          # Expected: C
print(s.pop())          # Expected: B
print(s.is_empty())     # Expected: False
print(s.pop())          # Expected: A
print(s.is_empty())     # Expected: True



# ██████████████████████████████
# PART 2 - is_palindrome using your Stack
# ██████████████████████████████

# Use your Stack from Part 1 to reverse s, then compare.
# Hint: "".join([...]) glues a list of chars into a string.


def is_palindrome(s):
    # TODO
    pass



# --- Tests for Part 2 ---
print(is_palindrome("racecar"))   # Expected: True
print(is_palindrome("level"))     # Expected: True
print(is_palindrome("madam"))     # Expected: True
print(is_palindrome("hello"))     # Expected: False
print(is_palindrome("python"))    # Expected: False
print(is_palindrome(""))          # Expected: True
print(is_palindrome("a"))         # Expected: True
print(is_palindrome("ab"))        # Expected: False



# ██████████████████████████████
# PART 2.5 - Bakery queue (5 min, fun)
# ██████████████████████████████

# A bakery opens. Regulars arrive in order and line up at the back.
# Then a VIP shows up and skips straight to the FRONT of the line.
# Then everyone is served from the front, one by one.
#
# deque ops you'll need (all O(1)):
#   .append(x)       → add at the BACK   (regular customer)
#   .appendleft(x)   → add at the FRONT  (VIP skipping the line)
#   .popleft()       → take from the FRONT (serve next person)


from collections import deque

def serve_all(regulars, vip):
    # TODO
    pass


# --- Tests ---
print(serve_all(["Alice", "Bob", "Charlie"], "Diana"))
# Expected: ['Diana', 'Alice', 'Bob', 'Charlie']

print(serve_all([], "Solo"))
# Expected: ['Solo']

print(serve_all(["X", "Y"], "VIP"))
# Expected: ['VIP', 'X', 'Y']



# ██████████████████████████████
# PART 3 - SinglyLinkedList: walk twice
# ██████████████████████████████

# THE WALK skeleton:
#     cur = self._head
#     while cur is not None:
#         # do something with cur.data
#         cur = cur.next
#
# `cur` is a worker pointer — only cur moves, self._head stays put.


class SinglyLinkedList:

    # _Node is a nested class (a blueprint for one node).
    # To create a new node:  new_node = self._Node(v)
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
    # Walk to the last node, attach a new node there.
    # If the list is empty → new_node IS the head.
    # Trap: loop on `cur.next is not None` (stop AT the last node).
    # Don't forget: self._size += 1.
    def add_tail(self, v):
        # TODO
        pass

    # --- Exo 3.2 : find_max ---
    # Walk every node, return the biggest .data. Empty → None.
    # Loop on `cur is not None` (we want to look at the last node too).
    def find_max(self):
        # TODO
        pass

    # Already implemented for you - so you can SEE your list.
    def to_list(self):
        out = []
        cur = self._head
        while cur is not None:
            out.append(cur.data)
            cur = cur.next
        return out


# --- Tests for Part 3 ---
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

ll.add_tail(11)              # duplicate max - still works
ll.add_tail(2)
print(ll.find_max())         # Expected: 11



# ██████████████████████████████
# BONUS - 30 min, for the strong students
# ██████████████████████████████

# Add `reverse(self)` to SinglyLinkedList that flips the chain
# IN PLACE. Same nodes, same _size — only the .next pointers
# change direction.
#
# THE WALK now uses THREE pointers instead of one:
#     prev (behind), cur (where you are), nxt (where you were going).
#
# Constraints: O(n) time, O(1) memory. No new _Node, no reversed(),
# no slicing. When cur becomes None, prev is the new head.


def reverse(self):
    # TODO
    pass

SinglyLinkedList.reverse = reverse


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
