# Project 1 — Bilibili Comment Tree

---

## Introduction

This project implements a hierarchical nested comment system just like the comment area under Bilibili videos. It builds a multi-way comment tree from JSON data, supports tree exploration, hot comment ranking, and an optional knockout tournament to select the best comment.

The project applies core data structures and algorithms: **N-ary tree, recursion, DFS traversal, and heap.** 

---

## Features

#### 1.Load & Parse Data
Load about 25 comment records from comments.json and parse raw data into structured comment nodes.

#### 2.Build & Display Comment Tree
Construct an n-ary tree recursively, and print the comment tree with clear hierarchical indentation.

#### 3.Tree Exploration
- Count total number of replies under any comment
- Find the deepest comment thread in the whole tree
- Delete a target comment together with all its child replies

#### 4.Top-K Hot Comments
Use Python heapq to rank comments by like count, and output the top-K most popular comments.

#### 5.Bonus: Comment Knockout Tournament
Take the top 8 comments to build a knockout bracket, use binary tree and post-order traversal to decide the final champion.

---

## Tech Stack

- Language: Python
- Data Structure: N-ary Tree, DFS Recursion, Heap
- Data Source: Local comments.json file
- Design: Object-oriented programming, modular file structure

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

---

## How to Run

1. Keep the complete project files and the comments.json dataset.
2. Run the main entry file:

```
python main.py
```
The program will automatically execute:

**Tree construction → Tree exploration → Hot comment ranking.** 

---

## Project Highlights

- Clear modular design, each module is independent and easy to maintain
- Implemented tree building, DFS recursion and heap ranking manually
- Real simulation of Bilibili nested comment business logic
- Standard coding style with necessary comments and good readability
