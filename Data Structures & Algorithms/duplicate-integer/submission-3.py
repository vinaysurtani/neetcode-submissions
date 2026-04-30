class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = defaultdict(int)
        for i in range(len(nums)):
            hm[nums[i]] += 1
            if hm[nums[i]] > 1:
                return True
        return False