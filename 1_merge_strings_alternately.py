import unittest
"""
Problem Understanding: This is simply asking to merge two strings. 
Solution Approach: get smallest string merge one by one, then take the larger string and append the rest

Time Complexity: O(len of larger string)
Space Complexity: O(len of output string)
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_w1 = len(word1)
        len_w2 = len(word2)

        if len_w1 == 0 and len_w2 == 0:
            return ''
        elif len_w1 == 0:
            return word2
        elif len_w2 == 0:
            return word1

        min_len = min(len_w1, len_w2)

        output = []
        for i in range(min_len):
            output.append(word1[i])
            output.append(word2[i])
        
        if len_w1 > len_w2:
            for i in range(min_len, len_w1):
                output.append(word1[i])
        elif len_w2 > len_w1:
            for i in range(min_len, len_w2):
                output.append(word2[i])

        return ''.join(output)
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.mergeAlternately('abc','pqr'),'apbqcr')
        self.assertEqual(self.sol.mergeAlternately('ab','pqrs'),'apbqrs')
        self.assertEqual(self.sol.mergeAlternately('abcd','pq'),'apbqcd')
        


if __name__ == '__main__':
    unittest.main()