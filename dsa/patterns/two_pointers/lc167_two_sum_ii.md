# LC167 - Two Sum II (Input Array Is Sorted)
**Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
**Difficulty:** Medium
**Pattern:** Two Pointers

## Fishka
Array is sorted → left pointer increases the sum (shift right), right pointer decreases the sum (shift left). Converge until you hit the target. No extra space needed.

## Approach
1. `left = 0`, `right = len-1`
2. `curr_sum = nums[left] + nums[right]`
   - `< target` → `left += 1`
   - `> target` → `right -= 1`
   - `== target` → return `[left+1, right+1]` (1-indexed)

## Complexity
- Time: O(n)
- Space: O(1)
