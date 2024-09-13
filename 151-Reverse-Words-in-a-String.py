class Solution(object):
    def reverseWords(self, s):
        \\\
        :type s: str
        :rtype: str
        \\\

        # return ' '.join(s.split()[::-1])


        length = len(s)
        word_positions = []  # To store start and end indices of words
        result = []

        i = 0
        # Iterate through the string to identify word boundaries
        while i < length:
            # Skip leading spaces
            while i < length and s[i] == ' ':
                i += 1
            if i == length:
                break
            
            start = i  # Start of the word
            
            # Move to the end of the word
            while i < length and s[i] != ' ':
                i += 1
            end = i - 1  # End of the word
            
            # Store the start and end indices of the word
            word_positions.append((start, end))
            result = [s[start:end + 1]] + result
        
        return ' '.join(result)