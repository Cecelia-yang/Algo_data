# COURSE 09 — Exercises (Heaps & Priority Queues) 
#
# ─────────────────────────────────────────────────────────────────────
# Min-heap reminder
# ─────────────────────────────────────────────────────────────────────
#
#                  ↓ next priority
#                  1
#                 / \
#                3   2
#               / \  /
#              7  5 8
#
#   array:  [ 1, 3, 2, 7, 5, 8 ]
#   index:    0  1  2  3  4  5
#
#   For a node at index i:
#       parent       = (i - 1) // 2
#       left child   = 2 * i + 1
#       right child  = 2 * i + 2
#
#   Example (i = 1, value 3):
#       parent       = 0   →  1
#       left child   = 3   →  7
#       right child  = 4   →  5
#
# ─────────────────────────────────────────────────────────────────────



# ─── Exo 1 — parent_index ────────────────────────────────────────────
#
# Write parent_index(i). It returns the index of the parent of i.
# If i is 0 (the root), return -1.

def parent_index(i):
    pass    # TODO


print("=== Exo 1 ===")
# print(parent_index(0))     # -1
# print(parent_index(1))     # 0
# print(parent_index(4))     # 1
# print(parent_index(6))     # 2



# ─── Exo 2 — smaller_child_index ─────────────────────────────────────
#
# Write smaller_child_index(heap, i). It returns the index of the
# smaller child of i.
#
# Three cases:
#   - No child:           return -1.
#   - Only left child:    return the index of the left child.
#   - Two children:       return the index of the smaller one.

def smaller_child_index(heap, i):
    pass    # TODO


print("\n=== Exo 2 ===")
# print(smaller_child_index([1, 3, 2, 7, 5, 8], 0))  # 2   (3 vs 2 → right)
# print(smaller_child_index([1, 3, 2, 7, 5, 8], 1))  # 4   (7 vs 5 → right)
# print(smaller_child_index([1, 3, 2, 7, 5, 8], 2))  # 5   (only left)
# print(smaller_child_index([1, 3, 2, 7, 5, 8], 4))  # -1  (no child)



# ─── Exo 3 — bubble_up ───────────────────────────────────────────────
#
# Write bubble_up(heap, i). Move heap[i] up until the heap is valid.
#
#   While i > 0:
#       parent = (i - 1) // 2
#       If heap[i] < heap[parent]: swap, move i up.
#       Else: stop.

def bubble_up(heap, i):
    pass    # TODO


print("\n=== Exo 3 ===")
# h = []
# for v in [5, 3, 8, 1, 9, 2]:
#     h.append(v)
#     bubble_up(h, len(h) - 1)
# print(h)                          # [1, 3, 2, 5, 9, 8]
# import heapq
# ref = []
# for v in [5, 3, 8, 1, 9, 2]:
#     heapq.heappush(ref, v)
# print(h == ref)                   # True



# ─── Exo 4 — bubble_down ─────────────────────────────────────────────
#
# Write bubble_down(heap, i). Move heap[i] down until the heap is valid.
#
#   While i has a child:
#       Find the smaller child.
#       If heap[i] > heap[smaller]: swap, move i down.
#       Else: stop.

def bubble_down(heap, i):
    pass    # TODO


print("\n=== Exo 4 ===")
# h = [1, 3, 2, 5, 9, 8]
# popped = h[0]
# h[0] = h[-1]
# h.pop()
# bubble_down(h, 0)
# print("Popped:", popped)          # 1
# print("Heap:", h)                 # [2, 3, 8, 5, 9]



# ─── Exo 5 — heapq as a max-heap ─────────────────────────────────────
#
# Python's heapq is a MIN-heap only. Trick for a max-heap: flip the
# sign. The smallest negative = the largest original.
#
#   import heapq
#   nums = [4, 1, 7, 3, 8, 2, 9]
#   negated = [-x for x in nums]        # flip every sign
#   heapq.heapify(negated)              # smallest negative = largest
#   largest = -heapq.heappop(negated)   # flip back when reading
#   print(largest)   # 9
#
# Write top_k(nums, k). Return the k largest values, biggest first.

import heapq

def top_k(nums, k):
    pass    # TODO


print("\n=== Exo 5 ===")
# print(top_k([4, 1, 7, 3, 8, 2, 9], 3))     # [9, 8, 7]
# print(top_k([10, 5, 8, 3, 12, 1, 7], 4))   # [12, 10, 8, 7]
# print(top_k([1, 1, 1, 2, 2, 3], 2))        # [3, 2]



# ██████████████████████████████
# BONUS
# ██████████████████████████████


# ─── Bonus 1 — heapify ───────────────────────────────────────────────
#
# Write heapify(lst). It turns any list into a valid min-heap.
#
# Trick:
#   Start at index n // 2 - 1 (the last node that has a child).
#   Go down to 0.
#   Call bubble_down at each index.
#
# This runs in O(n) — faster than adding values one by one.

def heapify(lst):
    pass    # TODO


print("\n=== Bonus 1 ===")
# arr = [9, 5, 8, 3, 2, 7, 4, 1, 6]
# heapify(arr)
# print(arr)
# print(arr[0] == min(arr))         # True
# ref = [9, 5, 8, 3, 2, 7, 4, 1, 6]
# heapq.heapify(ref)
# print(arr == ref)                 # True



# ─── Bonus 2 — heap_sort ─────────────────────────────────────────────
#
# Write heap_sort(lst). It returns a new list, sorted from smallest to
# biggest, using a min-heap.
#
# Steps:
#   1. Build a heap from the input (use heapify).
#   2. While the heap is not empty:
#        Take heap[0] and add it to the result.
#        Move the last value to the root.
#        Remove the last value (pop).
#        Call bubble_down at the root.
#   3. Return the result.

def heap_sort(lst):
    pass    # TODO


print("\n=== Bonus 2 ===")
# print(heap_sort([5, 3, 8, 1, 9, 2]))                # [1, 2, 3, 5, 8, 9]
# print(heap_sort([4, 1, 7, 3, 8, 2, 9, 6, 5]))       # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(heap_sort([]))                                # []
# print(heap_sort([42]))                              # [42]
# print(heap_sort([3, 3, 1, 1, 2, 2]))                # [1, 1, 2, 2, 3, 3]
