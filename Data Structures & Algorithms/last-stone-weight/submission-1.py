class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        #print(heap)
        while len(heap) > 1:
            x = (-1) * heapq.heappop(heap)
            #print(x)
            y = (-1) * heapq.heappop(heap)
            #print(y)
            if y < x:
                diff = (x - y)
                #print(diff)
                heapq.heappush(heap,-diff)
            #print(heap)
        if len(heap) == 0:
            return 0
        return heap[0]*(-1)