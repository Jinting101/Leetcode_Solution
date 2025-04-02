class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], nums[i - 1])
            rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])
        res = 0
        for j in range(1, n - 1):
            res = max(res, (leftMax[j] - nums[j]) * rightMax[j])
        return res



        
        n = len(nums)
        # If we fix k, then the value of the triplet is maximized when nums[i]−nums[j] takes the maximum value. We can use imax to maintain the maximum value of nums[i] and dmax to maintain the maximum value of nums[i]−nums[j]. During the enumeration of k, update dmax and imax.
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res