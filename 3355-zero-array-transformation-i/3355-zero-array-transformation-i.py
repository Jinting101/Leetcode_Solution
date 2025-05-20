class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        add = [0]*(n+1)
        for x,y in queries:
            add[x] += 1
            add[y+1] -= 1
        for i in range(1, n+1):
            add[i] += add[i-1]
        for i in range(n):
            if nums[i] > add[i]:
                return False
        return True