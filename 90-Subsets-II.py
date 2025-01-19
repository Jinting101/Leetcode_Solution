class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []
        def backtrack(cur, st):
            res.append(tuple(cur))
            for i in range(st, l):
                cur.append(nums[i])
                backtrack(cur, i + 1)
                cur.pop()
        backtrack([], 0)
        return list(set(res))