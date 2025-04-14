class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k or len(num)-num.count('0') <= k:
            return '0'
        st = [num[0]]
        for x in num[1:]:
            while st and k > 0 and x < st[-1]:
                st.pop()
                k -= 1
            st.append(x)
        if k > 0:
            st = st[:len(st)-k]
        i = 0
        if len(st) > 1:
            while st[i] == '0':
                i += 1
        return ''.join(st)[i:]
        
