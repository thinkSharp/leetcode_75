import unittest
import math
"""
Problem: asking to find the greatest common divisor of the string.
Solution approach: First get the length of both string. get the gcd of them
that will tell you where to stop. 
then pick that string length to make sure it is divisiable to both string
return the string

Time complexity: O(len of S1 + len of S2)
"""
class Solution:
    def bettersolution(self, word1: str, word2:str) -> str:
        if word1 + word2 == word2 + word1:
            len_gcd = math.gcd(len(word1), len(word2))
            return word1[:len_gcd]
        return ''
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_s1 = len(str1)
        len_s2 = len(str2)

        if len_s1 == 0 or len_s2 == 0:
            return ''

        len_gcd = math.gcd(len_s1, len_s2)
        output = str1[:len_gcd]
        for i in range(0,len_s1, len_gcd):
            if str1[i:i+len_gcd] != output:
                return ''
        for i in range(0, len_s2, len_gcd):
            if str2[i:i+len_gcd] != output:
                return ''
        return output
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.gcdOfStrings('ABCABC','ABC'),'ABC')
        self.assertEqual(self.sol.gcdOfStrings('ABABAB','ABAB'),'AB')
        self.assertEqual(self.sol.gcdOfStrings('LEET','CODE'),'')


if __name__ == '__main__':
    unittest.main()
