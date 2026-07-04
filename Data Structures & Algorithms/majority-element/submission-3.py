class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        max_val = 0
        for i, num in enumerate(nums):
            print(i, num)
            if i == 0:
                res = 1
                max_val = num
            else:
                res += (1 if num == max_val else -1)
                print(f'res is now {res}')
                if res <= 0:
                    max_val = num
                    print(f'max_val changed to {max_val}')
        return max_val