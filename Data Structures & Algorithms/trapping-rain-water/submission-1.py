class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        #print(maxLeft)
        #print(maxRight)
        #print(height)
        for i in range(len(maxLeft)):
            if i == 0:
                maxLeft[i] = 0
            else:
                maxLeft[i] = max(maxLeft[i-1], height[i-1])
        #print(maxLeft)
        #print(height)
        for i in range(len(maxRight)-1,-1,-1):
            if i == len(maxRight) - 1:
                maxRight[i] = 0
            else:
                maxRight[i] = max(maxRight[i+1], height[i+1])
        #print(maxRight)
        res = 0
        for i in range(len(height)):
            val = min(maxLeft[i],maxRight[i]) - height[i]
            if val < 0:
                val = 0
            res += val
        return res