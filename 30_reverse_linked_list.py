import unittest
from typing import Optional
"""
problem Understanding:
Reverse a singly linked list:
need three pointers:
first, second, curr
while curr:
	curr = second.next
	second.next = first
	first = second
	second = curr
	
	Solution Approach:
	first, second,curr
	first = head
	second, curr = first.next, first.next
	
	while curr:
		curr = curr.next
		second.next = first
		first = second
		second = curr.next
"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        l5 = ListNode(5)
        l4 = ListNode(4, l5)
        l3 = ListNode(3, l4)
        l2 = ListNode(2, l3)
        l1 = ListNode(1, l2)
        self.assertEqual(self.sol.reverseList(l4), l1)

if __name__ == '__main__':
    unittest.main()
