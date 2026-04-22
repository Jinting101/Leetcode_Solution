class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        def get_all(word):
            l = len(word)
            if l <= 2:
                return set(['*'*l])
            sets = set()
            for i in range(l):
                for j in range(i+1, l):
                    cur = word[:i] + '*' + word[i+1:j] + '*' + word[j+1:]
                    sets.add(cur)
            return sets

        dic = set()
        for word in dictionary:
            dic = dic.union(get_all(word))

        res = []
        for word in queries:
            check = get_all(word)
            for pattern in check:
                if pattern in dic:
                    res.append(word)
                    break
        
        return res