# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow/fast, find middle, then reverse 2nd half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            temp = prev
            prev = slow
            slow = slow.next
            prev.next = temp
        

        L = head
        R = prev
        while L and R:
            tempL = L.next
            L.next = R
            tempR = R.next
            R.next = tempL
            L = R.next
            R = tempR