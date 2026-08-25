from heapq import heappush, heappop, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapify(stones)

        while len(stones) > 1:
            stone1 = heappop(stones) * -1
            stone2 = heappop(stones) * -1
            if stone1 > stone2:
                new = stone1 - stone2
                heappush(stones, new * -1)
            elif stone2 > stone1:
                new = stone2 - stone1
                heappush(stones, new * -1)

        if stones:
            return heappop(stones) * -1
        else:
            return 0
