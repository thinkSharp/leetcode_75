import unittest
from typing import List
import heapq
"""
Problem Understanding:
- Total Cost of Hire K workers from first candidates workers or last candidates worker:
- get the min for cost by selecting  k workers from candidates
- selection should be either from first list of candidates or last list of candidates
- if total count is less then candidates, just select the min candidate

Solution approach:
- definitely using min-heap
- check len is greather then 2 * candiates
- if it is then create two min-heaf, first and last candidate:
	- check which everone has smallest num,
	- pop and add as K
- then add one element from the main list to the pop side
- do the same thing till all element are considered
- then pop from either side until  K is fullfill

time Complexity 
O(n) for traversing the list + O(2 * log c) => O(nlogn)

Space complexity
O(n)
"""
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost = 0
        heap = []
        lp, rp = 0, len(costs) - 1

        if len(costs) > (2 * candidates):
            for lp in range(0, candidates):
                heapq.heappush(heap, (costs[lp], 'l'))

            for rp in range(len(costs) - 1, len(costs) - candidates - 1, -1):
                heapq.heappush(heap, (costs[rp], 'r'))
            lp += 1
            rp -= 1
        else:
            for i in range(lp, len(costs)):
                heapq.heappush(heap, (costs[i], 'a'))

        while k != 0:
            c, d = heapq.heappop(heap)
            cost += c
            k -= 1

            if lp <= rp:
                if d == 'l':
                    heapq.heappush(heap, (costs[lp], 'l'))
                    lp += 1
                elif d == 'r':
                    heapq.heappush(heap, (costs[rp], 'r'))
                    rp -= 1
        return cost
    

class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_failed_cases(self):
        self.assertEqual(self.sol.totalCost([28,35,21,13,21,72,35,52,74,92,25,65,77,1,73,32,43,68,8,100,84,80,14,88,42,53,98,69,64,40,60,23,99,83,5,21,76,34], k = 32, candidates=12), 1407)
    def test_given_cases(self):
        
        self.assertEqual(self.sol.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4), 11)
        self.assertEqual(self.sol.totalCost(costs = [1,2,4,1], k = 3, candidates = 3), 4)
        self.assertEqual(self.sol.totalCost(costs = [17,12,10,2,3,1,7,2,1,2,11,20,8], k = 8, candidates = 3), 26)

if __name__ == '__main__':
    unittest.main()

