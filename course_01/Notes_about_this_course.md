# Notes About This Course
*A short letter to my students — read this before we begin.*

---

Welcome. Before we dive into Algorithms & Data Structures II, I want to tell you a few things about how this course works and how I want you to approach it. This document matters. Read it once now, and come back to it whenever you feel lost during the semester.

---

## 1. How this course works

We have **24 sessions of 90 minutes**. Most of them are lectures where I introduce a concept, show you how it works, and then **you practice**. We have two projects, one midterm exam, and one final exam *(more about grading in section 6).*

For every lecture session, you will find on the course repository:

- **Slides** — the visual support I use in class
- **Teaching notes** — the actual written course, more detailed than the slides; this is your real reference
- **Exercises** — what you'll work on during class and at home

Everything is on Gitee (link in section 5). The materials are pushed **before each class**, so you can take a look in advance if you want. You don't need to take fast notes during the lecture — focus on understanding, the written course will be there for you.

---

## 2. Exercises, exercises, exercises

This is a **programming course**. You do not learn algorithms by listening. You do not learn algorithms by reading. You learn algorithms by **writing code, breaking it, fixing it, writing it again**.

I know your curriculum is heavy on theory. This course is the opposite. A large part of every session is dedicated to exercises — and they are the **heart of the course**. The lecture exists to prepare you for the exercises. Not the other way around.

A few rules I want you to remember:

- **Always try.** Even if you didn't finish reading the lecture notes. Even if you don't feel ready. Open VS Code and start.
- **Struggling is normal.** If you're stuck, you are exactly where you should be. Stuck means your brain is working.
- **At least finish the first exercises.** They cover the basic ideas of the lecture. The last ones will be harder, sometimes really challenging — that's normal. But if you skip even the first ones, the lecture was useless.

The students who finish this course feeling confident with trees, recursion, and dynamic programming are not the smartest ones. They are the ones who **wrote the most code**.

---

## 3. About AI

AI is everywhere now. It's an incredible tool. But used badly — especially when you're a student — it can do more harm than good. We need to talk about this.

### 3.a — Why you should not lean on AI for your exercises

You are a student. Your job, right now, is to **build your brain**. Not to deliver code. Not to ship a product. To shape the way you think.

Here's the truth nobody tells you clearly:

> **Struggling is good. The more you struggle, the more you learn.**

When you're stuck on an exercise and you push through, your brain is literally building new connections. That feeling of "ugh, this is hard" is the sound of your brain getting stronger. It's a workout. Your brain is a muscle.

If, the moment it gets hard, you open Claude or DeepSeek and ask for the answer — you skip the workout. The connection is never built. And worse: **your brain learns a habit**. It learns "when things get hard, ask AI". Once that habit is set, you'll be stuck at the bottom of the mountain forever, watching others climb.

There's another problem nobody warns you about: **students who depend on AI start to feel sad and lose confidence**. They feel like they can't face anything alone. They feel like frauds. Don't be that student.

**The mecha analogy.** Think of AI as a giant mecha — like in Pacific Rim or Gundam. The mecha is incredibly powerful. But without a skilled pilot inside who knows how to fight, the mecha is useless. It can crush a few weak enemies, sure. But it will never save the city. The best pilots are the ones who trained their bodies and minds for years *before* getting in the cockpit. Once they're inside, the mecha becomes an extension of them — and they do impossible things.

That's what I want for you.

Right now, you are training. Later, when you've learned the basics, **you will use AI better than anyone**. You'll know what good code looks like. You'll spot when AI is wrong. You'll give tasks to AI the way a senior engineer gives tasks to a junior — with clear intent, knowing exactly what you want.

Meanwhile, most candidates applying to the same masters and the same jobs as you will be **just one more person using AI without understanding the foundation**. That's where you win.

### 3.b — How to use AI intelligently

Now — AI is not the enemy. Used the right way, it speeds up your learning a lot. Here's how.

**Don't ask AI to do the exercise.** Ask AI to help you *understand* what you need to do the exercise.

