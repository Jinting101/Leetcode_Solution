class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        travelDays = set(days)
        
        for day in range(1, 366):
            if day not in travelDays:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(dp[day - 1] + costs[0],
                              dp[max(0, day - 7)] + costs[1],
                              dp[max(0, day - 30)] + costs[2])
        
        return dp[365]

        
        dp = [0]*396
        for x in days:
            dp[x] = 1
        i = 1
        while i <= 395:
            a = dp[i-1]
            b = float('inf') if i-7 < 0 else dp[i-7] + costs[1]
            c = float('inf') if i-30 < 0 else dp[i-30] + costs[2]
            if dp[i] != 0:
                a = dp[i-1] + costs[0]
            dp[i] = min(a, b, c)
            i += 1
        return dp[-1]

