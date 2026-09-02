class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quads = []
        for first in range(len(nums) - 3):
            if first > 0 and nums[first-1] == nums[first]:
                continue
            for second in range(first + 1, len(nums) - 2):
                if second > first + 1 and nums[second-1] == nums[second]:
                    continue
                third = second + 1
                fourth = len(nums) - 1
                while third < fourth:
                    currSum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if currSum < target:
                        third += 1
                    elif currSum > target:
                        fourth -= 1
                    else:
                        quads.append([nums[first], nums[second], nums[third], nums[fourth]])
                        third += 1
                        fourth -= 1
                        while third < fourth and nums[third-1] == nums[third]:
                            third += 1
                        while third < fourth and nums[fourth+1] == nums[fourth]:
                            fourth -= 1
        
        return quads
                    