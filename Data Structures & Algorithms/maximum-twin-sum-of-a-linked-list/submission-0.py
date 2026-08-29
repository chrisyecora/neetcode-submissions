# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev, slow, fast = None, head, head

        # find middle, reverse first half
        while fast and fast.next:
            fast = fast.next.next
            temp = prev
            prev = slow
            slow = slow.next
            prev.next = temp
        
        # at the middle, traverse together
        maxSum = 0
        while slow:
            maxSum = max(maxSum, prev.val + slow.val)
            slow = slow.next
            prev = prev.next
        
        return maxSum

