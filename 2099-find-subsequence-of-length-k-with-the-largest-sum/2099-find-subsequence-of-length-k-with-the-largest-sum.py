class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sortnums = sorted(zip(nums, range(n)), reverse=True)
        inds = set([x[1] for x in sortnums][:k])
        res = [x for i,x in enumerate(nums) if i in inds]
        return res