class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap,(-dist, point))
        #print(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        #print(heap)
        res = []
        for val in heap:
            res.append(val[1])
        #print(res)
        return res