class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequencies = [[] for i in range(len(nums) + 1)]
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        for num, c in counts.items():
            frequencies[c].append(num)
        
        ans = []
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

