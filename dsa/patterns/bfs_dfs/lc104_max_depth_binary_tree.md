# LC104 - Maximum Depth of Binary Tree
**Link:** https://leetcode.com/problems/maximum-depth-of-binary-tree/
**Difficulty:** Easy
**Pattern:** BFS / DFS on Tree

## Fishka
Queue = horizontal (breadth). Stack = vertical (depth). For BFS: store `(node, depth)` pairs in the queue; the last depth popped is the answer. For DFS: use a stack the same way but track `max_depth` separately since you don't process level by level.

## Approach (BFS)
1. Push `(root, 1)` to queue
2. Pop each `(node, depth)`, push children with `depth + 1`
3. Last `depth` seen = max depth

## Approach (DFS)
1. Same but with stack + explicit `max_depth` variable

## Complexity
- Time: O(n)
- Space: O(n)
