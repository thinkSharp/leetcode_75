import unittest
"""
Problem Understanding:
edit distance => convert word1 to word2 in minum number of operations
- Operations
	- insert a char
	- delete
	- replace

Solution Approach:
	Example  horse
	    to ros
		  -
			replace h with r
			remove r
			remove e
			-
			intention
			execution
			- replace entention
			- replace enention
			- remove t
			-- 
			-- Patten is recursive function
			-- I am able to use memo as well
			-- base case index == len(word2)
									return
								word1[idx] == word2[idex] => just move to next index
								else:
									min of (insert, replace, remove)
								
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i >= n1:
                return n2 - j
            
            if j >= n2:
                return n1 - i
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i + 1, j + 1)
            else:
                insert = 1 + dp(i, j + 1)
                replace = 1 + dp(i + 1, j + 1)
                delete = 1 + dp(i + 1, j)
                memo[(i, j)] = min(insert, replace, delete)

            return memo[(i, j)]
        return dp(0, 0)



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.minDistance(word1 = "horse", word2 = "ros"), 3)
        self.assertEqual(self.sol.minDistance(word1 = "intention", word2 = "execution"), 5)

if __name__ == '__main__':
    unittest.main()

  
