#O(log(m*n)) time and O(m * n) space
class Solution(object):
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])

        start = 0
        end = (row*col) -1
        
        #find row idx by divide mid by col and the quotient is its row idx
        while start <= end:
            mid = (start + end) //2
            if matrix[mid//col][mid%col] == target:
                return True
            elif matrix[mid//col][mid%col] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
