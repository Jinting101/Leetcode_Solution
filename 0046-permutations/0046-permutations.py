class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        seen = set()

        def dfs(l, cur):
            if l == n:
                res.append(cur)
                return
            for i in range(n):
                if i in seen:
                    continue
                seen.add(i)
                dfs(l+1, cur + [nums[i]])
                seen.remove(i)
        
        dfs(0, [])
        return res