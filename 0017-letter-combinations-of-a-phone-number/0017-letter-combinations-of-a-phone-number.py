class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'],
        6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}

        n = len(digits)
        res = []
        def dfs(startind, cur):
            if len(cur) == n:
                res.append(cur)
                return
            for i in range(startind, n):
                letters = dic[int(digits[i])]
                for letter in letters:
                    dfs(i+1, cur+letter)
        dfs(0, '')
        return res