class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur = res = 0
        for a in values:
            res = max(res, cur + a)
            cur = max(cur, a) - 1
        return res


        v1 = [i + values[i] for i in range(len(values))]
        v2 = [-j + values[j] for j in range(len(values))]
        res = 0
        temp = v2[-1]
        for i in range(len(values)-2, -1, -1):
            cur = v1[i]
            temp = max(v2[i+1], temp)
            res = max(res, cur + temp)
        return res


