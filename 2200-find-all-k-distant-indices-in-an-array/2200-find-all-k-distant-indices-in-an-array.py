class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        inds = []
        for i,x in enumerate(nums):
            if x == key:
                inds.append(i)
        res = []
        n = len(nums)
        for ind in inds:
            cmin, cmax = max(0, ind-k), min(n-1, ind+k)
            while res and res[-1] >= cmin:
                cmin += 1
            if cmax >= cmin:
                res += [x for x in range(cmin, cmax+1)]
        return res
            