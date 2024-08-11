import unittest
from typing import List
from collections import defaultdict, deque
"""
Problem Understanding:
equaltion are given as list of list along with answers in list
solve list of query based on provided equation and answers:
if unknown value found return -1

example: ['a', 'b'] = 2.0
a/b = 2.0
a = 2.0b
b = a/ 2.0

b/c = 3.0
b = 3.0c
c = b/3.0

a/c = 2.0b / b/3.0
			= 20 * b * 3.0 / b
			= 6.0
			
Solution Approach:

based on the equation and values, calculate the individual value

same them in dictionary

for query get it from dictionary and calculate it
"""
class Solution:
    def dfs(self, start, end, graph, visited):
        if start not in graph or end not in graph:
            return -1
        if start == end:
            return 1
        visited.add(start)

        for neighbor, value in graph[start].items():
            if neighbor in visited:
                continue
            result = self.dfs(neighbor, end, graph, visited)
            if result != -1:
                return result * value
        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value
        
        result = []
        for c, d in queries:
            if c in graph and d in graph:
                result.append(self.dfs(c, d, graph, set()))
            else:
                result.append(-1.0)

        return result

    
class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.calcEquation([['a','b']], [0.5], [['b', 'a']]), [2.0])

if __name__ == '__main__':
    unittest.main()