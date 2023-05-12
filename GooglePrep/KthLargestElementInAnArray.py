#Quick select
#O(n) time and space
class Solution(object):
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        greatThanPivot = [x for x in nums if x > pivot]
        equaltoPivot = [x for x in nums if x == pivot]
        lessThanPivot = [x for x in nums if x < pivot]
        
        greatLength = len(greatThanPivot)
        equalLength = len(equaltoPivot)

        if k <= greatLength:
            return self.findKthLargest(greatThanPivot, k)
        elif k > greatLength + equalLength:
            return self.findKthLargest(lessThanPivot, k -greatLength -equalLength)
        else:
            return equaltoPivot[0]
