# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        que = deque()
        que.append(root)

        while que:
            curr_node = que.popleft()
            if curr_node is not None:
                left_node = curr_node.left
                right_node = curr_node.right
                if curr_node.left:
                    curr_node.left = right_node
                    que.append(right_node)
                if curr_node.right:
                    curr_node.right = left_node
                    que.append(left_node)

        return root


