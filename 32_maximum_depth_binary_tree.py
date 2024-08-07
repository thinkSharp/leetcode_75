import unittest
from typing import Optional
"""
Problem Understanding: Finding the max depth
- DFS => recursive approach
				- based check if it is null node: return zero
				- otherwise, return 1+ max(left, right)

Time complexity O(n)
Space complexity O(n) since this is recursive call and stack will be created at each node
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)