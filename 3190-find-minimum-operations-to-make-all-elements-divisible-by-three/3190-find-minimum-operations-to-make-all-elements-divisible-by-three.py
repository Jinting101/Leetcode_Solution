class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res += min(x%3, 3-x%3)
        return res