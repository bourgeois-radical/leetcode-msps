# LC200 - Number of Islands
**Link:** https://leetcode.com/problems/number-of-islands/
**Difficulty:** Medium
**Pattern:** DFS / BFS on Grid

## Fishka
Each connected component of `'1'`s is an island. When you hit an unvisited `'1'`, increment the counter and flood-fill the entire island (DFS via stack or BFS via queue), marking visited cells as `'0'` to avoid re-counting.

## Approach
1. Iterate the grid like reading a book (row by row)
2. On each `'1'`: `islands += 1`, then DFS to mark all connected `'1'`s as `'0'`
3. DFS: push cell to stack, pop and visit 4 neighbours, push unvisited land neighbours

## Complexity
- Time: O(m × n)
- Space: O(m × n) worst case stack
