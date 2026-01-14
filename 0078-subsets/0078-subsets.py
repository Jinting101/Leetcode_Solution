class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(ind, cur):
            if cur not in res:
                res.append(cur)
            if ind == n:
                return
            backtrack(ind+1, cur + [nums[ind]])
            backtrack(ind+1, cur)
        backtrack(0, [])
        return res