O(mn) time and O(1)space
class Solution(object):
    #since its imultaneous, we can only move 8 diffnt directions
    def gameOfLife(self, board):
        dirs = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                #livecount to maintain count of live cells in the board
                livecount = 0
                for r, c in dirs:
                    nr = i + r #new row after taking directions
                    nc = j + c #new column aftrer taking directions
                    
                    #if new row and newcol are in bound
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                        livecount += 1
                #if cells die from  over/under population        
                if board[i][j] == 1:
                    if livecount < 2 or livecount > 3:
                        board[i][j] = -1
                #cells ressurection
                else:
                    if livecount == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                elif board[i][j] == -1: board[i][j] = 0
        

