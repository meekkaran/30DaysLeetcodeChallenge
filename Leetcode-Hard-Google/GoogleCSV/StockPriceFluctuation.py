class StockPrice:
#Heap(Priority Queue)
#keep hashmap of timestamps to prices
#when updating timestamp, push it in heap along with timestamp
    def __init__(self):
        #timestamps and price
        self.timestamps = {}
        self.highestTimestamp = 0
        self.minHeap = []
        self.maxHeap = []
        

    def update(self, timestamp: int, price: int) -> None:
        #keep track of curr prices
        self.timestamps[timestamp] = price
        self.highestTimestamp = max(self.highestTimestamp, timestamp)

        #for maximum/minimum
        heappush(self.minHeap, (price,timestamp))
        heappush(self.maxHeap, (-price, timestamp))
        

    def current(self) -> int:
        #latest price at the latest timestamp recorded
        return self.timestamps[self.highestTimestamp]
        

    def maximum(self) -> int:
        #max price
        currPrice, timestamp = heappop(self.maxHeap)
        #if price from heap doesn't match price the timestamp indicates, keep popping from heap
        while -currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.maxHeap)
        
        heappush(self.maxHeap, (currPrice, timestamp))
        return -currPrice
        
    def minimum(self) -> int:
        #min price
        currPrice, timestamp = heappop(self.minHeap)
        #if price from heap doesn't match price the timestamp indicates, keep popping from heap
        while currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.minHeap)
        
        heappush(self.minHeap, (currPrice,timestamp))
        return currPrice

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
