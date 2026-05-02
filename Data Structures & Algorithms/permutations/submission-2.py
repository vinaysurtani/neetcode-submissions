class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res
# pick one number, mark it as seen(pick[i] = true), then recursively go through to get all orders till its equal
    def backtrack(self, perm, nums, pick):
        if len(perm) == len(nums):
            self.res.append(perm[:]) # breaking condition when perm length matches
            return
        for i in range(len(nums)):
            if not pick[i]: # basically means if pick[i] is False, ie not visited
                perm.append(nums[i])
                pick[i] = True 
                self.backtrack(perm, nums, pick) # add val, mark that pick[i] as true to not visit again, then recursive run fn
                perm.pop()
                pick[i] = False # once done, then remove val and mark pick[i] as false