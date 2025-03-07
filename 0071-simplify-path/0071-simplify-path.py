class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        # print(lst)
        i, n = 0, len(lst)
        res = []
        while i < n:
            x = lst[i]
            if x == '.' or x == '':
                i += 1
                continue
            elif x == '..':
                if res:
                    res.pop()
            else:
                res.append(x)
            i += 1
        ans = '/'
        if res:
            ans += '/'.join(res)
        return ans

