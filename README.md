# 🎯 LeetCode Challenge: MSPS Protocol

**Participants:** Gerti Sana & Andrius Rumša  

**Start Date:** November 17, 2025

**Target:** 50 problems solved  

---

## 🔤 What is MSPS?

**MSPS** = **M**ethod for **M**emorizing **S**olutions to **P**roblems  
*(Метод Запоминания Решения Задач)*

**The Core Method:**

This is NOT about solving problems from scratch. This is about **learning patterns through deliberate replication.**

### The MSPS Process:

1. **Study the solution**
   - Watch NeetCode video explanation
   - Read optimal solution (LeetCode editorial, LLM-generated, etc.)
   - Study until you **genuinely understand** the approach

2. **Close the reference**
   - No looking back at the solution
   - No peeking at the code
   - Pure replication from memory and understanding

3. **Replicate the solution**
   - Write the code from scratch
   - If you need to look back → **doesn't count, start over**
   - Only when you can replicate **without looking** → move to step 4

4. **Submit and document**
   - Add proper explanations (approach, edge cases, complexity)
   - Include clean code with descriptive variable names

### Why MSPS Works:

**Traditional approach (doesn't work):**
- Struggle for hours → give up → look at solution → copy-paste → "solved" ✓
- **Result:** Zero retention, wasted time, no pattern learned

**MSPS approach (actually works):**
- Study solution → understand deeply → replicate from memory → internalize pattern
- **Result:** Pattern is now IN YOUR HEAD, ready for variations in interviews

### The Philosophy:

> **"You don't need to solve 500 unique problems. You need to internalize 50 patterns."**

- Interviews don't test creativity, they test pattern recognition
- Copying a solution teaches nothing
- Replicating from understanding teaches everything
- If you can't replicate without looking, you didn't understand

### MSPS in Practice:

**Example: Two Sum**

❌ **Wrong way:**
```
1. Try for 10 minutes
2. Give up
3. Look at solution
4. Copy code
5. Submit
6. Move on
→ Pattern NOT learned
```

✅ **MSPS way:**
```
1. Watch NeetCode explanation (5-10 min)
2. Understand: "Use hashmap to store complements"
3. Close video
4. Try to code from memory
5. Stuck on syntax? → Look back (restart from step 3)
6. Successfully replicate without looking? → Submit
7. Add explanation in your own words
→ Pattern LEARNED and RETAINED
```

---

## 📋 Challenge Rules

### Core Protocol
- **Weekly Target:** 5 LeetCode problems per person (10 total per week)
- **Method:** Apply MSPS to each problem (study → understand → replicate → document)
- **Accountability:** €10 fine if weekly target missed
- **Recovery:** Solve 8 problems next week to reclaim fine money
- **Duration:** Until 50 problems solved, then evaluate continuation


### Quality Standards
Each solution must include:
1. **LeetCode link** at the top of file
2. **Explanation** with:
   - Reasoning and approach
   - Edge cases identified
   - Time & space complexity analysis
3. **Clean code principles:**
   - Handle `None`/null inputs explicitly
   - Use descriptive variable names (`left_pointer` not `l`, `right_pointer` not `r`)
   - Follow consistent formatting

### Mock Interview Extension
- **Peer review sessions:** Partners quiz each other on already-solved problems
- **Format:** Mock interview style - explain solution without looking at code
- **Goal:** Practice articulating thought process for real interviews

---

## 📂 Repository Structure
```
leetcode-msps/
├── README.md
├── progress.md
├── algorithms/
│   ├── gerti/
│   │   ├── binary_search/
│   │   │   ├── lc004_median_two_sorted_arrays.py
│   │   │   ├── lc033_search_rotated_sorted_array.py
│   │   │   └── lc074_search_2d_matrix.py
│   │   ├── dynamic_programming/
│   │   │   ├── lc070_climbing_stairs.py
│   │   │   ├── lc198_house_robber.py
│   │   │   └── lc322_coin_change.py
│   │   ├── greedy/
│   │   │   ├── lc055_jump_game.py
│   │   │   └── lc134_gas_station.py
│   │   ├── backtracking/
│   │   │   ├── lc039_combination_sum.py
│   │   │   └── lc046_permutations.py
│   │   └── divide_and_conquer/
│   │       ├── lc023_merge_k_sorted_lists.py
│   │       └── lc215_kth_largest_element.py
│   └── andrius/
│       ├── binary_search/
│       │   ├── lc033_search_rotated_sorted_array.py
│       │   └── lc153_find_minimum_rotated_sorted_array.py
│       ├── dynamic_programming/
│       │   ├── lc070_climbing_stairs.py
│       │   └── lc300_longest_increasing_subsequence.py
│       ├── greedy/
│       │   └── lc055_jump_game.py
│       ├── backtracking/
│       │   └── lc078_subsets.py
│       └── divide_and_conquer/
│           └── lc215_kth_largest_element.py
├── data_structures/
│   ├── gerti/
│   │   ├── arrays/
│   │   │   ├── lc001_two_sum.py
│   │   │   ├── lc011_container_most_water.py
│   │   │   ├── lc015_3sum.py
│   │   │   ├── lc217_contains_duplicate.py
│   │   │   └── lc238_product_except_self.py
│   │   ├── hash_tables/
│   │   │   ├── lc001_two_sum.py
│   │   │   ├── lc049_group_anagrams.py
│   │   │   └── lc128_longest_consecutive_sequence.py
│   │   ├── strings/
│   │   │   ├── lc003_longest_substring_no_repeat.py
│   │   │   ├── lc020_valid_parentheses.py
│   │   │   └── lc125_valid_palindrome.py
│   │   ├── linked_lists/
│   │   │   ├── lc021_merge_two_sorted_lists.py
│   │   │   ├── lc141_linked_list_cycle.py
│   │   │   ├── lc143_reorder_list.py
│   │   │   └── lc206_reverse_linked_list.py
│   │   ├── stacks/
│   │   │   ├── lc020_valid_parentheses.py
│   │   │   ├── lc150_evaluate_rpn.py
│   │   │   └── lc155_min_stack.py
│   │   ├── queues/
│   │   │   ├── lc232_implement_queue_using_stacks.py
│   │   │   └── lc622_design_circular_queue.py
│   │   ├── trees/
│   │   │   ├── lc098_validate_bst.py
│   │   │   ├── lc100_same_tree.py
│   │   │   ├── lc102_binary_tree_level_order.py
│   │   │   ├── lc104_max_depth_binary_tree.py
│   │   │   ├── lc226_invert_binary_tree.py
│   │   │   └── lc235_lca_bst.py
│   │   ├── graphs/
│   │   │   ├── lc133_clone_graph.py
│   │   │   ├── lc200_number_of_islands.py
│   │   │   └── lc207_course_schedule.py
│   │   └── heaps/
│   │       ├── lc215_kth_largest_element.py
│   │       └── lc347_top_k_frequent_elements.py
│   └── andrius/
│       ├── arrays/
│       │   ├── lc001_two_sum.py
│       │   ├── lc053_maximum_subarray.py
│       │   └── lc121_best_time_buy_sell_stock.py
│       ├── hash_tables/
│       │   ├── lc001_two_sum.py
│       │   └── lc242_valid_anagram.py
│       ├── strings/
│       │   ├── lc005_longest_palindromic_substring.py
│       │   └── lc049_group_anagrams.py
│       ├── linked_lists/
│       │   ├── lc019_remove_nth_from_end.py
│       │   └── lc206_reverse_linked_list.py
│       ├── stacks/
│       │   ├── lc020_valid_parentheses.py
│       │   └── lc739_daily_temperatures.py
│       ├── queues/
│       │   └── lc933_number_recent_calls.py
│       ├── trees/
│       │   ├── lc094_binary_tree_inorder.py
│       │   ├── lc102_binary_tree_level_order.py
│       │   └── lc543_diameter_binary_tree.py
│       ├── graphs/
│       │   ├── lc200_number_of_islands.py
│       │   └── lc994_rotting_oranges.py
│       └── heaps/
│           └── lc703_kth_largest_in_stream.py
└── patterns/
    ├── sliding_window/
    │   ├── lc003_longest_substring.md          # Reference only
    │   ├── lc076_minimum_window_substring.md   # Reference only
    │   └── lc121_best_time_buy_sell_stock.md   # Reference only
    ├── two_pointers/
    │   ├── lc001_two_sum.md                    # Reference only
    │   ├── lc015_3sum.md                       # Reference only
    │   └── lc167_two_sum_ii.md                 # Reference only
    ├── fast_and_slow_pointers/
    │   ├── lc141_linked_list_cycle.md          # Reference only
    │   └── lc142_linked_list_cycle_ii.md       # Reference only
    ├── merge_intervals/
    │   ├── lc056_merge_intervals.md            # Reference only
    │   └── lc057_insert_interval.md            # Reference only
    ├── cyclic_sort/
    │   ├── lc268_missing_number.md             # Reference only
    │   └── lc287_find_duplicate_number.md      # Reference only
    ├── in_place_reversal/
    │   ├── lc206_reverse_linked_list.md        # Reference only
    │   └── lc092_reverse_linked_list_ii.md     # Reference only
    └── bfs_dfs/
        ├── lc102_binary_tree_level_order.md    # Reference only
        ├── lc200_number_of_islands.md          # Reference only
        └── lc994_rotting_oranges.md            # Reference only
```
---

## 📝 Solution Template
```{python}
"""
LeetCode Problem: [Problem Name]
Link: https://leetcode.com/problems/[problem-slug]/
Difficulty: [Easy/Medium/Hard]
Date Solved: YYYY-MM-DD

PROBLEM DESCRIPTION:
[Brief description of the problem]

APPROACH:
[Explain your reasoning and strategy]

EDGE CASES:
1. [Edge case 1]
2. [Edge case 2]
3. [Edge case 3]

TIME COMPLEXITY: O(?)
SPACE COMPLEXITY: O(?)

LEARNINGS:
[What did you learn from this problem?]
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ...
        


# Test cases (maybe an overkill since we submit on leetcode.com)
if __name__ == "__main__":
    
    ...
    
    print("✅ All test cases passed!")
```

---

## 🤝 Mock Interview Protocol

### Session Structure
1. **Duration:** 2 medium leetcode problems/60 minutes
2. **Format:**
   - Partner selects a problem you've already solved
   - You explain solution from scratch (no looking at code)
   - Partner asks clarifying questions
   - Discuss alternative approaches
3. **Frequency:** Weekly or bi-weekly
4. **Goals:**
   - Practice articulating thought process
   - Identify gaps in understanding
   - Build interview confidence

### Sample Questions for Partner
- "Why did you choose this approach?"
- "What's the time complexity? Can you prove it?"
- "What if the input is empty/None/negative?"
- "Can you optimize this further?"
- "How would you test this solution?"

---

## 💡 Resources

### Primary
- [NeetCode.io](https://neetcode.io/) - Curated problem list with video explanations
- [LeetCode Patterns](https://seanprashad.com/leetcode-patterns/) - Problems grouped by pattern

### Supplementary
- [Grind 75](https://www.techinterviewhandbook.org/grind75) - Alternative curated list
- [Blind 75](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions) - Classic list

---

## 🔥 Motivation

> *"By your endurance you will gain your lives"*

This challenge is not just about solving problems. It's about:
- **Терпение (Patience/Endurance):** Building consistent practice over time
- **Accountability:** Supporting each other through the grind
- **Excellence:** Writing code that reflects our values (clean, thoughtful, well-documented)
- **Purpose:** Preparing for meaningful work in 1st-tier companies and beyond

LeetCode is absurd. Capitalism's gatekeeping is absurd. But we play the tactical game without losing our souls.

**50 problems. 10 weeks. Let's go.**

---

## 📅 Weekly Check-ins

**Format:** Every Sunday evening???
- Review week's progress
- Update progress.md
- Settle fines if applicable
- Plan next week's problems
- Optional: Schedule mock interview session

---

## 📜 License

This repository is for personal learning and mutual accountability.  
Solutions are educational and should not be used for academic dishonesty.


*"Die Wüste wächst: weh dem, der Wüsten birgt!"* - Nietzsche  
*But we cross the desert together.*