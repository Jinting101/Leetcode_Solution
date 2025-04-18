class Solution:
    def countAndSay(self, n: int) -> str:
        def backtrack(cur):
            if cur == 1:
                return '1'
            x = backtrack(cur - 1)
            num, prev = 0, x[0]
            res = ''
            for y in x:
                if y == prev:
                    num += 1
                else:
                    res = res + str(num) + prev
                    num = 1
                    prev = y
            if num != 0:
                res = res + str(num) + prev
            return res
        return backtrack(n)



            