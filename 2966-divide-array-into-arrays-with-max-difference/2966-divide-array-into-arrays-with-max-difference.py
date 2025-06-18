class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(0, n, 3):
            a, b, c = nums[i:i+3]
            if c - a <= k:
                res.append([a, b, c])
        return res if len(res) * 3 == n else []