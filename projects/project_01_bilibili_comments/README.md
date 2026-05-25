# Project 1 — Bilibili Comment Tree

*Build a hierarchical comment system, like the ones under every Bilibili video. Explore it. Find the top comments. Crown a champion. Have fun.*

---

## The story

Bilibili wants to elect the **Comment of the Week**. Your mission:

1. **Load** ~25 comments from a JSON file
2. **Build** a tree of comments and replies (replies have replies, which have replies...)
3. **Explore** the tree — count replies, find the deepest thread, delete a sub-thread
4. **Rank** the most-liked comments using a heap
5. *(Bonus)* Organize a knockout tournament with the top 8 to crown the champion

By the end, you will have used **most of the data structures and algorithms from this semester**: trees, recursion, heaps, traversal — all serving a real purpose. No abstract toy examples here.

---

## The big picture

```
                  data/comments.json
                  (~25 Bilibili comments)
                          │
                          ▼
                  ┌───────────────────┐
            M1    │   Build the       │   ← Session 10
                  │   comment tree    │
                  └─────────┬─────────┘
                            ▼
                  ┌───────────────────┐
            M2    │   Explore:        │   ← Session 11
                  │   count, depth,   │
                  │   delete          │
                  └─────────┬─────────┘
                            ▼
                  ┌───────────────────┐
            M3    │   Top-K hot       │   ← Session 12
                  │   comments        │
                  │   (heapq)         │
                  └─────────┬─────────┘
                            ▼  (optional)
                  ┌───────────────────┐
            M4    │   Tournament      │   ← Session 12 bonus
                  │   bracket         │
                  └───────────────────┘
```

---

## Milestones

| # | Goal | When | Skills used |
|---|------|------|-------------|
| **M1** | Build the tree from JSON, display it | Session 10 | N-ary tree, JSON, recursion |
| **M2** | Count replies, find deepest thread, delete | Session 11 | DFS, recursion |
| **M3** | Top-K most-liked comments | Session 12 | Heap (`heapq`), traversal |
| **M4** *(bonus)* | Knockout tournament bracket | Session 12 | Binary tree, postorder |

> **You are good if you finish M1, M2, M3.** 
M4 is for the curious and the brave. Skipping M4 has zero penalty.

---

## Project structure

```
project_01_bilibili_comments/
├── README.md                   ← you are here
├── branches_tutorial.md        ← how to work with Gitee branches
├── INSTRUCTIONS/
│   ├── session_10.md           ← M1 step-by-step (with JSON + n-ary tree tutorials)
│   ├── session_11.md           ← M2 step-by-step
│   └── session_12.md           ← M3 + bonus M4
├── data/
│   └── comments.json           ← provided dataset (~25 comments)
├── src/
│   ├── comment.py              ← M1: Comment class + tree building + display
│   ├── explorer.py             ← M2: count, deepest, delete
│   ├── leaderboard.py          ← M3: top-K with heap
│   └── tournament.py           ← M4 (bonus only)
└── main.py                     ← runs everything end-to-end
```

**One file per milestone.** Don't mix everything in `main.py`. Keep `main.py` clean — it just imports and orchestrates.

---

## How to read the instructions

Each session has its own `.md` file with:

- **A short recap** of where you should be
- **A list of steps** for the session
- **Mini-tutorials** when a new concept is needed
- **Pseudocode hints** (never full solutions to copy-paste)
- **A "done for today" marker** — if you reach it, you can stop and push

You can go further than the session marker if you want. But reaching the marker is **enough** for the current session.

---

## How to submit

1. On Gitee, create your branch named with your **student ID** (e.g. `202301232`) (only after accepting the repository invitation)
2. Inside your branch, the project directory: `projects/project_01_bilibili_comments/`
3. Push your code with clear commit messages — **one per session is ideal**:
   - End of session 10 → `M1: build comment tree, display, find_by_id`
   - End of session 11 → `M2: count_total_replies, deepest_thread, delete_comment`
   - End of session 12 → `M3: top-K leaderboard` (+ optional `M4: tournament bracket`)
4. **Deadline: saturday May 30, 11:59pm**

---

## Grading (20% of final grade)

| Criterion | Weight |
|---|---|
| Code runs end-to-end (M1 + M2 + M3) | **60%** |
| Correct use of recursion and heap | **20%** |
| Code quality (clean classes, readable functions, comments) | **10%** |
| Clear `README.md` describing your work | **5%** |
| Clear commit history with good messages | **5%** |
| **Bonus M4 (tournament)** | **+10%** (cannot go beyond 100%) |

---

## How to use AI

- Stuck on a syntax error? **Ask.**
- Don't understand what an error message means? **Ask.**
- Want to learn what `heapq.nlargest` does? **Ask.**
- **Do NOT** ask AI to write your `Comment` class, or your recursion. You learn nothing, and the grader will know.

Everything you need is in the **instructions** and in **your previous courses (sessions 1 to 9)**. Read them first. Ask questions second.

---

*Good luck. Build something you're proud of.*
