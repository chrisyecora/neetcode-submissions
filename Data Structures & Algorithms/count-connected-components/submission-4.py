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
                print(f"adding k {k} to the q")
                discovered = True
            while q:
                node = q.popleft()
                print(f"node is visited and now {node}")
                visit.add(node)

                for neigh in adj[node]:
                    if neigh not in visit:
                        q.append(neigh)
                        print(f"appended neigh {neigh} to q")
            if discovered:
                ans += 1 if discovered else 0
                print("adding 1 to ans")
            

        return ans