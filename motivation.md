# Morning Read — Don't Slack Off

**Schedule: 08:00–09:00. Every day. No Sunday.**
Open a problem before you open anything else.

---

## Why This Gate Matters

Live coding is the **only true hard-skill gatekeeper** in the interview loop. ML theory, system design, behavioral — you can handle those through frameworks and communication. Coding fluency you can't fake. It's the one gate that failed you at Revolut.

It's the **entry fee, not the destination.** You want breadth and leadership roles. But you can't skip to the broad role without first proving depth. The coding grind earns the platform where your multidimensionality becomes the edge.

It's also your **automation hedge in reverse**: the pure-coding layer is what AI erodes, but right now it still gates entry. Get through the narrowing gate to reach the widening room.

**If you execute, top 5%.** Most people don't attempt top-tier prep. Courage to try is necessary but not sufficient. Execution is the multiplier that converts willingness into outcome.

---

## The Honest Diagnosis

| Stage | Name | Description | State |
|-------|------|-------------|-------|
| 1 | Unconscious Incompetence | Not aware of what one doesn't know | Beginner; unaware of deficiencies |
| 2 | Conscious Incompetence | Aware of lack of skills; painful realization | The crucial turning point — motivation or discouragement |
| 3 | Conscious Competence | Active, intentional effort to apply new skills | Requires focus, discipline, and vigilance |
| 4 | Unconscious Competence | Mastery becomes automatic and effortless | Fluency and authentic execution |

Live coding = **Stage 2, conscious incompetence** — you now know you're slow and AI-dependent under time pressure. This is the productive turning point, not a dead end.

The cruel mismatch: you're Stage 3–4 at the actual job, Stage 2 at the interview format that gates it. That gap is closable. It's a drill problem, not a talent problem.

---

## What to Drill (Prioritized)

**70% — Pandas / SQL. This is your target domain and your actual gap.**
- Window functions, named aggregations, rolling windows, time-series ops
- Merges (all types, multiple keys), pivot / melt / reshape
- Handle nulls and duplicates **without loops** — vectorize everything
- Never `.iterrows()`. Think in sets, not rows.

**30% — DSA, just 4 core patterns (easy → medium only).**
- Hash maps
- Two pointers
- Sliding window
- Fast / slow pointers

Always state Big-O at the end. Mention scaling: "with 100M rows this would..."

Skip hard DP, advanced graphs, obscure data structures. Low ROI for DS roles.

---

## How to Use AI in a Live Interview

- **You navigate, AI drives syntax only.** Logic, decomposition, edge cases, validation = you. Method names, parameter recall = AI. Narrate when you use it.
- Solve task 1 by hand. Don't announce it — just do it. Proves you can code.
- Introduce AI on task 2 deliberately: "to save time on boilerplate."
- Never paste more than 10 lines of AI code without explaining every line.
- Time-box 15–18 min per task. Validate data first (`df.head()`, `df.dtypes`). State edge cases out loud even when none exist.

---

## The Plan (Sustainable, Not Heroic)

**Daily (08:00–09:00):**
- 1 pandas or SQL problem from StrataScratch or DataLemur
- OR 1 easy/medium DSA problem using MSPS
- Cap at 1 hour. Stop when the hour ends.

**Friday / Saturday:**
- Timed medium blocks (simulate interview pressure)
- Verbalize your reasoning out loud — practice the narration

**Sunday: off.** Non-negotiable. Protects the loop from burning out.

You've burned out on over-stacked plans before. Start at one hour. Grow only if it's sustainable after 3 weeks.

---

## Platforms (Don't Shop, Just Open)

1. **StrataScratch** (free tier) — real-dataset pandas and SQL, fintech-flavored, closest to what Revolut tests
2. **DataLemur** (free) — SQL window functions
3. **NeetCode** (free) — best structure for the 4 DSA patterns

Don't buy LeetCode Premium yet. Your gap is pandas/SQL fluency, not concept coverage. If you stick with it 3–4 weeks, then pay for StrataScratch. Not before.

The best platform is the one you open every morning.

---

## Timeline / Positioning

28, ~2.5–3 years effective experience → correctly positioned for **mid-level**. Senior is 2–3 years out. Sell **scope over tenure**: 250K-user credit scoring, LLM-as-Judge, drift detection, audit work.

Target ~6 months to convert. Hold the timeline loosely — the point is the loop runs and you improve each cycle. Each interview calibrates the next. You can't predict the exact format (pandas vs DSA vs Monte Carlo), so build broad enough to pass most bars.

Confidence + execution, not confidence alone. Believe it's yours, then do the reps that justify it.

---

> *"Die Wüste wächst: weh dem, der Wüsten birgt!"* — Nietzsche
> The desert grows only for those who carry one inside.

**Now stop reading. Open a problem.**
