import unittest
from typing import List
"""
find the consecutive 1s which allow to count zeros up to k
return max such sub_string

Solution Approach:
have flip_count =[]
curr_count, max_count
loop from 0 to n
count all 1s and 0s till K
if flip == K
    remove one zero
    reset curr
    check for max

return max

Time complexity: O(n) since this is looping nums once
space complexity O(k) for storing k indexes
"""
class Solution:
    def longestOnes(self, nums: List[int], k = int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1
    
    def longestOnes_original(self, nums: List[int], k = int) -> int:
        ln = len(nums)
        if ln <= k:
            return ln
        flipped = []
        cc, mc = 0 , 0
        for i in range(ln):
            if nums[i] == 1:
                cc += 1
            elif nums[i] == 0 and len(flipped) < k:
                cc += 1
                flipped.append(i)
            elif nums[i] == 0 and len(flipped) == k:
                
                if cc > mc:
                    mc = cc
                if k > 0:
                    first_index = flipped.pop(0)
                    cc = i - first_index
                    flipped.append(i)
                elif k == 0:
                    cc = 0
                    
        if cc > mc:
            mc = cc
        return mc

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2), 6)
        self.assertEqual(self.sol.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3), 10)
        self.assertEqual(self.sol.longestOnes([1,0,1,1,0,1,1,1,0], 0), 3)
if __name__ == '__main__':
    unittest.main()

