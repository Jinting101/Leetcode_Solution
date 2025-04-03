class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, imax, jmin, update = 0, 0, float('inf'), False
        for k in range(n):
            res = max(res, (imax-jmin) * nums[k])
            if imax < nums[k]:
                update = True
            else:
                update = False
            imax = max(imax, nums[k])
            jmin = min(jmin, nums[k])
            if update:
                jmin = float('inf')
        return res


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

        