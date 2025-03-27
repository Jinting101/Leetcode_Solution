class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dic = {}
        dom, occ, n = -1, 0, len(nums)
        for x in nums:
            dic[x] = dic.get(x, 0) + 1
            if dic[x] > occ:
                dom = x
                occ = dic[x]
        cur = 0
        for i in range(n-1):
            l = (i+1) // 2
            r = (n-1-i) // 2
            if nums[i] == dom:
                cur += 1
            if cur > l and occ-cur > r:
                return i
        return -1
        