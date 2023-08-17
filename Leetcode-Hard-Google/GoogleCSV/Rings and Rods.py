#O(n) time and space complexity
class Solution:
    def countPoints(self, rings: str) -> int:
        #inputs: rods [0-9] and colors{R,G,B}
        #return no. of rods with all colors in it

        rods = defaultdict(set)
        for i in range(0,len(rings) -1, 2):
            color = rings[i]
            rod = rings[i+1]

            rods[rod].add(color) #update rod with the color
        
        count = 0
        for rod in rods.values():
            if len(rod) == 3:
                count += 1
        return count
