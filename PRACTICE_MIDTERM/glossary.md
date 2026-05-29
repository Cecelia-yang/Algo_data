# Key Terms — English → 中文

The technical words from the course, with their Chinese translation and a short meaning.

| English | 中文 | Meaning (simple English) |
|---|---|---|
| Big-O notation | 大O表示法 | How the work grows when the input gets big. Not seconds. |
| O(1) / O(n) / O(log n) / O(n²) | 常数 / 线性 / 对数 / 平方 | constant / linear / logarithmic / quadratic time. |
| binary search | 二分查找 | Find a value in a SORTED list by cutting it in half. O(log n). |
| stack — LIFO | 栈 — 后进先出 | Last In, First Out. push / pop / peek. |
| queue — FIFO | 队列 — 先进先出 | First In, First Out. |
| deque | 双端队列 | Python's fast queue. `popleft()` is O(1). |
| linked list | 链表 | A chain of nodes; each one points to the next. |
| node | 节点 | One item that holds data and links. |
| hash table / dict | 哈希表 / 字典 | Stores key → value. Lookup is O(1) on average. |
| key / value | 键 / 值 | The name you look up / the data stored for it. |
| collision | 哈希冲突 | Two keys land on the same slot. The dict handles it. |
| recursion / recursive | 递归 / 递归的 | A function that calls itself. |
| base case | 基本情况 | When the function stops, without calling itself. |
| call stack | 调用栈 | The calls that are running right now, one on top of another. |
| RecursionError | 递归错误 | Crash when recursion never stops (no base case reached). |
| tree / binary tree | 树 / 二叉树 | Branches downward; binary = at most two children. |
| root / leaf | 根 / 叶子 | Top node (no parent) / node with no children. |
| parent / child / sibling | 父 / 子 / 兄弟节点 | Above / below / same parent. |
| subtree | 子树 | A node plus everything below it. |
| depth / height | 深度 / 高度 | Edges from root to a node / depth of the deepest leaf. |
| traversal | 遍历 | Visiting every node in a chosen order. |
| preorder / inorder / postorder | 前序 / 中序 / 后序 | root-first / left-root-right / root-last. |
| DFS / BFS | 深度优先 / 广度优先 | Go deep first / visit level by level (uses a queue). |
| binary search tree (BST) | 二叉搜索树 | Left subtree smaller, right subtree greater, everywhere. |
| inorder successor | 中序后继 | The smallest value in a node's right subtree. |
| degenerate | 退化的 | A tree shaped like a chain (a line) → search O(n). |
| balanced / self-balancing | 平衡 / 自平衡 | Short, wide tree / re-fixes its shape automatically (AVL, red-black). |
| heap — min-heap / max-heap | 堆 — 最小堆 / 最大堆 | Parent ≤ children (min) or ≥ children (max). |
| priority queue | 优先队列 | The most important item comes out first. A heap powers it. |
| complete binary tree | 完全二叉树 | Filled level by level, left to right. No gaps. |
| heapify / heappush / heappop | 建堆 / 入堆 / 出堆 | Python `heapq`: build / insert / remove-min. |
