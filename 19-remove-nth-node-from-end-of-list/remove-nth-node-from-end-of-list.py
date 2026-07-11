# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur=head
        for i in range(n):
            if not cur:
                break
            cur=cur.next
        
        dummy=ListNode(-1,head)
        rem=dummy
        while cur:
            rem=rem.next
            cur=cur.next
        
        if rem.next:
            rem.next=rem.next.next
        else:
            rem.next=None
        return dummy.next

        