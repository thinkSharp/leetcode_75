from typing import Optional
"""
Problem Understanding:
find the node equal to the search val and return the sub tree:

Solution Approach:
- loop through the tree:
	- check curr.val == search
		- return curr

	else check if search val less then curr:
			take left node:
				set curr = left
	else right node
	
	space and O(1)
	time is O(logn)
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if not curr:
                return None
            if curr.val == val:
                return curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        return None