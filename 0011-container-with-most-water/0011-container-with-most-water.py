class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height)-1
        while l < r:
            x, y = height[l], height[r]
            res = max(res, min(x, y)*(r-l))
            if x < y:
                l += 1
            else:
                r -= 1
        return res
            