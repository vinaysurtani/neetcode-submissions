class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        #print(heap)
        #while k > 0:
        #    val = heapq.heappop(heap)
        #    k -= 1
        return heap[0]