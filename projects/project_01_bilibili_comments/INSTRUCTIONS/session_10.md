# Session 10 — Milestone 1: Build the comment tree

*Today: load the data, build the tree, display it. By the end, you should see an indented comment thread on your screen.*

---

## What you do today

| Step | What | Where |
|------|------|-------|
| 1 | Load the JSON dataset | `main.py` |
| 2 | Read the n-ary tree mini-tutorial | (this doc) |
| 3 | Write the `Comment` class | `src/comment.py` |
| 4 | Build the tree from JSON | `src/comment.py` |
| 5 | Display the tree with indentation | `src/comment.py` |
| 6 | *(extra)* Find a comment by ID | `src/comment.py` |

> **If steps 1–5 work by the end of class, you are done. Push it.**

---

## Mini-tuto — JSON

JSON is a text format for structured data. It maps almost directly to Python:

| JSON | Python |
|------|--------|
| `{ ... }` | `dict` |
| `[ ... ]` | `list` |
| `"text"` | `str` |
| `42`, `3.14` | `int`, `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

Loading a JSON file in Python. Here's a generic example — say you have `school.json`:

```json
{
    "school": "Chang'an University",
    "students": [
        {"name": "Liu Wei", "courses": ["Math", "Physics"]},
        {"name": "Zhang Mei", "courses": ["English", "History", "Art"]}
    ]
}
```

You load it and use it like any other Python object:

```python
import json
DATA_PATH = os.path.join(HERE, "data", "comments.json")


with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# You can print whatever you want to make sure you load it right
print(data["school"])
print(len(data["students"]))

for student in data["students"]:
    print(student["name"], "—", student["courses"])
```

Output:

```
Chang'an University
2
Liu Wei — ['Math', 'Physics']
Zhang Mei — ['English', 'History', 'Art']
```

Try to print the value inside `data/comments.json` !!

Now open `data/comments.json`. Like `school.json` above, it is one object with the list of comments under a key — read it with `data["comments"]`. The difference: each comment is **recursive** — it carries its own `replies`, a list of more comments.

---

## Mini-tuto — N-ary trees

You know binary trees: every node has at most 2 children (`left`, `right`).

An **n-ary tree** is more flexible: every node can have **any number of children**, stored in a list.

```
                     "Great video!"
                      Alice (98 ❤️)
                  ┌────────┼────────┐
                  ▼        ▼        ▼
              "Agree!"  "Disagree" "First!"
                 Bob      David     Grace
                  │      ┌──┴──┐
                  ▼      ▼     ▼
              "Same"   "Why?" "Hmm"
              Charlie   Eve    Frank
```

Alice has 3 children. David has 2. Bob has 1. Charlie, Eve, Frank, Grace are leaves.

**Recursion pattern — binary tree:**

```python
def recurse(node):
    do_something(node)
    recurse(node.left)
    recurse(node.right)
```

**Recursion pattern — n-ary tree:**

```python
def recurse(node):
    do_something(node)
    for child in node.children:
        recurse(child)
```

Same logic, same recursion patterns. The only difference: iterate over a list of children instead of touching `left` and `right` separately.

---

## Step 3 — `Comment` class

In `src/comment.py`, define a class `Comment` with:

- **attributes**: `id`, `author`, `text`, `likes`, `children` (empty list at init)
- **method**: `add_reply(comment)` — appends a comment to `children`

Class skeleton (you fill in the bodies):

```python
class Comment:
    def __init__(self, id, author, text, likes):
        ...

    def add_reply(self, comment):
        ...
```

Quick sanity check in `main.py`:

```python
root = Comment(1, "Alice", "Great video!", 98)
root.add_reply(Comment(2, "Bob", "Agree!", 12))
# Expected: len(root.children) == 1, first child's author == "Bob"
```

---

## Step 4 — Build the tree from JSON

Each JSON comment looks like this:

```
{
  id, author, text, likes,
  replies: [ list of more comment dicts ]
}
```

The structure is **recursive** — a reply is itself a comment that can have replies.

Write `build_tree(comment_dict)`:

- **Base case**: a comment with `replies: []` → just create the Comment and return it
- **Inductive case**: a comment with replies → create the Comment, then for each reply dict, recursively call `build_tree` and `add_reply` the result

**Guided skeleton — `build_tree`** 

```python
def build_tree(comment_dict):

    # ① Build THIS comment. 4 fields live in comment_dict:
    #    id, author, text, likes
    node = Comment(???)

    # ② A reply is a comment too, and it may have its own replies.
    #    For each reply dict: build its WHOLE sub-tree, then attach it.
    for reply_dict in ???? :
        node.add_reply(build_tree(reply_dict))

    # ③ Hand the finished node back to whoever called us.
    return node
