# LC226 - Invert Binary Tree
**Link:** https://leetcode.com/problems/invert-binary-tree/
**Difficulty:** Easy
**Pattern:** BFS on Tree

## Fishka
BFS level-order traversal. At each node: save both children as local references first, then swap them on the node. Local references stay valid after the swap because they point to the original subtree objects, not through `curr.left`/`curr.right`.

## Approach
1. Push `root` to queue
2. For each `curr_node`: save `left = curr.left`, `right = curr.right`
3. `curr.left = right`, `curr.right = left`
4. Push non-null children to queue

## Complexity
- Time: O(n)
- Space: O(n) (queue holds up to one full level)
