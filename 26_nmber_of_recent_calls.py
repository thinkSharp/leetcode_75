import unittest
"""
Problem Understanding:
  1. return the no. of ping that happen past 3000 milliseconds
  2. example: [0, 1, 10, 100, 1001, 1002, 2001, 2003, 3001, 3005, 4001, 5002,6000]
  3. [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 5,5]
  4. queue [0, 1,10,100,1001,1002,2001,2003,3001, 3005]
  5. so top of the queue should be pop if greater then 3000, 


TimeComplexity O(n)
spac Complexity O(n) for creating a queue
"""

class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while t - self.queue[0] > 3000:
            self.queue.pop(0)
        return len(self.queue)