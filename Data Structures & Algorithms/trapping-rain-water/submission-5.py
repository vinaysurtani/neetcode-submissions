class Solution:
    def trap(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        leftmax = h[l]
        rightmax = h[r]
        res = 0
        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, h[l])
                res += leftmax - h[l]
            else:
                r -= 1
                rightmax = max(rightmax, h[r])
                res += rightmax - h[r]
        return res