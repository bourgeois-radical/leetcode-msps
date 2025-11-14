# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from inspect import stack
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        que = deque()
        if root:
            if root.left is None and root.right is None:
                return 1
            curr = root
            depth = 1
            que.append((curr, depth))
        else:
            return 0

        while que:
            curr, curr_depth = que.popleft()
            if curr is not None:
                left = curr.left
                right = curr.right
                if left is not None:
                    child_depth = curr_depth + 1
                    que.append((left, child_depth))
                if right is not None:
                    child_depth = curr_depth + 1
                    que.append((right, child_depth))

        return curr_depth

'''
Fishka №1:
The complexity of solution one can substitute through using more memory
Instead of using just one counter for the entire tree
We used additional info such as depth of each node (as opposed to the depth of the entire tree)
to calculate the depth of the entire tree

Fishka №2:
Write all edge cases first to improve runtime
For instance:
if root.left is None and root.right is None:
  return 1

Fishka №3
Why BFS is que and DFS is stack
becuase:
que is horizontal logic (clients in a que normally stay in line, hence breadth. que = breadth)
stack is verical logic (something drops down and you have to pick up what is on top first. stack = depth)

TODO: try to solve using DFS without recursion. Use curr_depth and child_depth but add one another variable
 for measuring max_depth. Use stack instead of que.
'''

class DFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        que = deque()
        if root:
            if root.left is None and root.right is None:
                return 1
            curr = root
            depth = 1
            que.append((curr, depth))
        else:
            return 0

        max_depth = depth
        while que:
            curr, curr_depth = que.pop()
            if max_depth < curr_depth:
                max_depth = curr_depth
            if curr is not None:
                left = curr.left
                right = curr.right
                if left is not None:
                    child_depth = curr_depth + 1
                    que.append((left, child_depth))
                if right is not None:
                    child_depth = curr_depth + 1
                    que.append((right, child_depth))

        return max_depth