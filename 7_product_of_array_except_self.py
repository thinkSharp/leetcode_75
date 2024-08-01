import unittest
from typing import List
"""

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        before = 1
        after = 1
        for i in range(len(nums)):
            output[i] = before
            before *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            output[i] *= after
            after *= nums[i]
        return output
    
    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        len_n = len(nums)
        if len_n <= 1:
            return nums
        forward, rev = [nums[0]], nums[::]
        for i in range(1, len_n):
            forward.append(forward[i - 1] * nums[i])
        for i in range(len_n - 2, -1, -1):
            rev[i] = rev[i + 1] * rev[i]


        output = [rev[1]]
        for i in range(1, len_n-1):
            left =  forward[i - 1]
            right = rev[i + 1]
            output.append(left * right)

        output.append(forward[-2])
        return output
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(self.sol.productExceptSelf([-1,1,0,-3,3]),[0,0,9,0,0])


if __name__ == '__main__':
    unittest.main()