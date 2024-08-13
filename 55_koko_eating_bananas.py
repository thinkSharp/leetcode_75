import unittest
from typing import List
"""
Problem understanding:
	eat minimum integer K such that Koko can eat all the bananas with h hours

Solution Approach:
		if h == len(piles): return max(piles)
		otherwise:
			sort the array:
			using binary search get the mid and calculate the hours for all
			if exceeding hours: 
				right = mid - 1
			else:
				left = mid + 1
			
			return mid matches with hours: then all good
			otherwise:
				left of returned right should be also perform binary search
				
				
				two functions:
					- binary search
					- calculate hours per K
"""
class Solution:
    def calculatehours(self, piles: List[int], h: int, k: int) -> int:
        sum_b = 0
        for bs in piles:
            if bs <= k:
                sum_b += 1
            else:
                sum_b += (bs // k) + (1 if (bs % k) > 0 else 0)
            if sum_b > h:
                return h + 1
        return sum_b
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n == h:
            return max(piles)
        
        left, right, ans = 1, max(piles), -1
        while left <= right:
            mid = (left + right) // 2
            s_h = self.calculatehours(piles, h, mid)
            if s_h <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
    


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test_given_tests(self):
        self.assertEqual(self.sol.minEatingSpeed(piles = [3,6,7,11], h = 800), 1)
        self.assertEqual(self.sol.minEatingSpeed(piles = [30,11,23,4,20], h = 8), 15)
        self.assertEqual(self.sol.minEatingSpeed(piles = [30,11,23,4,20], h = 7), 20)
        self.assertEqual(self.sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5), 30)
        self.assertEqual(self.sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6), 23)
        self.assertEqual(self.sol.minEatingSpeed(piles = [312884470], h = 312884469), 2)

if __name__ == '__main__':
    unittest.main()




