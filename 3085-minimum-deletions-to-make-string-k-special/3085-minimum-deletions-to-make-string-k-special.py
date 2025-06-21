class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        lst = [0]*26
        for x in word:
            lst[ord(x)-ord('a')] += 1
        lst = [x for x in lst if x != 0]
        lst.sort()
        res = float('inf')
        n = len(lst)
        for i in range(n):
            cur = 0
            for j in range(n):
                if j != i:
                    if lst[j] < lst[i]:
                        cur += lst[j]
                    elif lst[j] > lst[i] + k:
                        cur += lst[j] - lst[i] - k
            res = min(res, cur)
        return res