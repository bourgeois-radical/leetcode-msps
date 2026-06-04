# LC1 - Two Sum
**Link:** https://leetcode.com/problems/two-sum/
**Difficulty:** Easy
**Pattern:** Hash Map

## Fishka
Use a hash map to store `value → index` as you iterate. For each element, check if its complement (`target - curr`) already exists in the map. This trades O(n) space to cut time from O(n²) to O(n).

## Approach
1. For each `curr_num` at `curr_index`, compute `looked_for = target - curr_num`
2. If `looked_for` is in the map → return `[map[looked_for], curr_index]`
3. Else store `curr_num → curr_index` in the map

## Complexity
- Time: O(n)
- Space: O(n)
