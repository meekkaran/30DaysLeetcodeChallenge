"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#O(V+E) time for BFS and O(v) space for hashmap
class Solution(object):
    def cloneGraph(self, node):
        #base case
        if not node: return node
        #two things, run a bfs to traverse graph and have a hashmap to keep track of already visited and already cloned values

        q = deque([node]) #
        clones = {node.val: Node(node.val, [])} #to keep track of cloned nodes
 
        while q:
            cur = q.popleft() #push node to queue to make sure its cloned
            cur_clone = clones[cur.val]

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val,[])
                    q.append(ngbr)
                cur_clone.neighbors.append(clones[ngbr.val])

        return clones[node.val]


            
        
