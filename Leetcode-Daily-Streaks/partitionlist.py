# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #O(n) time and O(1) space
        #inputs: head, noe x
        #output: all nodes less than x come before nodes greater than or equal to x
        #any number greater than x should come after, a number less than x should come before
        #do this in place

        #create two dummy lists to store values<x and values >= x
        before = ListNode(0)
        after = ListNode(0)
        #create two pointers for the two dummy lists
        before_curr = before
        after_curr = after

        #if node is less than x, attach it to before node else attach to after node
        while head:
            if head.val < x:
                before_curr.next = head
                before_curr = head
            else:
                after_curr.next = head
                after_curr = head
            head = head.next
        
        #attach  after list to before list to form partitioned list
        after_curr.next = None
        before_curr.next = after.next

        #return before node as new head of partitioned list
        return before.next
