class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # def invert(x):
        #     res = ""
        #     for s in x:
        #         if s == '0':
        #             res += '1'
        #         else:
        #             res += '0'
        #     return res
        
        # def backtrack(n, memo):
        #     if n in memo:
        #         return memo[n]
        #     si1 = backtrack(n-1, memo)
        #     memo[n] = si1 + "1" + invert(si1)[::-1]
        #     return memo[n]
        # memo = {1:"0"}
        # ans = backtrack(n, memo)
        # return ans[k-1]

        bits = '0'
        for _ in range(n - 1):
            newBits = '1'
            size = len(bits)
            for i in range(size - 1, -1, -1):
                newBits += ('0' if bits[i] == '1' else '1')
            bits += newBits

        return bits[k - 1]