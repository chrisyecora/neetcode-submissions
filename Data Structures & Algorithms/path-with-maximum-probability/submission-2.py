class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1], succProb[i]))
            adj[edges[i][1]].append((edges[i][0], succProb[i]))


        print(adj)
        maxHeap = []
        prob = -1
        visited = {}
        heapq.heappush(maxHeap, (prob, start_node))
        
        while maxHeap:
            currProb, index = heapq.heappop(maxHeap)
            print(currProb, index)
            currProb *= -1
            prob = currProb
            if index == end_node:
                return prob

            visited[index] = True

            print(adj[index])
            for node, nextProb in adj[index]:
                if node not in visited:    
                    nextProb *= currProb
                    heapq.heappush(maxHeap, (nextProb * -1, node))

        return 0







        
