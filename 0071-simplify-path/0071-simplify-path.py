class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        res = []
        for x in lst:
            if x == '.' or x == '':
                continue
            elif x == '..':
                if res:
                    res.pop()
            else:
                res.append(x)
        return '/' + '/'.join(res)

