class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = 2*len(nums)
        ans = [0 for i in range(N)]
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans [i + len(nums)] = nums[i]
        return ans