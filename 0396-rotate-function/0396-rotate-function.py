class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        combined = sum([i*x for i,x in enumerate(nums)])
        total = sum(nums)
        res = combined
        n = len(nums)
        ls, rs = 0, total - nums[0]
        lc, rc = 0, combined
        for i in range(1, n):
            prev, cur = nums[i-1], nums[i]
            lc = lc - ls + prev * (n-1)
            rc -= rs
            res = max(res, lc + rc)
            rs -= cur
            ls += prev
        return res


        # 4 3 2 6 1 8 7 9 4 6