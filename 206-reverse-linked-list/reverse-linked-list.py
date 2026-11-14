# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        list=[]
        curr=head
        while curr!=None:
            list.append(curr.val)
            curr=curr.next
        dummy=ListNode()
        curr=dummy
        for i in range(len(list)-1,-1 ,-1):
            curr.next=ListNode(list[i])
            curr=curr.next
        return dummy.next

        