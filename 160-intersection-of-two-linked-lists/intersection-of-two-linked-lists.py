# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n=0
        curA=headA
        while curA:
            n+=1
            curA=curA.next
        m=0
        curB=headB
        while curB:
            m+=1
            curB=curB.next
        #print(n,m)
        if m>n:
            headA,headB=headB,headA
            n,m=m,n
        curA=headA
        for _ in range(n-m):
            curA=curA.next
        #print(n,m,curA.val)
        curB=headB
        while curA and curB:
            if curA==curB:
                return curA
            curA=curA.next
            curB=curB.next

        return None
            