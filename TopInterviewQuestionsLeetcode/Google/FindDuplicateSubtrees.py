# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #O(n) time and space
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        #use a hashmap to store nodes, if you find a repeated vsl, update result
        node_freq = {}
        res = []

        #come up with a dfs to serialize subtree and store in node
        def traverse(node):
            if not node:
                return "#"
            
            leftsubtree = traverse(node.left)
            rightsubtree = traverse(node.right)
            subtree = str(node.val) + "," + leftsubtree + "," + rightsubtree

            #update frequency of node
            node_freq[subtree] = node_freq.get(subtree, 0) + 1

            #check if frequency is 2 , then we have a duplicate
            if node_freq[subtree] == 2:
                res.append(node)
            return subtree

        traverse(root)
        return res
 
