class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)

        pre = [0] * N
        post = [0] * N
        r = N - 1
        for i in range(N):
            pre[i] = nums[i] + pre[i-1] if i >= 0 else nums[i]
            post[r] = nums[r] + post[r+1] if r < N-1 else nums[r]
            r -= 1

        for i in range(N):
            preFix = pre[i]
            postFix = post[i]
            if preFix == postFix:
                return i
        return -1