import unittest
from typing import List
"""
Problem Understanding:
- find the Kth largest element from the array without using sorting

Solution Approach:
- create a heap that allow to insert, pop, heapify the inserted item
- that way, we can get the desire output without sorting

Time complexity would be O(nlongk) where n is length of the array to heapify and logn to get the Kth element
Space complexity would be O(k) for saving array in the heap
"""
class heap:
    def __init__(self, k) -> None:
        self._heap = []
        self._k = k
    
    def heapify(self, index):
        n = len(self._heap)
        left = (2 * index) + 1
        right = (2 * index) + 2

        largest = index
        if left < n and self._heap[left] < self._heap[largest]:
            largest = left

        if right < n and self._heap[right] < self._heap[largest]:
            largest = right

        if largest != index:
            self._heap[index] , self._heap[largest] = self._heap[largest], self._heap[index]
            self.heapify(largest)

    def insert(self, val):
        if self._k == len(self._heap):
            if val <= self._heap[0]: # optimization to no go through the insert
                return
            
            self._heap[0] = val
            self.heapify(0)
        else:
            self._heap.append(val)

            index = len(self._heap) - 1

            while index != 0:
                parent = (index - 1) // 2
                if self._heap[parent] > self._heap[index]:
                    self._heap[parent] , self._heap[index] = self._heap[index], self._heap[parent]
                    index = parent
                else:
                    break

    def return_kth(self):
        return self._heap[0]
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = heap(k)

        for i in range(len(nums)):
            h.insert(nums[i])

        return h.return_kth()
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2), 5)
        self.assertEqual(self.sol.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4), 4)


if __name__ == '__main__':
    unittest.main()


