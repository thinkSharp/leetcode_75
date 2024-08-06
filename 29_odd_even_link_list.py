import unittest
from typing import Optional
"""
Solution Approach:
create optr, eptr, ehead
optr = head
if optr.next:
	eptr = optr.next
	ehead = optr.next
loop while (optr and optr.next) or (eptr and eptr.next):
	if eptr.next:
		optr.next = eptr.next
		optr = eptr.next
 if optr.next:
	 eptr.next = optr.next
	 eptr = optr.next
	 
optr.next = ehead

time complexity: o(n)
space complexity : o(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        optr = head

        eptr, ehead = optr.next, optr.next
        
        if not eptr or not eptr.next:
            return head

        while (optr and optr.next) or (eptr and eptr.next):

            if (eptr and eptr.next) and optr:
                optr.next = eptr.next
                optr = eptr.next

            if (optr and optr.next) and eptr:
                eptr.next = optr.next
                eptr = optr.next

            if not optr.next or not eptr.next:
                eptr.next = None
                break


        if optr:
            optr.next = ehead

        return head
    
class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):

        #l5 = ListNode(5)
        l4 = ListNode(4 )
        l3 = ListNode(3, next = l4)
        l2 = ListNode(2, next = l3)
        l1 = ListNode(1, next = l2)
        self.assertEqual(self.sol.oddEvenList(l1), l1)

if __name__ == '__main__':
    unittest.main()