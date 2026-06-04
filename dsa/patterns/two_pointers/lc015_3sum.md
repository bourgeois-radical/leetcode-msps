# LC15 - 3Sum
**Link:** https://leetcode.com/problems/3sum/
**Difficulty:** Medium
**Pattern:** Two Pointers

## Fishka
Sort first. Fix one element `i`, then use left/right pointers to find the pair that sums to `-nums[i]`. Skip duplicates at every level to avoid duplicate triplets.

## Approach
1. Sort `nums`
2. For each `i` (skip if `nums[i] == nums[i-1]`):
   - `left = i+1`, `right = len-1`
   - If sum == 0 → record, skip duplicate `left`/`right`, move both inward
   - If sum < 0 → `left += 1`
   - If sum > 0 → `right -= 1`

## Complexity
- Time: O(n²)
- Space: O(1) (output excluded)
