class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            requested = target - num
            if requested in seen:
                return [seen[requested], i]
            seen[num] = i