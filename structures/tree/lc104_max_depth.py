# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from math import ceil


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # append and popleft

        # curr = 3 que = 9 (left), 20 (right)
        # curr = 9 que = 20, null, null
        # curr = 20 que = 15, 7
        # curr = 15, que = 7
        # curr = 7, que =
        #

        # dfs solution

        def dfs_depth(stack):
            if len(stack) == 1:
                depth = 1
            else:
                return 0
            while stack:
                curr = stack.pop()
                if curr is not None:
                    left = curr.left
                    right = curr.right
                    if left is not None:
                        stack.append(left)
                    if right is not None:
                        stack.append(right)
                    if right is not None or left is not None:
                        depth += 1

        #    return depth

        # stack_right = deque()
        # stack_left = deque()

        # if root:
        #    if root.left is None and root.right is None:
        #        return 1
        #    curr = root
        #    stack_right.append(curr.right)
        #    stack_left.append(curr.left)
        # else:
        #    return 0

        # right_depth = dfs_depth(stack=stack_right) + 1
        # left_depth = dfs_depth(stack=stack_left) + 1

        # return max(right_depth, left_depth)

        que = deque()
        if root:
            if root.left is None and root.right is None:
                return 1
            curr = root

        else:
            return 0

        while que:
            curr = que.popleft()
            if curr is not None:
                left = curr.left
                right = curr.right
                if left is not None:
                    que.append(left)
                if right is not None:
                    que.append(right)

                # len(visited) - len(que)