```

🔍 **The two GIVEN lines, explained**
- `build_tree(reply_dict)` calls `build_tree` **again** on a smaller dict and returns the root of that reply's sub-tree. `add_reply` hangs it under `node`. → one line = *"build the sub-thread AND attach it"*.
- `return node`: every call must hand its node back — otherwise the line above would attach `None`. The `return` is what makes the recursion work.

🌳 **What ONE call does** (dict #1 = Alice, replies #2 and #4):

```
build_tree(Alice #1)
  ├─ build_tree(#2) → Bob's sub-tree   ┐ add_reply
  └─ build_tree(#4) → David's sub-tree ┘ add_reply
  └─ return Alice (now with 2 children)
```

Then in `main.py`: load the JSON, take the list `data["comments"]`, call `build_tree` on each comment dict in it, and store the list of roots.

> ### Why `roots` is a *list*, not one tree
>
> A video does not have **one** top comment. It has **many**.
> Each top comment starts its own tree (the comment + all its replies).
>
> ```
>   Alice       Hua Mei     Wang Lei    ...
>   / | \        /  \         /  \
>  Bob .. Grace Lin  Zhao   Chen  Old
> ```
>
> Many trees side by side = a **forest**.
> `build_tree(c)` builds **one** tree. We call it once per top comment → we get a **list** of trees.
>
> - **depth** (a reply inside a reply) → the **recursion**
> - **width** (top comments side by side) → the **list**

---

## Step 5 — Display the tree

Target output:

```
[#1] Alice (98 ❤️): Great video!
  [#2] Bob (12 ❤️): Agree!
    [#3] Charlie (5 ❤️): Same
  [#4] David (8 ❤️): Disagree
    [#5] Eve (2 ❤️): Why?
    [#6] Frank (3 ❤️): Hmm
  [#7] Grace (1 ❤️): First!
```

Each level adds 2 spaces. This is **DFS preorder** (session 6): print this node, then recurse on children.

Indentation trick — multiply a string by an integer:

```python
indent = "  " * depth   # depth=0 → "", depth=1 → "  ", depth=2 → "    "
```

`display(comment, depth=0)`:
- build the indent from `depth`
- print this comment line with the indent in front
- for each child → `display(child, depth + 1)`


How to use f-strings for formatting:
f-strings are a way to embed expressions inside string literals, using curly braces `{}`. For example:

```python
print(f"Hello, my name is {name} and I am {age} years old. I have {likes} likes on my comment, but i would like to have {likes * 10} likes!")
```

**Guided skeleton — `display`**

```python
def display(comment, depth=0):

    # ① Build the indent: 2 spaces per level.
    indent = ???    

    # ② Print THIS comment, indent in front, with right value inside 
	# to be exactly what is waited.
    print(f"???{???}???{???}???")

    # ③ Recurse on each child, ONE level deeper.
    for ??? in ??? :
		display(child, ???) #← you fill: display(child, ...) one level deeper
```

🔍 **Why it works**
- `display(child, ????)` is **preorder**: we print the parent first (②), THEN dive into its children. Adding `1` to `depth` is what shifts each level 2 more spaces to the right.
- A leaf has no children → the `for` loop runs zero times → it just prints its own line. No `if` needed (free base case).

---

## Step 6 — Find by ID *(extra)*

`find_by_id(comment, target_id)`:
- if this comment's id matches → return it
- otherwise try each child recursively
- if none found → return `None`

Same preorder pattern as `display`, with an early return.

**Guided skeleton — `find_by_id`**

```python
def find_by_id(comment, target_id):

    # ① Is it THIS comment? If yes, hand it back.
    if comment.??? == ???:
        return comment

    # ② Not here → search each child. The tricky part: the moment a child
    #    finds it, you must STOP and bubble that result back up.
    for child in comment.children:
        found = ???
        if ????
			return ????

    # ③ Searched everything under here, nothing matched.
    return ???
```

🔍 **Why the `found` check**
- `find_by_id(child, ...)` searches one whole sub-tree and returns the comment *or* `None`. The `if ??? return found` is what makes the search stop at the first hit — without it you'd give up after the first child and never look at the others.

---

## Debug pattern

Print after every step:

```
-----step 1: data loaded-----
Loaded 6 top-level comments

-----step 4: tree built-----
Built 6 comment trees

-----step 5: display-----
[#1] Alice (98 ❤️): Great video!
  ...
```

---

## Done for today ✅

You see your comment threads displayed nicely? Push:

```bash
git commit -m "M1: build comment tree, display"
git push
```

Next session: 3 recursive functions to explore the tree.
