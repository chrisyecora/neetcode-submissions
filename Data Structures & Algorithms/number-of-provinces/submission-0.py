class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]        

        def find(n):
            p = parent[n]
            while p != parent[p]:
                p = parent[p]
            return p

        def union(c1, c2):
            p1 = find(c1)
            p2 = find(c2)
            if p1 == p2:
                return 0

            parent[p1] = p2
            return 1


        provinces = len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    provinces -= union(i, j)
        
        return provinces
        