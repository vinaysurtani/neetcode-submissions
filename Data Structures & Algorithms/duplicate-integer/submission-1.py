class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        spot = set()
        for num in nums:
            if num in spot:
                return True
            spot.add(num)
        return False            