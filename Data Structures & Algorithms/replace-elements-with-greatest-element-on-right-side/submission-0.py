class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        right = len(arr) - 1
        while right >= 0:
            temp = arr[right]
            arr[right] = largest
            largest = max(largest, temp)
            right -= 1
        
        return arr
