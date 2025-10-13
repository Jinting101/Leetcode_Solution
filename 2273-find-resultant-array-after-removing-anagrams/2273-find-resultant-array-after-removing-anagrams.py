class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def getFreq(word):
            res = [0] * 26
            for char in word:
                res[ord(char) - ord('a')]+=1
            return res
        
        preAnagram = getFreq(words[0])
        res = [words[0]]

        for i in range(1, len(words)):
            curAnagram = getFreq(words[i])
            if curAnagram != preAnagram:
                res.append(words[i])
                preAnagram = curAnagram
        
        return res