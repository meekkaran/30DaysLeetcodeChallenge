#O(m*n) time and O(m + n) space
class Solution(object):
    def setZeroes(self, matrix):
        row = set()
        col = set()
        #iterate over original array
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        #iterate once again, this time chacking each cell - using rows and cols sets
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j] = 0
        
