class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """

        offsets = [0]*(len(s)+1)

        for start, end, direction in shifts:
            d = 1 if direction == 1 else -1 
            offsets[start] += d
            offsets[end+1] -= d

        for i in range(1,len(offsets)):
            offsets[i] += offsets[i-1]

        r = ""
        for i, offset in enumerate(offsets[:-1]):
            r += chr(((ord(s[i])-97+offset)%26)+97)
        return r

# In this problem, we should be doing the exact same thing as in the first part of this problem (shifting letters) but there is an extra complexity of finding the final changes for each of the letters.

# A brute force approach would be to iterate through all of the letters that need to be changed for each shift in array shifts (e.g., from 0 to 2 in forward direction). However, this adds extra complexity if we have large ranges of letters that need to be changed. This is why we should be using a cumulative sum approach here.

# For example, instead of iterating through the range, we can add a +1 if we are moving forward in the beginning of the range and -1 in the end of the range to make sure we are no longer applying the change. The same thing goes for the backward direction with the -1 at the beginning and +1 at the end.
            
