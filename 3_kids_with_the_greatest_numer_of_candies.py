from typing import List
import unittest
"""
problem: find if after given extracandies, the kid will have greatest no. of candies
solution approach:
    find the max
    create output of same size with marked them all true
    loop through the array and if current + extracandies < max: set output ith index to false

    return output

time complexity: O(len of candies)
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        len_candies = len(candies)
        output = [True] * len_candies
        max_c = max(candies)
        for i in range(len_candies):
            if candies[i] + extraCandies < max_c:
                output[i] = False

        return output
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.kidsWithCandies([2,3,5,1,3], 3),[True, True,True,False,True])
        self.assertEqual(self.sol.kidsWithCandies([4,2,1,1,2], 1),[True, False,False,False,False])
        self.assertEqual(self.sol.kidsWithCandies([12,1,12], 10),[True, False,True])



if __name__ == '__main__':
    unittest.main()