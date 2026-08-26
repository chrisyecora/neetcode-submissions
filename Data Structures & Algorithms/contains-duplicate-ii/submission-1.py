class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        d = {}
        for right in range(0, len(nums)):
            if nums[right] in d:
                if abs(d[nums[right]] - right) <= k:
                    return True
            while abs(left - right) > k and left < right - 1:
                left += 1
            d[nums[right]] = right

        return False

