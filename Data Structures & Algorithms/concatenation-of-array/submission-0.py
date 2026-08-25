class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)
        offset = len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[offset + i] = nums[i]

        return ans

        