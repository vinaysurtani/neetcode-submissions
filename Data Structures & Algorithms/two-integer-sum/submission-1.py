class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # map the value to its index
        for i, n in enumerate(nums): # traverse thru array with num and index val
            diff = target - n # calc difference value
            if diff in prevMap: 
                return [prevMap[diff],i] # if in map already, return index of diff and current value
            prevMap[n] = i #add to hashmap for future use in loop
        return