**Good prompt — asking for a hint:**
```
I'm working on the binary search exercise and I tried this:

  def binary_search(lst, target):
      low, high = 0, len(lst)
      while low < high:
          mid = (low + high) // 2
          if lst[mid] == target:
              return mid
          ...

But it goes into an infinite loop on some inputs. Can you give me a hint
about what's wrong, without giving me the answer directly?
```

**Good prompt — asking a conceptual question:**
```
Wait, I don't get it. The teacher said binary search is O(log n) and
naive search is O(n). On a list of 1 million items, what does that
actually mean in practice? Why is the difference so huge?
```

These are smart prompts. Notice that you're showing your work, asking for a *hint* or an *explanation*, and staying in the driver's seat. Your brain is still doing the work.

**After AI explains something, reformulate it in YOUR OWN words.**

Don't just nod and move on. Type back something like:

> "Ok so if I got this right, binary search only works because the list is sorted. At each step, I look at the middle, and I throw away the half where the target can't be. So even with a million items, I only need around 20 steps because each step cuts the work in half. Is that right?"

It's clumsy. That's fine. **The clumsiness is proof your brain is processing it.** If you can't reformulate, you didn't understand.

**Ask AI to test you.**

This is one of the best uses of AI as a student. After a class, paste the lecture notes (or a summary) into Claude or DeepSeek and try prompts like:

```
Make me a small quiz on the concepts from this lecture.
Ask me 5 questions one by one, wait for my answer, then
tell me if I'm right or wrong and explain.
```

Or:

```
Ask me questions to check if I really understood this
chapter. Don't give me the answer first — let me try,
then correct me.
```

This turns AI into a private tutor that drills you. Way more effective than re-reading. Your brain has to **produce** the answer, which is what builds memory.

**If you generated code with AI — make sure you understand it. How?**

Delete it. Try to rewrite it from memory.

If you can't rewrite it, **you don't understand it**. Don't keep going. Go back, read it line by line, ask the AI to explain each part, and try again. Same rule applies for solutions I give you in class.

This is the most important habit you can build this year.

**About autocomplete (Copilot, Cursor, etc.).**

These tools sit inside your code editor and finish your lines as you type. They feel magical when you know what you're doing. They are **poison when you're learning**.

When you do exercises this semester: **disable autocomplete**. Turn it off. Type every character yourself. Autocomplete is a tool to save time *when you already know* — not a tool to make up for not knowing.

**When is it OK to ask AI more directly?**

Examples of cases where it's perfectly fine:

- **Setup and configuration problems.** "How do I install Python on Windows?" — sure, ask.
- **Completely cryptic error messages.** When the error feels like alien language and you have no idea where to even start — don't hesitate to ask for help.
- **When you've been stuck on a bug for 15+ minutes.** You tried, you read, you tested. Now you're going in circles. Ask. Just make sure you understand the answer once you get it.
- **Reviewing code you already wrote.** "Here's what I did, can you point out any issues?" — great use of AI.

The principle is simple: **AI should help you learn, not replace your learning.**

---

## 4. About English

This course is taught entirely in English. I know that's a real difficulty. Most of your other courses are in Chinese, and now you're being asked to follow technical content — already hard in your native language — in a second language. I respect that. So let's talk about how we make it work, both sides.

My part:

- I will keep speech short. You won't hear me talk for an hour straight in English — nobody learns that way.
- I will write a lot. Slides, notes, code with heavy annotations. Reading is much easier than listening when you're not fluent yet.
- I will repeat. If I see confused faces, I'll say it again, slower, with different words. Don't be shy about asking me to.

Your part:

- **It's totally OK to use AI to translate** a paragraph or a sentence when you're really lost — I know it's going to happen often, and that's fine. Just don't forget to **try first**, even just for 30 seconds. Read the English once before the translation. That tiny effort is what makes you progress.
- **Always keep contact with the English.** Try to read the exercise statements yourself first. Learn the technical terms (`tree`, `node`, `recursion`, `traversal`, `complexity`, `heap`, `pivot`, `memoization`...). These will follow you for your whole career.
- Watch series, YouTube videos, tutorials in English whenever you can. Even 15 minutes a day adds up massively over a year.

