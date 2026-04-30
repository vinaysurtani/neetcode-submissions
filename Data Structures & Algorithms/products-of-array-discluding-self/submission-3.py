class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        print(nums)
        res = [1] * len(nums) #list of ones needed here
        print(res)
        for i in range(len(nums)): #prefix calc loop, you assign and then multiply
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #postfix calc loop, you assign an multiply from the start
            res[i] *= postfix
            postfix *= nums[i]
        print(res)
        return res