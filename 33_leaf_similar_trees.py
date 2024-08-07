import unittest
from typing import Optional, List
"""
Problem Understanding: Find the leaf node sequence for both trees
		create a recursive function that returns leaf nodes and build array along the way, 
		compare both trees
		
		
		Time complexity: O(n) + O(n)
		space Complexity same
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], output: List):
        if root and not root.left and not root.right:
            output.append(root.val)
            return
        if root.left:
            self.dfs(root.left, output)
        if root.right:
            self.dfs(root.right, output)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left, right = [], []
        self.dfs(root1, left)
        self.dfs(root2, right)

        return left == right