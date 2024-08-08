from typing import Optional
"""
Problem understanding: maximum level sum of a binary tree,
find the level where sum of that level is maximum
level start with 1
tree will not be empty

solution approach:
Breath First Search
- get nodes from one level at a time and sum them up, 
- compare the sum with the max_sum

return max_sum

O(n) for both time and space
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, max_level = float('-inf'), 0
        queue = [root]

        level = 0
        while queue:
            level += 1
            ln = len(queue)
            level_sum = 0
            for i in range(ln):
                item = queue.pop(0)
                level_sum += item.val
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
        return max_level
