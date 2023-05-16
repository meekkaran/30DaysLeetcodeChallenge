# O(log(n)) time due to sorting and O(n) space
class Solution(object):
    def merge(self, intervals):
        merged = []
        intervals.sort() 

        temp = intervals[0]
        for interval in intervals:
          if interval[0] <= temp[1]:
            temp[1] = max(temp[1], interval[1])
          else:
            merged.append(temp)
            temp = interval

        merged.append(temp)
        return merged
