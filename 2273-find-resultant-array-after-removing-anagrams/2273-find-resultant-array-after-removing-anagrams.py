class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        for x in words:
            if res and Counter(x) == Counter(res[-1]):
                continue
            res.append(x)
        return res
