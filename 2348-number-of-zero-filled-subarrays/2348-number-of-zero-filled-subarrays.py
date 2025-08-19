class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cur, res = 0, 0
        for x in nums:
            if x == 0:
                cur += 1
                res += cur
            else:
                cur = 0
        return res