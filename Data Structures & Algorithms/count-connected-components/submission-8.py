from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        visit = set()
        q = deque()
        ans = 0
        for node in range(n):
            if node not in visit:
                ans += 1
                q.append(node)
                visit.add(node)

            while q:
                curr = q.popleft()

                for neigh in adj[curr]:
                    if neigh not in visit:
                        q.append(neigh)
                        visit.add(neigh)
            

        return ans