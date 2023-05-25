"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    #dfs approach
    #O(n) time and O(log(N)) space
    def connect(self, root):
        if not root: return None
        L = root.left
        R = root.right
        N = root.next

        if L:
            L.next = R
            if N:
                R.next = N.left
            self.connect(L)
            self.connect(R)
        return root
