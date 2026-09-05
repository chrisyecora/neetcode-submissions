class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustees = [0] * n
        adj = defaultdict(list)
        for i in range(len(trust)):
            ai, bi = trust[i][0], trust[i][1]
            trustees[ai-1] += 1
            adj[bi].append(ai)

        
        judge = None
        for i in range(len(trustees)):
            if trustees[i] == 0:
                if judge: 
                    return -1
                judge = i + 1 # trustees 0-indexed

        if len(adj[judge]) == n - 1:
            return judge

        return -1        
        

