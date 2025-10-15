class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        def check(k):
            prev, cur, k2 = 0, 1, k*2
            for i in range(1, n):
                if nums[i] > nums[i-1]:
                    cur += 1
                else:
                    prev, cur = cur, 1
                if (prev >= k and cur >= k) or cur >= k2:
                    return True
            return False
        l, r = 0, n // 2 + 1
        while l < r:
            mid = (l+r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

