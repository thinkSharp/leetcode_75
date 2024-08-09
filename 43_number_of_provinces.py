import unittest
from typing import List
from collections import defaultdict, deque
"""
Problem Understanding:
- find number of provinces
	- provinces are connected cities
	- cities are marked with indexes
	- cities can be connected two ways
		- direct (1 to 2)
		- incorect (1 to 2) , (2, 3) therefore (1, 3)
	- connection i and j is equal to j and i
	- there will be at least one city

Solution approach:
create provences set of list
visited
loop through the grid:
	 check if provense it's belong to by directo or indirect connection
		else create a new provense
		
return length of provense

Time complexity  o(n * n * len(provences))
Space complexity o(n)
"""
class Solution:
    def findCircleNum3(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for neighbor, connected in enumerate(isConnected[node]):
                if connected == 1 and neighbor not in visited:
                    dfs(neighbor)

        visited = set()
        provinces = 0
        for node in range(len(isConnected)):
            if isConnected[node][node] and node not in visited:
                dfs(node)
                provinces += 1
        return provinces
    
    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)
        queue = deque()
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                count += 1
                queue.append(i)
                while queue:
                    node = queue.popleft()
                    for j in range(n):
                        if isConnected[node][j] and not visited[j]:
                            queue.append(j)
                            visited[j] = True
        return count
     
    def union_intersecting_sets(self, sets):
        result = []
        while sets:
            curr = sets.pop(0)
            merged = False
            for i, s in enumerate(result):
                if curr & s:
                    result[i] = result[i] | curr
                    merged = True
                    break
            if not merged:
                result.append(curr)
        return result
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provences = []
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    in_provence = False
                    for k, p in enumerate(provences):
                        if i in p or j in p:
                            in_provence = True
                            p.add(i)
                            p.add(j)
                            
                    if not in_provence:
                        provences.append({i, j})

        return len(self.union_intersecting_sets(provences))
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_given_cases(self):
        self.assertEqual(self.sol.findCircleNum3([[1,1,0],[1,1,0],[0,0,1]]),2)
        #self.assertEqual(self.sol.findCircleNum([[1,0,0], [0,1,0],[0,0,1]]),3)
        #self.assertEqual(self.sol.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]), 1)
    

    def test_failed_cases(self):
        #self.assertEqual(self.sol.findCircleNum([[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]),3)
        pass

if __name__ == '__main__':
    unittest.main()

