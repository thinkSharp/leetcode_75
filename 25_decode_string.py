
import unittest
"""
Problem Understanding:
1. decode the string from encoded string

Solution approach:
- create a stack 
- unless you see ] breaket, add everything to the stack
- example: 3[a]2[bc] add 3 

stack = []
for item in s:
	if item != ']':
	   stack.append(item)
 else:
	 items = []
	 while stack:
			 p_item = stack.pop()
			 if p_item.isdigit():
				 items * p_item
				 stack.push()
				 break
			 else
				 items.append(p_item)
				
				
		Time Complexity: 
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for item in s:
            if item == ']':
                items = []
                digits = []
                while stack:
                    if items and digits and not stack[-1].isdigit():
                        break
                    elif stack[-1].isdigit():
                        digits.append(stack.pop())
                    elif stack[-1] != '[':
                        items.append(stack.pop())
                    else:
                        stack.pop()

                items.reverse()
                digits.reverse()
                chars = ''.join(items)
                dig = int(''.join(digits))
                decoded_str = chars * dig
                stack.append(decoded_str)


            else:
                stack.append(item)

        return ''.join(stack)
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.decodeString('3[a]2[bc]'), 'aaabcbc')
        self.assertEqual(self.sol.decodeString('3[a10[c]]'), 'accccccccccaccccccccccacccccccccc')
        self.assertEqual(self.sol.decodeString('2[abc]3[cd]ef'),'abcabccdcdcdef')


if __name__ == '__main__':
    unittest.main()
