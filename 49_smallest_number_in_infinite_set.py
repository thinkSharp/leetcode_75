import unittest
from typing import List
"""
Problem Understanding:
	- problem is asking for an implementation of min-heap with the condition that if an element is already added, it should not add another one
	- since pop will remove the smallest emement, rearange the array
	- add positive integer if it is not in stack
	
Solution approach:
  - build a heap data structure
  - have list and set in the structure
  - create heapify method to move the elements according to min-heap
  - implement addback
  - implement popsmallest()


time complexity: O(nlogn) 
space complexity: O(n)
"""

class SmallestInfiniteSet:

    def __init__(self):
        self._h = []
        self._s = set()
        self._m = 1

    def heapify(self, index):
        n = len(self._h)
        left = (2 * index) + 1
        right = (2 * index) + 2

        smallest = index
        if left < n and self._h[left] < self._h[smallest]:
            smallest = left
        if right < n and self._h[right] < self._h[smallest]:
            smallest = right

        if smallest != index:
            self._h[smallest], self._h[index] = self._h[index], self._h[smallest]
            self.heapify(smallest)

    def popSmallest(self) -> int:
        n = len(self._h)
        if n > 0:
            p_val = self._h[0]
            if n > 1:
                self._h[0] = self._h.pop()
                self.heapify(0)
            else:
                self._h.pop()

            self._s.remove(p_val)
            return p_val
        else:
            p_val = self._m
            self._m += 1
            return p_val

    def addBack(self, num: int) -> None:
        if num >= self._m or num in self._s:
            return

        self._s.add(num)
        self._h.append(num)
        index = len(self._h) - 1

        while index != 0:
            parent = (index - 1) // 2
            if self._h[parent] > self._h[index]:
                self._h[parent], self._h[index] = self._h[index], self._h[parent]
                index = parent
            else:
                break


if __name__ == '__main__':
    unittest.main()