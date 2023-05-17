# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            Next = curr.next #another pointer
            curr.next = prev
            prev = curr
            curr = Next
        return prev
            
