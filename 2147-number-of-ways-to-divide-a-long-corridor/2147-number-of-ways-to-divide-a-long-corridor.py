class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seat_ind = [i for i,x in enumerate(corridor) if x == "S"]
        n = len(seat_ind)
        res = 1
        if n % 2 == 1 or n == 0:
            return 0
        for i in range(1, n-1, 2):
            res *= (seat_ind[i+1] - seat_ind[i]) % MOD
        return res % MOD