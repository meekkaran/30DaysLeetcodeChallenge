"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#O(n) time and space
class Solution(object):
    def copyRandomList(self, head):
        if not head: return None
        # Create a dictionary to store the mapping between original nodes and copy nodes
        map = {}
        # Iterate through the original linked list to create copy nodes and store the mapping
        curr = head
        while curr:
            # Make a new copy node
            copy = Node(curr.val)
            # Add the copy node in map
            map[curr] = copy
            # Move the curr
            curr = curr.next
        # Set the next and random pointers of the copy nodes based on the mapping
        curr = head
        # Traverse through the LinkedList
        while curr:
            copy = map[curr]
            copy.next = map.get(curr.next)
            copy.random = map.get(curr.random)
            # Move the curr
            curr = curr.next
        # Return the head of the copy linked list
        return map[head]







