# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional
from math import ceil


class Solution:
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