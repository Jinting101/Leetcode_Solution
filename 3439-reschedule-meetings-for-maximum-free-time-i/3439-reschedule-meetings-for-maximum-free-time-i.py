class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        if startTime[0] != 0:
            gaps.append(startTime[0])
        for i in range(1, n):
            st, ed = startTime[i], endTime[i-1]
            gaps.append(st-ed)
        if endTime[-1] != eventTime:
            gaps.append(eventTime-endTime[-1])
        m = max(1, len(gaps)-k)
        res = []
        for i in range(m):
            res.append(sum(gaps[i:i+k+1]))
        return max(res)


        


