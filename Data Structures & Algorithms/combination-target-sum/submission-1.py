class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(index, arr, total):
            # done - succeeded
            if total == target:
                ans.append(arr.copy())
                return
            
            # done - failed
            if index >= len(nums) or total > target:
                return
            
            # continue
            arr.append(nums[index])
            dfs(index, arr, total + nums[index])
            arr.pop()
            dfs(index + 1, arr, total)
        
        dfs(0, [], 0)
        return ans
            
