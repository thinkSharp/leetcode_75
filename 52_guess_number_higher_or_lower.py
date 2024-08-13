import random
"""
Problem Understanding:
- guessing game
	- interact with already defined guess api which return 3 possible indications:
	- depending on the return value, adjust your mid and call guess again
	
	Solution Apporach:
		define left, right, mid
		send mid as guess number, 
		adjust mid accordingly based on return value
"""
# Note this is incorrect implementation of guess
def guess(num: int) -> int:
    return random.randint(1, num)
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right, mid = 0, n, 0

        while left <= right:
            mid = (left + right) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == -1:
                right = mid - 1
            else:
                left = mid + 1
