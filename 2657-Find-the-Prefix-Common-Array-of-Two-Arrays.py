class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        cnt = [0] * n
        for i in range(0, n-1):
            cur = res[max(0,i-1)]
            x, y = A[i], B[i]
            cnt[x-1] += 1
            cnt[y-1] += 1
            if cnt[x-1] == 2:
                cur += 1
            if x != y and cnt[y-1] == 2:
                cur += 1
            res[i] = cur
        res[-1] = n
        return res