By the end of your third year, I want you to be able to **talk about your code with a recruiter or a manager in English**. That's a real career skill. It opens doors most of your peers can't open. You'll be a serious asset for any company — and for yourself, you'll be able to connect with people from all over the world.

---

## 5. Stay in touch

**Course repository (Gitee):**
> https://gitee.com/adnan-boudjelal/algo_data-II

All slides, teaching notes, and exercises will be pushed there **before each class** — so you can have a look in advance if you want to come prepared. Later in the course, I'll show you how to push your own exercises and projects to your own branch.

**WeChat:**
I'm in the class group. Add me. If you have **any** question — about a lesson, an exercise, a project, your career, your installation problems at 11pm — don't hesitate to message me. If I can help, I will.

One small thing: I sometimes take a bit of time to answer. If I forget, **just ping me again**. It's not personal. My head is sometimes in the clouds. Don't be shy about reminding me.

---

## 6. Grading

Your final grade for this course is built like this:

| Evaluation | Weight | When |
|---|---|---|
| **Project 1 — Bilibili Comment Tree** (solo) | 20% | Sessions 10–12 (one week of class time) |
| **Midterm exam** | 30% | Session 13 — 30 MCQ questions |
| **Project 2 — Anime Watchlist Optimizer** (solo or pair) | 20% | Sessions 20–22 (one week of class time) |
| **Final exam** | 30% | Session 24 - 30 MCQ questions |

Two projects + two exams. A bit less than half of the grade comes from doing real, hands-on work. A bit more comes from showing you understood the core concepts. Fair and balanced.

**A word on how I think about evaluations.**

My exams and projects are not designed to trap you. They are designed to check that you understood the **core concepts** — the ones that actually matter, the ones you'll genuinely need later in your career as an engineer. Not obscure trivia. Not edge cases meant to catch you off guard.

Some questions will be a bit challenging — that's normal, that's how I check that you really understood. But if you do **a little bit of work regularly** through the semester, you will get an excellent grade. I'm not saying this to be encouraging. I'm saying it because it's how the course is built.

**Two ways to earn bonus points** (which can round up your final grade):

1. **Doing exercises regularly and pushing them to your repo.** Not all of them. Not all correctly. Not all the time. The point is to show me you're **building the habit of trying**. I really don't want to see exercises solved fully by AI — that's the opposite of the goal. Honest, imperfect, half-finished attempts are worth much more to me than polished AI submissions.
2. **Being there and engaged.** Coming to class, working seriously during exercise time, being part of the course. And don't worry — missing a class here and there is completely normal, life happens. I'm looking at the **overall pattern** across the semester — I'm not keeping a strict count of who's there at every single class.

The deal is simple: **if you honestly try to work this course, I will make a real effort when the grading moment comes.** I don't grade harshly when I can see someone has been engaged all semester. That's a promise.

I'll give you all the details (rules, deliverables, evaluation criteria) when each project starts.

---

## 7. Tips

A few small things that will make your life easier this semester.

**Use a Markdown viewer to read these files.**

You'll notice all course materials are `.md` files. Markdown is just plain text with simple **formatting marks** — special characters that tell the computer "make this bold", "make this a title", "make this a list". The computer then displays your text nicely.

For example, when you write this in a `.md` file:

```
# My title
This is **important**.
- first item
- second item
```

A Markdown viewer will show it like this:

> # My title
> This is **important**.
> - first item
> - second item

So the `#`, the `**`, the `-` — these are formatting marks. They are everywhere in the dev world: README files on Gitee/GitHub, documentation, technical notes.

In **VS Code**, you can preview a `.md` file nicely formatted: open the file, then press `Ctrl+Shift+V` (or `Cmd+Shift+V` on Mac). Or click the little preview icon in the top-right corner. Much easier on the eyes than raw text.

**Type, don't copy-paste.**

When you see code that you don't know in the slides or notes or everywhere — *type it*, don't copy it. Yes, it's slower. Yes, you'll make typos. That's the point. Your fingers and your brain remember together. Copy-paste teaches you nothing. This is doubly true in this course: the patterns we'll see (recursion on a tree, partition for quick sort, the bubble-up of a heap…) need to live in your fingers, not on your clipboard.

---

That's it. Now let's get to work.

See you in VS Code.
