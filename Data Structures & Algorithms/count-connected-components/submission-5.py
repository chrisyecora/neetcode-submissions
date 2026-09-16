from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list, {k: [] for k in range(n)})
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        

        visit = set()
        q = deque()
        ans = 0
        for k, v in adj.items():
            discovered = False
            if k not in visit:
                q.append(k)
                discovered = True
            while q:
                node = q.popleft()
                visit.add(node)

                for neigh in adj[node]:
                    if neigh not in visit:
                        q.append(neigh)
            if discovered:
                ans += 1 if discovered else 0
            

        return ans