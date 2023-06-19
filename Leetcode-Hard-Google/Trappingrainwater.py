class Solution(object):
    #O(n)time and O(1)space
    def trap(self, height):
        res = 0 #to get total
        #two pointers left and right
        left = 0
        right = len(height) -1
        leftmax = 0 #max from left to right
        rightmax = 0 #max from right to left

        while left < right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])

            if leftmax < rightmax:
                res += leftmax - height[left]
                left  += 1
            else:
                res += rightmax - height[right]
                right -= 1
        return res
            
