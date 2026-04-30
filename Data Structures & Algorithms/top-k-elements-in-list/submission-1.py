class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        print(count)
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num],num))
            print(f'pushed ({count[num]},{num}) to {heap}')
            if len(heap) > k:
                a = heapq.heappop(heap)
                print(f'popped {a}')
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res