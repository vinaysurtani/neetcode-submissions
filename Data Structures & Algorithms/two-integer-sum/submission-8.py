class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # value, index
        for i, n in enumerate(nums):
            diff = target - n #to see if we already have the value in the set later
            if diff in seen: 
                return [seen[diff], i] 
                # if we already added it earlier, it should be in seen. so we return the index of i and value of seen[diff],
                # which is the index of diff
            seen[n] = i # if value not there, we add NUM and index to seen, NOT diff and index
        return []