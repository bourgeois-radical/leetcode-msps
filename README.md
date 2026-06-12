# LeetCode / Coding Prep — MSPS

**Participant:** Andrius Rumša | **Started:** 2025-11-17 | **Schedule:** 08:00–09:00 Mon–Sat

> Study the solution. Understand it deeply. Close the reference. Replicate from memory. Only then does the pattern stick.

---

## Method (MSPS)

**MSPS** = Method for Memorising Solutions to Problems

1. Watch/read the optimal solution until you genuinely understand the approach
2. Close everything
3. Replicate from scratch — if you look back, it doesn't count, start over
4. Submit, then document (approach, edge cases, complexity)

The goal is not 500 problems. It is 50 patterns internalized so well you can reproduce them under pressure.

---

## Repository Structure

`structures/` and `algorithms/` = code, organised by topic.
`patterns/` = one `.md` reference note per solved problem — the key insight only.

```
leetcode-msps/
├── README.md
├── progress.md
├── motivation.md
│
├── dsa/
│   ├── structures/
│   │   ├── arrays/
│   │   │   ├── lc001_two_sum.py
│   │   │   ├── lc015_3sum.py
│   │   │   ├── lc121_best_stock.py
│   │   │   ├── lc167_two_sum_II.py
│   │   │   ├── lc200_number_of_islands.py
│   │   │   └── lc238_except_self.py
│   │   ├── hash_tables/
│   │   ├── strings/
│   │   ├── linked_lists/
│   │   ├── stacks/
│   │   ├── queues/
│   │   ├── trees/
│   │   │   ├── lc104_max_depth.py
│   │   │   └── lc226_invert_binary.py
│   │   ├── graphs/
│   │   └── heaps/
│   │
│   ├── algorithms/
│   │   ├── two_pointers/
│   │   ├── sliding_window/
│   │   ├── binary_search/
│   │   ├── dynamic_programming/
│   │   ├── greedy/
│   │   ├── backtracking/
│   │   ├── sorting/
│   │   └── divide_and_conquer/
│   │
│   └── patterns/
│       ├── two_pointers/
│       │   ├── lc015_3sum.md
│       │   └── lc167_two_sum_ii.md
│       ├── sliding_window/
│       │   └── lc121_best_time_to_buy_sell_stock.md
│       ├── hash_map/
│       │   └── lc001_two_sum.md
│       ├── prefix_suffix/
│       │   └── lc238_product_except_self.md
│       ├── bfs_dfs/
│       │   ├── lc104_max_depth_binary_tree.md
│       │   ├── lc200_number_of_islands.md
│       │   └── lc226_invert_binary_tree.md
│       ├── binary_search/
│       ├── dynamic_programming/
│       ├── greedy/
│       ├── backtracking/
│       ├── fast_slow_pointers/
│       ├── merge_intervals/
│       └── monotonic_stack/
│
├── math/
│   ├── number_theory/
│   ├── combinatorics/
│   └── probability/
│
├── pandas/
│   ├── filtering/
│   ├── groupby_agg/
│   ├── merge_join/
│   └── window_functions/
│
└── sql/
    ├── joins/
    ├── aggregations/
    ├── window_functions/
    ├── subqueries/
    └── cte/
```

---

## Solution Template

```python
# https://leetcode.com/problems/[problem-slug]/
# Difficulty: Easy / Medium / Hard  |  Date: YYYY-MM-DD

"""
APPROACH:

EDGE CASES:

TIME:  O(?)
SPACE: O(?)

FISHKA (key insight):
"""

from typing import List


class Solution:
    def solve(self, ...) -> ...:
        ...


if __name__ == "__main__":
    ...
```

---

## Quality Bar

Every committed solution must have:
- LeetCode URL in the first line
- Fishka comment — one sentence on the core insight
- Descriptive variable names (`left_pointer` not `l`)
- Time and space complexity stated

---

## Resources

### ML
- [Deep-ML](https://www.deep-ml.com/problems) - Practice Machine Learning and Data Science leetcode-style problems

### DSA
- [NeetCode 150](https://neetcode.io/practice/practice/neetcode150) — structured 150 with video explanations
- [LeetCode Patterns](https://seanprashad.com/leetcode-patterns/) — problems grouped by pattern
- [StrataScratch — Algorithms](https://platform.stratascratch.com/algorithms) — real tech interview questions

### SQL
- [DataLemur](https://datalemur.com/questions) — SQL window functions and analytics

### Pandas / Analytics
- [StrataScratch — Analytical Questions](https://platform.stratascratch.com/coding) — real-dataset pandas + SQL

### Conceptual / Non-coding
- [StrataScratch — Non-coding](https://platform.stratascratch.com/technical) — stats, probability, theory

---

> *"Fortune favors the prepared mind."*
> Open [motivation.md](motivation.md) if you need a reason to start.
