#we are peforming four diffnt acrions
#initialise dict with keys and values to store snapid with its specfic idx
#
class SnapshotArray:

    def __init__(self, length: int):
        self.data = {}
        self.snapid = 0
        self.length = length


    # Update the value for the specified index at the current snap_id
    def set(self, index: int, val: int) -> None:
        self.data[(index, self.snapid)] = val
        
    # Find the most recent snap_id that is less than or equal to the provided snap_id
    #return snapshot id that corresponds to the last snap taken
    def snap(self) -> int:
        prevsnapid = self.snapid
        self.snapid += 1
        return prevsnapid
        
    # Find the most recent snap_id that is less than or equal to the provided snap_id
    #if its not found we will return 0
    def get(self, index: int, snapid: int) -> int:
        while snapid >= 0:
            if (index, snapid) in self.data:
                return self.data[(index, snapid)]
            snapid += 1
        return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
