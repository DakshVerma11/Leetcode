# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:   
    def merge(self,list1,list2):
        head=ListNode()
        cur=head

        while list1 and list2:
            if list1.val<=list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        if list1:
            cur.next=list1
        if list2:
            cur.next=list2
        return head.next
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        


        for i in range(1,len(lists)):
            lists[i]=self.merge(lists[i-1],lists[i])
        return lists[-1]
    
        