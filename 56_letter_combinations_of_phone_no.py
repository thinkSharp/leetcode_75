import unittest
from typing import List
"""
problem understanding:
- finding all possible letter combinations:
- digits will be 0 to 4
- 256
- abc, jkl, mno
 queue:
	=> a, b, c

Loop approach from 1 to last:
	get size of the queu:
		pop a, append aj, ak, al
		pop b append bj, bk, bl
		pop c append cj, ck, cl
		pop aj append ajm, ajn ajo
		...
		
at the end: return list of queue

Time complexity: will start with no. of first digit, and each time we would expend for n digit so o(k^n)
space complexity: same becaues we store all combination O(k^n)
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        dict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'] 
        }

        combination = list(dict[digits[0]])
        for i in range(1, len(digits)):
            new_c = []
            for item in combination:
                for d in dict[digits[i]]:
                    new_c.append(item + d)
            combination = new_c
        return combination