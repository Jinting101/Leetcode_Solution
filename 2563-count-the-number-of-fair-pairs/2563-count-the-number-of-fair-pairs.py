class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort(reverse=True)
        n = len(nums)

        def get_one(limit):
            l, r, res = 0, n-1, 0
            while l < r:
                if nums[l] + nums[r] > limit:
                    l += 1
                else:
                    res += r-l
                    r -= 1
            return res

        return get_one(upper) - get_one(lower-1)