# COURSE 09 — Exercises (Heaps & Priority Queues) — CORRECTION


# ─── Exo 1 — parent_index ────────────────────────────────────────────

def parent_index(i):
    if i == 0:
        return -1
    return (i - 1) // 2


print("=== Exo 1 ===")
print(parent_index(0))
print(parent_index(1))
print(parent_index(4))
print(parent_index(6))



# ─── Exo 2 — smaller_child_index ─────────────────────────────────────

def smaller_child_index(heap, i):
    n = len(heap)
    left = 2 * i + 1
    right = 2 * i + 2
    if left >= n:
        return -1
    if right >= n:
        return left
    if heap[left] <= heap[right]:
        return left
    return right


print("\n=== Exo 2 ===")
print(smaller_child_index([1, 3, 2, 7, 5, 8], 0))
print(smaller_child_index([1, 3, 2, 7, 5, 8], 1))
print(smaller_child_index([1, 3, 2, 7, 5, 8], 2))
print(smaller_child_index([1, 3, 2, 7, 5, 8], 4))



# ─── Exo 3 — bubble_up ───────────────────────────────────────────────

def bubble_up(heap, i):
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break


print("\n=== Exo 3 ===")
h = []
for v in [5, 3, 8, 1, 9, 2]:
    h.append(v)
    bubble_up(h, len(h) - 1)
print(h)
import heapq
ref = []
for v in [5, 3, 8, 1, 9, 2]:
    heapq.heappush(ref, v)
print(h == ref)



# ─── Exo 4 — bubble_down ─────────────────────────────────────────────

def bubble_down(heap, i):
    n = len(heap)
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        if left >= n:
            break
        smaller = left
        if right < n and heap[right] < heap[left]:
            smaller = right
        if heap[smaller] < heap[i]:
            heap[i], heap[smaller] = heap[smaller], heap[i]
            i = smaller
        else:
            break


print("\n=== Exo 4 ===")
h = [1, 3, 2, 5, 9, 8]
popped = h[0]
h[0] = h[-1]
h.pop()
bubble_down(h, 0)
print("Popped:", popped)
print("Heap:", h)



# ─── Exo 5 — heapq as a max-heap ─────────────────────────────────────

import heapq

def top_k(nums, k):
    negated = [-x for x in nums]
    heapq.heapify(negated)
    result = []
    for _ in range(k):
        result.append(-heapq.heappop(negated))
    return result


print("\n=== Exo 5 ===")
print(top_k([4, 1, 7, 3, 8, 2, 9], 3))
print(top_k([10, 5, 8, 3, 12, 1, 7], 4))
print(top_k([1, 1, 1, 2, 2, 3], 2))



# ██████████████████████████████
# BONUS
# ██████████████████████████████


# ─── Bonus 1 — heapify ───────────────────────────────────────────────

def heapify(lst):
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        bubble_down(lst, i)


print("\n=== Bonus 1 ===")
arr = [9, 5, 8, 3, 2, 7, 4, 1, 6]
heapify(arr)
print(arr)
print(arr[0] == min(arr))
ref = [9, 5, 8, 3, 2, 7, 4, 1, 6]
heapq.heapify(ref)
print(arr == ref)



# ─── Bonus 2 — heap_sort ─────────────────────────────────────────────

def heap_sort(lst):
    heap = list(lst)
    heapify(heap)
    result = []
    while heap:
        result.append(heap[0])
        last = heap.pop()
        if heap:
            heap[0] = last
            bubble_down(heap, 0)
    return result


print("\n=== Bonus 2 ===")
print(heap_sort([5, 3, 8, 1, 9, 2]))
print(heap_sort([4, 1, 7, 3, 8, 2, 9, 6, 5]))
print(heap_sort([]))
print(heap_sort([42]))
print(heap_sort([3, 3, 1, 1, 2, 2]))
