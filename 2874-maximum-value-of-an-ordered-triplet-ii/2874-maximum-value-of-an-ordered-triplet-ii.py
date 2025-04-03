class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        leftmax = [0]*n
        rightmax = [0]*n
        for i in range(1, n):
            leftmax[i] = max(leftmax[i-1], nums[i-1])
        for i in range(n-2, 0, -1):
            rightmax[i] = max(rightmax[i+1], nums[i+1])
        
        res = 0
        for i in range(1, n-1):
            x = nums[i]
            res = max(res, (leftmax[i] - x) * rightmax[i])

        return res