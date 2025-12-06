# 332
from collections import defaultdict

class Solution(object):
    def dfs(self, adj, path, u):
        while (adj[u]):
            v = adj[u].pop()
            self.dfs(adj, path, v)
        path.append(u)
            
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = defaultdict(list)

        for u, v in tickets:
            adj[u].append(v)

        for u in adj:
            adj[u].sort(reverse = True)

        path = []
        self.dfs(adj, path, "JFK")
        return path[::-1]