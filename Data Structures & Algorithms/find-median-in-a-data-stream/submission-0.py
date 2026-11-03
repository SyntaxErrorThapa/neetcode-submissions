class MedianFinder:

    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) # Max heap

        # make sure every element num small is <= every num in large 
        if self.small and self.large and self.small[0] * -1 > self.large[0]: # Need to add inside large heap
            temp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, temp)

        # Check the difference in length between large and small 
        if len(self.large) > len(self.small) + 1: # Meaning greater than 2
            temp = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * temp)
        
        if len(self.small) > len(self.large) + 1:
            temp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, temp)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] + (-1 * self.small[0])) / 2
        