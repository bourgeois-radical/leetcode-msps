# LC238 - Product of Array Except Self
**Link:** https://leetcode.com/problems/product-of-array-except-self/
**Difficulty:** Medium
**Pattern:** Prefix / Suffix Product

## Fishka
"Everything except i" = "everything before i" × "everything after i". Two sequential O(n) passes are still O(n) total — not nested loops. Reuse the output array: first pass fills prefix products, second pass multiplies in suffix products in-place → O(1) extra space.

## Approach
1. Forward pass: `output[i]` = product of all elements before `i` (start with `1`)
2. Backward pass: multiply each `output[i]` by the running suffix product

## Complexity
- Time: O(n)
- Space: O(1) (output array excluded per problem statement)
