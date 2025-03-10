class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        res, l = 0, len(word)
        cur, left = [0] * 6, 0
        ind = {x:i for i,x in enumerate(['a', 'e', 'i', 'o', 'u'])}
        vowels = set(ind.keys())
        def check(cur, k):
            for i,x in enumerate(cur):
                if not((i != 5 and x >= 1) or (i == 5 and x == k)):
                    return False
            return True
        for i, x in enumerate(word):
            if x in vowels:
                cur[ind[x]] += 1
            else:
                cur[5] += 1
            
            if cur[5] > k:
                temp = ind[word[left]] if word[left] in ind else 5
                cur[temp] -= 1
                if not check(cur, k):
                    cur = [0] * 6
                    cur[5] += 1
                    left = i
                else:
                    left += 1
            
            if check(cur, k):
                res += 1

        return res
            

            