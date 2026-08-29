class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0

        triplets = defaultdict(set)
        for i in range(len(nums)):
            left, right = i+1, len(nums) - 1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum > 0:
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    triplets[0].add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        

        return list(triplets[0])


                
