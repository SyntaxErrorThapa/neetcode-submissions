# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle and End 
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Fast would be at end Slow would be at middle 
        cur = slow.next
        slow.next = pre = None
        
        # Reverse the second half
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        # Use Pre and Head to form the reorder
        first, second = head, pre

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
