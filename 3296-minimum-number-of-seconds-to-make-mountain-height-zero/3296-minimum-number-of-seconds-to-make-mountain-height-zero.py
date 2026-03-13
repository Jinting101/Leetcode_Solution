class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        def isOK(k):
            res = 0
            for time in workerTimes:
                res += int((-1+(1 + 4 * k*2/time)**0.5) / 2)
            return res >= mountainHeight


        l = min(workerTimes)
        r = l * (mountainHeight+1) * mountainHeight // 2

        while l < r:
            mid = (l+r) // 2
            if isOK(mid):
                r = mid
            else:
                l = mid + 1
        
        return l



        # for worker i to reduce the height by h, should take times[i] * (h+1) * h // 2



        # maximize h subject to: (h+1)*h <= k*2/time
        # h**2 + h - k*2/time <= 0

        # time=1, k=3

        # int((1+(1 + 4 * k*2/time)**0.5) / 2)
