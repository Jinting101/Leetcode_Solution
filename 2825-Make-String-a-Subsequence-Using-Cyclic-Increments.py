class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False
        j = 0
        i, l = 0, len(str1)
        while i < l:
            x = str1[i]
            y = str2[j]
            if x == y or chr((ord(x)+1-ord('a'))%26 + ord('a')) == y:
                j += 1
            i += 1
            if j == len(str2):
                return True

        return False



        if len(str2) > len(str1):
            return False
        y = 0
        lst = [0]*28
        for x in str1:
            if x == 'a':
                lst[1] = 1
                lst[-1] = 1
            elif x == 'z':
                lst[-2] = 1
                lst[0] = 1
            else:
                lst[ord(x)-ord('a')+1] = 1
            ind = ord(str2[y])-ord('a')+1
            if (lst[ind-1]==1 or lst[ind]==1):
                y += 1
            if y == len(str2):
                return True

        return False