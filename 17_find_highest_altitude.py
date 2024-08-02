import unittest
from typing import List
"""
find highest altitude from the point.

solution approach,
have two variables ma and ca
loop through the gains
constrains gains -100 to 100
len 1 to 100

pseudo code:
ma, ca = -101, 0
for i in range(len(gain)):
	ca += gain[i]
	if ca > ma:
		ma = ca
	
	return ma
	
Time complexity; O(n) loop through the gain
Space complexity: O(1)
"""
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ma, ca = 0, 0
        for i in range(len(gain)):
            ca += gain[i]
            if ca > ma:
                ma = ca
        return ma
    
class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.largestAltitude([-5,1,5,0,-7]), 1)
        self.assertEqual(self.sol.largestAltitude( [-4,-3,-2,-1,4,3,2]), 0)

if __name__ == '__main__':
    unittest.main()