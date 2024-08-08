from typing import Optional, List
from collections import deque
"""
Problem Understanding: binary tree right side view:

Solution approach:
- using Breath first search:
	- add all nodes from one level:
	- while stack is not empty
		- get the count:
		- loop the count:
			- get the last one: add to array:
			- add all the children

repeat till stack is empty

O(n) for both Time and Space complexity
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right_side = []
        queue = deque()
        queue.append(root)
        while queue:
            ln = len(queue)
            for i in range(1, ln + 1):
                item = queue.popleft()
                if i == ln:
                    right_side.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
        return right_side