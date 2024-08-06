import unittest
from typing import Optional
"""
Problem Understanding:
delete the middle node of the linked list
n is the size of link list
if n is 0, 1, 2, 3, 4, 5 => 0, 0, 1,1,2,2

[0,1,2,3,4,5,6]
slow = false = head
while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
						
slow = fast = 0
prev = slow = 0
slow = slow.next = 1
fast = fast.next.next = 2

prev = slow = 1
slow = slow.next = 2
fast = fast.next.next = 4

prev = slow = 2
slow = slow.next = 3
fast = fast.next.next = 6


delete the middle node:
prev.next = slow.next

"""
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev = ListNode()
        prev.next = head
        slow = prev
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return prev.next
    