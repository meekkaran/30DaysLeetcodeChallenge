
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path, target):
            path.append(node)
            if node == target:
                res_path.append(path[:])
            else:
                for neighbour in graph[node]:
                    dfs(neighbour, path , target)
            path.pop()
    
        res_path = []
        source = 0
        target = len(graph) - 1
        dfs(source,[], target)
        return res_path
