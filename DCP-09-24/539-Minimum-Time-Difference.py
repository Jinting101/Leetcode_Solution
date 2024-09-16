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

        # If there is any two of the same return 0
        if len(timePoints) != len(set(timePoints)):
            return 0
        
        # First instince is to order them 
        sorted_time = sorted(timePoints)
        # add first time to the end for measurement
        sorted_time.append(sorted_time[0])

        def subtract_time(time_1, time_2):
            \\\
            time_1: (str) lesser time e.g. 00:13
            time_2: (str) greater time eg. 01:02
            \\\
            time_2_hour = int(time_2.split(':')[0])
            time_1_hour = int(time_1.split(':')[0])

            time_2_min = int(time_2.split(':')[-1])
            time_1_min = int(time_1.split(':')[-1])
            # different hours
            # if 13:10 - 09:50 can be read as 12:70 - 09:50
            if time_2_min < time_1_min:
                time_2_hour = time_2_hour - 1
                time_2_min = time_2_min + 60
            
            # if time 2 is across the 24 hour mark, convert it to 24
            # this should only happen at the end of the cycle.
            if time_2_hour < time_1_hour:
                time_2_hour = time_2_hour + 24
                
            # caluclate hour and minute difference
            hour_diff = time_2_hour - time_1_hour
            min_diff = time_2_min - time_1_min
            
            # Add total minutes
            total_diff = hour_diff*60 + min_diff

            return total_diff
        
        min_diff_seen = 60*24
        for i, time in enumerate(sorted_time[:-1]):
            difference = subtract_time(time, sorted_time[i + 1])
            if difference < min_diff_seen:
                min_diff_seen = difference
        
        return min_diff_seen