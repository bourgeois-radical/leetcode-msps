# Assessor-quality case — clean walkthrough

The dataset (`interview_data.csv`) is one row per **assessor's answer to one question on one job**. Columns: `project_type, project, job, question, assessor, dt, label`. Hierarchy: project → many jobs → many questions → answered by multiple assessors. `label` is binary (0/1).

The golden rule for a live interview: **write the simplest thing that answers the question, run it, show the output, then ask "do you want me to handle edge cases / make it faster?"** Let the interviewer pull you toward complexity. Don't push.

---

## Step 0 — Load and look

Always look at the data before touching it. Thirty seconds here saves you from wrong assumptions later.

```python
import pandas as pd

df = pd.read_csv("interview_data.csv")

df.head()
df.shape
df.dtypes        # <- this tells you dt is an 'object', not a datetime
df.isna().sum()  # <- this tells you there's a null
df.duplicated().sum()  # <- this tells you there's a dupe
```

Saying out loud "let me check dtypes and nulls first" signals seniority. It's also where you'd have caught the `dt` issue.

---

## Step 1 — Fix the dtypes (the bit you missed)

`dt` loads as a string. Convert it once, up front.

```python
df["dt"] = pd.to_datetime(df["dt"])
```

That's it. `pd.to_datetime` parses ISO strings (`2025-07-08`) automatically. After this, `df["dt"].dtype` is `datetime64[ns]` and you can do `.dt.year`, comparisons, resampling, etc.

Useful follow-ups only if asked:
- `pd.to_datetime(df["dt"], format="%Y-%m-%d")` — explicit format is faster on big data and fails loudly on bad rows (good).
- `errors="coerce"` — turns unparseable dates into `NaT` instead of raising. Mention it, don't reach for it by default.
- Timezone: the brief said "assume same timezone", so naive datetimes are fine. Say that assumption out loud.

---

## Step 2 — Clean edge cases (nulls + dupes)

Two lines. Resist the urge to write a class.

```python
df = df.dropna()           # removes the null row
df = df.drop_duplicates()  # removes exact duplicate rows
```

**This is where you over-engineered.** The composite-PK conflict logic (same assessor, two different labels) is a real concern — but it's a *follow-up*, not the opening move. The right move in the room:

> "I'll drop exact duplicates first. There's a subtler case — the same assessor answering the same question twice with *different* labels — do you want me to handle that, or is exact-duplicate removal enough for now?"

That one sentence shows you see the depth **without** spending 10 minutes coding it unprompted. If they say yes, then you write:

```python
# only if asked: detect same-PK conflicting labels
pk = ["project", "job", "question", "assessor"]
conflicts = df.groupby(pk)["label"].nunique()
conflicts[conflicts > 1]   # these PKs are ambiguous
```

---

## Step 3 — Q1: how many projects

```python
df["project"].nunique()
```

One line. Don't wrap it in a function unless asked. Answer: 3.

---

## Step 4 — Q2: how many questions per project

```python
df.groupby("project")["question"].nunique()
```

`nunique`, not `count` — you want *distinct* questions, not row counts. State that distinction; it's the kind of thing they're probing for.

---

## Step 5 — Q3: how many assessors labeled the same question

A "question" only means something inside its job, so group by the full key:

```python
df.groupby(["project", "job", "question"])["assessor"].nunique()
```

Again `nunique` on assessor. If they want a summary:

```python
per_q = df.groupby(["project","job","question"])["assessor"].nunique()
per_q.describe()      # mean, min, max assessors per question
```

---

## Step 6 — Majority vote per question

For binary labels, the majority is just **mean ≥ 0.5**. No need for `value_counts` or `mode` gymnastics.

```python
votes = df.groupby(["project","job","question"])["label"].mean()
majority = (votes >= 0.5).astype(int)
```

`mean` is the trick to know cold: for 0/1 data the mean *is* the proportion voting 1. Mention the tie case (mean exactly 0.5, only possible with an even number of assessors) and how you'd break it — drop, or default to a class. Don't implement unless asked.

---

## Step 7 — Assessor quality (leave-one-out deviation)

The metric: for each assessor, how far do their answers sit from what *the other* assessors said on the same question. The "exclude yourself" part is the whole point.

**The key trick — leave-one-out mean as a closed form.** Don't loop. For a group with sum `S` and count `n`, the mean excluding one value `x` is:

```
(S - x) / (n - 1)
```

So:

```python
g = df.groupby(["project","job","question"])["label"]
df["grp_sum"] = g.transform("sum")
df["grp_n"]   = g.transform("count")

# drop questions with only one assessor — no peers to compare against
df = df[df["grp_n"] > 1]

# peer consensus, excluding this assessor
df["peer_mean"] = (df["grp_sum"] - df["label"]) / (df["grp_n"] - 1)

# signed deviation of this assessor from their peers
df["dev"] = df["label"] - df["peer_mean"]
```

Then aggregate per assessor. The brief asked for **median** (central tendency) and **std** (the actual quality score — bigger = worse):

```python
quality = (
    df.groupby("assessor")["dev"]
      .agg(bias="median", noise="std", n_replies="count")
      .sort_values("noise", ascending=False)   # worst at top
)
quality.head(10)
```

`transform` is the thing to know: it computes a per-group value and broadcasts it back to every row in original order, in one vectorized C pass. That's how you do leave-one-out without an O(n²) loop. The interviewer is almost certainly listening for either "transform" or the `(S-x)/(n-1)` identity.

Two interpretation points worth saying aloud:
- **bias** (median deviation) ≈ 0 means unbiased; far from 0 means the assessor systematically leans one way vs peers.
- **noise** (std) is the headline score: an erratic assessor has high std even if their bias is 0.

---

## What actually sank you, and the fix

1. **Forgot `pd.to_datetime`.** Add "check + fix dtypes" to your Step 0 reflex. Always run `df.dtypes` after loading.

2. **Over-engineered the simple part.** Tasks 1–3 are one-liners. The instinct to build a `Col` dataclass, a cleaning pipeline, and conflict-resolution logic is good *engineering* but bad *interviewing* — it spends your time budget on the wrong thing and signals you can't gauge scope. The senior move is to write the minimal correct answer, then verbally flag the edge cases and let them choose.

3. **Reframe the over-engineering instinct as a strength.** You clearly *see* the edge cases — that's valuable. Just voice them instead of coding them: "There's a subtlety here with X, want me to handle it?" You get full credit for the insight at zero time cost, and you look senior for managing scope.

Practice loop: load → dtypes/nulls/dupes → answer each question in one line → only elaborate when prompted. Run it a few times against the CSV until the simple path feels automatic.
