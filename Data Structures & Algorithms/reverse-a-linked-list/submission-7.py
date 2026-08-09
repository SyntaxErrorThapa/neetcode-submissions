# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        post = None
        
        while cur:
            tmp = cur.next
            cur.next = post
            post = cur
            cur = tmp
            
        return post
