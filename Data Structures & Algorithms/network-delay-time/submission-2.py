class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # init adj list
        adj = defaultdict(list)
        for connection in times:
            adj[connection[0]].append((connection[1], connection[2]))
        

        # init minHeap
        minHeap = []

        # init shortest dict
        shortest = {}
        
        
        # dijkstra's algo
        heapq.heappush(minHeap, (0, k))
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue
            
            shortest[n1] = w1

            for neighbor in adj[n1]:
                n2, w2 = neighbor
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # take the max of the result to get min time to reach all
        if len(shortest) != n:
            return -1
        return max(shortest.values())
