class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res += 1 if len(str(x)) % 2 == 0 else 0
        return res