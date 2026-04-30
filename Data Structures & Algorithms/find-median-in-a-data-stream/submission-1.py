class MedianFinder:

    def __init__(self):
        self.leftmax = []
        self.rightmin = []

    def addNum(self, num: int) -> None:
        # always start with pushing to left heap
        heapq.heappush(self.leftmax, -num)
        # to check if all values in left heap are less than right heap
        if self.leftmax and self.rightmin and (-1* self.leftmax[0]) > self.rightmin[0]:
            val = -1 * heapq.heappop(self.leftmax)
            heapq.heappush(self.rightmin, val)

        # balancing heap lens, so diff is never 2
        if len(self.leftmax) > len(self.rightmin) + 1:
            val = -1 * heapq.heappop(self.leftmax)
            heapq.heappush(self.rightmin, val)
        elif len(self.rightmin) > len(self.leftmax) + 1:
            val = heapq.heappop(self.rightmin)
            heapq.heappush(self.leftmax, -val)


    def findMedian(self) -> float:
        # for odd length
        if len(self.leftmax) > len(self.rightmin):
            return -1*self.leftmax[0]
        if len(self.rightmin) > len(self.leftmax):
            return self.rightmin[0]
        # for even length
        return ((-1*self.leftmax[0]) + self.rightmin[0]) / 2
        