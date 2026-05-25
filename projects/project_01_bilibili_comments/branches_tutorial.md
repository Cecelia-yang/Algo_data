# Working with branches on Gitee

*One repo, two branches: `master` for the lessons, `your_branch` for your work.*

---

## What is a branch?

A branch is a parallel version of the repo. Think of it as a separate timeline.

```
   master         ──●──●──●──●──●──●  ← lessons added by teacher (read-only)
                          │
                          └──●──●──●  ← YOUR branch (your project goes here)
```

| Branch | What lives there | You can... |
|---|---|---|
| `master` | Teacher's lessons, exercises, slides | **pull** new lessons |
| `your_branch` | Your project, your work | **push** your commits |

---

## Where am I right now?

Always check first:

```bash
git status
```

The first line tells you:

```
On branch master
```

or

```
On branch 202301232 # your student ID
```

---

## Switching branches

```bash
git checkout master              # go to master (for lessons)
git checkout <your_student_id>   # go to your branch (for project)
```

---

## The two workflows

### 📥 Get a new lesson

```bash
git checkout master
git pull
```

### 📤 Push your project

```bash
git checkout <your_student_id>   # go to your branch (for project)
git add .
git commit -m "Project 1: M1 done"
git push
```

---

## ⚠️ "git pull does nothing!"

If you're on **your branch** and run `git pull`, **nothing new appears**. Lessons live on `master`, not on your branch. Switch first:

```bash
git checkout master   # ← go where lessons live
git pull              # NOW it works
```

---

## First-time setup: move your existing work to your branch

You already have weeks of exercises on `master` locally. We move them to your own branch, **without losing anything**.

**1. Check you are on master:**

```bash
git status
# expect: "On branch master"
```

**2. Create your branch from your current state:**

```bash
git checkout -b <your_student_id> #for example: git checkout -b 202301232
```

Your files stay exactly where they are. You're just on a new timeline now.

**3. Commit everything and push:**

```bash
git add .
git commit -m "Initial: existing exercises"
git push -u origin <your_student_id>
```

The `-u origin <name>` part means *"remember this branch"*. Next time, plain `git push` works.

**4. Go back to master and clean it up:**

```bash
git checkout master
```

Your exercise files revert to the teacher's starter versions on the screen.
**Your work is NOT lost** — it's safe on your branch (and on Gitee). To see it again:

```bash
git checkout <your_student_id>   # your work is back
```

---

## Quick reference

| Goal | Command |
|---|---|
| Which branch am I on? | `git status` |
| List my branches | `git branch` |
| Switch to master | `git checkout master` |
| Switch to my branch | `git checkout <your_student_id>` |
| Create a new branch | `git checkout -b <name>` |
| Get latest lessons | `git checkout master` → `git pull` |
| Save my project work | `git checkout <your_student_id>` → `git add .` → `git commit -m "..."` → `git push` |

---

## Golden rule

> **Before any `git pull` or `git push`, run `git status`. Know where you are first.**
