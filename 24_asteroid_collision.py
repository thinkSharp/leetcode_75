import unittest
from typing import List
"""
Problem Understanding:
list has positive and negative numbers: they will colide based on the direction. bigger number wins

Solution Approach:
create a stack
add all the positive no. 
once a negative no. found,
	pop positive from the stack in while loop
			until negative lost or till stack is empty
			
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for item in asteroids:

            exploded = False
            while stack:
                if (stack[-1] < 0) == (item < 0) :
                    stack.append(item) # same sign
                    break
                else:
                    if abs(stack[-1]) > abs(item):
                        exploded = True
                        break
                    elif abs(stack[-1]) == abs(item):
                        exploded = True
                        stack.pop()
                    else:
                        stack.pop()

            if not stack  and not exploded:
                stack.append(item)
                            
        return stack
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.asteroidCollision([-2,-1,1,2]),[])
        self.assertEqual(self.sol.asteroidCollision([8, -8]), [])
        self.assertEqual(self.sol.asteroidCollision([-8, 8]), [])
        self.assertEqual(self.sol.asteroidCollision([5, 10, -5]), [5, 10])
        self.assertEqual(self.sol.asteroidCollision([10, 2, -5]), [10])
        self.assertEqual(self.sol.asteroidCollision([5, -10, -5]), [-10, -5])


if __name__ == '__main__':
    unittest.main()

