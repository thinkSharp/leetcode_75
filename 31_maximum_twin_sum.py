import unittest
from typing import Optional
"""
Problem understanding: finding the twin sum of a linked list
Since we will not be able to traverse back
we will use deque
append all the link list

once linklist end:
use while loop to popleft and right and save the max.

Time complexity O(n)
space complexity O(n)

++ Second approach
using fast pointer technique, move the fast pointer to the end of the linkedlist
while slow pointer would be in the middle. Along the way, reverse the slow pointer direction.
once the fast pointer reached the end, slow pointer would be in the middle and prev would be behind
then loop both slow and prev till the end and find the max.

Time Complexity O(n)
Space complexity O(1)
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        max_sum = 0
        while prev and slow:
            max_sum = max(max_sum, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return max_sum
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        l4 = ListNode(4)
        l3 = ListNode(3, l4)
        l2 = ListNode(2, l3)
        l1 = ListNode(1, l2)
        self.assertEqual(self.sol.pairSum(l1), l1)


if __name__ == '__main__':
    unittest.main()
    