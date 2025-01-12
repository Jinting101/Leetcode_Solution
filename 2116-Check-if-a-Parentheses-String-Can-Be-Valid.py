class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        open_count = 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return False

        close_count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False

        return True


        
        def check(s):
            st = []
            for x in s:
                if x == ')' and st and st[-1] =='(':
                    st.pop()
                else:
                    st.append(x)
            return len(st) == 0
        if check(s):
            return True
        if len(s) % 2 == 1:
            return False
        l = len(s)
        perm = [0] * l
        op, cp, indcp = 0, 0, []
        for i,x in enumerate(locked):
            if x == '1':
                if s[i] == '(':
                    perm[i] = 1
                    op += 1
                else:
                    perm[i] = -1
                    cp += 1
                    indcp.append(i)
        if op > l / 2 or cp > l / 2:
            return False
        if (perm[0] == -1 and s[0] == ')') or (perm[-1] == 1 and s[-1] == '('):
            return False
        res = True
        cur = 1
        for x in indcp:
            if x < cur:
                res = False
                break
            cur += 2
        return res