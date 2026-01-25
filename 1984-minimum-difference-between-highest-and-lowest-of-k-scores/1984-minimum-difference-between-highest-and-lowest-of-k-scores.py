class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')
        n = len(nums)
        if n == k:
            return nums[-1] - nums[0]
        for i in range(n-k+1):
            a, b = nums[i], nums[i+k-1]
            res = min(res, b-a)
        return res


        # 1 1 2 3 4 5 6 7 7 9 n=10 k=7