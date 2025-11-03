class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        n = len(colors)
        cur, curmax = 0, 0
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                if not cur:
                    cur += neededTime[i-1]
                    curmax = neededTime[i-1]
                cur += neededTime[i]
                curmax = max(curmax, neededTime[i])
            else:
                res += cur - curmax
                cur = curmax = 0
        if cur:
            res += cur - curmax
        return res