class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float('inf')
        for i,x in enumerate(nums):
            if x == target:
                res = min(res, abs(i-start))
        return res