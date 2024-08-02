import unittest
from typing import List
"""
problem understanding:
count the loungest subarray of 1's after deleting one element
which mean zero or 1

Example Walk through:
[1,1,1,0,1,1,0,1,1,1,1,0]

Solution Approach:
lzi = -1
l = 0
for r in range(ln(nums)):
	if nums[r] == 0:
		if lzi == -1:
			lzi = r
	  else:
		  if r - l > mc:
				mc = r - 1
			l = lzi + 1
	if r - l > mc:
		mc = r - l
	return mc -1 if lzi == -1 else mc

time complexity = O(n)
space complexity = O(1)
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        lei, mc, lf = -1, 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                if lei == -1:
                    lei = r
                else:
                    if r - lf > mc:
                        mc = r - lf
                    lf = lei + 1
                    lei = r
        if r + 1 - lf > mc:
            mc = r + 1 - lf

        return mc - 1
    
class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.longestSubarray([1,1,0,1]), 3)
        self.assertEqual(self.sol.longestSubarray([0,1,1,1,0,1,1,0,1]), 5)
        self.assertEqual(self.sol.longestSubarray([1,1,1]), 2)
        self.assertEqual(self.sol.longestSubarray([1,1,1,0]),3)
        self.assertEqual(self.sol.longestSubarray([0,0,0,1]),1)
        self.assertEqual(self.sol.longestSubarray([1]), 0)

if __name__ == '__main__':
    unittest.main()

