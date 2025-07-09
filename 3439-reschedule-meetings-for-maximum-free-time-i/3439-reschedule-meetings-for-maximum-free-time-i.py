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
        window_size = k + 1
        window_sum = sum(gaps[:window_size])
        max_sum = window_sum

        for i in range(1, m):
            window_sum += gaps[i + window_size - 1] - gaps[i - 1]
            max_sum = max(max_sum, window_sum)

        return max_sum


        


