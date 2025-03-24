class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        lst = [0]*(days+1)
        for x,y in meetings:
            lst[x-1] += 1
            lst[y] -= 1
        for i in range(1, days):
            lst[i] += lst[i-1]
        res = 0
        for x in lst[:-1]:
            if x == 0:
                res += 1
        return res


        # [1 0 0 -1 1 0 0 -1 1 0 -1]
        # [1 1 1 0  1 1 1 0  1 1 0]