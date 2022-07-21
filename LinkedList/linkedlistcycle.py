class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None
        # initialise two pointers both at the head of the list
        fast = head
        slow = head
        # the fast pointer moves two nodes ahead of the slow pointer which moves one node ahead
        while fast != None and fast.next != None: 
            fast = fast.next.next
            slow = slow.next
            # if the two pointers meet, then that means there is a cycle 
            if fast == slow:
                return True 
        return False
