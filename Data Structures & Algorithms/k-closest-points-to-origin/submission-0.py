from heapq import heapify, heappush, heappop
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapify(minHeap)
        for point in points:
            item = self._calcDistance(point)
            heappush(minHeap, item)
        

        

        ans = []
        for i in range(k):
            item = heappop(minHeap)
            ans.append(item[1])

        return ans



    def _calcDistance(self, coord: [int, int]) -> (float, [int, int]):
        # (distance, [xi, yi])
        distance = sqrt(coord[0]**2 + coord[1]**2)

        return (distance, coord)
