# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Removing nth item from end means removing (N - n)th item from the front where N is the total length of linked list
        dummy = cur = ListNode(None)
        dummy.next = head
        length = 0

        while cur:
            length += 1
            cur = cur.next

        # Remove N - n item
        cur = dummy        
        for i in range((length - n) - 1):
            cur = cur.next

        if cur.next and cur.next.next:
            cur.next = cur.next.next 
        
        elif cur.next and not cur.next.next:
            
            cur.next = None
        
        return dummy.next