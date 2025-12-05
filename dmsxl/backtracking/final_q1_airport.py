# 332
from collections import defaultdict

class Solution(object):
    def dfs(self, order, adj, path, n):
        if len(path) == n + 1:
            return True
        
        current = path[-1]

        # If current has no outgoing edges, we cannot extend the path.
        if current not in order:
            return False
        
        for end in order[path[-1]]:
            if adj[path[-1]][end] > 0:
                adj[path[-1]][end] -= 1
                path.append(end)
                if self.dfs(order, adj, path, n):
                    return True
                path.pop()
                adj[path[-1]][end] += 1

        return False
        
            
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = {}

        for start, end in tickets:
            if start not in adj:
                adj[start] = defaultdict(int)
            adj[start][end] += 1

        # for start in sorted(adj.keys()):
        #     for end in sorted(adj[start].keys()):
        #         print(start, "->", end, adj[start][end])

        order = {}
        for start in adj:
            # Only sort once here
            order[start] = sorted(adj[start].keys())

        n = len(tickets)
        path = ["JFK"]
        self.dfs(order, adj, path, n)
        return path