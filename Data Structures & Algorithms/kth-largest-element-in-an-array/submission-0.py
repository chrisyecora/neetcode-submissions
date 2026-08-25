from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # flip for maxHeap
        for i in range(len(nums)):
            nums[i] *= -1
        
        heapify(nums)
        ans = 0
        for i in range(k):
            ans = heappop(nums) * -1
        
        return ans