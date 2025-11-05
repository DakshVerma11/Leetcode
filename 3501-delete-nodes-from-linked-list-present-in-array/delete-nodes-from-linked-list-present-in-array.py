# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num=set(nums)

        while head and head.val in num:
            head=head.next

        cur=head
        if not cur:
            return head
        while cur and cur.next:
            while cur.next and cur.next.val in num:
                cur.next=cur.next.next
            cur=cur.next
        return head