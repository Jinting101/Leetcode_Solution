class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        dp = [0] + [len(s)] * (len(s))
        wordSet = set(dictionary)
        
        for i in range(1, len(s)+1):
            dp[i] = dp[i-1] + 1
            for j in range(0, i):
                if s[j:i] in wordSet:
                    dp[i] = min(dp[i], dp[j])
        return dp[-1]

# Dictionary Setup: The first step is to store the dictionary words in a set (or hash map in Go) for O(1) lookup. This allows us to efficiently check if a substring is in the dictionary.

# DP Array Initialization: We initialize a DP array dp of size n + 1 (where n is the length of string s). Each entry dp[i] represents the minimum number of extra characters for the substring s[0:i]. We initialize the array with the maximum possible value, n, as this is the worst case.

# Dynamic Programming Transition: For each index i, we check all substrings ending at i-1. If a valid word from the dictionary is found, we update dp[i] by considering the state before the start of the substring (dp[j]). Additionally, we handle the case where the current character is considered extra.

# Final Result: The final result is stored in dp[n], which gives the minimum number of extra characters left after optimally splitting the string.

        