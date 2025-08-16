class Solution:
    def maximum69Number (self, num: int) -> int:
        return (int(str(num).replace('6', '9', 1)))
        
        res = ''
        unchanged = True
        num = str(num)
        for x in num:
            if x == '9':
                res += '9'
            elif unchanged:
                res += '9'
                unchanged = False
            else:
                res += '6'
        return int(res)
