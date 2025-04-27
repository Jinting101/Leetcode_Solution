class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        prev, cur, curnext = nums[:3]
        res = 1 if 2*(prev+curnext) == cur else 0
        for x in nums[3:]:
            temp = curnext
            curnext = x
            prev = cur
            cur = temp
            res += 1 if 2*(prev+curnext) == cur else 0
        return res