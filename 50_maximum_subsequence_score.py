import unittest
from typing import List
import heapq
"""
Problem understanding:
- finding maximum subsequence from two array
- first array is some of K sub sequence
- second array is min from k sub sequence
- return the max of the multiplication of sum and min

Solution Approach:
- trying to get max min from second array that produce the max_score
- zip and sort the array by num 2 decending order
- loop through the new array and add the K items in the heap
- calculate sum and multiple with min value
- if heap length is reater then k remove the min value
- return the max_s

Time complexity:
    - ziping and sorting => nlogn
    - creating heap for k => logk for n elements => nlogk
    - nlogn + nlogk => 2 nlogn => nlog
Space complexity o(n)
"""
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        z_nums = sorted(zip(nums1, nums2), key=lambda x : -x[1])

        min_heap = []
        max_score = 0
        curr_score = 0

        for i in range(len(z_nums)):
            n1, n2 = z_nums[i]
            
            heapq.heappush(min_heap, n1)
            curr_score += n1

            if len(min_heap) > k:
                curr_score -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                score = curr_score * n2
                max_score = max(max_score, score)

        return max_score
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3), 12)
        self.assertEqual(self.sol.maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1), 30)

if __name__ == '__main__':
    unittest.main()
