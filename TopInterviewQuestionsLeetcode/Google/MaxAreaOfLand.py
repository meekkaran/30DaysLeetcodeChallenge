class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set() #a set to store visited node 

        rows = len(grid)
        cols = len(grid[0])

        def traverse(r,c):
            if r < 0 or r==rows or c < 0 or c==cols or grid[r][c]== 0 or(r,c) in visited:
                return 0
            visited.add((r,c))
            return 1 + traverse(r-1,c) + traverse(r+1,c) + traverse(r,c-1) + traverse(r,c+1)
        
        area = 0
        for i in range(rows):
            for j in range(cols):
                area = max(area, traverse(i,j))
        return area
