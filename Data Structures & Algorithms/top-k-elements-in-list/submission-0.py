class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        #print(count)
        lens = [[] for _ in range(len(nums)+1)]
        #print(lens)
        for key, value in count.items():
            lens[value].append(key)
        #print(lens)
        res = []
        for i in range(len(lens)-1,0,-1):
            for val in lens[i]:
                res.append(val)
                if len(res) == k:
                    return res
        return []