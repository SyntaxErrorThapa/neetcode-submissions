# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = dummy = ListNode(None)
        dummy.next = head
        right = head

        # First move right pointer n steps, encodes that distance as physical
        # gap between two pointers instead of needing to know the total lenght upfront

        for i in range(n):
            right = right.next
        
        # With the gap, we move right along with left till the end of linked list for right pointer.
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next