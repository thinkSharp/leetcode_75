import unittest
from collections import defaultdict
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = defaultdict(bool)
        vowels['a'] = True
        vowels['e'] = True
        vowels['i'] = True
        vowels['o'] = True
        vowels['u'] = True
        output = [i for i in s]
        first, last = 0, (len(s) - 1)
        while first < last:
            first_v = vowels[output[first]]
            last_v = vowels[output[last]]
            if first_v and last_v:
                output[first], output[last] = output[last], output[first]
                first += 1
                last -= 1
            elif first_v and not last_v:
                last -= 1
            elif not first_v and last_v:
                first += 1
            else:
                first += 1
                last -= 1

        return ''.join(output)
    
class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.reverseVowels('hello'), 'holle')
        self.assertEqual(self.sol.reverseVowels('leetcode'),'leotcede')

if __name__ == '__main__':
    unittest.main()


    
