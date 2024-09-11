class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        res = ""
        shift = 0
        for i in range(len(s)-1, -1, -1):
            shift += shifts[i]
            res += chr((ord(s[i])+shift-ord('a')) % 26 + ord('a'))
        return res[::-1]
        # Just a test to see if leetpush works!