# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        cur = head
        while(cur!=None):
            if(cur.next!=None and cur.next.val==cur.val):
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head