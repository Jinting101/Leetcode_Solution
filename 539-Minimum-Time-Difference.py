class Solution(object):
    def findMinDifference(self, timePoints):
        \\\
        :type timePoints: List[str]
        :rtype: int
        \\\

        # version 1

        # def find_td(t1, t2):
        #     h1, m1, h2, m2 = t1[:2], t1[-2:], t2[:2], t2[-2:]
        #     m1t, m2t = int(h1)*60+int(m1), int(h2)*60+int(m2)
        #     return m2t-m1t

        # std = sorted(timePoints, key=lambda x : x[:2]+x[-2:])
        # pn = std[0]
        # pn = str(int(pn[:2])+24) + pn[2:]
        # std.append(pn)
        # res = find_td('00:00', '24:00')
        # for i in range(len(std)-1):
        #     dif = find_td(std[i], std[i+1])
        #     if dif < res:
        #         res = dif
        # return res

        # version 2

        # Convert times to minutes
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)
        
        # Sort times in ascending order
        minutes.sort()
        
        # Find minimum difference across adjacent elements
        min_diff = float('inf')
        for i in range(len(minutes) - 1):
            min_diff = min(min_diff, minutes[i + 1] - minutes[i])
        
        # Consider the circular difference between last and first element
        min_diff = min(min_diff, 24 * 60 - minutes[-1] + minutes[0])
        
        return min_diff