class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (count*-1, num))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans