import unittest
from typing import List
"""
Problem: find if given n integer can be planted in flowbed . Condition: cannot be adjacent plot
Solution Approach:
Find all the indexes of the planted plot
loop through them and find the slot:
    example count -= i - (i-1) // 3

we have to handle special case
    first position to first planted index
    count -= first planted index // 2

    last position to last index:
    count -= last position to index // 2

    return count <= 0
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = []
        len_f = len(flowerbed)
        count = n
        for i in range(len_f):
            if flowerbed[i] == 1:
                planted.append(i)
        if not planted:
            return (len_f + 1) // 2 >= 2
        
        for i in range(1, len(planted)):
            val = (planted[i] - planted[i-1] - 2) 
            count -= (val) // 2

        if planted[0] != 0:
            count -= planted[0] // 2

        if planted[-1] != len_f -1:
            count -= (len_f - planted[-1] -1) // 2

        return count <= 0
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.canPlaceFlowers([0,0,0,0,0,0,0,0,0],5), True)
        self.assertEqual(self.sol.canPlaceFlowers([1,0], 1), False)
        self.assertEqual(self.sol.canPlaceFlowers([1,0,0,0,0,1], 2), False)
        self.assertEqual(self.sol.canPlaceFlowers([1,0,1,0,0,0,0,0,1],2), True)
        self.assertEqual(self.sol.canPlaceFlowers([1,0,1,0,1,0,1],1), False)
        self.assertEqual(self.sol.canPlaceFlowers([1,0,0,0,1,0,0,0,0],3), True)
        self.assertEqual(self.sol.canPlaceFlowers([1,0,0,0,0,0,1,0,0],3), True)
        self.assertEqual(self.sol.canPlaceFlowers([1,0,0,0,0,0,0,0,1],3), True)
        self.assertEqual(self.sol.canPlaceFlowers([1,0,0,0,0,0,0,0,1],3), True)
        self.assertEqual(self.sol.canPlaceFlowers([1,0,0,0,0,0,0,1],2), True)
        self.assertEqual(self.sol.canPlaceFlowers([1,0,0,0,0,0,1], 2), True)
        
        self.assertEqual(self.sol.canPlaceFlowers([1,0,0,0,1], 1), True)
        self.assertEqual(self.sol.canPlaceFlowers([1,0,0,0,1], 2), False)


if __name__ == '__main__':
    unittest.main()