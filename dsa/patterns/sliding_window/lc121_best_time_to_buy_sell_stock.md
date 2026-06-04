# LC121 - Best Time to Buy and Sell Stock
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
**Difficulty:** Easy
**Pattern:** Sliding Window (fixed left = best buy)

## Fishka
Track `best_buy` (minimum seen so far) as you scan. At each step compute `curr_price - best_buy` and keep a running max. The window's left boundary slides forward only when a new minimum is found.

## Approach
1. `best_buy = prices[0]`, `max_roi = 0`
2. For each `curr_price`:
   - `best_buy = min(best_buy, curr_price)`
   - `max_roi = max(max_roi, curr_price - best_buy)`
3. Return `max_roi`

## Complexity
- Time: O(n)
- Space: O(1)
