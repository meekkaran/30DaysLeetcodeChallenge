# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        #O(n) time and space
        #Encodes a tree to a single string.
        return str(root.val) + ',' + self.serialize(root.left)+',' + self.serialize(root.right) if root else "None"

        

    def deserialize(self, data):
        #O(n)time and space
        #Decodes your encoded data to tree.
        def fn(arr):
            node = arr.popleft() if arr else None
            return TreeNode(int(node), fn(arr), fn(arr)) if node != 'None' else None
        return fn(collections.deque(data.split(',')))

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
