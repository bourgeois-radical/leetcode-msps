# https://leetcode.com/problems/invert-binary-tree/

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        que = deque()
        que.append(root)

        while que:
            curr_node = que.popleft()
            if curr_node is not None:
                # left_node = copy.deepcopy(curr_node.left)
                # right_node = copy.deepcopy(curr_node.right)
                # Why it works even without deepcopy?
                left_node = curr_node.left  # left_node points to -> curr_node.left
                right_node = curr_node.right  # right_node points to -> curr_node.right

                curr_node.left = right_node  # curr_node.left points to -> right_node -> curr_node.right
                que.append(left_node)

                curr_node.right = left_node  # curr_node.right points to -> left_node -> curr_node.left
                que.append(right_node)

                # So: 1. left -> curr.left
                # then 2. right -> curr.right
                # 3. curr.left -> right -> curr.right
                # left still points to -> curr.left that is why curr.right -> left -> curr.left still works

        return root
